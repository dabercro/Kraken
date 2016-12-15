#---------------------------------------------------------------------------------------------------
# Python Module File to describe task
#
# Author: C.Paus                                                                      (Jun 16, 2016)
#---------------------------------------------------------------------------------------------------
import os,sys,re,string,socket
import rex

DEBUG = 0

#---------------------------------------------------------------------------------------------------
"""
Class:  Request(scheduler=None,sample=None,config='filefi',version='046',py='data')
A request will have to specify the configuration, version and python configuration file to be
applied to the also given a scheduler and a sample.
"""
#---------------------------------------------------------------------------------------------------
class Request:
    "Description of a request for a specific sample processing."

    #-----------------------------------------------------------------------------------------------
    # constructor
    #-----------------------------------------------------------------------------------------------
    def __init__(self,scheduler=None,sample=None,config='filefi',version='046',py='data'):
        
        self.base = os.getenv('KRAKEN_SE_BASE')

        self.scheduler = scheduler
        self.sample = sample
        self.config = config
        self.version = version
        self.py = py

        self.loadQueuedLfns()
        self.loadHeldLfns()
        self.loadCompletedLfns()
        self.sample.createMissingLfns()

    #-----------------------------------------------------------------------------------------------
    # load all lfns so far completed relevant to this task
    #-----------------------------------------------------------------------------------------------
    def loadCompletedLfns(self):

        # initialize from scratch
        path = self.base + '/' + self.config + '/' + self.version + '/' \
            + self.sample.dataset
        # first fully checked files
        cmd = 'list ' + path + '  2> /dev/null | grep root'
        for line in os.popen(cmd).readlines():  # run command
            f    = line.split()
            file = (f[1].split("/")).pop()
            self.sample.addCompletedLfn(file)
        # now also look at the temporary files (not yet cataloged)
        cmd = 'list ' + path + '/crab_*/  2> /dev/null | grep _tmp.root'
        for line in os.popen(cmd).readlines():  # run command
            f    = line.split()
            file = (f[1].split("/")).pop()
            file = file.replace('_tmp','')
            self.sample.addNoCatalogLfn(file)
        if DEBUG > 0:
            print ' NOCATAL - Lfns: %6d'%(len(self.sample.noCatalogLfns))
            print ' DONE    - Lfns: %6d'%(len(self.sample.completedLfns))

    #-----------------------------------------------------------------------------------------------
    # load all lfns that are presently queued
    #-----------------------------------------------------------------------------------------------
    def loadQueuedLfns(self):

        # initialize from scratch
        self.sample.resetQueuedLfns()

        path = self.base + '/' + self.config + '/' + self.version + '/' + self.sample.dataset
        pattern = "%s %s %s %s"%(self.config,self.version,self.py,self.sample.dataset)
        cmd = 'condor_q ' + self.scheduler.user \
            + ' -constraint JobStatus!=5 -format \'%s\n\' Args 2> /dev/null|grep \'' + pattern + '\''

        if not self.scheduler.isLocal():
            cmd = 'ssh -x ' + self.scheduler.user + '@' + self.scheduler.host \
                + ' \"' + cmd + '\"'
        for line in os.popen(cmd).readlines():  # run command
            f    = line.split(' ')
            file = f[4] + '.root'
            self.sample.addQueuedLfn(file)
        if DEBUG > 0:
            print ' QUEUED  - Lfns: %6d'%(len(self.sample.queuedLfns))

    #-----------------------------------------------------------------------------------------------
    # load all lfns that are presently queued but in held state
    #-----------------------------------------------------------------------------------------------
    def loadHeldLfns(self):

        # initialize from scratch
        self.sample.resetHeldLfns()

        path = self.base + '/' + self.config + '/' + self.version + '/' \
            + self.sample.dataset
        pattern = "%s %s %s %s"%(self.config,self.version,self.py,self.sample.dataset)
        cmd = 'condor_q ' + self.scheduler.user \
            + ' -constraint JobStatus==5 -format \'%s\n\' Args 2> /dev/null|grep \'' + pattern + '\''

        if not self.scheduler.isLocal():
            cmd = 'ssh -x ' + self.scheduler.user + '@' + self.scheduler.host \
                + ' \"' + cmd + '\"'
        for line in os.popen(cmd).readlines():  # run command
            f    = line.split(' ')
            file = f[4] + '.root'
            self.sample.addHeldLfn(file)

        if DEBUG > 0:
            print ' HELD    - Lfns: %6d'%(len(self.sample.heldLfns))

