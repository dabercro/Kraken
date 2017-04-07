# Where does stuff come from

myRoot=/home/dabercro
pkgRoot=/home/cmsprod/Tools

# Kraken parameters (edit as needed)

# this is mostly used for the agents
export KRAKEN_USER=dabercro
export KRAKEN_GROUP=zh

# user for submit (can be different from Tier-3)
export KRAKEN_REMOTE_USER=dabercro
export KRAKEN_BASE=$myRoot/Panda/Kraken
export KRAKEN_WORK=$myRoot/cms/jobs
export KRAKEN_SCRIPT=releaseKraken.sh
export KRAKEN_EXE=slimmer
export KRAKEN_CMSSW=$myRoot/cms/cmssw

export KRAKEN_SE_BASE=/cms/store/user/paus
export KRAKEN_CATALOG_INPUT=/home/cmsprod/catalog/t2mit
export KRAKEN_CATALOG_OUTPUT=/home/dabercro/catalog/t2mit

export PATH=${PATH}:${KRAKEN_BASE}/bin
export PYTHONPATH=${PYTHONPATH}:${KRAKEN_BASE}/python

# other packages needed
source $pkgRoot/Dools/setup.sh
source $pkgRoot/T2Tools/setup.sh

# access to Tier-2
export T2TOOLS_USER="dabercro"
export T2TOOLS_TICKET="dabercro"

# bad fix but needed so curl works with cmsweb
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/curl/7.47.1/etc/profile.d/init.sh
source /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/openssl/1.0.2d/etc/profile.d/init.sh
