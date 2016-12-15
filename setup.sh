export KRAKEN_BASE=$HOME/Tools/Kraken
export KRAKEN_WORK=$HOME/cms/jobs
export KRAKEN_SCRIPT=releaseKraken.sh
export KRAKEN_CMSSW=$HOME/cms/cmssw

export KRAKEN_SE_BASE=/cms/store/user/paus

export PATH=${PATH}:${KRAKEN_BASE}/bin
export PYTHONPATH=${PYTHONPATH}:${KRAKEN_BASE}/python

# bad fix but needed so curl works with cmsweb
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/curl/7.47.1/etc/profile.d/init.sh
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/openssl/1.0.2d/etc/profile.d/init.sh
