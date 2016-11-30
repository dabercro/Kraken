#!/usr/bin/env python
#---------------------------------------------------------------------------------------------------
# Simple interface to command line DBS to prepare my crabTask input files.
#---------------------------------------------------------------------------------------------------
import os,sys,types,string,getopt

def cleanupSite(site):
    # Remove the tape entries and convert the Disk entries to the generic site name

    newSite = site
    if '_MSS' in site:
        newSite = ''
    elif '_Disk' in site:
        newSite = site.replace('_Disk','') 

    return newSite

# adding the certificate
#cert = "--cert ~/.globus/usercert.pem --key ~/.globus/userkey.pem "
cert = ""

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

cmd = 'das_client ' + cert + ' --format=plain --limit=0 --query="block dataset=' + dataset \
    + ' instance=' + dbs + ' | grep block.name block.replica.site" | grep %s'%(dataset)

sites = {}
for line in os.popen(cmd).readlines():
    line = line[:-1]
    line = line.translate(None, '"[]\',')
    f    = line.split(' ');
    block = f[0]
    siteString = ''
    for site in f[2:]:
        site = cleanupSite(site)
        if site != '':
            if siteString == '':
                siteString = site
            else:
                siteString = site + "," + siteString
    sites[block] = siteString

# print each block and the sites that hold it in a comma seperate list 
for block,sites in sites.iteritems():
    print block + ' : ' + sites
