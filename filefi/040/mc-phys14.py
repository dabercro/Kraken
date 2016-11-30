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
  # make sure this is for the right version
  fileNames = cms.untracked.vstring('file:/mnt/hadoop/cmsprod/00165B45-82E6-E311-B68D-002590AC4FEC.root')
)
process.source.inputCommands = cms.untracked.vstring(
  "keep *",
  "drop *_MEtoEDMConverter_*_*",
  "drop L1GlobalTriggerObjectMapRecord_hltL1GtObjectMap__HLT"
)

#>> configurations

# determine the global tag to use
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MCRUN2_74_V6::All'

# define meta data for this production
process.configurationMetadata = cms.untracked.PSet(
  name       = cms.untracked.string('BambuProd'),
  version    = cms.untracked.string('Mit_040'),
  annotation = cms.untracked.string('AODSIM')
)

#>> standard sequences

# load some standard sequences we will need
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi')
process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')

# define sequence for ProductNotFound
process.options = cms.untracked.PSet(
  Rethrow = cms.untracked.vstring('ProductNotFound'),
  fileMode = cms.untracked.string('NOMERGE'),
)


# Import/Load the filler so all is already available for config changes
from MitProd.TreeFiller.MitTreeFiller_cfi import *
process.load('MitProd.TreeFiller.MitTreeFiller_cfi')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               R E C O  S E Q U E N C E
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

## Load jet reco producers
from RecoJets.Configuration.RecoJets_cff import *
process.load('RecoJets.Configuration.RecoJets_cff')

## Load particle flow jet reco producers
from RecoJets.Configuration.RecoPFJets_cff import *
process.load('RecoJets.Configuration.RecoPFJets_cff')

## Load stablePart producers
from MitEdm.Producers.conversionElectronsStable_cfi import *
process.load('MitEdm.Producers.conversionElectronsStable_cfi')

# Load Mit Mvf Conversion producer
from MitProd.TreeFiller.conversionProducer_cff import *

# Electron likelihood-based id
from RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi import *
process.load('RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi')
MitTreeFiller.Electrons.eIDLikelihoodName = 'eidLikelihoodExt'

# Load FastJet L1 corrections
from MitProd.TreeFiller.FastJetCorrection_cff import *
process.load('MitProd.TreeFiller.FastJetCorrection_cff')

# Load btagging
from MitProd.TreeFiller.newbtagging_cff import *
process.load('MitProd.TreeFiller.newbtagging_cff')

# Load basic particle flow collections
from CommonTools.ParticleFlow.pfMET_cfi  import *
from CommonTools.ParticleFlow.pfParticleSelection_cff import *
from CommonTools.ParticleFlow.pfNoPileUp_cff  import *
from CommonTools.ParticleFlow.pfPhotons_cff import *
from CommonTools.ParticleFlow.pfElectrons_cff import *
from CommonTools.ParticleFlow.pfMuons_cff import *
from CommonTools.ParticleFlow.pfJets_cff import *
from CommonTools.ParticleFlow.pfTaus_cff import *
from CommonTools.ParticleFlow.TopProjectors.pfNoMuon_cfi import * 
from CommonTools.ParticleFlow.TopProjectors.pfNoElectron_cfi import * 
from CommonTools.ParticleFlow.TopProjectors.pfNoJet_cff import *
from CommonTools.ParticleFlow.TopProjectors.pfNoTau_cff import *

process.load('CommonTools.ParticleFlow.pfMET_cfi')
process.load('CommonTools.ParticleFlow.pfParticleSelection_cff')
process.load('CommonTools.ParticleFlow.pfNoPileUp_cff')
process.load('CommonTools.ParticleFlow.pfPhotons_cff')
process.load('CommonTools.ParticleFlow.pfElectrons_cff')
process.load('CommonTools.ParticleFlow.pfMuons_cff')
process.load('CommonTools.ParticleFlow.pfJets_cff')
process.load('CommonTools.ParticleFlow.pfTaus_cff')
process.load('CommonTools.ParticleFlow.TopProjectors.pfNoMuon_cfi') 
process.load('CommonTools.ParticleFlow.TopProjectors.pfNoElectron_cfi') 
process.load('CommonTools.ParticleFlow.TopProjectors.pfNoJet_cff')
process.load('CommonTools.ParticleFlow.TopProjectors.pfNoTau_cff')

