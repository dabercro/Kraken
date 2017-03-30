# Where does stuff come from

myRoot=/home/$USER
pkgRoot=/home/cmsprod/Tools

# Kraken parameters (edit as needed)

# this is mostly used for the agents
export KRAKEN_USER=cmsprod
export KRAKEN_GROUP=zh

# user for submit (can be different from Tier-3)
export KRAKEN_REMOTE_USER=paus
export KRAKEN_BASE=$pkgRoot/Kraken
export KRAKEN_WORK=$myRoot/cms/jobs
export KRAKEN_SCRIPT=releaseKraken.sh
export KRAKEN_EXE=cmsRun
export KRAKEN_CMSSW=$myRoot/cms/cmssw

export KRAKEN_SE_BASE=/cms/store/user/paus
export KRAKEN_CATALOG=/home/cmsprod/catalog/t2mit

export PATH=${PATH}:${KRAKEN_BASE}/bin
export PYTHONPATH=${PYTHONPATH}:${KRAKEN_BASE}/python

# other packages needed
source $pkgRoot/Dools/setup.sh
source $pkgRoot/FiBS/setup.sh
source $pkgRoot/T2Tools/setup.sh

# access to Tier-2
export TICKET_HOLDER="paus"
export TIER2_USER="paus"

# bad fix but needed so curl works with cmsweb
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/curl/7.47.1/etc/profile.d/init.sh
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/openssl/1.0.2d/etc/profile.d/init.sh
