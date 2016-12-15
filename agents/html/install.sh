#!/bin/bash
#---------------------------------------------------------------------------------------------------
# Install the web environment (should be done once at installation phase only). Make sure the
# environment is setup correctly
# 
#
# Author: C.Paus                                                                     (May 14, 2015)
#---------------------------------------------------------------------------------------------------
OPTION="$1"
source $KRAKEN_BASE/agents/setupAgents.sh
source $KRAKEN_BASE/agents/cycle.cfg

# Message at the begining
echo " "
echo " $0 -> installing the web pages"
echo " "

# loop over all requested configurations
for reqset in $KRAKEN_REVIEW_CYCLE
do

  echo " ReqSet: $reqset"

  cfg=`echo $reqset | cut -d: -f1`
  vrs=`echo $reqset | cut -d: -f2`
  pys=`echo $reqset | cut -d: -f3`


  # images
  echo " Copy images from $KRAKEN_BASE"
  cp $KRAKEN_BASE/agents/html/agent*jpg $KRAKEN_AGENTS_WWW/$cfg/$vrs
  
  # index files to log area
  echo " Generate index files"
  cp $KRAKEN_BASE/agents/html/index.php $KRAKEN_AGENTS_LOG/$cfg/$vrs
  
  cat $KRAKEN_BASE/agents/html/index.php-Template \
     | sed 's/XX-NAME-XX/reviewd/g' | sed 's/XX-AKA-XX/Smith/' \
     > $KRAKEN_AGENTS_LOG/reviewd/index.php
  cat $KRAKEN_BASE/agents/html/index.php-Template \
     | sed 's/XX-NAME-XX/catalogd/g' | sed 's/XX-AKA-XX/Johnson/' \
     > $KRAKEN_AGENTS_LOG/catalogd/index.php


  for py in `echo $pys | tr ',' ' '`
  do
    echo " -adding->  %py"
  done

done



# update web pages from log area
echo " Sync files to the web area - no deletions"
echo " - $KRAKEN_AGENTS_LOG --> $KRAKEN_AGENTS_WWW/../"
mkdir -p $KRAKEN_AGENTS_WWW 
rsync -Cavz $KRAKEN_AGENTS_LOG $KRAKEN_AGENTS_WWW/../

chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $KRAKEN_AGENTS_LOG $KRAKEN_AGENTS_WWW

exit 0