#---------------------------------------------------------------------------------------------------
"""
Class:  Scheduler(host='submit.mit.edu',user='paus')
Each sample can be described through this class
"""
#---------------------------------------------------------------------------------------------------
class Scheduler:
    "Description of a scheduler using condor"

    #-----------------------------------------------------------------------------------------------
    # constructor
    #-----------------------------------------------------------------------------------------------
    def __init__(self,host='submit.mit.edu',user='cmsprod',base=''):

        self.here = socket.gethostname()
        self.update(host,user,base)

    #-----------------------------------------------------------------------------------------------
    # find number of all jobs on this scheduler
    #-----------------------------------------------------------------------------------------------
    def findNumberOfTotalJobs(self):

        cmd = 'condor_q | grep running| cut -d\' \' -f1  2> /dev/null'
        if not self.isLocal():
            cmd = 'ssh -x ' + self.user + '@' + self.host + ' \"' + cmd + '\"'

        nJobs = 1000000
        if DEBUG > 0:
            print " CMD " + cmd
        for line in os.popen(cmd).readlines():  # run command
            nJobs = int(line[:-1])

        cmd = 'condor_q ' + self.user + '| grep running| cut -d\' \' -f1  2> /dev/null'
        if not self.isLocal():
            cmd = 'ssh -x ' + self.user + '@' + self.host + ' \"' + cmd + '\"'

        nMyJobs = 1000000
        for line in os.popen(cmd).readlines():  # run command
            nMyJobs = int(line[:-1])

        return (nJobs,nMyJobs)

    #-----------------------------------------------------------------------------------------------
    # find the home directory where we submit
    #-----------------------------------------------------------------------------------------------
    def findHome(self,host,user):

        cmd = 'ssh ' + user + '@' + host + ' pwd'
        #print 'CMD: ' + cmd
        home = ''
        for line in os.popen(cmd).readlines():  # run command
            line = line[:-1]
            home = line

        return home

    #-----------------------------------------------------------------------------------------------
    # find the user id where we submit
    #-----------------------------------------------------------------------------------------------
    def findRemoteUid(self,host,user):

        cmd = 'ssh ' + user + '@' + host + ' id -u'
        #print 'CMD: ' + cmd
        ruid = ''
        for line in os.popen(cmd).readlines():  # run command
            line = line[:-1]
            ruid = line

        return ruid

    #-----------------------------------------------------------------------------------------------
    # find local proxy path
    #-----------------------------------------------------------------------------------------------
    def findLocalProxy(self):

        localProxy = ""
        cmd = 'voms-proxy-info -path'
        for line in os.popen(cmd).readlines():  # run command
            line = line[:-1]
            localProxy = line

        return localProxy

    #-----------------------------------------------------------------------------------------------
    # Is the scheduler local?
    #-----------------------------------------------------------------------------------------------
    def isLocal(self):

        return (self.host == self.here)

    #-----------------------------------------------------------------------------------------------
    # push local proxy to remote location
    #-----------------------------------------------------------------------------------------------
    def pushProxyToScheduler(self):

        if self.isLocal():
            pass
        else:
            localProxy = self.findLocalProxy()
            remoteProxy = "/tmp/x509up_u" + self.ruid
            cmd = "scp -q " + localProxy + " " + self.user + '@' +  self.host + ':' + remoteProxy
            os.system(cmd)

        return

    #-----------------------------------------------------------------------------------------------
    # show the scheduler parameters
    #-----------------------------------------------------------------------------------------------
    def show(self):

        print ' ====  S c h e d u l e r  ===='
        print ' Here: ' + self.here
        print ' Host: ' + self.host
        print ' User: ' + self.user
        print ' Base: ' + self.base

    #-----------------------------------------------------------------------------------------------
    # update on the fly
    #-----------------------------------------------------------------------------------------------
    def update(self,host='submit.mit.edu',user='cmsprod',base=''):

        self.host = host
        self.user = user

        if base == '':
            self.base = self.findHome(host,user)
        else:
            self.base = base
        self.ruid = self.findRemoteUid(host,user)
        (self.nTotal,self.nMyTotal) = self.findNumberOfTotalJobs()

        self.pushProxyToScheduler()

        return

