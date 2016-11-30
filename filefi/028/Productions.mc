#---------------------------------------------------------------------------------------------------
# Configuration for the productions with this configuration
#
# XX-MITCFG-XX     = filefi
# XX-MITVERSION-XX = 028
#
# crontab          = 1
#---------------------------------------------------------------------------------------------------
# Production Parameters
# Ex:
# CDF_Dataset_name \
#  MIT_Dataset_name  nEvtsPreJob  ProductionStatus  StorageLocation  LocalLocation [ DbsInstance ]
#
# example for no DBS sample:
#  /Photon/Run2011B-30Nov2011-v1/AOD                 r11b-pho-n30-v1  1 new - none cern.ch
#---------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
# Samples made with Mit_028 - low pileup samples
#----------------------------------------------------------------------------------------------------

/WW_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S8_START52_V9-v1/AODSIM                        s12-ww-v9-s8                 1  new  -
/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S8_START52_V9-v1/AODSIM                        s12-wz-v9-s8                 1  new  -
/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S8_START52_V9-v1/AODSIM                        s12-zz-v9-s8                 1  new  -
/WminusToMuNu_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM         s12-wmm-v9-s8                1  new  -
/WplusToMuNu_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM          s12-wpm-v9-s8                1  new  -
/WminusToENu_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM          s12-wme-v9-s8                1  new  -
/WplusToENu_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM           s12-wpe-v9-s8                1  new  -
/WToTauNu_TuneZ2star_8TeV_pythia6_tauola_cff/Summer12-PU_S8_START52_V9-v2/AODSIM              s12-wt-v9-s8                 1  new  -
/DYToMuMu_M-20_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM        s12-zmm-v9-s8                1  new  -
/DYToEE_M-20_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12-PU_S8_START52_V9-v2/AODSIM          s12-zee-v9-s8                1  new  -
/DYToTauTau_M_20_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S8_START52_V9-v1/AODSIM           s12-ztt-v9-s8                1  new  -
/TTJets_TuneZ2star_8TeV-madgraph-tauola/Summer12-E8TeV4BX50ns-v1/AODSIM                       s12-ttj-v9-s8                1  new  -

#----------------------------------------------------------------------------------------------------
# Samples made with Mit_028 - standard pileup samples
#----------------------------------------------------------------------------------------------------

# signal samples
/GluGluToHToGG_M-90_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                   s12-h90gg-gf-v9              1  new  -
/GluGluToHToGG_M-100_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h100gg-gf-v9             1  new  -
/GluGluToHToGG_M-105_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h105gg-gf-v9             1  new  -
/GluGluToHToGG_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h110gg-gf-v9             1  new  -
/GluGluToHToGG_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h115gg-gf-v9             1  new  -
/GluGluToHToGG_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h120gg-gf-v9             1  new  -
/GluGluToHToGG_M-123_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h123gg-gf-v9             1  new  -
/GluGluToHToGG_M-124_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h124gg-gf-v9             1  new  -
/GluGluToHToGG_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h125gg-gf-v9             1  new  -
/GluGluToHToGG_M-129_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h129gg-gf-v9             1  new  -
/GluGluToHToGG_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h130gg-gf-v9             1  new  -
/GluGluToHToGG_M-135_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h135gg-gf-v9             1  new  -
/GluGluToHToGG_M-140_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h140gg-gf-v9             1  new  -
/GluGluToHToGG_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h145gg-gf-v9             1  new  -
/GluGluToHToGG_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h150gg-gf-v9             1  new  -
/GluGluToHToGG_M-155_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h155gg-gf-v9             1  new  -

/GluGluToHToGG_M-124_8TeV-powheg-pythia6/Summer12-newBS_PU_S7_START52_V9-v1/AODSIM            s12-h124gg-gf-nbs-v9         1  new  -
/GluGluToHToGG_M-125_8TeV-powheg-pythia6/Summer12-newBS_PU_S7_START52_V9-v1/AODSIM	      s12-h125gg-gf-nbs-v9         1  new  -
/GluGluToHToGG_M-126_8TeV-powheg-pythia6/Summer12-newBS_PU_S7_START52_V9-v1/AODSIM	      s12-h126gg-gf-nbs-v9         1  new  -

