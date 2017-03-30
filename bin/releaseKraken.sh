#!/bin/bash
#===================================================================================================
#
# Execute one job on the grid or interactively.
#
#===================================================================================================

#----------------------------------------------------------------------------------------------------
#  U S E F U L   F U N C T I O N S
#----------------------------------------------------------------------------------------------------

function exeCmd {
  # provide a small frame for each command, also allows further steering
  echo " Executing: $*"
  $*
}  

function executeCmd {
  # provide a nice frame for each command, also allows further steering

  echo " "
  echo " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
  exeCmd $*
  echo " Completed: $*"
  echo " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
  echo " "
  
}  

function configureSite {
  # in case we are not at a CMS site we need to have a configuration
  #
  # -- ATTENTION -- CMSSW has to be setup before calling configure site
  #
  link="/cvmfs/cms.cern.ch/SITECONF/local"
  xml="$link/JobConfig/site-local-config.xml"

  echo "---- Setup SiteConfig ----"
  echo " Link       = $link"
  echo " Xml        = $xml"
  echo " CMSSW_BASE = $CMSSW_BASE"

  if [ -e "$xml" ]
  then
    echo " Config exists: $xml."
    return
  else
    echo " ERROR -- config does not exist: $xml"
  fi

  ls -lh $CMSSW_BASE/tgz/siteconf.tgz
  echo "  -- unpacking private local config to recover"
  executeCmd tar fzx $CMSSW_BASE/tgz/siteconf.tgz
  cd SITECONF
  rm -f local
  testGeoId=`curl -s http://cmsopsquid.cern.ch/wpad.dat | grep 'Bad Request'`
  if [ "$testGeoId" == "" ]
  then
    ln -s ./T3_US_OSG ./local
  else
    ln -s ./T2_US_MIT ./local
  fi

  ls -lhrt
  cd -
  # make sure this is the config to be used
  export CMS_PATH=`pwd`

  # get the certificates
  echo "---- Setup certificates ----"
  CERTS_DIR="/etc/grid-security/certificates"
  if ! [ -d "$CERTS_DIR" ] 
  then
    CERTS_DIR="/cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.2/current/el6-x86_64/etc/grid-security/certificates"
    echo "Using OSG location at: $CERTS_DIR"
    export X509_CERT_DIR=$CERTS_DIR
  else
    echo "Using local certificates: $CERTS_DIR"
  fi
}

function downloadFiles {
  # find all input files and loop through to 

  # read command line parameters
  task="$1"
  gpack="$2"
  lfn="$3"

  echo " Downloading all input files: $task $gpack $lfn"
  cat $BASEDIR/$task.lfns

  # grep the input files belonging to this job
  inputLfns=`grep ^$gpack $BASEDIR/$task.lfns | cut -d' ' -f2`
  voms-proxy-info -all
  cd $WORKDIR; pwd; ls -lhrt

  rm -rf ./inputFiles
  touch  ./inputFiles

  for lfn in $inputLfns
  do
    fileId=`basename $lfn | sed 's/.root//'`
    downloadFile $fileId $lfn
    if ! [ -e "./$fileId.root" ]
    then
      echo " EXIT(255) -- download failed."
      exit 255
    fi
    echo "$fileId.root" >> ./inputFiles
  done

  echo " =========================="
  echo "  Input files for this job "
  echo " =========================="
  cat ./inputFiles
}

function downloadFile {
  # download one given lfn using xrootd

  # read command line parameters
  gpack="$1"
  lfn="$2"

  serverList="cms-xrd-global.cern.ch cmsxrootd.fnal.gov xrootd.unl.edu"
  if [ "`grep store/user/paus $lfn`" != "" ]
  then
    serverList="xrootd.cmsaf.mit.edu xrootd1.cmsaf.mit.edu xrootd10.cmsaf.mit.edu "
  fi

  echo ""
  echo " Make local copy of the root file with LFN: $lfn"

  if [ -e "./$gpack.root" ]
  then
    echo " File exists already locally: ./$gpack.root"
  else
    for server in $serverList
    do
      echo " Trying server: $server at "`date`
  
      echo " Execute:  xrdcp -d 1 -s root://$server/$lfn ./$gpack.root"
      xrdcp -d 1 -s root://$server/$lfn ./$gpack.root
      rc="$?"
  
      if [ "$rc" != "0" ]
      then
        echo " ERROR -- Copy command failed -- RC: $rc at "`date`
        rm -f ./$gpack.root
      fi
  
      if [ -e "./$gpack.root" ]
      then
        echo " Looks like copy worked on server: $server at "`date`
        break
      else
        echo " ERROR -- ./$gpack.root does not exist or corrupt (RC:$rc, server:$server at "`date`")"
      fi
    done
  fi

  if [ -e "./$gpack.root" ]
  then
    ls -lhrt ./$gpack.root
  else
    echo " ERROR -- input file ./$gpack.root does not exist. Failed on all servers: $serverList"
    echo "          EXIT now because there is no AOD* file to process."
    return
  fi
}  

