from CRABClient.UserUtilities import config
import datetime
import time

config = config()

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

channel = '1-XibToJpsiXi'
year = '2022'
step = 'PrivateMC-'+year
nEvents = 50000
NJOBS = 200
myrun = 'step0-RAWSIM-1-XibToJpsiXi-run_cfg.py'
myname = step+'-'+channel

config.General.requestName = step+'-'+channel+'-'+st
config.General.transferOutputs = True
config.General.transferLogs = False
config.General.workArea = 'crab_'+step+'-'+channel

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = myrun
config.JobType.inputFiles = ['step1-PREMIXRAW-1-XibToJpsiXi-run_cfg.py',
                             'step2-AODSIM-1-XibToJpsiXi-run_cfg.py',
                             'step3-MINIAODSIM-1-XibToJpsiXi-run_cfg.py',
                             'chain_Run3Summer22EEwmLHEGS-Run3Summer22EENanoAODv12.txt']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.eventsPerLumi = 10000
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 3300
config.JobType.scriptExe = 'Condorjob-XibToJpsiXi_fullgen.sh'

#config.JobType.scriptArgs = ['CHANNEL_DECAY='+channel,'YEAR='+year] ## for MCcrabJobScript.sh if necessary
#config.JobType.outputFiles = ['MC-'+year+'-'+channel+'.root']
config.JobType.outputFiles = ['step3-MINIAODSIM-1-XibToJpsiXi-result.root']

config.Data.outputPrimaryDataset = myname
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = nEvents
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/ctorresc/PrivateMC_Xib2022/'
config.Data.publication = False

config.Site.storageSite = 'T3_CH_CERNBOX'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_IT_Bari'
