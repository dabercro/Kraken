#!/usr/bin/env python
#---------------------------------------------------------------------------------------------------
# Simple interface to command line DBS to prepare my crabTask input files.
#---------------------------------------------------------------------------------------------------
import os,sys,types,string,re,getopt

# adding the certificate
cert = "--cert ~/.globus/usercert.pem --key ~/.globus/userkey.pem "

# Define string to explain usage of the script
usage =  "Usage: input.py --dataset=<name>\n"
usage += "                --option=[ lfn, xml ]\n"
usage += "                [ --dbs= ]\n"
usage += "                --help\n"

# --------------------------------------------------------------------------------------------------
# H E L P E R S 
# --------------------------------------------------------------------------------------------------
def printHeader(option):
    line = ''
    if option == 'xml':
        line = '<arguments>'
    return line
        
def printFooter(option):
    line = ''
    if option == 'xml':
        line = '</arguments>'
    return line

def printLine(option,nEvents,block,lfn,iJob):
    if option == 'xml':
        line = '  <Job MaxEvents="%d'%nEvents + '"  InputFiles="' + lfn \
              + '" SkipEvents="0" JobID="%d'%iJob + '" > </Job>'
    else:
        line = "%s %s %d"%(block,lfn,nEvents)
    return line


def generateContentFromCache(option):
    # use our local cache to generate the content

    cmd = 'cat ' + db
    iJob = 1
    content = []
    content.append(printHeader(option))
    for line in os.popen(cmd).readlines():
        line    = line[:-1]
        f       = line.split()
        block   = f[0]
        lfn     = f[1]
        nEvents = int(f[2])
    
        f       = lfn.split("/")
        file    = f[-1]

        if nEvents != 0:
            content.append(printLine(option,nEvents,block,lfn,iJob))
            iJob = iJob + 1
    content.append(printFooter(option))

    return content

def generateContentFromDisk(option):
    # use our Tier-2 disk to generate the content

    lfn = '/store/user/paus' + dataset
    dir = '/cms/store/user/paus' + dataset
    cmd = 'list ' + dir

    content = []
    content.append(printHeader(option))
    for line in os.popen(cmd).readlines():
        line = line[:-1]
        f = line.split(' ')
        size = int(f[0])
        file = f[1]

        cmdCount = 'catalogFile.sh /cms' + lfn + \
                   '/' + file + ' >& /tmp/cata.TMP; grep XX-CATALOG-XX /tmp/cata.TMP' 
        nEvts = 0
        for tmp in os.popen(cmdCount).readlines():
            tmp = tmp[:-1]
            f = tmp.split(" ")
            if len(f) > 4:
                nEvts = f[4]

        if nEvts == 0:
            for tmp in os.popen(cmdCount).readlines():
                tmp = tmp[:-1]
                f = tmp.split(" ")
                if len(f) > 4:
                    nEvts = f[4]
            
        if nEvts > 0:
            content.append('%s#00000000-0000-0000-0000-000000000000 %s/%s %s'%(dataset,lfn,file,nEvts))
    content.append(printFooter(option))

    return content

def generateContentFromDas(option):
    # use officical dbs commands to generate the content

    cmd = 'das_client --format=plain --limit=0 --query="file dataset=' + \
          dataset + ' instance=' + dbs + ' | grep file.block.name file.name file.nevents" | sort'
    iJob = 1
    content = []
    content.append(printHeader(option))
    for line in os.popen(cmd).readlines():
        line = line[:-1]
        line = line.translate(None, '"[]\',')
        f = line.split()
        nEvents = 0
        try:
            block   = f[0]
            lfn     = f[1]
            nEvents = int(f[3])
            g       = lfn.split("/")
            file    = g[-1]
        except:
            #print " ERROR in line: %s (cmd: %s)"%(line,cmd)
            continue

        if nEvents != 0:
            content.append(printLine(option,nEvents,block,lfn,iJob))
            iJob = iJob + 1
    content.append(printFooter(option))

    return content
    
# --------------------------------------------------------------------------------------------------
# M A I N
# --------------------------------------------------------------------------------------------------
# Define the valid options which can be specified and check out the command line
valid = ['db=','dbs=','dataset=','option=','help']
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex: 
    print usage
    print str(ex)
    sys.exit(1)

# --------------------------------------------------------------------------------------------------
# Get all parameters for the production
# --------------------------------------------------------------------------------------------------
# Set defaults for each option
db      = None
dbs     = 'prod/global'
dataset = None
option  = 'lfn'
private = False

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--db":
        db      = arg
    if opt == "--dbs":
        dbs     = arg
    if opt == "--dataset":
        dataset = arg
        if dataset[0] != '/':
            dataset = '/' + dataset.replace('+','/')
    if opt == "--option":
        option  = arg

# Deal with obvious problems
if dataset == None:
    cmd = "--dataset=  required parameter not provided."
    raise RuntimeError, cmd

# is it a private production
f = dataset.split('/')
if len(f) > 1 and f[1] == "mc":
    private = True


# initialize the content of the file
content = []

# generate the content according to the given options
if db:
    # option one: we are using a privatly produced dataset
    content = generateContentFromCache(option)
elif private:
    # option two: this is a private dataset
    content = generateContentFromDisk(option)
elif not db:
    # option two: use DBS (official database)
    content = generateContentFromDas(option)
else:
    print ' ERROR -- no option selected'

# here is where we print
for line in content:
    if line != '':
        print line
