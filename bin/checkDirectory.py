#!/usr/bin/env python
#===================================================================================================
# This script checks all files in a given directory using the checkFile.py script.
#===================================================================================================
import os,sys,subprocess
import rex

usage = "\n   usage:  checkDirectory.py  <directory> \n"

#===================================================================================================
#  H E L P E R S
#===================================================================================================

#===================================================================================================
#  M A I N
#===================================================================================================
# make sure command line is complete
if len(sys.argv) < 1:
    print " ERROR -- " + usage
    sys.exit(1)

# command line variables
directory = sys.argv[1]
print " INFO - checkDirectory.py %s"%(directory)
cmd = "t2tools.py --action ls --source " +  directory + " | grep root"
# make sure we can work remotely/locally
remoteX = rex.Rex('none','none')
(rc,out,err) = remoteX.executeLocalAction(cmd)

content = out.split("\n")
print " INFO - number of files to check: %d\n"%(len(content)-1)

for line in content:
    f = line.split(" ")
    if len(f) > 1:
        file = f[1]
        cmd = "checkFile.py %s"%(file)
        print " %s"%(cmd)
        os.system(cmd)
