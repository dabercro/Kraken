#!/usr/bin/python
#---------------------------------------------------------------------------------------------------
# Script to review all samples which are kept in our database and take approriate action to get
# them into the processing queues.
#
# Author: C.Paus                                                                (September 23, 2008)
#---------------------------------------------------------------------------------------------------
import os,sys,getopt,re,string
import MySQLdb
import task

#---------------------------------------------------------------------------------------------------
# H E L P E R
#---------------------------------------------------------------------------------------------------

def testTier2Disk(debug=0):
    # make sure we can see the Tier-2 disks: returns -1 on failure

    nFiles = -1
    cmd = "list /cms/store/user/paus 2> /dev/null"
    if debug > 0:
        print " CMD: %s"%(cmd)
    try:
        for line in os.popen(cmd).readlines():   # run command
            nFiles += 1
    except:
        nFiles = -1

    return nFiles

def productionStatus(config,version,dataset,debug=0):
    # make sure we can see the Tier-2 disks: returns -1 on failure

    cmd = "cat /home/cmsprod/catalog/t2mit/%s/%s/%s/Files 2> /dev/null | wc -l"\
        %(config,version,dataset)
    if debug > 0:
        print " CMD: %s"%(cmd)

    nDone = 0
    try:
        for line in os.popen(cmd).readlines():   # run command
            nDone = int(line[:-1])
    except:
        nDone = -1

    cmd = "grep root /home/cmsprod/cms/jobs/lfns/%s.lfns 2> /dev/null | wc -l"%(dataset)
    if debug > 0:
        print " CMD: %s"%(cmd)

    nTotal = 0
    try:
        for line in os.popen(cmd).readlines():   # run command
            nTotal = int(line[:-1])
    except:
        nTotal = -1
    
    return(nDone,nTotal)

def findNumberOfFilesDone(config,version,dataset,debug=0):
    # Find out how many files have been completed for this dataset so far

    if debug > 0:
        print " Find completed files for dataset: %s"%(dataset)

    cmd = "list /cms/store/user/paus/%s/%s/%s 2> /dev/null | grep .root | wc -l"\
        %(config,version,dataset)
    if debug > 0:
        print " CMD: %s"%(cmd)

    nFilesDone = 0
    try:
        for line in os.popen(cmd).readlines():   # run command
            nFilesDone = int(line[:-1])
    except:
        nFileDone = -1

    return nFilesDone

def testEnvironment(config,version,cmssw):
    # Basic checks will be implemented here to remove the clutter from the main

    # Does the local environment exist?
    dir = './' + config + '/' + version
    if not os.path.exists(dir):
        cmd = "\n Local work directory does not exist: %s\n" % dir
        raise RuntimeError, cmd
 
    # Look for the standard CMSSW python configuration file (empty file is fine)
    cmsswFile = os.environ['KRAKEN_BASE'] + '/' + config + '/' + version + '/' + cmssw + '.py'
    if not os.path.exists(cmsswFile):
        cmd = "Cmssw file not found: %s" % cmsswFile
        raise RuntimeError, cmd

def findPath(config,version):
    # Find the path to where we store our samples

    # start with T2_US_MIT as default
    storageTag = 'T2_US_MIT'
    domain = task.Domain()
    if   re.search('mit.edu',domain):
        storageTag = 'T2_US_MIT'
    elif re.search('cern.ch',domain):
        storageTag = 'T0_CH_CERN'
    # make connection with our storage information
    seTable = os.environ['KRAKEN_BASE'] + '/' + config + '/' + version + '/' + 'seTable'
    if not os.path.exists(seTable):
        cmd = "seTable file not found: %s" % seTable
        raise RuntimeError, cmd
    # extract the path name
    cmd = 'grep ^' + storageTag + ' ' + seTable + ' | cut -d = -f2 | sed \'s# : ##\''
    path = ''
    for line in os.popen(cmd).readlines():
        path = line[:-1] +  '/' + config + '/' + version

    return path

#---------------------------------------------------------------------------------------------------
# M A I N
#---------------------------------------------------------------------------------------------------
# Define string to explain usage of the script
usage  = "\nUsage: findSamples.py --config=<name>\n"
usage += "                      --version=<version> [ default: MIT_VERS ]\n"
usage += "                      --cmssw=<name>\n"
usage += "                      --pattern=<name>\n"
usage += "                      --useExistingLfns\n"
usage += "                      --useExistingSites\n"
usage += "                      --displayOnly\n"
usage += "                      --exe\n"
usage += "                      --debug\n"
usage += "                      --help\n\n"

