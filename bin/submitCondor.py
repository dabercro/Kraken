#!/usr/bin/env python
#---------------------------------------------------------------------------------------------------
# Script to submit one complete production task
#
# Complete refers here to the proper preparation of the ultimate storage location (a storge element
# with a given storage path etc.) and the creation of the job configurations and the submission of
# the jobs to the grid sites. The grid is accessed via condor tools.
#
# Author: C.Paus                                                                     (June 16, 2016)
#---------------------------------------------------------------------------------------------------
import os,sys,getopt,re,string
import processing

t2user = os.environ['T2TOOLS_USER']
SRMSRC='/usr/bin'
 
#===================================================================================================
# M A I N
#===================================================================================================
# Define string to explain usage of the script
usage =  "Usage: submitCondor.py --dataset=<name>\n"
usage += "                       --py=<name>\n"
usage += "                       --config=<name>\n"
usage += "                       --version=<version>\n"
usage += "                       --dbs=<name>\n"
usage += "                       --nJobsMax=<n>\n"
usage += "                       --local  # submitting to the local scheduler (ex. t3serv015)\n"
usage += "                       --useExistingLfns\n"
usage += "                       --useExistingSites\n"
usage += "                       --noCleanup\n"
usage += "                       --help\n"

# Define the valid options which can be specified and check out the command line
valid = ['dataset=','py=','config=','version=','dbs=','nJobsMax=',
         'local','useExistingLfns','useExistingSites','noCleanup',
         'help']
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

# debugging level
DEBUG = 1

# Set defaults for each command line parameter/option
dataset = None
py = "cmssw"
config = "pandaf"
version = "000"
dbs = "prod/global"
nJobsMax = 20000
local = False
useExistingLfns = False
useExistingSites = False
noCleanup = False

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--dataset":
        dataset = arg
    if opt == "--py":
        py = arg
    if opt == "--config":
        config = arg
    if opt == "--version":
        version = arg
    if opt == "--dbs":
        dbs = arg
    if opt == "--nJobsMax":
        nJobsMax = int(arg)
    if opt == "--local":
        local = True
    if opt == "--useExistingLfns":
        useExistingLfns  = True
    if opt == "--useExistingSites":
        useExistingSites = True
    if opt == "--noCleanup":
        noCleanup = True

# Deal with obvious problems
if dataset == None:
    cmd = "--dataset  required parameter not provided."
    raise RuntimeError, cmd

# --------------------------------------------------------------------------------------------------
# Get all parameters for the production
# --------------------------------------------------------------------------------------------------
# condor id
cmd = "date +crab_0_%y%m%d_%H%M%S"
for line in os.popen(cmd).readlines():  # run command
    line = line[:-1]
    condorId = line
print ""
print " o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o"
print "\n This job will be CondorId: " + condorId + "\n"
print " o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o"
print ""

# Read all information about the sample
if DEBUG > 0:
    print ' DG0: Setting up sample.'
sample = processing.Sample(dataset,dbs,useExistingLfns,useExistingLfns,useExistingSites)

# Setup the scheduler we are going to use
if DEBUG > 0:
    print ' DG0: Setting up scheduler.'
scheduler = None
if local:
    scheduler = processing.Scheduler('t3serv015.mit.edu',os.getenv('USER','paus'),nJobsMax)
else:
    scheduler = processing.Scheduler('submit.mit.edu',
                                     os.getenv('KRAKEN_REMOTE_USER','paus'),
                                     '/work/%s'%(os.getenv('KRAKEN_REMOTE_USER','paus')),
                                     nJobsMax)

# Generate the request
if DEBUG > 0:
    print ' DG0: Setting up request.'
request = processing.Request(scheduler,sample,config,version,py)

# Create the corresponding condor task
if DEBUG > 0:
    print ' DG0: Setting up task.'
task = processing.Task(condorId,request)

# Cleaning up only when you nwant to (careful cleanup only works as agent)
if not noCleanup:
    # Quick analysis of ongoing failures and related logfile cleanup
    taskCleaner = processing.TaskCleaner(task)
    taskCleaner.logCleanup()

# Prepare the environment
if len(task.sample.missingJobs) > 0:

    # Make the local/remote directories
    task.createDirectories()
    task.makeTarBall()

    # Make the submit file
    task.writeCondorSubmit()
 
    # Submit this job
    task.condorSubmit()

# Make it clean
task.cleanUp()

print ''

sys.exit(0)
