#!/bin/bash

cd $CMSSW_BASE/src

git clone -n -b CMSSW_8_0_X-METFilterUpdate https://github.com/cms-met/cmssw.git
cd cmssw
git checkout HEAD RecoMET/METFilters
mv RecoMET ../
cd $CMSSW_BASE/src
rm -rf cmssw

scram b -j12
