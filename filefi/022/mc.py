# $Id: mc.py,v 1.1.2.1 2011/04/24 05:03:32 paus Exp $

import FWCore.ParameterSet.Config as cms

process = cms.Process('FILEFI')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version    = cms.untracked.string('Mit_021'),
    annotation = cms.untracked.string('AODSIM'),
    name       = cms.untracked.string('BambuProduction')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
   Rethrow = cms.untracked.vstring('ProductNotFound'),
   fileMode = cms.untracked.string('NOMERGE'),
)

# input source
process.source = cms.Source("PoolSource",
#  fileNames = cms.untracked.vstring('file:/data/blue/bendavid/392aodsim/62FE6208-38E8-DF11-A912-0018F3D09648.root')
   fileNames = cms.untracked.vstring('/store/relval/CMSSW_4_2_1/RelValProdTTbar/AODSIM/MC_42_V10-v1/0030/48D6019C-6D67-E011-9083-002618943856.root')
)
process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*", "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT")

# other statements
process.GlobalTag.globaltag = 'START42_V12::All'

process.add_(cms.Service("ObjectService"))

process.load("MitProd.BAMBUSequences.BambuFillAODSIM_cfi")

process.MitTreeFiller.TreeWriter.fileName = 'XX-MITDATASET-XX'
process.MitTreeFiller.TreeWriter.maxSize  = cms.untracked.uint32(1790)

process.bambu_step  = cms.Path(process.BambuFillAODSIM)

# schedule definition
process.schedule = cms.Schedule(process.bambu_step)