#---------------------------------------------------------------------------------------------------
"""
Class:  Sample(dataset='undefined',dbs='instance=prod/global',
               useExistingLfns=False,useExistingSites=False)
Each sample can be described through this class
"""
#---------------------------------------------------------------------------------------------------
class Sample:
    "Description of a datasample to be produced using condor"

    #-----------------------------------------------------------------------------------------------
    # constructor
    #-----------------------------------------------------------------------------------------------
    def __init__(self,dataset='undefined',dbs='instance=prod/global',\
                     useExistingLfns=False,useExistingSites=False):

        # define command line parameters
        self.dataset = dataset
        self.dbs = dbs
        self.useExistingLfns = useExistingLfns
        self.useExistingSites = useExistingSites

        # define the other contents
        self.nEvents = 0
        self.nEvtTotal = 0
        self.nMissingLfns = 0
        self.allLfns = {}
        self.queuedLfns = {}               # queued lfns do NOT include the held ones
        self.heldLfns = {}                 # those are kept separate for further analysis
        self.noCatalogLfns = {}
        self.completedLfns = {}
        self.missingLfns = {}

        # fill contents
        self.loadAllLfns(self.makeLfnFile())
        self.loadSites(self.makeSiteFile())


    #-----------------------------------------------------------------------------------------------
    # generate the lfn file and return it's location
    #-----------------------------------------------------------------------------------------------
    def makeLfnFile(self):

        lfnFile  = os.getenv('KRAKEN_WORK') + '/lfns/' + self.dataset + '.lfns'
    
        # give notice that file already exists
        if os.path.exists(lfnFile):
            print " INFO -- Lfn file found: %s. Someone already worked on this dataset." % lfnFile
    
        # remove what we need to to start clean
        cmd = 'rm -f ' +  lfnFile + '-TMP'
        os.system(cmd)
        if not self.useExistingLfns:
            cmd = 'rm -f ' + lfnFile
            os.system(cmd)
        
        # recreate if requested or not existing
        if not self.useExistingLfns or not os.path.exists(lfnFile):
            cmd = 'input.py --dbs=' + self.dbs + ' --option=lfn --dataset=' + self.dataset \
                  + ' | sort -u > ' + lfnFile + '-TMP'
            print ' Input: ' + cmd
            os.system(cmd)
    
        # move the new file into the proper location
        if os.path.exists(lfnFile + '-TMP'):
            cmd = 'mv ' + lfnFile + '-TMP ' + lfnFile
            print ' Move: ' + cmd
            os.system(cmd)
    
        return lfnFile
    
    #-----------------------------------------------------------------------------------------------
    # generate the sites file and return it's location
    #-----------------------------------------------------------------------------------------------
    def makeSiteFile(self):

        siteFile  = os.getenv('KRAKEN_WORK') + '/sites/' + self.dataset + '.sites'

        if os.path.exists(siteFile):
            print " INFO -- Site file found: %s. Someone already worked on this dataset." % siteFile
            if not self.useExistingSites:
                cmd = 'rm ' + siteFile
                os.system(cmd)
        
        # recreate if requested or not existing
        if not self.useExistingSites or not os.path.exists(siteFile):
            cmd = 'sites.py --dbs=' + self.dbs + ' --dataset=' + self.dataset + ' > ' + siteFile
            print ' Sites: ' + cmd + '\n'
            os.system(cmd)
    
        return siteFile

    #-----------------------------------------------------------------------------------------------
    # present the current samples
    #-----------------------------------------------------------------------------------------------
    def show(self):
        print ' ====  S a m p l e  ===='
        print ' Dataset       : ' + self.dataset
        print ' Dbs           : ' + self.dbs
        print ' NEvtTotal     : ' + str(self.nEvtTotal)
        print ' All Lfns      : ' + str(len(self.allLfns))
        print ' Queued Lfns   : ' + str(len(self.queuedLfns))
        print ' Held Lfns     : ' + str(len(self.heldLfns))
        print ' NoCatalog Lfns: ' + str(len(self.noCatalogLfns))
        print ' Completed Lfns: ' + str(len(self.completedLfns))
        print ' Missing Lfns  : ' + str(len(self.missingLfns))

    #-----------------------------------------------------------------------------------------------
    # return a string for all valid sites
    #-----------------------------------------------------------------------------------------------
    def getSitesString(self,pattern=''):
        siteString = ''
        for site in self.Sites:
            if pattern in site and not '_MSS' in site and not '_Buffer' in site:
                if siteString == '':
                    siteString = site
                else:
                    siteString += "," + site
        return siteString

    #-----------------------------------------------------------------------------------------------
    # load all lfns relevant to this task
    #-----------------------------------------------------------------------------------------------
    def loadAllLfns(self, lfnFile):
        
        # initialize from scratch
        self.allLfns = {}
        self.nEvtTotal = 0
        # use the complete lfn file list
        cmd = 'cat ' + lfnFile
        print ' LFN file: %s'%(lfnFile)
        for line in os.popen(cmd).readlines():  # run command
            line = line[:-1]
            # get ride of empty or commented lines
            if line == '' or line[0] == '#':
                continue

            # decoding the input line
            f       = line.split() # splitting every blank
            lfn     = f[1]
            file    = (f[1].split("/")).pop()

            self.nEvents = int(f[2])
            self.nEvtTotal += self.nEvents
            if file in self.allLfns.keys():
                print " ERROR -- lfn appeared twice! This should never happen. IGNORE. (%s)"%file
                #print " ERROR -- lfn appeared twice! This should never happen. EXIT."
                #sys.exit(1)
            # add this lfn to the mix
            self.allLfns[file] = lfn

        if DEBUG > 0:
            print ''
            print ' TOTAL   - Lfns: %6d  [ Events: %9d ]'\
                %(len(self.allLfns),self.nEvtTotal)

    #-----------------------------------------------------------------------------------------------
    # load sites for this sample/task
    #-----------------------------------------------------------------------------------------------
    def loadSites(self, siteFile):

        # initialize from scratch
        self.Sites = []
        # use the complete site file list
        cmd = 'cat ' + siteFile
        print ' SITES file: %s'%(siteFile)
        for line in os.popen(cmd).readlines():  # run command
            line = line[:-1]
            # get ride of empty or commented lines
            if line == '' or line[0] == '#':
                continue

            # decoding the input line
            f = line.split(" ") # splitting every blank
            sites = f.pop()
            for site in sites.split(","):
                if site not in self.Sites:
                    self.Sites.append(site)

        if DEBUG > 0:
            siteString = ''
            if len(self.Sites)>0:
                siteString = self.Sites[0]
                for site in self.Sites[1:]:
                    siteString += "," + site
            print ' Sites: %2d: %s'%(len(self.Sites),siteString)

    #-----------------------------------------------------------------------------------------------
    # add one queued lfn to the list
    #-----------------------------------------------------------------------------------------------
    def addQueuedLfn(self,file):

        if file not in self.allLfns.keys():
            print ' ERROR -- found queued lfn not in list of all lfns?! ->' + file + '<-'
            #print ' DEBUG - length: %d'%(len(self.allLfns))
        if file in self.queuedLfns.keys():
            print " ERROR -- queued lfn appeared twice! Should not happen but no danger. (%s)"%file
            #sys.exit(1)
        # add this lfn to the mix
        self.queuedLfns[file] = self.allLfns[file]

        return

    #-----------------------------------------------------------------------------------------------
    # add one held lfn to the list
    #-----------------------------------------------------------------------------------------------
    def addHeldLfn(self,file):

        if file not in self.allLfns.keys():
            print ' ERROR -- found queued lfn not in list of all lfns?! ->' + file + '<-'
        if file in self.heldLfns.keys():
            print " ERROR -- held lfn appeared twice! Should not happen but no danger. (%s)"%file
            #sys.exit(1)
        # add this lfn to the mix
        self.heldLfns[file] = self.allLfns[file]

        return

    #-----------------------------------------------------------------------------------------------
    # reset the list of queued lfns
    #-----------------------------------------------------------------------------------------------
    def resetQueuedLfns(self):

        self.queuedLfns = {}

        return

    #-----------------------------------------------------------------------------------------------
    # reset the list of held lfns
    #-----------------------------------------------------------------------------------------------
    def resetHeldLfns(self):

        self.heldLfns = {}

        return

    #-----------------------------------------------------------------------------------------------
    # add all lfns so far completed but not yet cataloged relevant to this task
    # - they might fail cataloging but we assume they worked
    #-----------------------------------------------------------------------------------------------
    def addNoCatalogLfn(self,file):

        if file not in self.allLfns.keys():
            print ' ERROR -- found queued lfn not in list of all lfns?! ->' + file + '<-'
        if file in self.noCatalogLfns.keys():
            print " ERROR -- noCatalog lfn appeared twice! Should not happen. EXIT (%s)"%file
            sys.exit(1)
        # add this lfn to the mix
        self.noCatalogLfns[file] = self.allLfns[file]

        return

    #-----------------------------------------------------------------------------------------------
    # add all lfns so far completed relevant to this task
    #-----------------------------------------------------------------------------------------------
    def addCompletedLfn(self,file):

        if file not in self.allLfns.keys():
            print ' ERROR -- found completed lfn not in list of all lfns?! ->' + file + '<-'
        if file in self.completedLfns.keys():
            print " ERROR -- completed lfn appeared twice! Should not happen. EXIT (%s)"%file
            sys.exit(1)
        # add this lfn to the mix
        self.completedLfns[file] = self.allLfns[file]

        return

    #-----------------------------------------------------------------------------------------------
    # create the list of missing Lfns extracted fromt he previously created lists
    #-----------------------------------------------------------------------------------------------
    def createMissingLfns(self):

        # fill the remaining lfns from complete database
        self.missingLfns = {}
        for file,lfn in self.allLfns.iteritems():
            if file in self.missingLfns.keys():
                print " ERROR -- missing lfn appeared twice! Should never happen. EXIT. (%s)"%file
                sys.exit(1)
            # is it already completed?
            if file not in self.completedLfns.keys() and \
               file not in self.noCatalogLfns.keys() and \
               file not in self.queuedLfns.keys():
                # adding this one to the missing ones
                self.missingLfns[file] = lfn

        if DEBUG > 0:
            print ' MISSING - Lfns: %6d'%(len(self.missingLfns))

