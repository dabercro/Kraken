#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------------
# Script to execute any condor command on the given scheduler.
#
# Author: C.Paus                                                                     (June 16, 2016)
#---------------------------------------------------------------------------------------------------
import sys,getopt
from scheduler import Scheduler
 
#===================================================================================================
# M A I N
#===================================================================================================
# Define string to explain usage of the script
usage =  "Usage: rCondor.py --cmd=<condor command>  (ex. condor_q)"
usage += "                  --local  # use local scheduler (ex. t3serv015)\n"
usage += "                  --help\n"

# Define the valid options which can be specified and check out the command line
valid = ['cmd=','local','help']
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

# Set defaults for each command line parameter/option
cmd = 'condor_q'
local = False

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--local":
        local = True
    if opt == "--cmd":
        cmd = arg

# Setup the scheduler we are going to use
scheduler = None
if local:
    scheduler = Scheduler('t3serv015.mit.edu','cmsprod')
else:
    scheduler = Scheduler()

# Issue the condor command
scheduler.executeCondorCmd(cmd,True)

sys.exit(0)
