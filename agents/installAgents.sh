#!/bin/bash
# --------------------------------------------------------------------------------------------------
#
# Installation script for MitProd/Processing/agents. There will be lots of things to test and to
# fix, but this is the starting point. This installation has to be performed as user root.
#
#                                                                Ch.Paus: Version 0.0 (Apr 27, 2015)
# --------------------------------------------------------------------------------------------------

function init {
  # function to initialize the local environment
  source ../setup.sh
  source setupAgents.sh
  source ../../FiBS/setup.sh
}

function install {
  # function that will install the daemon named as the given first parameter
  #   example: install reviewd

  # command line parameter
  daemon="$1"

  # make sure directories exist
  mkdir -p $KRAKEN_AGENTS_LOG/${daemon}
  chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $KRAKEN_AGENTS_LOG

  # stop potentially existing server process
  if [ -e "/etc/init.d/${daemon}" ]
  then
    /etc/init.d/${daemon} status
    /etc/init.d/${daemon} stop
  fi
  
  # copy daemon
  cp $KRAKEN_AGENTS_BASE/sysv/${daemon} /etc/init.d/
  
  # start new server
  /etc/init.d/${daemon} status
  /etc/init.d/${daemon} start
  sleep 2
  /etc/init.d/${daemon} status
  
  # start on boot
  chkconfig --level 345 ${daemon} on
}

#---------------------------------------------------------------------------------------------------
#                                               M A I N
#---------------------------------------------------------------------------------------------------
init

# General installation (you have to be in the directory of install script and you have to be root)

TRUNC=`dirname $KRAKEN_AGENTS_BASE`
if ! [ -d "$TRUNC" ]
then
  mkdir -p "$TRUNC"
  chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $TRUNC
fi

# copy the software
#==================

if [ -d "$KRAKEN_AGENTS_BASE" ]
then
  # make sure to remove completely the previous installed software
  echo " Removing previous installation."
  rm -rf "$KRAKEN_AGENTS_BASE"
fi
cp -r ../agents "$TRUNC"
chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $KRAKEN_AGENTS_BASE

# create log/db structure
#========================
# owner has to be $KRAKEN_USER:$KRAKEN_GROUP, this user runs the process
mkdir -p $KRAKEN_AGENTS_LOG
chown ${KRAKEN_USER}:${KRAKEN_GROUP} -R $KRAKEN_AGENTS_LOG

# install and start daemons
#==========================

install reviewd
install catalogd

# install web pages
#==================

su - ${KRAKEN_USER} -c $KRAKEN_AGENTS_BASE/html/install.sh

exit 0
