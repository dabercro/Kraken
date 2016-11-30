import FWCore.ParameterSet.Config as cms

#---------------------------------------------------------------------------------------------------
#                                           M A I N
#---------------------------------------------------------------------------------------------------
# create the process
process = cms.Process('FILEFI')

# say how many events to process (-1 means no limit)
process.maxEvents = cms.untracked.PSet(
  #input = cms.untracked.int32(100)
  input = cms.untracked.int32(-1)
)

#>> input source

process.source = cms.Source(
  "PoolSource",
  fileNames = cms.untracked.vstring(
        'root://xrootd.unl.edu//store/user/dmytro/POWHEG_DMS_NNPDF30_13TeV_Scalar_1000_1/RunIISpring15DR74/150625_192020/0000/xAODSIM_27.root'
  )
)
process.source.inputCommands = cms.untracked.vstring(
  "keep *"
)

#>> configurations

# determine the global tag to use
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = 'MCRUN2_74_V9'

# define meta data for this production
process.configurationMetadata = cms.untracked.PSet(
  name       = cms.untracked.string('BambuProd'),
  version    = cms.untracked.string('Mit_041'),
  annotation = cms.untracked.string('MINIAODSIM')
)

#>> standard sequences

# load some standard sequences we will need
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')

# define sequence for ProductNotFound
process.options = cms.untracked.PSet(
  Rethrow = cms.untracked.vstring('ProductNotFound'),
  fileMode = cms.untracked.string('NOMERGE'),
)

# Import/Load the filler so all is already available for config changes
from MitProd.TreeFiller.MitTreeFiller_cfi import MitTreeFiller
process.load('MitProd.TreeFiller.MitTreeFiller_cfi')

from MitProd.TreeFiller.utils.configureForMiniAOD import configureForMiniAOD
configureForMiniAOD(MitTreeFiller)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               R E C O  S E Q U E N C E
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# change of source on kt6 must come before loading l1FastJetSequence
from RecoJets.Configuration.RecoPFJets_cff import kt6PFJets, ak4PFJets, ak8PFJets
ak4PFJets.src = 'packedPFCandidates'
ak8PFJets.src = 'packedPFCandidates'
kt6PFJets.src = 'packedPFCandidates'

# Load FastJet L1 corrections
from MitProd.TreeFiller.FastJetCorrection_cff import l1FastJetSequence, l1FastJetSequenceCHS
process.load('MitProd.TreeFiller.FastJetCorrection_cff')

# Load PF CHS using PackedCandidates
from MitProd.TreeFiller.pfCHSFromPacked_cff import pfCHSSequence
process.load('MitProd.TreeFiller.pfCHSFromPacked_cff')

# Load tracking off packedCandidates
from PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi import unpackedTracksAndVertices
process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

# Load btagging
from MitProd.TreeFiller.utils.setupBTag import setupBTag
ak4PFBTagSequence = setupBTag(process, 'ak4PFJets', 'AKt4PF',
                              candidates = 'packedPFCandidates',
                              primaryVertex = 'offlineSlimmedPrimaryVertices',
                              muons = 'slimmedMuons',
                              electrons = 'slimmedElectrons')

from RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff import inclusiveVertexing,inclusiveCandidateVertexing
process.load('RecoVertex/AdaptiveVertexFinder/inclusiveVertexing_cff')


#> Setup jet corrections
process.load('JetMETCorrections.Configuration.JetCorrectionServices_cff')

#> The bambu reco sequence
recoSequence = cms.Sequence(
  unpackedTracksAndVertices *
  pfCHSSequence *
  l1FastJetSequence *
  l1FastJetSequenceCHS *
  ak4PFJets *
  ak8PFJets *
  ak4PFBTagSequence *
  inclusiveVertexing *
  inclusiveCandidateVertexing
)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               G E N  S E Q U E N C E
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Import/Load genjets
from RecoJets.Configuration.GenJetParticles_cff import *
process.load('RecoJets.Configuration.GenJetParticles_cff')
from RecoJets.Configuration.RecoGenJets_cff import ak4GenJets, ak8GenJets
process.load('RecoJets.Configuration.RecoGenJets_cff')

genParticlesForJets.src = 'packedGenParticles'
genParticlesForJets.isMiniAOD = cms.bool(True)

genSequence = cms.Sequence(
  genParticlesForJets *
  ak4GenJets *
  ak8GenJets
)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               B A M B U  S E Q U E N C E
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# remember the bambu sequence has been imported and loaded already in the beginning

# configure the filler
MitTreeFiller.TreeWriter.fileName = 'bambu-output-file-tmp'
MitTreeFiller.PileupInfo.active = True
MitTreeFiller.MCParticles.active = True
MitTreeFiller.MCEventInfo.active = True
MitTreeFiller.MCVertexes.active = True

# NOTRIG - special
MitTreeFiller.Trigger.active = False
MitTreeFiller.EvtSelData.active = False

# define fill bambu filler sequence

bambuFillerSequence = cms.Sequence(
  MitTreeFiller
)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               C M S S W  P A T H
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

process.path = cms.Path(
  recoSequence *
  genSequence *
  bambuFillerSequence
)

process.schedule = cms.Schedule(process.path)
process.prune()
