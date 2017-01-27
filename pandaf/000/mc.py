import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import re
import os

process = cms.Process("PandaNtupler")
cmssw_base = os.environ['CMSSW_BASE']

options = VarParsing.VarParsing ('analysis')
options.register('isData',
                 False,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "True if running on Data, False if running on MC")

options.register('isSignal',
                 True,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.bool,
                 "True if running on MC signal samples")

options.parseArguments()
isData = options.isData

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# ---- define the input file --------------------------------------------
process.source = cms.Source(
	"PoolSource", fileNames = cms.untracked.vstring('XX-LFN-XX')
	)

# ---- define the output file -------------------------------------------
process.TFileService = cms.Service(
	"TFileService",
	closeFileFast = cms.untracked.bool(True),
	fileName = cms.string("kraken-output-file-tmp_000.root"),
	)

##----------------GLOBAL TAG ---------------------------
# used by photon id and jets
process.load("Configuration.Geometry.GeometryIdeal_cff") 
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
if (isData):
    process.GlobalTag.globaltag = '80X_dataRun2_2016SeptRepro_v3'
else:
    process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v6'

### LOAD DATABASE
from CondCore.DBCommon.CondDBSetup_cfi import *
#from CondCore.CondDB.CondDB_cfi import *

######## LUMI MASK
if isData and False:
		import FWCore.PythonUtilities.LumiList as LumiList
		process.source.lumisToProcess = LumiList.LumiList(filename='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt').getVLuminosityBlockRange()
		print "Using local JSON"

### LOAD CONFIGURATION
process.load('PandaProd.Filter.infoProducerSequence_cff')
process.load('PandaProd.Filter.MonoXFilterSequence_cff')
process.load('PandaProd.Ntupler.PandaProd_cfi')
#process.load('PandaProd.Ntupler.VBF_cfi')

process.PandaNtupler.isData = isData
if isData:
	process.triggerFilter = cms.EDFilter('TriggerFilter',
																triggerPaths = process.PandaNtupler.triggerPaths,
																trigger = process.PandaNtupler.trigger
															)
	process.triggerFilterSequence = cms.Sequence( process.triggerFilter )
else:
	process.triggerFilterSequence = cms.Sequence()

if options.isSignal:
	process.PandaNtupler.nSystWeight = -1

#-----------------------JES/JER----------------------------------
if isData:
    jeclabel = 'Spring16_23Sep2016AllV2_DATA'
else:
    jeclabel = 'Spring16_23Sep2016V2_MC'
    process.jec = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               timetype = cms.string('runnumber'),
                               toGet = cms.VPSet(
            cms.PSet(record = cms.string('JetCorrectionsRecord'),
                     tag = cms.string('JetCorrectorParametersCollection_'+jeclabel+'_AK4PFPuppi'),
                     label = cms.untracked.string('AK4Puppi')
                     ),
            cms.PSet(record = cms.string('JetCorrectionsRecord'),
                     tag = cms.string('JetCorrectorParametersCollection_'+jeclabel+'_AK8PFPuppi'),
                     label = cms.untracked.string('AK8Puppi')
                     ),
            cms.PSet(record = cms.string('JetCorrectionsRecord'),
                     tag = cms.string('JetCorrectorParametersCollection_'+jeclabel+'_AK4PFchs'),
                     label = cms.untracked.string('AK4chs')
                     ),
            cms.PSet(record = cms.string('JetCorrectionsRecord'),
                     tag = cms.string('JetCorrectorParametersCollection_'+jeclabel+'_AK8PFchs'),
                     label = cms.untracked.string('AK8chs')
                     ),
            ),
                               
                               )	

process.jec.connect = cms.string('sqlite:jec/%s.db'%jeclabel)
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

if isData:
	jerlabel = 'Spring16_25nsV6_DATA'
else:
	jerlabel = 'Spring16_25nsV6_MC'
