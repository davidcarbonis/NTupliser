# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/NLO_HToSS_MH125_MS2_ctauS0_SmuonHadronFiltered_2018_13TeV.py --fileout file:Higgs_GEN_SIM.root -s LHE,GEN,SIM --mc --eventcontent RAWSIM --geometry DB:Extended --era Run2_2018 --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --datatier GEN-SIM --no_exec -n 10 --python_filename NLO_ggHToSSTobbbb_MH125_MS55_ctauS10_TuneCP2_13TeV_pythia8_GENSIM.py

import FWCore.ParameterSet.Config as cms

##The line below always has to be included to make VarParsing work
import FWCore.ParameterSet.VarParsing as VarParsing

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('SIM',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/NLO_HToSS_MH125_MS2_ctauS0_SmuonHadronFiltered_2018_13TeV.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP2Settings', 
            'pythia8PowhegEmissionVetoSettings', 
            'processParameters'),
        processParameters = cms.vstring('POWHEG:nFinal = 1', 
#            <particle id="..." name, antiName, spinType=, chargeType, colType, m0, mWidth, mMin, mMax, tau0> ##tau0 = nominal proper lifetime (mm/c) 
            '9000006:all = sk   skbar    0        0          0       2.0  1.9732e-12  1.0  75.0 0',
            '9000006:oneChannel = 2  1.0 101  13 -13',
            '9000006:addChannel = 3  1.0 101  211 -211',
            '9000006:addChannel = 3  1.0 101  321 -321',
            '9000006:addChannel = 3  1.0 101  310 -310',
            '9000006:mayDecay = on',
            '9000006:isResonance = on',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:addChannel = 1 0.000000001 101 9000006 -9000006',
            '25:onIfMatch = 9000006 -9000006',
            '9000006:onMode = off',
            '9000006:onNegIfAny = 211',
            '9000006:onNegIfAny = 321',
            '9000006:onNegIfAny = 310',
            '9000006:onPosIfAny = 13',
            '9000006:0:bRatio = 1.',    ### channel 0 = 13
            '9000006:1:bRatio = 0.67',  ### channel 1 = 211
            '9000006:2:bRatio = 0.165', ### channel 2 = 321
            '9000006:3:bRatio = 0.165'  ### channel 3 = 310
        ),
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
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/powheg/V2/gg_H_quark-mass-effects_slc7_amd64_gcc820_CMSSW_10_6_20_ggH_M125/v1/gg_H_quark-mass-effects_slc7_amd64_gcc820_CMSSW_10_6_20_ggH_M125.tgz'), ## Correct UL version
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

process.ProductionFilterSequence = cms.Sequence(process.generator) 

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(8)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
        if path in ['lhe_step']: continue
        getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
