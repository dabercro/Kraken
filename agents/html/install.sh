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

# images
echo " Copy images from $KRAKEN_BASE"
cp $KRAKEN_BASE/agents/html/agent*jpg $KRAKEN_AGENTS_LOG

# global index files to log area
#echo " Generate index files"
#cp $KRAKEN_BASE/agents/html/index-kraken.php $KRAKEN_AGENTS_LOG
echo " Generate index files"
cp $KRAKEN_BASE/agents/html/index.php $KRAKEN_AGENTS_LOG

# agent specific index files
cat $KRAKEN_BASE/agents/html/index.php-Template \
   | sed 's/XX-NAME-XX/reviewd/g' | sed 's/XX-AKA-XX/Smith/' \
   > $KRAKEN_AGENTS_LOG/reviewd/index.php
cat $KRAKEN_BASE/agents/html/index.php-Template \
   | sed 's/XX-NAME-XX/catalogd/g' | sed 's/XX-AKA-XX/Johnson/' \
   > $KRAKEN_AGENTS_LOG/catalogd/index.php

# update web pages from log area
echo " Sync files to the web area - no deletions"
echo " - $KRAKEN_AGENTS_LOG --> $KRAKEN_AGENTS_WWW/../"
mkdir -p $KRAKEN_AGENTS_WWW 
rsync -Cavz $KRAKEN_AGENTS_LOG $KRAKEN_AGENTS_WWW/../

chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $KRAKEN_AGENTS_LOG $KRAKEN_AGENTS_WWW

exit 0
