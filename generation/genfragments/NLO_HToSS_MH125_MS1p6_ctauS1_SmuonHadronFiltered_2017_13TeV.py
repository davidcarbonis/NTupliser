import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF31_13TeV_M125/v1/gg_H_quark-mass-effects_NNPDF31_13TeV_M125_slc6_amd64_gcc630_CMSSW_9_3_0.tgz'),
    nEvents = cms.untracked.uint32(1000000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
                                       saveBarCodes = cms.untracked.bool(True),
                                       src = cms.InputTag("generator", "unsmeared"),
                                       abortOnUnknownPDGCode = cms.untracked.bool(False)
)

scalarDecayFilter = cms.EDFilter("MCScalarDecayFilter",
                           filterAlgoPSet = cms.PSet(genParticles = cms.InputTag("genParticlesForFilter"))
)


generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP2Settings', 
            'pythia8PowhegEmissionVetoSettings', 
            'processParameters'),
        processParameters = cms.vstring('POWHEG:nFinal = 1', 
            '9000006:all = sk   skbar    0        0          0       1.6  1.9732e-13  1.0  75.0 1',
            '9000006:oneChannel = 2  1.0 101  13 -13',
            '9000006:addChannel = 3  1.0 101  1 -1',
            '9000006:addChannel = 3  1.0 101  2 -2',
            '9000006:addChannel = 3  1.0 101  3 -3',
            '9000006:addChannel = 3  1.0 101  4 -4',
            '9000006:addChannel = 3  1.0 101  5 -5',
            '9000006:mayDecay = on',
            '9000006:isResonance = on',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:addChannel = 1 0.000000001 101 9000006 -9000006',
            '25:onIfMatch = 9000006 -9000006',
            '9000006:onMode = off',
            '9000006:onNegIfAny = 1',
            '9000006:onNegIfAny = 2',
            '9000006:onNegIfAny = 3',
            '9000006:onNegIfAny = 4',
            '9000006:onNegIfAny = 5',
            '9000006:onPosIfAny = 13'),
        pythia8CP2Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.1391', 
            'PDF:pSet=17', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=2.306', 
            'MultipartonInteractions:coreRadius=0.3755', 
            'MultipartonInteractions:coreFraction=0.3269', 
            'ColourReconnection:range=2.323', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:rapidityOrder=off', 
            'SpaceShower:alphaSvalue=0.13', 
            'TimeShower:alphaSvalue=0.13'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8PowhegEmissionVetoSettings = cms.vstring('POWHEG:veto = 1', 
            'POWHEG:pTdef = 1', 
            'POWHEG:emitted = 0', 
            'POWHEG:pTemt = 0', 
            'POWHEG:pThard = 0', 
            'POWHEG:vetoCount = 100', 
            'SpaceShower:pTmaxMatch = 2', 
            'TimeShower:pTmaxMatch = 2')
    ),
)

ProductionFilterSequence = cms.Sequence(generator * (genParticlesForFilter + scalarDecayFilter))
