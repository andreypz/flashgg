import FWCore.ParameterSet.Config as cms
from os import environ

#https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideBTagMCTools#Hadron_parton_based_jet_flavour
#B Tag MC efficiencies
bTagEffBins = cms.PSet(
    variables = cms.vstring("hadronFlavour","abs(eta)","pt"),
    bins = cms.VPSet(
                     #udsg jets
                     cms.PSet(lowBounds = cms.vdouble(-0.5,0.0,0.0), upBounds = cms.vdouble(3.5,2.4,50.0), values = cms.vdouble(0.01812901), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,0.0,50.0), upBounds = cms.vdouble(3.5,2.4,100.0), values = cms.vdouble(0.01454259), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,0.0,100.0), upBounds = cms.vdouble(3.5,2.4,200.0), values = cms.vdouble(0.01671879), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,0.0,200.0), upBounds = cms.vdouble(3.5,2.4,999999.0), values = cms.vdouble(0.0192372), uncertainties = cms.vdouble(0.0)),
                     #
                     cms.PSet(lowBounds = cms.vdouble(-0.5,2.4,0.0), upBounds = cms.vdouble(3.5,10.0,50.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,2.4,50.0), upBounds = cms.vdouble(3.5,10.0,100.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,2.4,100.0), upBounds = cms.vdouble(3.5,10.0,200.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(-0.5,2.4,200.0), upBounds = cms.vdouble(3.5,10.0,999999.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     #c jets
                     cms.PSet(lowBounds = cms.vdouble(3.5,0.0,0.0), upBounds = cms.vdouble(4.5,2.4,50.0), values = cms.vdouble(0.1738908), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,0.0,50.0), upBounds = cms.vdouble(4.5,2.4,100.0), values = cms.vdouble(0.1855356), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,0.0,100.0), upBounds = cms.vdouble(4.5,2.4,200.0), values = cms.vdouble(0.1714802), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,0.0,200.0), upBounds = cms.vdouble(4.5,2.4,999999.0), values = cms.vdouble(0.162211), uncertainties = cms.vdouble(0.0)),
                     #
                     cms.PSet(lowBounds = cms.vdouble(3.5,2.4,0.0), upBounds = cms.vdouble(4.5,10.0,50.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,2.4,50.0), upBounds = cms.vdouble(4.5,10.0,100.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,2.4,100.0), upBounds = cms.vdouble(4.5,10.0,200.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(3.5,2.4,200.0), upBounds = cms.vdouble(4.5,10.0,999999.0), values = cms.vdouble(0.0), uncertainties = cms.vdouble(0.0)),
                     #b jets
                     cms.PSet(lowBounds = cms.vdouble(4.5,0.0,0.0), upBounds = cms.vdouble(5.5,2.4,50.0), values = cms.vdouble(0.6482595), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,0.0,50.0), upBounds = cms.vdouble(5.5,2.4,100.0), values = cms.vdouble(0.6953824), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,0.0,100.0), upBounds = cms.vdouble(5.5,2.4,200.0), values = cms.vdouble(0.6815274), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,0.0,200.0), upBounds = cms.vdouble(5.5,2.4,999999.0), values = cms.vdouble(0.6496513), uncertainties = cms.vdouble(0.0)),
                     #
                     cms.PSet(lowBounds = cms.vdouble(4.5,2.4,0.0), upBounds = cms.vdouble(5.5,10.0,50.0), values = cms.vdouble(1.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,2.4,50.0), upBounds = cms.vdouble(5.5,10.0,100.0), values = cms.vdouble(1.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,2.4,100.0), upBounds = cms.vdouble(5.5,10.0,200.0), values = cms.vdouble(1.0), uncertainties = cms.vdouble(0.0)),
                     cms.PSet(lowBounds = cms.vdouble(4.5,2.4,200.0), upBounds = cms.vdouble(5.5,10.0,999999.0), values = cms.vdouble(1.0), uncertainties = cms.vdouble(0.0))
                  ))   

bDiscriminator74X = cms.double(0.890)
bDiscriminator76X = cms.double(0.800)
from flashgg.MicroAOD.flashggJets_cfi import flashggBTag

RMSShiftBins = cms.PSet(
    variables = cms.vstring("abs(eta)","pt"),
    bins = cms.VPSet(
                     cms.PSet( lowBounds = cms.vdouble(2.5,20.), upBounds = cms.vdouble(2.75,30.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.005 )),
                     cms.PSet( lowBounds = cms.vdouble(2.75,20.), upBounds = cms.vdouble(3.0,30.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.004 )),
                     cms.PSet( lowBounds = cms.vdouble(3.0,20.), upBounds = cms.vdouble(4.7,30.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.004 )),
                     cms.PSet( lowBounds = cms.vdouble(2.5,30.), upBounds = cms.vdouble(2.75,50.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.004 )),
                     cms.PSet( lowBounds = cms.vdouble(2.75,30.), upBounds = cms.vdouble(3.0,50.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.003 )),
                     cms.PSet( lowBounds = cms.vdouble(3.0,30.), upBounds = cms.vdouble(4.7,50.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.003 )),
                     cms.PSet( lowBounds = cms.vdouble(2.5,50.), upBounds = cms.vdouble(2.75,99999999.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.003 )),
                     cms.PSet( lowBounds = cms.vdouble(2.75,50.), upBounds = cms.vdouble(3.0,99999999.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.003 )),
                     cms.PSet( lowBounds = cms.vdouble(3.0,50.), upBounds = cms.vdouble(4.7,99999999.), values = cms.vdouble(0.0), uncertainties = cms.vdouble( 0.003 )),
                     )
    )