function iniState {
  # provide a short summary of where we are when we start the job

  h=`basename $0`
  echo "Script:    $h"
  echo "Arguments: $*"
  
  # some basic printing
  echo " "
  echo "${h}: Show who and where we are"
  echo " start time    : "`date`
  echo " user executing: "`id`
  echo " running on    : "`hostname`
  echo " executing in  : "`pwd`
  echo " submitted from: $HOSTNAME"
  echo ""
}  

function initialState {
  # provide a summary of where we are when we start the job

  iniState $*
  echo ""
  echo " HOME:" ~/
  echo " "
  env
  ls -lhrt
  showDiskSpace
}  

function setupCmssw {
  # setup a specific CMSSW release and add the local python path

  THIS_CMSSW_VERSION="$1"
  PWD=`pwd`
  echo ""
  echo "============================================================"
  echo " Initialize CMSSW $THIS_CMSSW_VERSION"
  source /cvmfs/cms.cern.ch/cmsset_default.sh
  if [ "`echo $THIS_CMSSW_VERSION | grep ^8_`" != "" ]
  then
    export SCRAM_ARCH=slc6_amd64_gcc530
  fi
  scram project CMSSW CMSSW_$THIS_CMSSW_VERSION
  pwd
  ls -lhrt
  ls -lhrt *
  cd CMSSW_$THIS_CMSSW_VERSION/src 
  eval `scram runtime -sh`
  if [ -e  "$BASEDIR/kraken_$THIS_CMSSW_VERSION.tgz" ]
  then
    cd ..
    tar fzx $BASEDIR/kraken_$THIS_CMSSW_VERSION.tgz
  fi
  cd $PWD
  echo "============================================================"
  configureSite
  echo ""
}

