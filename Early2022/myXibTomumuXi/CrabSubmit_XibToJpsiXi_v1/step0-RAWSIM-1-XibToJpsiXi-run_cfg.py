# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/Xib-JpsiXi-pythia-Run3Summer22EEGS.py --fileout file:step0-RAWSIM-1-XibToJpsiXi-result.root --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_postEE_v1 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --python_filename step0-RAWSIM-1-XibToJpsiXi-run_cfg.py --no_exec -n 5000
import FWCore.ParameterSet.Config as cms
from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter


from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('SIM',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper 
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13p6TeVEarly2022Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/Xib-JpsiXi-pythia-Run3Summer22EEGS.py nevts:5000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step0-RAWSIM-1-XibToJpsiXi-result.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
if hasattr(process, "XMLFromDBSource"): process.XMLFromDBSource.label="Extended"
if hasattr(process, "DDDetectorESProducerFromDB"): process.DDDetectorESProducerFromDB.label="Extended"
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_mcRun3_2022_realistic_postEE_v1', '')

process.psifilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(13, -13),
    MaxEta = cms.untracked.vdouble(2.6, 2.6),
    MinEta = cms.untracked.vdouble(-2.6, -2.6),
    MinPt = cms.untracked.vdouble(3.0, 3.0),
    MotherID = cms.untracked.int32(5132),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(443),
    verbose = cms.untracked.int32(0)
)


process.xibfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(443, 3312),
    MaxEta = cms.untracked.vdouble(9999.0, 9999.0),
    MinEta = cms.untracked.vdouble(-9999.0, -9999.0),
    MinPt = cms.untracked.vdouble(6.0, 0.0),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(5132),
    verbose = cms.untracked.int32(1)
)


process.generator = ExternalGeneratorFilter(
    cms.EDFilter("Pythia8GeneratorFilter",
        ExternalDecays = cms.PSet(
            EvtGen130 = cms.untracked.PSet(
                convertPythiaCodes = cms.untracked.bool(False),
                decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
                list_forced_decays = cms.vstring(
                    'MyXi_b-',
                    'Myanti-Xi_b+'
                ),
                operates_on_particles = cms.vint32(),
                particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
                user_decay_embedded = cms.vstring(
                    '#',
                    'Particle   pi+           1.3957061e-01   0.0000000e+00',
                    'Particle   pi-           1.3957061e-01   0.0000000e+00',
                    'Particle   K_S0          4.9761100e-01   0.0000000e+00',
                    'Particle   K*+           8.9176000e-01   5.0300000e-02',
                    'Particle   K*-           8.9176000e-01   5.0300000e-02',
                    'Particle   K*0           8.9555000e-01   4.7300000e-02',
                    'Particle   anti-K*0      8.9555000e-01   4.7300000e-02',
                    'Particle   rho0          7.7526000e-01   1.4910000e-01',
                    'Particle   phi           1.0194610e+00   4.2490000e-03',
                    'Particle   B-            5.2793200e+00   0.0000000e+00',
                    'Particle   B+            5.2793200e+00   0.0000000e+00',
                    'Particle   B0            5.2796300e+00   0.0000000e+00',
                    'Particle   anti-B0       5.2796300e+00   0.0000000e+00',
                    'Particle   B_s0          5.3668900e+00   0.0000000e+00',
                    'Particle   anti-B_s0     5.3668900e+00   0.0000000e+00',
                    'Particle   J/psi         3.0969000e+00   9.2900006e-05',
                    'Particle   Xi-           1.3217100e+00   0.0000000e+00',
                    'Particle   anti-Xi+      1.3217100e+00   0.0000000e+00',
                    'Particle   psi(2S)       3.6860970e+00   2.9400000e-04',
                    'Particle   Xi_b-         5.7970000e+00   0.0000000e+00',
                    'Particle   anti-Xi_b+    5.7970000e+00   0.0000000e+00',
                    '#',
                    'Alias      MyXi_b-        Xi_b-',
                    'Alias      Myanti-Xi_b+   anti-Xi_b+',
                    'ChargeConj Myanti-Xi_b+   MyXi_b-',
                    '#',
                    'Alias       Mypsi      J/psi',
                    'ChargeConj  Mypsi      Mypsi',
                    '#',
                    'Decay Mypsi',
                    '1.000  mu+       mu-       PHOTOS VLL;',
                    'Enddecay',
                    '#',
                    'Decay MyXi_b-',
                    '1.000     Mypsi  Xi-      PHSP;',
                    'Enddecay',
                    'CDecay Myanti-Xi_b+',
                    'End'
                )
            ),
            parameterSets = cms.vstring('EvtGen130')
        ),
        PythiaParameters = cms.PSet(
            parameterSets = cms.vstring(
                'pythia8CommonSettings',
                'pythia8CP5Settings',
                'processParameters'
            ),
            processParameters = cms.vstring(
                'SoftQCD:nonDiffractive = on',
                '5132:m0=5.7970',
                'PTFilter:filter = on',
                'PTFilter:quarkToFilter = 5',
                'PTFilter:scaleToFilter = 2.0'
            ),
            pythia8CP5Settings = cms.vstring(
                'Tune:pp 14',
                'Tune:ee 7',
                'MultipartonInteractions:ecmPow=0.03344',
                'MultipartonInteractions:bProfile=2',
                'MultipartonInteractions:pT0Ref=1.41',
                'MultipartonInteractions:coreRadius=0.7634',
                'MultipartonInteractions:coreFraction=0.63',
                'ColourReconnection:range=5.176',
                'SigmaTotal:zeroAXB=off',
                'SpaceShower:alphaSorder=2',
                'SpaceShower:alphaSvalue=0.118',
                'SigmaProcess:alphaSvalue=0.118',
                'SigmaProcess:alphaSorder=2',
                'MultipartonInteractions:alphaSvalue=0.118',
                'MultipartonInteractions:alphaSorder=2',
                'TimeShower:alphaSorder=2',
                'TimeShower:alphaSvalue=0.118',
                'SigmaTotal:mode = 0',
                'SigmaTotal:sigmaEl = 22.08',
                'SigmaTotal:sigmaTot = 101.037',
                'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
            ),
            pythia8CommonSettings = cms.vstring(
                'Tune:preferLHAPDF = 2',
                'Main:timesAllowErrors = 10000',
                'Check:epTolErr = 0.01',
                'Beams:setProductionScalesFromLHEF = off',
                'SLHA:minMassSM = 1000.',
                'ParticleDecays:limitTau0 = on',
                'ParticleDecays:tau0Max = 10',
                'ParticleDecays:allowPhotonRadiation = on'
            )
        ),
        comEnergy = cms.double(13600.0),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(0)
    )
    ,
    _external_process_waitTime_ = cms.untracked.uint32(300),
    _external_process_verbose_ = cms.untracked.bool(False),
    _external_process_components_ =cms.vstring(),
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.xibfilter+process.psifilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