UnmatchedPUBins = cms.PSet(
    variables = cms.vstring("abs(eta)","pt"),
    bins = cms.VPSet(
                   cms.PSet( lowBounds = cms.vdouble(2.50,20.), upBounds = cms.vdouble(2.75,25.), values = cms.vdouble(1.039), uncertainties = cms.vdouble( -0.039 )),
                   cms.PSet( lowBounds = cms.vdouble(2.75,20.), upBounds = cms.vdouble(3.00,25.), values = cms.vdouble(1.008), uncertainties = cms.vdouble( -0.008 )),
                   cms.PSet( lowBounds = cms.vdouble(3.00,20.), upBounds = cms.vdouble(4.00,25.), values = cms.vdouble(0.954), uncertainties = cms.vdouble( 0.046 )),
                   cms.PSet( lowBounds = cms.vdouble(4.00,20.), upBounds = cms.vdouble(4.70,25.), values = cms.vdouble(0.894), uncertainties = cms.vdouble( 0.106 )),
                   cms.PSet( lowBounds = cms.vdouble(2.50,25.), upBounds = cms.vdouble(2.75,30.), values = cms.vdouble(0.974), uncertainties = cms.vdouble( 0.026 )),
                   cms.PSet( lowBounds = cms.vdouble(2.75,25.), upBounds = cms.vdouble(3.00,30.), values = cms.vdouble(0.891), uncertainties = cms.vdouble( 0.109 )),
                   cms.PSet( lowBounds = cms.vdouble(3.00,25.), upBounds = cms.vdouble(4.00,30.), values = cms.vdouble(0.941), uncertainties = cms.vdouble( 0.059 )),
                   cms.PSet( lowBounds = cms.vdouble(4.00,25.), upBounds = cms.vdouble(4.70,30.), values = cms.vdouble(0.924), uncertainties = cms.vdouble( 0.076 )),
                   cms.PSet( lowBounds = cms.vdouble(2.50,30.), upBounds = cms.vdouble(2.75,50.), values = cms.vdouble(1.068), uncertainties = cms.vdouble( -0.068 )),
                   cms.PSet( lowBounds = cms.vdouble(2.75,30.), upBounds = cms.vdouble(3.00,50.), values = cms.vdouble(0.680), uncertainties = cms.vdouble( 0.320 )),
                   cms.PSet( lowBounds = cms.vdouble(3.00,30.), upBounds = cms.vdouble(4.00,50.), values = cms.vdouble(0.893), uncertainties = cms.vdouble( 0.107 )),
                   cms.PSet( lowBounds = cms.vdouble(4.00,30.), upBounds = cms.vdouble(4.70,50.), values = cms.vdouble(0.877), uncertainties = cms.vdouble( 0.123 ))
                   )
    )

def createJetSystematicsForTag(process,jetInputTag):
  num = jetInputTag.productInstanceLabel
  newName = 'flashggJetSystematics'+num
  setattr(process,newName,
          cms.EDProducer('FlashggJetSystematicProducer',
                         src = jetInputTag,
                         SystMethods2D = cms.VPSet(),
                         SystMethods = cms.VPSet(cms.PSet( MethodName = cms.string("FlashggJetEnergyCorrector"),
                                                           Label = cms.string("JEC"),
                                                           NSigmas = cms.vint32(-1,1),
                                                           OverallRange = cms.string("abs(eta)<5.0"),
                                                           Debug = cms.untracked.bool(False),
                                                           ApplyCentralValue = cms.bool(True),
                                                           SetupUncertainties = cms.bool(True),
                                                           JetCorrectorTag = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
                                                           ),
                                                 cms.PSet( MethodName = cms.string("FlashggJetSmear"),
                                                           Label = cms.string("JER"),
                                                           NSigmas = cms.vint32(-1,1),
                                                           OverallRange = cms.string("abs(eta)<5.0"),
                                                           RandomLabel = cms.string("rnd_g_JER"), # for no-match case
                                                           rho = cms.InputTag('fixedGridRhoAll'),
                                                           Debug = cms.untracked.bool(False),
                                                           ApplyCentralValue = cms.bool(True),
                                                           UseTextFiles = cms.bool(True),
                                                           TextFileResolution = cms.string("%s/src/flashgg/Systematics/data/JER/Spring16_25nsV6_MC_PtResolution_AK4PFchs.txt" % environ['CMSSW_BASE']),
                                                           TextFileSF = cms.string("%s/src/flashgg/Systematics/data/JER/Spring16_25nsV6_MC_SF_AK4PFchs.txt" % environ['CMSSW_BASE'])
                                                           ),
                                                 cms.PSet( MethodName = cms.string("FlashggJetBTagWeight"),
                                                           Label = cms.string("JetBTagWeight"),
                                                           NSigmas = cms.vint32(-1,1),
                                                           OverallRange = cms.string("pt>25.0&&abs(eta)<2.4"),
                                                           BinList = bTagEffBins,
						 	   bTag = cms.string(flashggBTag),
						 	   bDiscriminator = bDiscriminator76X, #Medium working point for CSV B tagger, for CMSSW74X use: bDiscriminator74X
							   Debug = cms.untracked.bool(False),
                                                           ApplyCentralValue = cms.bool(True)
                                                           ),
                                                 cms.PSet( MethodName = cms.string("FlashggJetRMSShift"),
                                                           Label = cms.string("RMSShift"),
                                                           NSigmas = cms.vint32(-1,1),
                                                           OverallRange = cms.string("abs(eta)>2.5&&abs(eta)<4.7&&pt>20."),
                                                           BinList  = RMSShiftBins,
                                                           ApplyCentralValue = cms.bool(False),
                                                           Debug = cms.untracked.bool(False)
                                                           ),
                                                 cms.PSet( MethodName = cms.string("FlashggJetWeight"),
                                                           Label = cms.string("UnmatchedPUWeight"),
                                                           NSigmas = cms.vint32(-1,1),
                                                           OverallRange = cms.string("abs(eta)>2.5&&abs(eta)<4.7&&pt>20.&&pt<50.&&hasGenMatch==0"),
                                                           BinList = UnmatchedPUBins,
                                                           ApplyCentralValue = cms.bool(False),
                                                           Debug = cms.untracked.bool(False),
                                                           )
                                                 )
                         )
          )