process.jer = cms.ESSource("PoolDBESSource",
                  CondDBSetup,
                  toGet = cms.VPSet(
              cms.PSet(record  = cms.string('JetResolutionRcd'),
                       tag     = cms.string('JR_%s_PtResolution_AK4PFchs'%jerlabel),
                       label   = cms.untracked.string('AK4PFchs_pt'),
                      ),
              cms.PSet(record  = cms.string('JetResolutionRcd'),
                       tag     = cms.string('JR_%s_PhiResolution_AK4PFchs'%jerlabel),
                       label   = cms.untracked.string('AK4PFchs_phi'),
                      ),
              cms.PSet(record  = cms.string('JetResolutionScaleFactorRcd'),
                       tag     = cms.string('JR_%s_SF_AK4PFchs'%jerlabel),
                       label   = cms.untracked.string('AK4PFchs'),
                      ),
              cms.PSet(record  = cms.string('JetResolutionRcd'),
                       tag     = cms.string('JR_%s_PtResolution_AK4PFPuppi'%jerlabel),
                       label   = cms.untracked.string('AK4PFPuppi_pt'),
                      ),
              cms.PSet(record  = cms.string('JetResolutionRcd'),
                       tag     = cms.string('JR_%s_PhiResolution_AK4PFPuppi'%jerlabel),
                       label   = cms.untracked.string('AK4PFPuppi_phi'),
                      ),
              cms.PSet(record  = cms.string('JetResolutionScaleFactorRcd'),
                       tag     = cms.string('JR_%s_SF_AK4PFPuppi'%jerlabel),
                       label   = cms.untracked.string('AK4PFPuppi'),
                      ),
             )
        )
process.jer.connect = cms.string('sqlite:jer/%s.db'%jerlabel)
process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')


#-----------------------ELECTRON ID-------------------------------
from PandaProd.Ntupler.egammavid_cfi import *

initEGammaVID(process,options)

### ##ISO
process.load("RecoEgamma/PhotonIdentification/PhotonIDValueMapProducer_cfi")
process.load("RecoEgamma/ElectronIdentification/ElectronIDValueMapProducer_cfi")

#### RECOMPUTE JEC From GT ###
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
 
jecLevels= ['L1FastJet',  'L2Relative', 'L3Absolute']
if options.isData:
        jecLevels.append('L2L3Residual')
 
updateJetCollection(
    process,
    jetSource = process.PandaNtupler.chsAK4,
    labelName = 'UpdatedJEC',
    jetCorrections = ('AK4PFchs', cms.vstring(jecLevels), 'None')  
)

process.PandaNtupler.chsAK4=cms.InputTag('updatedPatJetsUpdatedJEC') # replace CHS with updated JEC-corrected

process.jecSequence = cms.Sequence( process.patJetCorrFactorsUpdatedJEC* process.updatedPatJetsUpdatedJEC)

########### MET Filter ################
process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.BadPFMuonFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.BadChargedCandidateFilter.taggingMode = cms.bool(True)

process.metfilterSequence = cms.Sequence(process.BadPFMuonFilter
                                          *process.BadChargedCandidateFilter)

if not options.isData:
  process.PandaNtupler.metfilter = cms.InputTag('TriggerResults','','PAT')

############ RECOMPUTE PUPPI/MET #######################
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
from PhysicsTools.PatAlgos.slimming.puppiForMET_cff import makePuppiesFromMiniAOD

makePuppiesFromMiniAOD(process,True)
process.puppi.useExistingWeights = False # I still don't trust miniaod...
process.puppiNoLep.useExistingWeights = False

runMetCorAndUncFromMiniAOD(process,         ## PF MET
                            isData=isData)
runMetCorAndUncFromMiniAOD(process,         ## Puppi MET
                           isData=options.isData,
                           metType="Puppi",
                           pfCandColl=cms.InputTag("puppiForMET"),
                           recoMetFromPFCs=True,
                           jetFlavor="AK4PFPuppi",
                           postfix="Puppi")
process.PandaNtupler.pfmet = cms.InputTag('slimmedMETs','','PandaNtupler')
process.PandaNtupler.puppimet = cms.InputTag('slimmedMETsPuppi','','PandaNtupler')
process.MonoXFilter.met = cms.InputTag('slimmedMETs','','PandaNtupler')
process.MonoXFilter.puppimet = cms.InputTag('slimmedMETsPuppi','','PandaNtupler')

############ RUN CLUSTERING ##########################
process.jetSequence = cms.Sequence()

