#!/bin/sh
#===================================================================================================
#
# Script to run a cmsRun job file by file.
#
#===================================================================================================

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX id; env; pwd"
id; env; pwd

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ls -lhrt"
ls -lhrt

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ls -lhrt *"
ls -lhrt *

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX find ./"
find ./

# Here is where our stuff happens

export      JOBID=$1
export    DATADIR=$2
export InputFiles=`head -$JOBID *.lfns_* | tail -1`

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "Produce the input files: $InputFiles"
echo "  input files: $InputFiles"

echo " XXXXXXXXXXXXXXXXXXX"
cat pset.py
echo " XXXXXXXXXXXXXXXXXXX"
echo \
  python ./wCfg.py pset.py cmssw_ex.py
echo " XXXXXXXXXXXXXXXXXXX"

python ./wCfg.py pset.py cmssw_ex.py

echo ""
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "Python file: cmssw_ex.py"
## cat cmssw_ex.py

echo ""
echo "Start running at `date -u`"
echo ""
start_exe_time=`date +%s`
CPU_INFOS=-1

/usr/bin/time       \
  -f "%U %S %P"     \
  -o cpu_timing.txt \
  cmsRun            \
  -j ${RUNTIME_AREA}/crab_fjr_${JOBID}.xml \
  -p cmssw_ex.py

cmsrun_exit_status=$?

CPU_INFOS=`tail -n 1 cpu_timing.txt`
stop_exe_time=`date +%s`

echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "Running ended at `date -u`"
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo ""

echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "Present working directory is `pwd`"
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo ""

echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo "Directory content is `ls -l`"
echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
echo ""

exit 0