/VBF_HToGG_M-90_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                       s12-h90gg-vbf-v9             1  new  -
/VBF_HToGG_M-100_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h100gg-vbf-v9            1  new  -
/VBF_HToGG_M-105_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h105gg-vbf-v9            1  new  -
/VBF_HToGG_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h110gg-vbf-v9            1  new  -
/VBF_HToGG_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h115gg-vbf-v9            1  new  -
/VBF_HToGG_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h120gg-vbf-v9            1  new  -
/VBF_HToGG_M-123_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h123gg-vbf-v9            1  new  -
/VBF_HToGG_M-124_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h124gg-vbf-v9            1  new  -
/VBF_HToGG_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h125gg-vbf-v9            1  new  -
/VBF_HToGG_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h130gg-vbf-v9            1  new  -
/VBF_HToGG_M-135_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h135gg-vbf-v9            1  new  -
/VBF_HToGG_M-140_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h140gg-vbf-v9            1  new  -
/VBF_HToGG_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h145gg-vbf-v9            1  new  -
/VBF_HToGG_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-h150gg-vbf-v9            1  new  -

/WH_ZH_HToGG_M-90_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                            s12-h90gg-vh-v9              1  new  -
/WH_ZH_HToGG_M-105_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h105gg-vh-v9             1  new  -
/WH_ZH_HToGG_M-110_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h110gg-vh-v9             1  new  -
/WH_ZH_HToGG_M-115_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h115gg-vh-v9             1  new  -
/WH_ZH_HToGG_M-120_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h120gg-vh-v9             1  new  -
/WH_ZH_HToGG_M-140_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h140gg-vh-v9             1  new  -
/WH_ZH_HToGG_M-145_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                           s12-h145gg-vh-v9             1  new  -

/TTH_HToGG_M-100_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h100gg-tt-v9             1  new  -
/TTH_HToGG_M-105_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h105gg-tt-v9             1  new  -
/TTH_HToGG_M-110_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h110gg-tt-v9             1  new  -
/TTH_HToGG_M-115_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h115gg-tt-v9             1  new  -
/TTH_HToGG_M-120_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h120gg-tt-v9             1  new  -
/TTH_HToGG_M-121_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h121gg-tt-v9             1  new  -
/TTH_HToGG_M-124_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h124gg-tt-v9             1  new  -
/TTH_HToGG_M-126_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h126gg-tt-v9             1  new  -
/TTH_HToGG_M-127_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h127gg-tt-v9             1  new  -
/TTH_HToGG_M-128_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h128gg-tt-v9             1  new  -
/TTH_HToGG_M-130_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h130gg-tt-v9             1  new  -
/TTH_HToGG_M-135_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h135gg-tt-v9             1  new  -
/TTH_HToGG_M-140_8TeV-pythia6/Summer12-PU_S7_START52_V9-v2/AODSIM                             s12-h140gg-tt-v9             1  new  -

/GluGluToHToWWTo2LAndTau2Nu_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h110ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h115ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h120ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h125ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h130ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-135_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h135ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-140_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h140ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h145ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h150ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-155_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h155ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-160_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h160ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-170_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h170ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-180_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h180ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-190_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h190ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-200_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h200ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-250_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h250ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-300_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h300ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-350_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h350ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-400_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h400ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-450_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h450ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-500_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h500ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-550_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h550ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-600_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h600ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-700_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h700ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-800_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h800ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-900_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-h900ww2l-gf-v9           1  new  -
/GluGluToHToWWTo2LAndTau2Nu_M-1000_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM    s12-h1000ww2l-gf-v9          1  new  -

/VBF_HToWWTo2LAndTau2Nu_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h110ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h115ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h120ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h125ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h130ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-135_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h135ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-140_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h140ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h145ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h150ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-155_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h155ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-160_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h160ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-170_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h170ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-180_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h180ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-190_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h190ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-200_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h200ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-250_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h250ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-300_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h300ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-350_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h350ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-400_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h400ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-450_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h450ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-500_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h500ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-550_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h550ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-600_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h600ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-700_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h700ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-800_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h800ww2l-vbf-v9	   1  new  -
/VBF_HToWWTo2LAndTau2Nu_M-900_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM	      s12-h900ww2l-vbf-v9	   1  new  -