# btag and patify puppi AK4 jets
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
from PhysicsTools.PatAlgos.tools.pfTools import *

if not isData:
    process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", 
      src = cms.InputTag("packedGenParticles"), 
      cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16")
    )
    process.ak4GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')
    process.jetSequence += process.packedGenParticlesForJetsNoNu
    process.jetSequence += process.ak4GenJetsNoNu

# btag and patify jets for access later
addJetCollection(
  process,
  labelName = 'PFAK4Puppi',
  jetSource=cms.InputTag('ak4PFJetsPuppi'), # this is constructed in runMetCorAndUncFromMiniAOD
  algo='AK4',
  rParam=0.4,
  pfCandidates = cms.InputTag("puppiForMET"),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  svSource = cms.InputTag('slimmedSecondaryVertices'),
  muSource = cms.InputTag('slimmedMuons'),
  elSource = cms.InputTag('slimmedElectrons'),
  btagInfos = ['pfImpactParameterTagInfos','pfInclusiveSecondaryVertexFinderTagInfos'],
  btagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
  genJetCollection = cms.InputTag('ak4GenJetsNoNu'),
  genParticles = cms.InputTag('prunedGenParticles'),
  getJetMCFlavour = False,                  # jet flavor disabled
)

if not isData:
  process.jetSequence += process.patJetPartonMatchPFAK4Puppi
  process.jetSequence += process.patJetGenJetMatchPFAK4Puppi
process.jetSequence += process.pfImpactParameterTagInfosPFAK4Puppi
process.jetSequence += process.pfInclusiveSecondaryVertexFinderTagInfosPFAK4Puppi
process.jetSequence += process.pfCombinedInclusiveSecondaryVertexV2BJetTagsPFAK4Puppi
process.jetSequence += process.patJetsPFAK4Puppi

##################### FAT JETS #############################

from PandaProd.Ntupler.makeFatJets_cff import *
fatjetInitSequence = initFatJets(process,isData)
process.jetSequence += fatjetInitSequence

if process.PandaNtupler.doCHSAK8:
  ak8CHSSequence    = makeFatJets(process,
                                  isData=isData,
                                  pfCandidates='pfCHS',
                                  algoLabel='AK',
                                  jetRadius=0.8)
  process.jetSequence += ak8CHSSequence
if process.PandaNtupler.doPuppiAK8:
  ak8PuppiSequence  = makeFatJets(process,
                                  isData=isData,
                                  pfCandidates='puppi',
                                  algoLabel='AK',
                                  jetRadius=0.8)
  process.jetSequence += ak8PuppiSequence
if process.PandaNtupler.doCHSCA15:
  ca15CHSSequence   = makeFatJets(process,
                                  isData=isData,
                                  pfCandidates='pfCHS',
                                  algoLabel='CA',
                                  jetRadius=1.5)
  process.jetSequence += ca15CHSSequence
if process.PandaNtupler.doPuppiCA15:
  ca15PuppiSequence = makeFatJets(process,
                                  isData=isData,
                                  pfCandidates='puppi',
                                  algoLabel='CA',
                                  jetRadius=1.5)
  process.jetSequence += ca15PuppiSequence

if not isData:
  process.ak4GenJetsYesNu = ak4GenJets.clone(src = 'packedGenParticles')
  process.jetSequence += process.ak4GenJetsYesNu

###############################

process.p = cms.Path(
    process.infoProducerSequence *
    process.triggerFilterSequence *
    process.jecSequence *
    process.egmGsfElectronIDSequence *
    process.egmPhotonIDSequence *
    process.photonIDValueMapProducer *		 # iso map for photons
    process.electronIDValueMapProducer *	 # iso map for photons
    process.fullPatMetSequence *	         # pf MET 
    process.puppiMETSequence *			 # builds all the puppi collections
    process.egmPhotonIDSequence *		 # baseline photon ID for puppi correction
    process.fullPatMetSequencePuppi *	         # puppi MET
    process.monoXFilterSequence *		 # filter
    process.jetSequence *			 # patify ak4puppi and do all fatjet stuff
    process.metfilterSequence *
    process.PandaNtupler
    )
