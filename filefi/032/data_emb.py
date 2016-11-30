# $Id: data_emb.py,v 1.2 2013/07/26 14:53:31 paus Exp $

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
  version    = cms.untracked.string('Mit_029'),
  annotation = cms.untracked.string('AOD'),
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
  fileNames = cms.untracked.vstring('/store/results/tau-pflow/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/DoubleMuParked/USER/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau115_ptelec1_20had1_18_v1-5ef1c0fd428eb740081f19333520fdc8/0000/FEDB3320-CEE7-E211-8BED-0023AEFDEE84.root')
)
#process.source.inputCommands = cms.untracked.vstring("keep *",
#                                                     "drop *_MEtoEDMConverter_*_*",
#                                                     "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT")

# other statements
process.GlobalTag.globaltag = 'START53_V15::All'

process.add_(cms.Service("ObjectService"))

process.load("MitProd.BAMBUSequences.BambuFillAOD_cfi")

#process.MitTreeFiller.TreeWriter.fileName = 'XX-MITDATASET-XX'
process.MitTreeFiller.TreeWriter.fileName = 'bambu-output-file-tmp'

process.load('TauAnalysis/MCEmbeddingTools/embeddingKineReweight_cff')
process.embeddingKineReweightRECembedding.inputFileName = cms.FileInPath('TauAnalysis/MCEmbeddingTools/data/embeddingKineReweight_recEmbedding_mutau.root')
# process.embeddingKineReweightRECembedding.inputFileName = cms.FileInPath('TauAnalysis/MCEmbeddingTools/data/embeddingKineReweight_recEmbedding_etau.root')
# process.embeddingKineReweightRECembedding.inputFileName = cms.FileInPath('TauAnalysis/MCEmbeddingTools/data/embeddingKineReweight_recEmbedding_emu.root')

from MitProd.TreeFiller.filltauembedded_cff import *
filltauembedded(process.MitTreeFiller)
process.MitTreeFiller.MergedConversions.checkTrackRef           = cms.untracked.bool(False)
process.MitTreeFiller.EmbedWeight.useGenInfo                    = True
process.MitTreeFiller.EmbedWeight.useRecHit                     = False
process.MitTreeFiller.MergedEmbeddedTracks.edmName              = 'tmfTracks'
process.MitTreeFiller.MergedEmbeddedTracks.trackMapName         = 'tmfTracksMapName'
process.MitTreeFiller.PrimaryVertexes.trackMapName              = 'tmfTracksMapName'
process.MitTreeFiller.PrimaryVertexesBS.trackMapName            = 'tmfTracksMapName'
process.MitTreeFiller.PFCandidates.trackerTrackMapNames         = cms.untracked.vstring('tmfTracksMapName')
process.MitTreeFiller.ShrinkingConePFTaus.trackMapNames         = cms.untracked.vstring('tmfTracksMapName')
process.MitTreeFiller.HPSTaus.trackMapNames                     = cms.untracked.vstring('tmfTracksMapName')
#process.MitTreeFiller.Electrons.trackerTrackMapName             = 'tmfTracksMapName'
process.MitTreeFiller.Electrons.trackerTrackMapName             = 'TracksMapName'
process.MitTreeFiller.PFCandidates.gsfTrackMapName              = ''
process.MitTreeFiller.PFCandidates.allowMissingPhotonRef        = True
process.newJetTracksAssociatorAtVertex.tracks = "tmfTracks"
process.bambu_step  = cms.Path(process.BambuFillAOD)
# schedule definition
process.schedule = cms.Schedule(process.bambu_step)