/GluGluToHToTauTau_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h110tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h115tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h120tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h125tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h130tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-135_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h135tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-140_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h140tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h145tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h150tt-gf-v9             1  new  -
/GluGluToHToTauTau_M-160_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h160tt-gf-v9             1  new  -

/VBF_HToTauTau_M-110_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h110tt-vbf-v9            1  new  -
/VBF_HToTauTau_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h115tt-vbf-v9            1  new  -
/VBF_HToTauTau_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h120tt-vbf-v9            1  new  -      
/VBF_HToTauTau_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h125tt-vbf-v9            1  new  -
/VBF_HToTauTau_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h145tt-vbf-v9            1  new  -
/VBF_HToTauTau_M-155_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h155tt-vbf-v9            1  new  -

/WH_ZH_TTH_HToTauTau_M-115_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM            s12-h115tt-vtth-v9           1  new  -
/WH_ZH_TTH_HToTauTau_M-150_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM            s12-h150tt-vtth-v9           1  new  -
/WH_ZH_TTH_HToTauTau_M-155_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM            s12-h155tt-vtth-v9           1  new  -
/WH_ZH_TTH_HToTauTau_M-160_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM            s12-h160tt-vtth-v9           1  new  -

/SUSYGluGluToHToTauTau_M-90_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM           s12-h90tt-ggh-v9             1  new  -
/SUSYGluGluToHToTauTau_M-600_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v2/AODSIM          s12-h600tt-ggh-v9            1  new  -

# Higgs to ZZ4l MC
/GluGluToHToZZTo4L_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h115zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-117_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h117zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-119_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h119zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h120zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-121_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h121zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-123_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h123zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-124_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h124zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h125zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-126_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h126zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-127_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h127zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-145_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h145zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h150zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-180_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h180zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-200_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h200zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-220_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h220zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-250_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h250zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-300_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h300zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-325_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h325zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-350_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h350zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-400_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h400zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-450_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h450zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-500_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h500zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-550_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h550zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-600_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h600zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-650_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h650zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-700_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h700zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-750_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h750zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-800_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h800zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-850_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h850zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-900_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h900zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-950_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-h950zz4l-gf-v9           1 new -
/GluGluToHToZZTo4L_M-1000_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM             s12-h1000zz4l-gf-v9          1 new -

/VBF_HToZZTo4L_M-115_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h115zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-117_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h117zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-119_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h119zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-120_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h120zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-121_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h121zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-123_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h123zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-124_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h124zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-125_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h125zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-126_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h126zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-127_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h127zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-130_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h130zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-150_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h150zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-180_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h180zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-200_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h200zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-220_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h220zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-250_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h250zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-300_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h300zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-325_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h325zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-350_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h350zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-400_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h400zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-450_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h450zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-500_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h500zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-550_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h550zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-600_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h600zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-650_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h650zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-700_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h700zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-750_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h750zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-800_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h800zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-850_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h850zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-900_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h900zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-950_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-h950zz4l-vbf-v9          1 new -
/VBF_HToZZTo4L_M-1000_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                 s12-h1000zz4l-vbf-v9         1 new -

# background samples
/GJet_Pt40_doubleEMEnriched_TuneZ2star_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM       s12-pj40-2em-v9              1  new  -
/GJet_Pt-20to40_doubleEMEnriched_TuneZ2star_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM  s12-pj20_40-2em-v9           1  new  -

