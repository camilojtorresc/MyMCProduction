# My Monte Carlo Production
This is a public repository with my MC production with the CMSSW.

## Prepare

Monte Carlo production with the **CMSSW** needs a `prepare` file, e.g. `Early2022/myXibTomumuXi/prepare_Xib_jpsiXiv1.sh`, to create the *cfg* files for the MC production steps. The **cmsDrivers** and CMS realeses for each year and each step (*for 2022 there are four steps, for different years there are different number of steps*) need to be extract from an official MC request, for example for 2022 the *cfg* with the cmsDrivers [Bd MC production 2022](https://cms-pdmv-prod.web.cern.ch/mcm/requests?dataset_name=BdToJpsiK0s_Unbiased_TuneCP5_13p6TeV_pythia8-evtgen&page=0&shown=2151940099):
- **step0: GEN**
cmsDriver command origin: [https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_setup/BPH-Run3Summer22EEGS-00112](https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_setup/BPH-Run3Summer22EEGS-00112)
- **step1: DIGI**
cmsDriver command origin: [https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEDRPremix-00130](https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEDRPremix-00130)

    There is an [issue missing pileup files for DIGIPremix step](https://cms-talk.web.cern.ch/t/missing-files-for-digipremix-step-runiisummer20ul17-private-production/80581/2). You have to put your own pileup list with available files in disk as follows:
    > - Modify the cmsDriver.py command that you use to generate the configuration file by replacing `--pileup_input "dbs:<name of the dataset>"` (or whatever you are using to specify the pileup input files/dataset) by `--pileup_input "filelist:<name of the txt file>"`, where the txt file is the file with the list of available premixing files on disk, one per line.
    >- Make sure the file is transfered to the CRAB sandbox, by adding it to the list of `inputFiles` in the CRAB config file.
- **step2: RECO**
cmsDriver command origin: [https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEDRPremix-00130](https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEDRPremix-00130)
- **step3: MINIAOD**
cmsDriver command origin: [https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEMiniAODv3-00130](https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_test/BPH-Run3Summer22EEMiniAODv3-00130)

## Fragment
For ***step0 GEN*** the input file must be a `fragment` with the specifics of the decay in **Pythia** for hadronization, **EvtGen** for decaying process, **Geant4** for detector simulation and **PHOTOS** for final state radiation of the muons, e.g. for 2022 `/Early2022/myXibTomumuXi/Xib-JpsiXi-pythia-Run3Summer22EEGS.py`. The file has to be upload to GitHub to download directly from there with the **raw** link to put it in the **prepare** file as follows:
```
CHANNEL_DECAY="1-XibToJpsiXi"
step0_fragmentfile="Xib-JpsiXi-pythia-Run3Summer22EEGS.py"
step0_configfile="step0-RAWSIM-${CHANNEL_DECAY}-run_cfg.py"
step0_resultfile="step0-RAWSIM-${CHANNEL_DECAY}-result.root"

# Download fragment from myGitHub
curl -s -k https://raw.githubusercontent.com/camilojtorresc/MyMCProduction/refs/heads/main/Early2022/myXibTomumuXi/$step0_fragmentfile --retry 3 --create-dirs -o Configuration/GenProduction/python/$step0_fragmentfile
[ -s Configuration/GenProduction/python/$step0_fragmentfile ] || exit $?;
```

## CRAB submit
Write a simple CRAB ***config file***, `Early2022/myXibTomumuXi
/CrabSubmit_XibToJpsiXi/crab-MC-XibToJpsiXi_cfg.py`, and a simply ***bash code*** ,`Early2022/myXibTomumuXi
/CrabSubmit_XibToJpsiXi/Condorjob-XibToJpsiXi_fullgen.sh`, to setting up the CMS realeses where all the steps must be run, The steps to run and submit the MC jobs with **CRAB** to the GRID, e.g, for 2022,
```
cmssw-el8
cat /etc/redhat-release
cmsrel CMSSW_12_4_14_patch3 # send the jobs from the realese where you run your step0 GEN in the prepare file or the cfg file for this step
cd CMSSW_12_4_14_patch3/src/
cmsrel
cd ../../CrabSubmit_XibToJpsiXi/
voms-proxy-init -voms cms -valid 192:00
source /cvmfs/cms.cern.ch/common/crab-setup.sh
crab submit -c crab-MC-XibToJpsiXi_cfg.py
```

To check how the submission process proceedsse use:
```
crab status -d crab_PrivateMC-2022-1-XibToJpsiXi/crab_PrivateMC-2022-1-XibToJpsiXi-2025-01-31-23-55
```