# Define the valid options which can be specified and check out the command line
valid = ['config=','version=','cmssw=','pattern=', \
         'help','exe','useExistingLfns','useExistingSites','debug', \
         'displayOnly' ]
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

# Get all parameters for the production
# -------------------------------------
# Set defaults for each option
config = 'filefi'
version = '000'
cmssw = 'data'
pattern = ''
displayOnly = False
exe = False
useExistingLfns = False
useExistingSites = False
debug = False

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--config":
        config = arg
    if opt == "--version":
        version = arg
    if opt == "--cmssw":
        cmssw = arg
    if opt == "--pattern":
        pattern = arg
    if opt == "--exe":
        exe = True
    if opt == "--useExistingLfns":
        useExistingLfns = True
    if opt == "--useExistingSites":
        useExistingSites = True
    if opt == "--debug":
        debug = True
    if opt == "--displayOnly":
        displayOnly = True

# Access the database to determine all requests
db = MySQLdb.connect(read_default_file="/etc/my.cnf",read_default_group="mysql",db="Bambu")
cursor = db.cursor()
sql = 'select ' + \
    'Datasets.DatasetProcess,Datasets.DatasetSetup,Datasets.DatasetTier,'+\
    'Datasets.DatasetDbsInstance,Datasets.DatasetNFiles,' + \
    'RequestConfig,RequestVersion,RequestPy,RequestId,RequestNFilesDone from Requests ' + \
    'left join Datasets on Requests.DatasetId = Datasets.DatasetId '+ \
    'where RequestConfig="' + config + '" and RequestVersion = "' + version + \
    '" and RequestPy = "' + cmssw + \
    '" order by Datasets.DatasetProcess, Datasets.DatasetSetup, Datasets.DatasetTier;'
if debug:
    print ' SQL: ' + sql

# Try to access the database
try:
    # Execute the SQL command
    cursor.execute(sql)
    results = cursor.fetchall()      
except:
    print " Error (%s): unable to fetch data."%(sql)
    sys.exit(0)

#============================================
# D I S P L A Y  A N D  S E L E C T  L O O P
#============================================

# Take the result from the database and look at it
filteredResults = []
first = True
nAllTotal = 0
nDoneTotal = 0
nMissingTotal = 0
for row in results:
    process = row[0]
    setup = row[1]
    tier = row[2]
    dbs = row[3]
    nFiles = int(row[4])
    requestId = int(row[8])
    dbNFilesDone = int(row[9])

    # make up the proper mit datset name
    datasetName = process + '+' + setup+ '+' + tier

    matchObj = re.match(pattern,datasetName)
    if matchObj:
        # Make filtered list
        filteredResults.append(row)
        (nDone,nAll) = productionStatus(config,version,datasetName,debug)
        if first:
            first = False
            print '#---------------------------------------------------------------------------'
            print '#'
            print '#                            O V E R V I E W '
            print '#                              %s/%s'%(config,version)
            print '#'
            print '# Perct   Done/ Total--Dataset Name'
            print '#---------------------------------------------------------------------------'

        percentage = 0.0
        if nAll > 0:
            percentage = 100.0 * float(nDone)/float(nAll)
        if nDone != nAll:
            print " %6.2f  %5d/ %5d  %s"%(percentage,nDone,nAll,datasetName)
        else:
            print " %6.2f  %5d= %5d  %s"%(percentage,nDone,nAll,datasetName)

        nMissing = nAll-nDone

        nAllTotal += nAll
        nDoneTotal += nDone
        nMissingTotal += nMissing

percentage = 0.0
if nAll > 0:
    percentage = 100.0 * float(nDoneTotal)/float(nAllTotal)
print '#'
print '# TOTAL:  %6.2f%% (%d/ %d) -->  %6.2f%% (%d) missing.'\
    %(percentage,nDoneTotal,nAllTotal,100.-percentage,nMissingTotal)
print '#'

#===============================================
# D A T A S E T   V A L I D A T I O N   L O O P
#===============================================