/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12-PU_S7_START52_V9-v1/AODSIM         s12-zllm50-v9                1  new  -
/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12-PU_S7_START52_V9-v2/AODSIM         s12-zllm50-2-v9              1  new  -
/DYJetsToLL_M-10To50filter_8TeV-madgraph/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-zllm1050-v9              1  new  -
/DYToTauTau_M_20_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S7_START52_V9-v1/AODSIM           s12-zttm20-v9                1  new  -
/DYToTauTau_M-100to200_TuneZ2Star_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-zttm100_200-v9           1  new  -
/DYToTauTau_M-200to400_TuneZ2Star_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-zttm200_400-v9           1  new  -
/DYToTauTau_M-400to800_TuneZ2Star_8TeV-pythia6-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM     s12-zttm400_800-v9           1  new  -

/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12-PU_S7_START52_V9-v1/AODSIM              s12-wjets-v9                 1  new  -

/GluGluToWWTo4L_TuneZ2star_8TeV-gg2ww-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM             s12-ggww2l-v9                1  new  -
/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM            s12-wwj-v9                   1  new  -
/WWTo2L2Nu_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                 s12-ww2l-v9                  1  new  -
/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                        s12-wz-v9                    1  new  -
/WZTo3LNu_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-wz3l-v9                  1  new  -
/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                        s12-zz-v9                    1  new  -
/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S7_START52_V9-v3/AODSIM            s12-zz2l2n-v9                1  new  -
/ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S7_START52_V9-v3/AODSIM             s12-zz2l2q-v9                1  new  -
/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S7_START52_V9-v3/AODSIM               s12-zz4l-v9                  1  new  -
/ZZTo4tau_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                             s12-zz4t-powheg-v9           1  new  -
/ZZTo4mu_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                              s12-zz4m-powheg-v9           1  new  -
/ZZTo4e_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                               s12-zz4e-powheg-v9           1  new  -
/ZZTo2mu2tau_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                          s12-zz2m2t-powheg-v9         1  new  -
/ZZTo2e2tau_8TeV-powheg-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                           s12-zz2e2t-powheg-v9         1  new  -

/QCD_Pt-30to40_doubleEMEnriched_TuneZ2star_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM   s12-qcd-2em3040-v9           1  new  -
/QCD_Pt-40_doubleEMEnriched_TuneZ2star_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM       s12-qcd-2em40-v9             1  new  -

/G_Pt-15to30_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-pj15_30-v9               1  new  -
/G_Pt-30to50_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-pj30_50-v9               1  new  -
/G_Pt-50to80_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-pj50_80-v9               1  new  -
/G_Pt-80to120_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                     s12-pj80_120-v9              1  new  -
/G_Pt-120to170_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                    s12-pj120_170-v9             1  new  -
/G_Pt-170to300_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                    s12-pj170_300-v9             1  new  -
/G_Pt-300to470_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                    s12-pj300_470-v9             1  new  -
/G_Pt-470to800_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                    s12-pj470_800-v9             1  new  -
/G_Pt-800to1400_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                   s12-pj800_1400-v9            1  new  -
/G_Pt-1400to1800_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                  s12-pj1400_1800-v9           1  new  -
/G_Pt-1800_TuneZ2star_8TeV_pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                        s12-pj1800-v9                1  new  -

/DiPhotonBorn_Pt-10To25_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-2pibo10_25-v9            1  new  -
/DiPhotonBorn_Pt-25To250_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                     s12-2pibo25_250-v9           1  new  -
/DiPhotonBorn_Pt-250ToInf_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                    s12-2pibo250-v9              1  new  -
/DiPhotonBox_Pt-10To25_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                       s12-2pibx10_25-v9            1  new  -
/DiPhotonBox_Pt-25To250_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                      s12-2pibx25_250-v9           1  new  -
/DiPhotonBox_Pt-250ToInf_8TeV-pythia6/Summer12-PU_S7_START52_V9-v1/AODSIM                     s12-2pibx250-v9              1  new  -

/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM         s12-wtopb-dr-v9              1  new  -
/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM            s12-wtop-dr-v9               1  new  -
/TTJets_TuneZ2star_8TeV-madgraph-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                   s12-ttj-v9                   1  new  -
/T_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM                s12-top-tch-v9               1  new  -
/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/Summer12-PU_S7_START52_V9-v1/AODSIM             s12-tbar-tch-v9              1  new  -
