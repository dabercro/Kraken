#!/usr/bin/env python
#---------------------------------------------------------------------------------------------------
# Script to get a quick overview how far the production has come.
#
# Author: C.Paus                                                                      (Feb 16, 2016)
#---------------------------------------------------------------------------------------------------
import os,sys,re,getopt

def getHeader():
    header = '<!DOCTYPE html><html><head><title>Bambu Production</title></head><style>a:link{color:#000000; background-color:transparent; text-decoration:none}a:visited{color:#009000; background-color:transparent; text-decoration:none}a:hover{color:#900000;background-color:transparent; text-decoration:underline}a:active{color:#900000;background-color:transparent; text-decoration:underline}body.ex{margin-top: 0px; margin-bottom:25px; margin-right: 25px; margin-left: 25px;}</style><body class="ex" bgcolor="#eeeeee"><body style="font-family: arial;font-size: 20px;font-weight: bold;color:#900000;"><pre>\n'
    return header

def getFooter():
    footer = '</pre></body></html>\n'
    return footer

#===================================================================================================
# Main starts here
#===================================================================================================
# Define string to explain usage of the script
usage = "\nUsage: htmlDressing.py [ --input=<id>  --help ]\n"

# Define the valid options which can be specified and check out the command line
valid = ['input=','version=','help']
try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

# --------------------------------------------------------------------------------------------------
# Get all parameters for this little task
# --------------------------------------------------------------------------------------------------
# Set defaults
input = ''
version = '000'

# Read new values from the command line
for opt, arg in opts:
    if opt == "--help":
        print usage
        sys.exit(0)
    if opt == "--input":
        input = arg
    if opt == "--version":
        version = arg

# Deal with obvious problems
if input == "":
    cmd = "--input  parameter not provided. This is a required parameter."
    raise RuntimeError, cmd

# --------------------------------------------------------------------------------------------------
# Here is where the real action starts -------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

# find new file name
htmlFile = input + '.html'
#print ' ASCII: ' + input
#print ' HTML:  ' + htmlFile

fileInput  = open(input,'r')
fileOutput = open(htmlFile,'w')
line = ' '

# insert header
fileOutput.write(getHeader())

# translate the body
with open(input,"r") as fileInput:
    for line in fileInput:
        # cleanup CR
        line = line[:-1]
        ## cleanup duplicate blanks
        #line = re.sub(' +',' ',line)

        # remove commented lines
        if '+' in line:
            f = line.split(' ')
            dataset = f.pop()
            line = ' '.join(f) \
                 + ' <a href="filefi/' + version + '/' + dataset + '">' + dataset + '</a>'
        else:
            f = line.split(' ')
            if len(f) > 1:
                v = f.pop()
                test = f.pop()
                if test == "VERSION:":
                    version = v

        fileOutput.write(line+'\n')
    
    
# insert footer
fileOutput.write(getFooter())

fileInput .close()
fileOutput.close()