# Take the result from the database and look at it
for row in filteredResults:
    process = row[0]
    setup = row[1]
    tier = row[2]
    # make up the proper mit datset name
    datasetName = process + '+' + setup+ '+' + tier
    if debug:
        print ' addDatasetToBambu.py --dataset=/' + process + '/' + setup+ '/' + tier

if displayOnly:
    sys.exit(0)

# Basic tests first
testEnvironment(config,version,cmssw)
if testTier2Disk(0) < 0:
    print '\n ERROR -- Tier-2 disks seem unavailable, please check! EXIT review process.\n'
    sys.exit(0)
else:
    print '\n INFO -- Tier-2 disks are available, start review process.\n'


# Where is our storage?
path = findPath(config,version)

#==================
# M A I N  L O O P
#==================

# Make sure we have a valid ticket, because now we will need it
cmd = "voms-proxy-init --valid 168:00 -voms cms; voms-proxy-info -all"
os.system(cmd)

# Initial message 
print ''
print ' @-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@'
print ''
print '                    S T A R T I N G   R E V I E W   C Y L E '
print ''
print ' @-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@-@'

# Take the result from the database and look at it
for row in filteredResults:
    process = row[0]
    setup = row[1]
    tier = row[2]
    dbs = row[3]
    nFiles = int(row[4])
    requestId = int(row[8])
    dbNFilesDone = int(row[9])

    # make up the proper mit datset name
    datasetName = process + '+' + setup+ '+' + tier

    # remove all datasets that do not match our pattern
    if pattern != '' and pattern not in datasetName:
        continue

    # check how many files are done
    nFilesDone = findNumberOfFilesDone(config,version,datasetName)
    print ' Number of files completed: %d (last check: %d) -- Dataset: %s' \
        %(nFilesDone,dbNFilesDone,datasetName)

    # what to do when the two numbers disagree
    if dbNFilesDone == -1:
        # this is a new dataset
        print '\n INFO - this seems to be a new dataset.'
        pass
        
    elif dbNFilesDone != nFilesDone:
        lUpdate = False

        # assume more files have been found
        if nFilesDone > 0 and nFilesDone > dbNFilesDone:
            lUpdate = True
        # less files are done now than before (this is a problem)
        else:
            if nFilesDone > 0: # looks like files have disappeared, but not all -> we should update
                lUpdate = True
                print '\n WARNING -- files have disappeared but there are files (%d -> %d now)'\
                    %(dbNFilesDone,nFilesDone)
            else:              # looks like we did not connect with the storage
                lUpdate = False
                print '\n WARNING -- files have all disappeared, very suspicious (%d -> %d now)'\
                    %(dbNFilesDone,nFilesDone)

        # 
        if lUpdate:
            sql = 'update Requests set RequestNFilesDone=%d'%(nFilesDone) + \
                ' where RequestId=%d'%(requestId)
            if debug:
                print ' SQL: ' + sql

            # Try to access the database
            try:
                # Execute the SQL command
                cursor.execute(sql)
                results = cursor.fetchall()      
            except:
                print " Error (%s): unable to update the database."%(sql)
                sys.exit(0)
        
    # did we already complete the job?

    if nFilesDone == nFiles:   # this is the case when all is done
        print ' DONE all files have been produced.\n'
        continue
    elif nFilesDone < nFiles:  # second most frequent case: work started but not completed
        print ' files missing, submit the missing ones.\n'
    else:                      # weird, more files found than available               
        print '\n ERROR more files found than available in dataset. NO ACTION on this dataset'
        print '       done: %d   all: %d'%(nFilesDone,nFiles)
        cmd = 'addDataset --exec --dataset=' + datasetName
        print '       updating the dataset from dbs: ' + cmd
        os.system(cmd)

    # if work not complete submit the remainder
    print '# Submit new dataset: ' + datasetName
    cmd = ' submitCondor.py --cmssw=' + cmssw + ' --config=' + config + ' --version=' \
        + version + ' --dbs=' + dbs

    # make sure to use existing cache if requested
    if useExistingLfns:
        cmd += " --useExistingLfns"
    if useExistingSites:
        cmd += " --useExistingSites"

    # last thing to add is the dataset itself (nicer printing)
    cmd += ' --dataset=' + datasetName

    print ' submitting: ' + cmd
    if exe:
        os.system(cmd)

sys.exit(0)
