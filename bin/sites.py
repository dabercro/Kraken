#!/usr/bin/env python
#---------------------------------------------------------------------------------------------------
# Simple interface to command line DBS to prepare my processing task input files.
#---------------------------------------------------------------------------------------------------
import os,sys,subprocess,getopt
import json
import rex

# Define string to explain usage of the script
usage =  "Usage: sitesList.py --dataset=<name>\n"
usage += "                  [ --dbs=<name> ]\n"
usage += "                    --help\n"
    
# Define the valid options which can be specified and check out the command line
valid = ['dataset=','dbs=','help']
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

def getProxy():
    cmd = 'voms-proxy-info -path'
    for line in subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readlines():
        proxy = line[:-1]
    
    return proxy

# --------------------------------------------------------------------------------------------------
# Get all parameters for the production
# --------------------------------------------------------------------------------------------------
# Set defaults for each option
dataset = None
dbs     = 'prod/global'
private = False

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--dataset":
        dataset = arg
        if dataset[0] != '/':
            dataset = '/' + dataset.replace('+','/')
    if opt == "--dbs":
        dbs     = arg

# Deal with obvious problems
if dataset == None:
    cmd = "--dataset=  required parameter not provided."
    raise RuntimeError, cmd

# is it a private production
f = dataset.split('/')

if len(f) > 1 and f[1] == "mc":
    private = True

#---------------------------------------------------------------------------------------------------
# main
#---------------------------------------------------------------------------------------------------
# handle private production first
if private:
    print dataset + '#00000000-0000-0000-0000-000000000000 : ' + 'T2_US_MIT'
    sys.exit()
    
proxy = getProxy()
cmd = 'curl -s --cert %s -k -H "Accept: application/json"'%proxy \
    + ' "https://cmsweb.cern.ch/phedex/datasvc/json/prod/'  \
    + 'blockreplicas?dataset=%s"'%(dataset)
myRx = rex.Rex()
(rc,out,err) = myRx.executeLocalAction(cmd)

if rc != 0:
    print ' ERROR ocurred in %s'%(url)
    sys.exit(1)

data = json.loads(out)

if "phedex" in data:
    phedex = data["phedex"]
    if "block" in phedex:
        blocks = phedex["block"]
        for block in blocks:
            blockName = block["name"]
            replicas = block["replica"]
            replicaString = ""
            for replica in replicas:
                if replicaString == "":
                    replicaString += '%s'%(replica["node"])
                else:
                    replicaString += ',%s'%(replica["node"])
            print "%s : %s"%(blockName,replicaString)