# Load the collections to remake more specialized jets
from CommonTools.ParticleFlow.ParticleSelectors.pfAllChargedHadrons_cfi import *
from CommonTools.ParticleFlow.ParticleSelectors.pfAllNeutralHadrons_cfi import *
from CommonTools.ParticleFlow.ParticleSelectors.pfAllNeutralHadronsAndPhotons_cfi import *
process.load('CommonTools.ParticleFlow.ParticleSelectors.pfAllChargedHadrons_cfi')
process.load('CommonTools.ParticleFlow.ParticleSelectors.pfAllNeutralHadrons_cfi')
process.load('CommonTools.ParticleFlow.ParticleSelectors.pfAllNeutralHadronsAndPhotons_cfi')

# Loading PFProducer to get the ptrs
from RecoParticleFlow.PFProducer.pfLinker_cff import particleFlowPtrs
process.load('RecoParticleFlow.PFProducer.pfLinker_cff')

# Load generator tools
from CommonTools.ParticleFlow.genForPF2PAT_cff import *
process.load('CommonTools.ParticleFlow.genForPF2PAT_cff')

pfPileUp.PFCandidates = 'particleFlowPtrs'
pfNoPileUp.bottomCollection = 'particleFlowPtrs'
pfPileUpIso.PFCandidates = 'particleFlowPtrs' 
pfNoPileUpIso.bottomCollection='particleFlowPtrs'
pfPileUpJME.PFCandidates = 'particleFlowPtrs' 
pfNoPileUpJME.bottomCollection='particleFlowPtrs'

pfPileUp.Enable = True
pfPileUp.Vertices = 'goodOfflinePrimaryVertices'
pfPileUp.checkClosestZVertex = cms.bool(False)
pfJets.doAreaFastjet = True
pfJets.doRhoFastjet = False

#> Setup the met filters
from MitProd.TreeFiller.metFilters_cff import *
process.load('MitProd.TreeFiller.metFilters_cff')

#> The bambu reco sequence
recoSequence = cms.Sequence(
  electronsStable *
  eidLikelihoodExt *
  newBtaggingAll *
  goodOfflinePrimaryVertices *
  particleFlowPtrs *
  pfNoPileUpSequence *
  pfNoPileUpJMESequence *
  pfParticleSelectionSequence * 
  pfPhotonSequence *
  pfMuonSequence * 
  pfNoMuon *
  pfNoMuonJME *
  pfElectronSequence *
  pfNoElectron *
  pfNoElectronJME *
  pfNoElectronJMEClones*
  pfJetSequence *
  pfNoJet * 
  pfTauSequence *
  pfNoTau *
  pfMET *
  pfAllNeutralHadrons *
  pfAllChargedHadrons *
  pfAllNeutralHadronsAndPhotons *
  kt6PFJets *
  kt6PFJetsCentralChargedPileUp *
  kt6PFJetsCentralNeutral *
  kt6PFJetsCentralNeutralTight *
  ak4PFJets *
  l1FastJetSequence *
  l1FastJetSequenceCHS *
  metFilters
)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#
#                               G E N  S E Q U E N C E
#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Import/Load genjets
from RecoJets.Configuration.GenJetParticles_cff import *
process.load('RecoJets.Configuration.GenJetParticles_cff')
from RecoJets.Configuration.RecoGenJets_cff import *
process.load('RecoJets.Configuration.RecoGenJets_cff')

genSequence = cms.Sequence(
  genJetParticles *
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
#MitTreeFiller.TreeWriter.fileName = 'XX-MITDATASET-XX'
MitTreeFiller.TreeWriter.fileName = 'bambu-output-file-tmp'
MitTreeFiller.PileupInfo.active = True
MitTreeFiller.MCParticles.active = True
MitTreeFiller.MCEventInfo.active = True
MitTreeFiller.MCVertexes.active = True

# for PHYS14
MitTreeFiller.GlobalCosmicMuonTracks.edmName = "globalCosmicMuons"

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