#---------------------------------------------------------------------------------------------------
"""
Class:  Task(tag,config,version,cmssw,dataset,dbs,lfnFile,siteFile)
Each task in condor can be described through this class
"""
#---------------------------------------------------------------------------------------------------
class Task:
    "Description of a Task in condor"

    #-----------------------------------------------------------------------------------------------
    # constructor for new creation
    #-----------------------------------------------------------------------------------------------
    def __init__(self,tag,request):


        # from the call
        self.tag = tag
        self.request = request

        # create some shortcuts
        self.scheduler = self.request.scheduler
        self.sample = self.request.sample

        # derived
        self.cmsswVersion = self.findCmsswVersion()
        self.nJobs = 0
        self.submitCmd = 'submit_' +  self.tag + '.cmd'
        self.logs = self.scheduler.base + '/cms/logs/' + self.request.config + '/' \
            + self.request.version + '/' + self.sample.dataset
        self.outputData = self.scheduler.base + '/cms/data/' + self.request.config + '/' \
            + self.request.version + '/' + self.sample.dataset
        self.executable = self.logs + '/' + os.getenv('KRAKEN_SCRIPT')
        self.tarBall = self.logs + '/kraken_' + self.cmsswVersion + '.tgz'

        # show what we got
        print ''
        self.show()
        print ''

    #-----------------------------------------------------------------------------------------------
    # add specification to given file for exactly one more condor queue request (one lfn)
    #-----------------------------------------------------------------------------------------------
    def addLfn(self,fileH,file,lfn):

        gpack = file.replace('.root','')

        fileH.write("Arguments = " + self.request.config + ' ' + self.request.version + ' ' \
                        + ' ' + self.request.py + ' ' + self.sample.dataset + ' ' + gpack + ' ' \
                        + lfn + ' ' + self.tag + '\n')
        fileH.write("Output = " + self.logs + '/' + gpack + '.out' + '\n')
        fileH.write("Error = " + self.logs + '/' + gpack + '.err' + '\n')
        fileH.write("transfer_output_files = " + gpack + '.empty' + '\n')
        fileH.write("Queue" + '\n')

    #-----------------------------------------------------------------------------------------------
    # remove remainders from submission
    #-----------------------------------------------------------------------------------------------
    def cleanUp(self):

        # log and output data dirs
        print " INFO - removing submit script "
        os.system("rm -rf " + self.submitCmd)

    #-----------------------------------------------------------------------------------------------
    # submit condor job
    #-----------------------------------------------------------------------------------------------
    def condorSubmit(self):

        # make sure this condorTask has jobs to be submitted
        if self.nJobs<1 or self.scheduler.nMyTotal > 20000 or self.scheduler.nTotal > 100000:
            print ' NO SUBMISSION: %d (nJobs)  %d (nMyTotal)  %d (nTotal)\n'\
                %(self.nJobs,self.scheduler.nMyTotal,self.scheduler.nTotal)
            return

        # start with the base submit script
        cmd = 'condor_submit ' +  self.submitCmd
        if not self.scheduler.isLocal():
            cmd = 'ssh -x ' + self.scheduler.user + '@' + self.scheduler.host \
                + ' \"cd ' + self.logs + '; ' + cmd + '\"'
        os.system(cmd)

    #-----------------------------------------------------------------------------------------------
    # create the required local and remote directories
    #-----------------------------------------------------------------------------------------------
    def createDirectories(self):

        # log and output data dirs
        print " INFO - make local directories "
        cmd = "mkdir -p " + self.logs + " " + self.outputData
        if not self.scheduler.isLocal():
            cmd = 'ssh -x ' + self.scheduler.user + '@' + self.scheduler.host + ' ' + cmd
        os.system(cmd)

        # remote directories for kraken output
        print " INFO - make remote directories "
        cmd = "makedir --p " + self.request.base + "/" + self.request.config + '/' \
                      + self.request.version + '/' + self.sample.dataset + '/' + self.tag
        #print " MKDIR: " + cmd
        os.system(cmd)
        cmd = "changemod --options=a+rwx " + self.request.base + "/" \
                      + self.request.config + '/' + self.request.version + '/' \
                      + self.sample.dataset + '/' + self.tag
        #print " CHMOD: " + cmd
        os.system(cmd)


    #-----------------------------------------------------------------------------------------------
    # find the present CMSSW version
    #-----------------------------------------------------------------------------------------------
    def findCmsswVersion(self):
        myRex = rex.Rex()
        (rc,out,err) = myRex.executeLocalAction("ls -rt %s/%s/"%
                                                (os.getenv('KRAKEN_CMSSW'),self.request.version))
        #print " CMD: ls -1rt %s/%s/"%(os.getenv('KRAKEN_CMSSW'),self.request.version)
        cmsswVersion = ""
        for line in out.split("/n"):
            if 'CMSSW_' in line:
                cmsswVersion = line[:-1]
        #print " CMSSW: " + cmsswVersion
    
        return (cmsswVersion.replace('CMSSW_',''))

    #-----------------------------------------------------------------------------------------------
    # generate actual tarball, or leave as is if already up to date
    #-----------------------------------------------------------------------------------------------
    def makeTarBall(self):

        cmsswBase = "%s/%s/CMSSW_%s"%\
            (os.getenv('KRAKEN_CMSSW'),self.request.version,self.cmsswVersion)

        # check if the tar ball exists locally
        if os.path.exists(cmsswBase + "/kraken_" + self.cmsswVersion + ".tgz"):
            print " INFO - tar ball exists: " \
                + cmsswBase + "/kraken_" + self.cmsswVersion + ".tgz"
        else:
            print ' Make kraken tar ball: ' \
                + cmsswBase + "/kraken_" + self.cmsswVersion + ".tgz"
            cmd = "cd " + cmsswBase \
                + "; tar fch kraken_" + self.cmsswVersion + ".tar lib/ src/"
            os.system(cmd)
            cmd = "cd " + cmsswBase \
                + "; tar fr kraken_" + self.cmsswVersion + ".tar  python/"
            os.system(cmd)
            cmd = "cd " + os.getenv('KRAKEN_BASE') \
                + "; tar fr " + cmsswBase + "/kraken_" + self.cmsswVersion + ".tar tgz/ " \
                + self.request.config + "/" + self.request.version
            os.system(cmd)
            cmd = "cd " + cmsswBase \
                + "; gzip kraken_" + self.cmsswVersion + ".tar; mv  kraken_" \
                + self.cmsswVersion + ".tar.gz  kraken_"  + self.cmsswVersion + ".tgz"
            os.system(cmd)

        # see whether the tar ball needs to be copied locally or to remote scheduler
        if self.scheduler.isLocal():
            cmd = "cp " + cmsswBase+ "/kraken_" + self.cmsswVersion + ".tgz " \
                + self.logs
            os.system(cmd)
            # also copy the script over
            cmd = "cp " + os.getenv('KRAKEN_BASE') + "/bin/" + os.getenv('KRAKEN_SCRIPT') + " " \
                + self.logs
            os.system(cmd)
        else:
            cmd = "scp -q " + cmsswBase + "/kraken_" + self.cmsswVersion + ".tgz " \
                + self.scheduler.user + '@' +  self.scheduler.host + ':' + self.logs
            os.system(cmd)
            cmd = "scp -q " + os.getenv('KRAKEN_BASE') + "/bin/" + os.getenv('KRAKEN_SCRIPT') \
                + " " + self.scheduler.user + '@' +  self.scheduler.host + ':' + self.logs
            os.system(cmd)

        return

    #-----------------------------------------------------------------------------------------------
    # present the current condor task
    #-----------------------------------------------------------------------------------------------
    def show(self):

        print ' ==== C o n d o r  T a s k  I n f o r m a t i o n  ===='
        print ' '
        print ' Tag     : ' + self.tag
        print ' Base    : ' + self.request.base
        print ' Config  : ' + self.request.config
        print ' Version : ' + self.request.version
        print ' CMSSW py: ' + self.request.py
        print ' '
        self.sample.show()
        print ' '
        self.scheduler.show()

    #-----------------------------------------------------------------------------------------------
    # write condor submission configuration
    #-----------------------------------------------------------------------------------------------
    def writeCondorSubmit(self):

        # make sure to keep track of the number of jobs created
        self.nJobs = 0

        # start with the base submit script
        cmd = 'cp ' + os.getenv('KRAKEN_BASE') + '/condor/base.sub ' +  self.submitCmd
        os.system(cmd)

        # attach the additional processing lines defining the specifc LFN productions
        with open(self.submitCmd,'a') as fileH:
            fileH.write("Environment = \"HOSTNAME=" + os.getenv('HOSTNAME') + "\"" + '\n')
            fileH.write("Initialdir = " + self.outputData + '\n')
            fileH.write("Executable = " + self.executable + '\n')
            fileH.write("Log = " + self.logs + '/' + self.sample.dataset + '.log' + '\n')
            fileH.write("transfer_input_files = " + self.tarBall+ '\n')

            for file,lfn in self.sample.missingLfns.iteritems():
                print ' Adding : %s %s'%(file,lfn)
                self.nJobs += 1
                self.addLfn(fileH,file,lfn)

        # make sure submit script is in the right place
        if not self.scheduler.isLocal() and self.nJobs>0:
            cmd = "scp -q " + self.submitCmd + " " \
                + self.scheduler.user + '@' +  self.scheduler.host + ':' + self.logs
            os.system(cmd)
            cmd = "ssh -x " + self.scheduler.user + '@' +  self.scheduler.host \
                + ' \"voms-proxy-init --valid 168:00 -voms cms >& /dev/null\" '
            os.system(cmd)