#  setattr(process.RandomNumberGeneratorService,newName,cms.PSet(initialSeed = cms.untracked.uint32(int(num)))) 
  # e.g. process.RandomNumberGeneratorService.flashggJetSystematics3 = cms.PSet(initialSeed = cms.untracked.uint32(3))
  return (getattr(process,newName),cms.InputTag(newName))
  
def createJetSystematics(process,replaceTagList):
  process.load("JetMETCorrections.Configuration.JetCorrectors_cff")
  process.jetCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorChain)
  process.jetSystematicsSequence = cms.Sequence(process.jetCorrectorChain)
  systematicsInputList = cms.VInputTag()
  for jetInputTag in replaceTagList:
    module,tag = createJetSystematicsForTag(process,jetInputTag)
    process.jetSystematicsSequence += module
    systematicsInputList.append(tag)
  createJECESource(process)  
#  createJERESource(process)  
  return systematicsInputList

def createJECESource(process):
    datadir = "%s/src/flashgg/Systematics/data/JEC" % environ['CMSSW_BASE']
    print "WARNING: we are reading JEC from %s so GRID jobs might not work" % datadir
    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    process.load("CondCore.DBCommon.CondDBSetup_cfi")
    process.jec = cms.ESSource("PoolDBESSource",
                               DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
                               timetype = cms.string('runnumber'),
                               toGet = cms.VPSet(cms.PSet(
          record = cms.string('JetCorrectionsRecord'),
          tag    = cms.string('JetCorrectorParametersCollection_Spring16_25nsV6_MC_AK4PFchs'),
          label  = cms.untracked.string("AK4PFchs")
          )),
                               connect = cms.string('sqlite_file:%s/Spring16_25nsV6_MC.db' % datadir)
                               )                               
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')

def createJERESource(process):
    datadir = "%s/src/flashgg/Systematics/data/JER" % environ['CMSSW_BASE']
    print "WARNING: we are reading JER from %s so GRID jobs might not work" % datadir
    process.load('Configuration.StandardSequences.Services_cff')
    process.load("JetMETCorrections.Modules.JetResolutionESProducer_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup

    process.jer = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               toGet = cms.VPSet(
        # Resolution
        cms.PSet(
          record = cms.string('JetResolutionRcd'),
          tag    = cms.string('JR_Spring16_25nsV6_MC_PtResolution_AK4PFchs'),
          label  = cms.untracked.string('AK4PFchs_pt')
          ),
        
        # Scale factors
        cms.PSet(
          record = cms.string('JetResolutionScaleFactorRcd'),
          tag    = cms.string('JR_Spring16_25nsV6_MC_SF_AK4PFchs'),
          label  = cms.untracked.string('AK4PFchs')
          ),
        ),
# [2016-02-21 14:50:14,703] INFO: Connecting to Systematics/data/JER/Summer15_25nsV6_MC.db [sqlite:///Systematics/data/JER/Summer15_25nsV6_MC.db]
# JR_Summer15_25nsV6_MC_SF_AK4PFchs             Run       JME::JetResolutionObject  any              -1             2016-02-05 20:59:34.061327  New Tag      
# JR_Summer15_25nsV6_MC_PtResolution_AK4PFchs   Run       JME::JetResolutionObject  any              -1             2016-02-05 20:59:34.064554  New Tag      
                               connect = cms.string('sqlite_file:%s/Spring16_25nsV6_MC.db' % datadir)

                               )
    process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')

