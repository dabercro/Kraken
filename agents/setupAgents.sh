#---------------------------------------------------------------------------------------------------
#
# ==== MAIN PARAMETERS FOR KRAKEN AGENTS ====
#
#---------------------------------------------------------------------------------------------------
# Environment: CMSSW, CRAB etc.

# find latest MIT/CMSSW versions
export MIT_VERS=`ls -1 ~cmsprod/cms/cmssw| grep ^[0-9]| tail -1`
export MIT_TAG=Mit_$MIT_VERS
export LATEST_CMSSW=`ls -rt ~cmsprod/cms/cmssw/$MIT_VERS| grep ^CMSSW_[0-9] | tail -1`

# general agents info

export KRAKEN_AGENTS_BASE="/usr/local/Kraken/agents"
export KRAKEN_AGENTS_WORK="/home/$KRAKEN_USER/cms/jobs"
export KRAKEN_AGENTS_LOG="/local/$KRAKEN_USER/Kraken/agents"
export KRAKEN_AGENTS_WWW="/home/$KRAKEN_USER/public_html/Kraken/agents"

# review process

export KRAKEN_REVIEW_CYCLE_HOURS=1
export KRAKEN_REVIEW_PYS="data mc"
export KRAKEN_REVIEW_OLD_JOBS_AGE=7200 # In seconds

# catalog process

export KRAKEN_CATALOG_CYCLE_SECONDS=300
