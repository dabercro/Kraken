# $Id: cmssw.py,v 1.3 2010/10/06 14:09:40 paus Exp $

import FWCore.ParameterSet.Config as cms

process = cms.Process('FILEFI')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.configurationMetadata = cms.untracked.PSet(
    version    = cms.untracked.string('Mit_014e'),
    annotation = cms.untracked.string('RECOSIM'),
    name       = cms.untracked.string('BambuProduction')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
   Rethrow  = cms.untracked.vstring('ProductNotFound'),
   fileMode = cms.untracked.string('NOMERGE')
)

# input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
   'file:/build/bendavid/RECOSIMSummer09/TTbar_Summer09-MC_3XY_V25_preproduction-v1/969AE5D9-DA2B-DF11-931D-001CC4C10E02.root'
   )
)
process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*", "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT")

# other statements
process.GlobalTag.globaltag = 'START38_V12::All'

# load MitTreeFiller 
process.add_(cms.Service("ObjectService"))

process.load("MitProd.BAMBUSequences.BambuFillRECOSIM_cfi")

# set the name for the output file
process.MitTreeFiller.TreeWriter.fileName = 'XX-MITDATASET-XX'
process.MitTreeFiller.TreeWriter.maxSize  = cms.untracked.uint32(1790)

process.bambu_step  = cms.Path(process.BambuFillRECOSIM)

# schedule definition
process.schedule = cms.Schedule(process.bambu_step)