function showDiskSpace {
  # implement a simple minded summary of the available disk space and usage

  [ -z $BASEDIR ] && $BASEDIR="./"

  echo ""
  echo " Disk space overview "
  echo " =================== "
  df -h $BASEDIR
  echo ""
  echo " Disk space usage "
  echo " ================ "
  du -sh $BASEDIR/*
}

function testBatch {
  # implement simple minded/not perfect test to see whether script is run in batch

  batch=0
  if [ "`echo $PWD | grep $USER`" == "" ]
  then
    batch=1
  fi
  return $batch
}

#----------------------------------------------------------------------------------------------------
#  M A I N   S T A R T S   H E R E
#----------------------------------------------------------------------------------------------------

# make sure we are locked and loaded
export BASEDIR=`pwd`
echo " Executing: $0 $* "

# command line arguments
             # -- example
EXE="$1"     # cmsRun
CONFIG="$2"  # pandaf
VERSION="$3" # 002
PY="$4"	     # data-03feb2017
TASK="$5"    # MET+Run2016B-03Feb2017_ver2-v2+MINIAOD
GPACK="$6"   # 6EBC0286-34EE-E611-832F-0025905B8600
LFN="$7"     # /store/data/Run2016B/ ... /6EBC0286-34EE-E611-832F-0025905B8600.root
CRAB="$8"    # crab_0_170302_132124                               

# load all parameters relevant to this task
echo " Initialize package"
test=`ls kraken_*tgz 2> /dev/null`
if [ "$test" == "" ]
then
  echo ' ERROR - Kraken tar ball is missing. No point to continue.'
  exit 1
fi

cmsswVersion=`echo kraken_*.tgz | sed -e 's@kraken_@@' -e 's@.tgz@@'`

# make sure to contain file mess
mkdir ./work
cd    ./work
export WORKDIR=`pwd`

# this might be an issue with root
export HOME=$WORKDIR

# tell us the initial state
initialState $*

####################################################################################################
# initialize KRAKEN
####################################################################################################

# setting up the software
setupCmssw $cmsswVersion

# download all input files to have them local
downloadFiles $TASK $GPACK $LFN

# prepare the python config from the given templates
cat $CMSSW_BASE/$CONFIG/$VERSION/${PY}.py \
    | sed -e "s@XX-LFN-XX@$LFN@g" -e "s@XX-GPACK-XX@$GPACK@g" \
    > $WORKDIR/${PY}.py

# create the local links
cd $WORKDIR
echo " Preparing links -- $CMSSW_BASE/src/PandaProd/Ntupler/test"
ls -l $CMSSW_BASE/src/PandaProd/Ntupler/test 2> /dev/null
if [ -d "$CMSSW_BASE/src/PandaProd/Ntupler/test/jec" ]
then
  ln -s $CMSSW_BASE/src/PandaProd/Ntupler/test/jec 
fi
if [ -d "$CMSSW_BASE/src/PandaProd/Ntupler/test/jer" ]
then
  ln -s $CMSSW_BASE/src/PandaProd/Ntupler/test/jer 
fi

####################################################################################################
# run KRAKEN
####################################################################################################

# run KRAKEN making
cd $WORKDIR
pwd
ls -lhrt

echo " Exe: python ${PY}.py" 
python ${PY}.py
echo " Exe: $KRAKEN_EXE ${PY}.py inputFiles=./inputFiles outputFile=kraken_000.root" 
$KRAKEN_EXE ${PY}.py inputFiles=./inputFiles outputFile=kraken_000.root

rc=$?

if [ "$rc" != "0" ] 
then
  echo ""
  echo " ERROR -- Return code is not zero: $rc"
  echo "          EXIT, no file copies!!"
  echo ""
  exit $rc
fi

# this is a little naming issue that has to be fixed
mv kraken*.root  ${GPACK}_tmp.root

# cleanup the input
rm -f ./$GPACK.root

if ! [ -e "${GPACK}_tmp.root" ]
then
  echo " ERROR -- kraken production failed. No output file: ${GPACK}_tmp.root"
  echo "          EXIT(254) now because there is no KRAKEN file."
  exit 254
fi

showDiskSpace

####################################################################################################
# push our files out to the Tier-2 / Dropbox
####################################################################################################

cd $WORKDIR
pwd
ls -lhrt

# define base output location
REMOTE_SERVER="se01.cmsaf.mit.edu"
REMOTE_BASE="srm/v2/server?SFN=/mnt/hadoop/cms/store"
REMOTE_USER_DIR="/user/paus/$CONFIG/$VERSION"

sample=`echo $GPACK | sed 's/\(.*\)_nev.*/\1/'`

# this is somewhat overkill but works very reliably, I suppose
#setupCmssw 7_6_3 # should work with new releases... right?
tar fzx $CMSSW_BASE/tgz/copy.tgz
pwd=`pwd`
for file in `echo ${GPACK}*`
do
  # always first show the proxy
  voms-proxy-info -all
  # now do the copy
  ./cmscp.py --debug \
    --middleware OSG --PNN $REMOTE_SERVER --se_name $REMOTE_SERVER \
    --inputFileList $pwd/${file} \
    --destination srm://$REMOTE_SERVER:8443/${REMOTE_BASE}${REMOTE_USER_DIR}/${TASK}/${CRAB} \
    --for_lfn ${REMOTE_USER_DIR}/${TASK}/${CRAB}
  rcCmsCp=$?
  echo " Copying: $file"
  echo " Copy RC: $rcCmsCp"
  if [ "$rcCmsCp" != "0" ]
  then
    # now do the backup copy
    echo "Remove file remainders: srm-rm  srm://$REMOTE_SERVER:8443/${REMOTE_BASE}${REMOTE_USER_DIR}/${TASK}/${CRAB}/${file}"
    srm-rm  srm://$REMOTE_SERVER:8443/${REMOTE_BASE}${REMOTE_USER_DIR}/${TASK}/${CRAB}/${file}
    rcSrmRm=$?
    echo " Remove RC: $rcSrmRm"
    echo " Try again: cmscp.py .... srm://$REMOTE_SERVER:8443/${REMOTE_BASE}${REMOTE_USER_DIR}/${TASK}/${CRAB}/${file}"
    ./cmscp.py --debug \
      --middleware OSG --PNN $REMOTE_SERVER --se_name $REMOTE_SERVER \
      --inputFileList $pwd/${file} \
      --destination srm://$REMOTE_SERVER:8443/${REMOTE_BASE}${REMOTE_USER_DIR}/${TASK}/${CRAB} \
      --for_lfn ${REMOTE_USER_DIR}/${TASK}/${CRAB}
    rcCmsCp=$?
    echo " ReCopying: $file"
    echo " ReCopy RC: $rcCmsCp"
  fi
done

# make condor happy because it also might want some of the files
executeCmd mv $WORKDIR/*.root $BASEDIR/

# leave the worker super clean

testBatch
if [ "$?" == "1" ]
then
  cd $BASEDIR
  executeCmd rm -rf $WORKDIR *.root
fi

# create the pickup output file for condor

echo " ---- D O N E ----" > $BASEDIR/${GPACK}.empty

pwd
ls -lhrt
echo " ---- D O N E ----"

exit 0