#---------------------------------------------------------------------------------------------------
"""
Class:  TaskCleaner(condorTask)

A given condor task can be cleaned with this tool.

Method to remove all log files of successfully completed jobs and analysis of all failed jobs and
remove the remaining condor queue entires of the held jobs.

We are assuming that any failed job is converted into a held job. We collect all held jobs from the
condor queue and safe those log files into our web repository for browsing. Only the last copy of
the failed job is kept as repeated failure overwrites the old failed job's log files. The held job
entries in the condor queue are removed on the failed job is resubmitted.

It should be noted that if a job succeeds all log files including the ones from earlier failures
will be removed.

"""
#---------------------------------------------------------------------------------------------------
class TaskCleaner:

    "The cleaner of a given condor task."

    #-----------------------------------------------------------------------------------------------
    # constructor for new creation
    #-----------------------------------------------------------------------------------------------
    def __init__(self,task):

        self.task = task
        self.localUser = os.getenv('USER')

        self.logRemoveScript = ''  # '#!/bin/bash\n'
        self.webRemoveScript = ''  # '#!/bin/bash\n'
        self.logSaveScript = ''    # '#!/bin/bash\n'

        self.rex = rex.Rex(self.task.scheduler.host,self.task.scheduler.user)

    #-----------------------------------------------------------------------------------------------
    # analyze known failures
    #-----------------------------------------------------------------------------------------------
    def logCleanup(self):
        #

        print '\n ====  C l e a n e r  ===='

        # A - take all completed lfns and remove all related logs
        self.removeCompletedLogs()

        # B - find all logs from the held jobs, save them and generate failure summary
        self.saveFailedLogs()
        ## self.analyzeLogs()
        ## 
        ## # C - remove all held jobs from the queue
        self.removeHeldJobs()

        return

    #-----------------------------------------------------------------------------------------------
    # analyze saved logs and produce a summary web page
    #-----------------------------------------------------------------------------------------------
    def analyzeLogs(self):

        print ' - analyze failed logs \n     FAKE FOR NOW \n\n'

        return

    #-----------------------------------------------------------------------------------------------
    # remove all log files of completed jobs
    #-----------------------------------------------------------------------------------------------
    def removeCompletedLogs(self):

        cfg = self.task.request.config
        vers = self.task.request.version
        dset = self.task.request.sample.dataset

        local = '/local/' + self.localUser + '/MitProd/agents/reviewd'

        print ' - remove completed logs'

        for file,lfn in self.task.sample.completedLfns.iteritems():
            # we will make a lot of reference to the ID
            id = file.replace('.root','')

            cmd = 'rm -f cms/*/%s/%s/%s/*%s*\n'%(cfg,vers,dset,id)
            self.logRemoveScript += cmd

            cmd = 'rm -f %s/%s/%s/%s/*%s*\n'%(local,cfg,vers,dset,id)
            self.webRemoveScript += cmd

        for file,lfn in self.task.sample.noCatalogLfns.iteritems():
            # we will make a lot of reference to the ID
            id = file.replace('.root','')

            cmd = 'rm cms/*/%s/%s/%s/*%s* 2> /dev/null\n'%(cfg,vers,dset,id)
            self.logRemoveScript += cmd

            cmd = 'rm -f %s/%s/%s/%s/*%s*\n'%(local,cfg,vers,dset,id)
            self.webRemoveScript += cmd

        print ' -- LogRemoval'
        #print self.logRemoveScript
        (irc,rc,out,err) = self.rex.executeLongAction(self.logRemoveScript)
        print ' -- WebRemoval'
        #print self.webRemoveScript
        (rc,out,err) = self.rex.executeLocalLongAction(self.webRemoveScript)

        return

    #-----------------------------------------------------------------------------------------------
    # remove held jobs from the queue
    #-----------------------------------------------------------------------------------------------
    def removeHeldJobs(self):

        base = self.task.scheduler.base + "/cms/data"
        iwd = base + "/%s/%s/%s"%\
            (self.task.request.config,self.task.request.version,self.task.request.sample.dataset)
        cmd = 'condor_rm -constraint "JobStatus==5 && Iwd==\\\"%s\\\""'%(iwd)
        debug = 1
        irc = 0
        rc = 0

        print ' - remove Held jobs (there are %d): %s'%(len(self.task.request.sample.heldLfns),cmd)
        if not self.task.scheduler.isLocal():
            (irc,rc,out,err) = self.rex.executeAction(cmd)
            if debug > 0 and (irc != 0 or rc != 0):
                print ' IRC: %d'%(irc) 
        else:
            (rc,out,err) = self.rex.executeLocalAction(cmd)
            
        if debug > 0 and (irc != 0 or rc != 0):
            print ' RC: %d'%(rc) 
            print ' ERR:\n%s'%(err) 
            print ' OUT:\n%s'%(out) 

        return

    #-----------------------------------------------------------------------------------------------
    # save the log files of the failed jobs
    #-----------------------------------------------------------------------------------------------
    def saveFailedLogs(self):

        cfg = self.task.request.config
        vers = self.task.request.version
        dset = self.task.request.sample.dataset

        local = '/local/' + self.localUser + '/MitProd/agents/reviewd'

        print ' - find failed logs'

        self.logSaveScript += 'cd cms/logs/%s/%s/%s\ntar fzc %s-%s-%s.tgz'\
            %(cfg,vers,dset,cfg,vers,dset)

        # find out whether we have held jobs == failures
        haveFailures = False
        for file,lfn in self.task.sample.heldLfns.iteritems():
            id = file.replace('.root','')
            cmd = '  \\\n  %s.{out,err}'%(id)
            self.logSaveScript += cmd
            haveFailures = True

        # no need to continue if there are no failures
        if not haveFailures:
            print ' INFO - no failed jobs found.'
            return

        # log saver script
        print self.logSaveScript
        (irc,rc,out,err) = self.rex.executeLongAction(self.logSaveScript)

        cmd = 'mkdir -p %s/%s/%s/%s/;'%(local,cfg,vers,dset)
        print ' Mkdir: ' + cmd
        (rc,out,err) = self.rex.executeLocalAction(cmd)

        cmd = 'scp ' + self.task.scheduler.user + '@' + self.task.scheduler.host \
            + ':cms/logs/%s/%s/%s/%s-%s-%s.tgz'%(cfg,vers,dset,cfg,vers,dset) \
            + ' %s/%s/%s/%s/'%(local,cfg,vers,dset)
        print ' Get tar: ' + cmd
        (rc,out,err) = self.rex.executeLocalAction(cmd)

        cmd = 'cd %s/%s/%s/%s/\n'%(local,cfg,vers,dset) \
            + 'tar fzx %s-%s-%s.tgz\n'%(cfg,vers,dset) \
            + 'chmod a+r *'
        print ' Untar: ' + cmd
        (rc,out,err) = self.rex.executeLocalAction(cmd)

        cmd = 'rm -f %s/%s/%s/%s/%s-%s-%s.tgz'%(local,cfg,vers,dset,cfg,vers,dset) 
        print ' Remove local tar: ' + cmd
        (rc,out,err) = self.rex.executeLocalAction(cmd)

        cmd = 'rm -f cms/logs/%s/%s/%s/%s-%s-%s.tgz'%(cfg,vers,dset,cfg,vers,dset)
        print ' Remove remote tar: ' + cmd
        (irc,rc,out,err) = self.rex.executeAction(cmd)

        return
