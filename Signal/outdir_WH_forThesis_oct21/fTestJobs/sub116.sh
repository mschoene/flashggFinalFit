#!/bin/bash
set -x
touch /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21/fTestJobs/sub116.sh.run
cd /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal
source $VO_CMS_SW_DIR/cmsset_default.sh
source /swshare/glite/external/etc/profile.d/grid-env.sh
export SCRAM_ARCH=slc6_amd64_gcc481
export LD_LIBRARY_PATH=/swshare/glite/d-cache/dcap/lib/:$LD_LIBRARY_PATH
set +x
eval `scramv1 runtime -sh`
set -x
cd $TMPDIR
number=$RANDOM
mkdir -p scratch_$number
cd scratch_$number
if ( /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/bin/signalFTest -i /work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part1.root  -p higgs_2016 -f j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j1to3_b0_pT2_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT2_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j1to3_b1_pT2_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT2_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT2_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT2_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j1to3_b0_pT2_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j4toInf_b0_pT2_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j1to3_b1_pT2_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j4toInf_b1_pT2_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j1to3_b2toInf_pT2_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT2_mt2_30,is1El_pT0_mt2_0,is1Mu_pT0_mt2_0,is1El_pT0_mt2_30,is1Mu_pT0_mt2_30,is1El_pT1_mt2_0,is1Mu_pT1_mt2_0,is1El_pT1_mt2_30,is1Mu_pT1_mt2_30,is1El_pT2_mt2_0,is1Mu_pT2_mt2_0,is1El_pT2_mt2_30,is1Mu_pT2_mt2_30,diBBZ_pT0_mt2_0,diBBZ_pT1_mt2_0,diBBZ_pT2_mt2_0,diBBH_pT0_mt2_0,diBBH_pT1_mt2_0,diBBH_pT2_mt2_0,diBBZ_pT0_mt2_30,diBBZ_pT1_mt2_30,diBBZ_pT2_mt2_30,diBBH_pT0_mt2_30,diBBH_pT1_mt2_30,diBBH_pT2_mt2_30,diLepZ,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2 --considerOnly diBBH_pT1_mt2_0 -o /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21 --datfilename /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21/fTestJobs/outputs/config_117.dat ) then
	 touch /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21/fTestJobs/sub116.sh.done
else
	 touch /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21/fTestJobs/sub116.sh.fail
fi
rm -f /work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/Signal/outdir_WH_forThesis_oct21/fTestJobs/sub116.sh.run
rm -rf scratch_$number
