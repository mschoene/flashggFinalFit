#!/bin/bash

whichSig="WH"

FILE=""

#bash variables
if [[ $whichSig == "HH" ]]; then
    echo "Doing HH"
    FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHH_HToGG_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHH_HToGG_comb_mt2_30_part2.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHH_HToGG_comb_mt2_30_part3.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHH_HToGG_comb_mt2_30_part4.root"
fi

if [[ $whichSig == "HZ" ]]; then
    FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHZ_HToGG_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHZ_HToGG_comb_mt2_30_part2.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHZ_HToGG_comb_mt2_30_part3.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiHZ_HToGG_comb_mt2_30_part4.root"
fi


if [[ $whichSig == "WH" ]]; then
    echo "Doing WH"
    #FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part10.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part11.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part12.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part13.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part14.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part15.root";
    
 #   FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part10.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part11.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part12.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part13.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part14.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part15.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part2.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part3.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part4.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part5.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part6.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part7.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part8.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part9.root";

   FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_TChiWH_HToGG_comb_mt2_30_part1.root";

fi



if [[ $whichSig == "T2bH" ]]; then
    echo "Doing T2bH"

    FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part10.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part2.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part3.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part4.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part5.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part6.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part7.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part8.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part9.root"

#    FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part11.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part12.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part13.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part14.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part15.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part16.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part17.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part18.root"

#    FILE="/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMHDonly_comb_mt2_30_part1.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part20.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part21.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part22.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part23.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part24.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part25.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part26.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part27.root,/work/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_2016_mar13/WS/ws_SMS_T2bH_mSbottom_comb_mt2_30_part19.root"



fi




#EXT=${whichSig}"_mar30_corrSumGenMET"; #extensiom for all folders and files created by this script
#EXT=${whichSig}"_mar30"; #extensiom for all folders and files created by this script
EXT=${whichSig}"_forThesis_oct21"; #extensiom for all folders and files created by this script

PROCS=""





if [[ $whichSig == "T2bH" ]]; then

    PROCS="SMS_T2bH_mSbottom450_mLSP300,SMS_T2bH_mSbottom450_mLSP300_2017,SMS_T2bH_mSbottom450_mLSP1_2017,SMS_T2bH_mSbottom450_mLSP1,SMS_T2bH_mSbottom600_mLSP1_2017,SMS_T2bH_mSbottom600_mLSP1"

    #PROCS="higgs_2017,higgs_2016,SMS_T2bH_mSbottom250_mLSP1,SMS_T2bH_mSbottom250_mLSP50,SMS_T2bH_mSbottom250_mLSP100,SMS_T2bH_mSbottom300_mLSP1,SMS_T2bH_mSbottom300_mLSP50,SMS_T2bH_mSbottom300_mLSP100,SMS_T2bH_mSbottom300_mLSP150,SMS_T2bH_mSbottom350_mLSP1,SMS_T2bH_mSbottom350_mLSP50,SMS_T2bH_mSbottom350_mLSP100,SMS_T2bH_mSbottom350_mLSP150,SMS_T2bH_mSbottom350_mLSP200,SMS_T2bH_mSbottom400_mLSP1,SMS_T2bH_mSbottom400_mLSP50,SMS_T2bH_mSbottom400_mLSP100,SMS_T2bH_mSbottom400_mLSP150,SMS_T2bH_mSbottom400_mLSP200,SMS_T2bH_mSbottom400_mLSP250,SMS_T2bH_mSbottom450_mLSP1,SMS_T2bH_mSbottom450_mLSP50,SMS_T2bH_mSbottom450_mLSP100,SMS_T2bH_mSbottom450_mLSP150,SMS_T2bH_mSbottom450_mLSP200,SMS_T2bH_mSbottom450_mLSP250,SMS_T2bH_mSbottom450_mLSP300,SMS_T2bH_mSbottom500_mLSP1,SMS_T2bH_mSbottom500_mLSP50,SMS_T2bH_mSbottom500_mLSP100,SMS_T2bH_mSbottom500_mLSP150,SMS_T2bH_mSbottom500_mLSP200,SMS_T2bH_mSbottom500_mLSP250,SMS_T2bH_mSbottom500_mLSP300,SMS_T2bH_mSbottom500_mLSP350,SMS_T2bH_mSbottom550_mLSP1,SMS_T2bH_mSbottom550_mLSP50,SMS_T2bH_mSbottom550_mLSP100,SMS_T2bH_mSbottom550_mLSP150,SMS_T2bH_mSbottom550_mLSP200,SMS_T2bH_mSbottom550_mLSP250,SMS_T2bH_mSbottom550_mLSP300,SMS_T2bH_mSbottom550_mLSP350,SMS_T2bH_mSbottom550_mLSP400,SMS_T2bH_mSbottom600_mLSP1,SMS_T2bH_mSbottom600_mLSP50,SMS_T2bH_mSbottom600_mLSP100,SMS_T2bH_mSbottom600_mLSP150,SMS_T2bH_mSbottom600_mLSP200,SMS_T2bH_mSbottom600_mLSP250,SMS_T2bH_mSbottom600_mLSP300,SMS_T2bH_mSbottom600_mLSP350,SMS_T2bH_mSbottom250_mLSP1_2017,SMS_T2bH_mSbottom250_mLSP50_2017,SMS_T2bH_mSbottom250_mLSP100_2017,SMS_T2bH_mSbottom300_mLSP1_2017,SMS_T2bH_mSbottom300_mLSP50_2017,SMS_T2bH_mSbottom300_mLSP100_2017,SMS_T2bH_mSbottom300_mLSP150_2017,SMS_T2bH_mSbottom350_mLSP1_2017,SMS_T2bH_mSbottom350_mLSP50_2017,SMS_T2bH_mSbottom350_mLSP100_2017,SMS_T2bH_mSbottom350_mLSP150_2017,SMS_T2bH_mSbottom350_mLSP200_2017,SMS_T2bH_mSbottom400_mLSP1_2017,SMS_T2bH_mSbottom400_mLSP50_2017,SMS_T2bH_mSbottom400_mLSP100_2017,SMS_T2bH_mSbottom400_mLSP150_2017,SMS_T2bH_mSbottom400_mLSP200_2017,SMS_T2bH_mSbottom400_mLSP250_2017,SMS_T2bH_mSbottom450_mLSP1_2017,SMS_T2bH_mSbottom450_mLSP50_2017,SMS_T2bH_mSbottom450_mLSP100_2017,SMS_T2bH_mSbottom450_mLSP150_2017,SMS_T2bH_mSbottom450_mLSP200_2017,SMS_T2bH_mSbottom450_mLSP250_2017,SMS_T2bH_mSbottom450_mLSP300_2017,SMS_T2bH_mSbottom500_mLSP1_2017,SMS_T2bH_mSbottom500_mLSP50_2017,SMS_T2bH_mSbottom500_mLSP100_2017,SMS_T2bH_mSbottom500_mLSP150_2017,SMS_T2bH_mSbottom500_mLSP200_2017,SMS_T2bH_mSbottom500_mLSP250_2017,SMS_T2bH_mSbottom500_mLSP300_2017,SMS_T2bH_mSbottom500_mLSP350_2017,SMS_T2bH_mSbottom550_mLSP1_2017,SMS_T2bH_mSbottom550_mLSP50_2017,SMS_T2bH_mSbottom550_mLSP100_2017,SMS_T2bH_mSbottom550_mLSP150_2017,SMS_T2bH_mSbottom550_mLSP200_2017,SMS_T2bH_mSbottom550_mLSP250_2017,SMS_T2bH_mSbottom550_mLSP300_2017,SMS_T2bH_mSbottom550_mLSP350_2017,SMS_T2bH_mSbottom550_mLSP400_2017,SMS_T2bH_mSbottom600_mLSP1_2017,SMS_T2bH_mSbottom600_mLSP50_2017,SMS_T2bH_mSbottom600_mLSP100_2017,SMS_T2bH_mSbottom600_mLSP150_2017,SMS_T2bH_mSbottom600_mLSP200_2017,SMS_T2bH_mSbottom600_mLSP250_2017,SMS_T2bH_mSbottom600_mLSP300_2017,SMS_T2bH_mSbottom600_mLSP350_2017"

#    PROCS="higgs_2017,higgs_2016,SMS_T2bH_mSbottom600_mLSP400,SMS_T2bH_mSbottom600_mLSP450,SMS_T2bH_mSbottom650_mLSP1,SMS_T2bH_mSbottom650_mLSP50,SMS_T2bH_mSbottom650_mLSP100,SMS_T2bH_mSbottom650_mLSP150,SMS_T2bH_mSbottom650_mLSP200,SMS_T2bH_mSbottom650_mLSP250,SMS_T2bH_mSbottom650_mLSP300,SMS_T2bH_mSbottom650_mLSP350,SMS_T2bH_mSbottom650_mLSP400,SMS_T2bH_mSbottom650_mLSP450,SMS_T2bH_mSbottom650_mLSP500,SMS_T2bH_mSbottom700_mLSP1,SMS_T2bH_mSbottom700_mLSP50,SMS_T2bH_mSbottom700_mLSP100,SMS_T2bH_mSbottom700_mLSP150,SMS_T2bH_mSbottom700_mLSP200,SMS_T2bH_mSbottom700_mLSP250,SMS_T2bH_mSbottom700_mLSP300,SMS_T2bH_mSbottom700_mLSP350,SMS_T2bH_mSbottom700_mLSP400,SMS_T2bH_mSbottom700_mLSP450,SMS_T2bH_mSbottom700_mLSP500,SMS_T2bH_mSbottom700_mLSP550,SMS_T2bH_mSbottom750_mLSP1,SMS_T2bH_mSbottom750_mLSP50,SMS_T2bH_mSbottom750_mLSP100,SMS_T2bH_mSbottom750_mLSP150,SMS_T2bH_mSbottom750_mLSP200,SMS_T2bH_mSbottom750_mLSP250,SMS_T2bH_mSbottom750_mLSP300,SMS_T2bH_mSbottom750_mLSP350,SMS_T2bH_mSbottom750_mLSP400,SMS_T2bH_mSbottom750_mLSP450,SMS_T2bH_mSbottom750_mLSP500,SMS_T2bH_mSbottom750_mLSP550,SMS_T2bH_mSbottom750_mLSP600,SMS_T2bH_mSbottom800_mLSP1,SMS_T2bH_mSbottom800_mLSP50,SMS_T2bH_mSbottom600_mLSP400_2017,SMS_T2bH_mSbottom600_mLSP450_2017,SMS_T2bH_mSbottom650_mLSP1_2017,SMS_T2bH_mSbottom650_mLSP50_2017,SMS_T2bH_mSbottom650_mLSP100_2017,SMS_T2bH_mSbottom650_mLSP150_2017,SMS_T2bH_mSbottom650_mLSP200_2017,SMS_T2bH_mSbottom650_mLSP250_2017,SMS_T2bH_mSbottom650_mLSP300_2017,SMS_T2bH_mSbottom650_mLSP350_2017,SMS_T2bH_mSbottom650_mLSP400_2017,SMS_T2bH_mSbottom650_mLSP450_2017,SMS_T2bH_mSbottom650_mLSP500_2017,SMS_T2bH_mSbottom700_mLSP1_2017,SMS_T2bH_mSbottom700_mLSP50_2017,SMS_T2bH_mSbottom700_mLSP100_2017,SMS_T2bH_mSbottom700_mLSP150_2017,SMS_T2bH_mSbottom700_mLSP200_2017,SMS_T2bH_mSbottom700_mLSP250_2017,SMS_T2bH_mSbottom700_mLSP300_2017,SMS_T2bH_mSbottom700_mLSP350_2017,SMS_T2bH_mSbottom700_mLSP400_2017,SMS_T2bH_mSbottom700_mLSP450_2017,SMS_T2bH_mSbottom700_mLSP500_2017,SMS_T2bH_mSbottom700_mLSP550_2017,SMS_T2bH_mSbottom750_mLSP1_2017,SMS_T2bH_mSbottom750_mLSP50_2017,SMS_T2bH_mSbottom750_mLSP100_2017,SMS_T2bH_mSbottom750_mLSP150_2017,SMS_T2bH_mSbottom750_mLSP200_2017,SMS_T2bH_mSbottom750_mLSP250_2017,SMS_T2bH_mSbottom750_mLSP300_2017,SMS_T2bH_mSbottom750_mLSP350_2017,SMS_T2bH_mSbottom750_mLSP400_2017,SMS_T2bH_mSbottom750_mLSP450_2017,SMS_T2bH_mSbottom750_mLSP500_2017,SMS_T2bH_mSbottom750_mLSP550_2017,SMS_T2bH_mSbottom750_mLSP600_2017,SMS_T2bH_mSbottom800_mLSP1_2017,SMS_T2bH_mSbottom800_mLSP50_2017"

#    PROCS="higgs_2017,higgs_2016,SMS_T2bH_mSbottom800_mLSP100,SMS_T2bH_mSbottom800_mLSP150,SMS_T2bH_mSbottom800_mLSP200,SMS_T2bH_mSbottom800_mLSP250,SMS_T2bH_mSbottom800_mLSP300,SMS_T2bH_mSbottom800_mLSP350,SMS_T2bH_mSbottom800_mLSP400,SMS_T2bH_mSbottom800_mLSP450,SMS_T2bH_mSbottom800_mLSP500,SMS_T2bH_mSbottom800_mLSP550,SMS_T2bH_mSbottom800_mLSP600,SMS_T2bH_mSbottom800_mLSP650,SMS_T2bH_mSbottom850_mLSP1,SMS_T2bH_mSbottom850_mLSP50,SMS_T2bH_mSbottom850_mLSP100,SMS_T2bH_mSbottom850_mLSP150,SMS_T2bH_mSbottom850_mLSP200,SMS_T2bH_mSbottom850_mLSP250,SMS_T2bH_mSbottom850_mLSP300,SMS_T2bH_mSbottom850_mLSP350,SMS_T2bH_mSbottom850_mLSP400,SMS_T2bH_mSbottom850_mLSP450,SMS_T2bH_mSbottom850_mLSP500,SMS_T2bH_mSbottom850_mLSP550,SMS_T2bH_mSbottom850_mLSP600,SMS_T2bH_mSbottom850_mLSP650,SMS_T2bH_mSbottom850_mLSP700,SMS_T2bH_mSbottom900_mLSP1,SMS_T2bH_mSbottom900_mLSP50,SMS_T2bH_mSbottom900_mLSP100,SMS_T2bH_mSbottom900_mLSP150,SMS_T2bH_mSbottom900_mLSP200,SMS_T2bH_mSbottom900_mLSP250,SMS_T2bH_mSbottom900_mLSP300,SMS_T2bH_mSbottom900_mLSP350,SMS_T2bH_mSbottom900_mLSP400,SMS_T2bH_mSbottom900_mLSP450,SMS_T2bH_mSbottom900_mLSP500,SMS_T2bH_mSbottom900_mLSP550,SMS_T2bH_mSbottom900_mLSP600,SMS_T2bH_mSbottom900_mLSP650,SMS_T2bH_mSbottom900_mLSP700,SMS_T2bH_mSbottom900_mLSP750,SMS_T2bH_mSbottom800_mLSP100_2017,SMS_T2bH_mSbottom800_mLSP150_2017,SMS_T2bH_mSbottom800_mLSP200_2017,SMS_T2bH_mSbottom800_mLSP250_2017,SMS_T2bH_mSbottom800_mLSP300_2017,SMS_T2bH_mSbottom800_mLSP350_2017,SMS_T2bH_mSbottom800_mLSP400_2017,SMS_T2bH_mSbottom800_mLSP450_2017,SMS_T2bH_mSbottom800_mLSP500_2017,SMS_T2bH_mSbottom800_mLSP550_2017,SMS_T2bH_mSbottom800_mLSP600_2017,SMS_T2bH_mSbottom800_mLSP650_2017,SMS_T2bH_mSbottom850_mLSP1_2017,SMS_T2bH_mSbottom850_mLSP50_2017,SMS_T2bH_mSbottom850_mLSP100_2017,SMS_T2bH_mSbottom850_mLSP150_2017,SMS_T2bH_mSbottom850_mLSP200_2017,SMS_T2bH_mSbottom850_mLSP250_2017,SMS_T2bH_mSbottom850_mLSP300_2017,SMS_T2bH_mSbottom850_mLSP350_2017,SMS_T2bH_mSbottom850_mLSP400_2017,SMS_T2bH_mSbottom850_mLSP450_2017,SMS_T2bH_mSbottom850_mLSP500_2017,SMS_T2bH_mSbottom850_mLSP550_2017,SMS_T2bH_mSbottom850_mLSP600_2017,SMS_T2bH_mSbottom850_mLSP650_2017,SMS_T2bH_mSbottom850_mLSP700_2017,SMS_T2bH_mSbottom900_mLSP1_2017,SMS_T2bH_mSbottom900_mLSP50_2017,SMS_T2bH_mSbottom900_mLSP100_2017,SMS_T2bH_mSbottom900_mLSP150_2017,SMS_T2bH_mSbottom900_mLSP200_2017,SMS_T2bH_mSbottom900_mLSP250_2017,SMS_T2bH_mSbottom900_mLSP300_2017,SMS_T2bH_mSbottom900_mLSP350_2017,SMS_T2bH_mSbottom900_mLSP400_2017,SMS_T2bH_mSbottom900_mLSP450_2017,SMS_T2bH_mSbottom900_mLSP500_2017,SMS_T2bH_mSbottom900_mLSP550_2017,SMS_T2bH_mSbottom900_mLSP600_2017,SMS_T2bH_mSbottom900_mLSP650_2017,SMS_T2bH_mSbottom900_mLSP700_2017,SMS_T2bH_mSbottom900_mLSP750_2017"

fi


if [[ $whichSig == "WH" ]]; then
    
    PROCS="higgs_2017,higgs_2016"
#    PROCS="SMS_TChiWH_HToGG_m200_m1,SMS_TChiWH_HToGG_m200_m1_2017,SMS_TChiWH_HToGG_m225_m50,SMS_TChiWH_HToGG_m225_m50_2017,SMS_TChiWH_HToGG_m175_m1,SMS_TChiWH_HToGG_m175_m1_2017"
    
#    PROCS="higgs_2017,higgs_2016,SMS_TChiWH_HToGG_m325_m1,SMS_TChiWH_HToGG_m325_m25,SMS_TChiWH_HToGG_m325_m50,SMS_TChiWH_HToGG_m325_m75,SMS_TChiWH_HToGG_m325_m100,SMS_TChiWH_HToGG_m325_m125,SMS_TChiWH_HToGG_m325_m150,SMS_TChiWH_HToGG_m325_m175,SMS_TChiWH_HToGG_m325_m199,SMS_TChiWH_HToGG_m325_m1_2017,SMS_TChiWH_HToGG_m325_m25_2017,SMS_TChiWH_HToGG_m325_m50_2017,SMS_TChiWH_HToGG_m325_m75_2017,SMS_TChiWH_HToGG_m325_m100_2017,SMS_TChiWH_HToGG_m325_m125_2017,SMS_TChiWH_HToGG_m325_m150_2017,SMS_TChiWH_HToGG_m325_m175_2017,SMS_TChiWH_HToGG_m325_m199_2017"

#    PROCS="higgs_2017,higgs_2016,SMS_TChiWH_HToGG_m127_m1,SMS_TChiWH_HToGG_m150_m1,SMS_TChiWH_HToGG_m150_m24,SMS_TChiWH_HToGG_m175_m1,SMS_TChiWH_HToGG_m175_m25,SMS_TChiWH_HToGG_m175_m49,SMS_TChiWH_HToGG_m200_m1,SMS_TChiWH_HToGG_m200_m25,SMS_TChiWH_HToGG_m200_m50,SMS_TChiWH_HToGG_m200_m74,SMS_TChiWH_HToGG_m225_m1,SMS_TChiWH_HToGG_m225_m25,SMS_TChiWH_HToGG_m225_m50,SMS_TChiWH_HToGG_m225_m75,SMS_TChiWH_HToGG_m225_m99,SMS_TChiWH_HToGG_m250_m1,SMS_TChiWH_HToGG_m250_m25,SMS_TChiWH_HToGG_m250_m50,SMS_TChiWH_HToGG_m250_m75,SMS_TChiWH_HToGG_m250_m100,SMS_TChiWH_HToGG_m250_m124,SMS_TChiWH_HToGG_m127_m1_2017,SMS_TChiWH_HToGG_m150_m1_2017,SMS_TChiWH_HToGG_m150_m24_2017,SMS_TChiWH_HToGG_m175_m1_2017,SMS_TChiWH_HToGG_m175_m25_2017,SMS_TChiWH_HToGG_m175_m49_2017,SMS_TChiWH_HToGG_m200_m1_2017,SMS_TChiWH_HToGG_m200_m25_2017,SMS_TChiWH_HToGG_m200_m50_2017,SMS_TChiWH_HToGG_m200_m74_2017,SMS_TChiWH_HToGG_m225_m1_2017,SMS_TChiWH_HToGG_m225_m25_2017,SMS_TChiWH_HToGG_m225_m50_2017,SMS_TChiWH_HToGG_m225_m75_2017,SMS_TChiWH_HToGG_m225_m99_2017,SMS_TChiWH_HToGG_m250_m1_2017,SMS_TChiWH_HToGG_m250_m25_2017,SMS_TChiWH_HToGG_m250_m50_2017,SMS_TChiWH_HToGG_m250_m75_2017,SMS_TChiWH_HToGG_m250_m100_2017,SMS_TChiWH_HToGG_m250_m124_2017,SMS_TChiWH_HToGG_m275_m1,SMS_TChiWH_HToGG_m275_m25,SMS_TChiWH_HToGG_m275_m50,SMS_TChiWH_HToGG_m275_m75,SMS_TChiWH_HToGG_m275_m100,SMS_TChiWH_HToGG_m275_m125,SMS_TChiWH_HToGG_m275_m149,SMS_TChiWH_HToGG_m300_m1,SMS_TChiWH_HToGG_m300_m25,SMS_TChiWH_HToGG_m300_m50,SMS_TChiWH_HToGG_m300_m75,SMS_TChiWH_HToGG_m300_m100,SMS_TChiWH_HToGG_m300_m125,SMS_TChiWH_HToGG_m300_m150,SMS_TChiWH_HToGG_m300_m174,SMS_TChiWH_HToGG_m275_m1_2017,SMS_TChiWH_HToGG_m275_m25_2017,SMS_TChiWH_HToGG_m275_m50_2017,SMS_TChiWH_HToGG_m275_m75_2017,SMS_TChiWH_HToGG_m275_m100_2017,SMS_TChiWH_HToGG_m275_m125_2017,SMS_TChiWH_HToGG_m275_m149_2017,SMS_TChiWH_HToGG_m300_m1_2017,SMS_TChiWH_HToGG_m300_m25_2017,SMS_TChiWH_HToGG_m300_m50_2017,SMS_TChiWH_HToGG_m300_m75_2017,SMS_TChiWH_HToGG_m300_m100_2017,SMS_TChiWH_HToGG_m300_m125_2017,SMS_TChiWH_HToGG_m300_m150_2017,SMS_TChiWH_HToGG_m300_m174_2017,SMS_TChiWH_HToGG_m325_m1,SMS_TChiWH_HToGG_m325_m25,SMS_TChiWH_HToGG_m325_m50,SMS_TChiWH_HToGG_m325_m75,SMS_TChiWH_HToGG_m325_m100,SMS_TChiWH_HToGG_m325_m125,SMS_TChiWH_HToGG_m325_m150,SMS_TChiWH_HToGG_m325_m175,SMS_TChiWH_HToGG_m325_m199,SMS_TChiWH_HToGG_m350_m1,SMS_TChiWH_HToGG_m350_m25,SMS_TChiWH_HToGG_m350_m50,SMS_TChiWH_HToGG_m350_m75,SMS_TChiWH_HToGG_m350_m100,SMS_TChiWH_HToGG_m350_m125,SMS_TChiWH_HToGG_m350_m150,SMS_TChiWH_HToGG_m350_m175,SMS_TChiWH_HToGG_m350_m200,SMS_TChiWH_HToGG_m350_m224,SMS_TChiWH_HToGG_m325_m1_2017,SMS_TChiWH_HToGG_m325_m25_2017,SMS_TChiWH_HToGG_m325_m50_2017,SMS_TChiWH_HToGG_m325_m75_2017,SMS_TChiWH_HToGG_m325_m100_2017,SMS_TChiWH_HToGG_m325_m125_2017,SMS_TChiWH_HToGG_m325_m150_2017,SMS_TChiWH_HToGG_m325_m175_2017,SMS_TChiWH_HToGG_m325_m199_2017,SMS_TChiWH_HToGG_m350_m1_2017,SMS_TChiWH_HToGG_m350_m25_2017,SMS_TChiWH_HToGG_m350_m50_2017,SMS_TChiWH_HToGG_m350_m75_2017,SMS_TChiWH_HToGG_m350_m100_2017,SMS_TChiWH_HToGG_m350_m125_2017,SMS_TChiWH_HToGG_m350_m150_2017,SMS_TChiWH_HToGG_m350_m175_2017,SMS_TChiWH_HToGG_m350_m200_2017,SMS_TChiWH_HToGG_m350_m224_2017"

fi




#SMS_TChiWH_HToGG_m375_m1_2017,SMS_TChiWH_HToGG_m375_m25_2017,SMS_TChiWH_HToGG_m375_m50_2017,SMS_TChiWH_HToGG_m375_m75_2017,SMS_TChiWH_HToGG_m375_m100_2017,SMS_TChiWH_HToGG_m375_m125_2017,SMS_TChiWH_HToGG_m375_m150_2017,SMS_TChiWH_HToGG_m375_m175_2017,SMS_TChiWH_HToGG_m375_m200_2017,SMS_TChiWH_HToGG_m375_m225_2017,SMS_TChiWH_HToGG_m375_m249_2017
#SMS_TChiWH_HToGG_m375_m1,SMS_TChiWH_HToGG_m375_m25,SMS_TChiWH_HToGG_m375_m50,SMS_TChiWH_HToGG_m375_m75,SMS_TChiWH_HToGG_m375_m100,SMS_TChiWH_HToGG_m375_m125,SMS_TChiWH_HToGG_m375_m150,SMS_TChiWH_HToGG_m375_m175,SMS_TChiWH_HToGG_m375_m200,SMS_TChiWH_HToGG_m375_m225,SMS_TChiWH_HToGG_m375_m249,

#SMS_TChiWH_HToGG_m400_m1_2017,SMS_TChiWH_HToGG_m400_m25_2017,SMS_TChiWH_HToGG_m400_m50_2017,SMS_TChiWH_HToGG_m400_m75_2017,SMS_TChiWH_HToGG_m400_m100_2017,SMS_TChiWH_HToGG_m400_m125_2017,SMS_TChiWH_HToGG_m400_m150_2017,SMS_TChiWH_HToGG_m400_m175_2017,SMS_TChiWH_HToGG_m400_m200_2017,SMS_TChiWH_HToGG_m400_m225_2017,SMS_TChiWH_HToGG_m400_m250_2017,SMS_TChiWH_HToGG_m400_m274_2017
#SMS_TChiWH_HToGG_m400_m1,SMS_TChiWH_HToGG_m400_m25,SMS_TChiWH_HToGG_m400_m50,SMS_TChiWH_HToGG_m400_m75,SMS_TChiWH_HToGG_m400_m100,SMS_TChiWH_HToGG_m400_m125,SMS_TChiWH_HToGG_m400_m150,SMS_TChiWH_HToGG_m400_m175,SMS_TChiWH_HToGG_m400_m200,SMS_TChiWH_HToGG_m400_m225,SMS_TChiWH_HToGG_m400_m250,SMS_TChiWH_HToGG_m400_m274

#use
if [[ $whichSig == "HZ" ]]; then

    PROCS="SMS_TChiHZ_HToGG_m127_2017,SMS_TChiHZ_HToGG_m127,SMS_TChiHZ_HToGG_m175_2017,SMS_TChiHZ_HToGG_m175"

    #PROCS="higgs_2017,SMS_TChiHZ_HToGG_m127_2017,SMS_TChiHZ_HToGG_m150_2017,SMS_TChiHZ_HToGG_m175_2017,SMS_TChiHZ_HToGG_m200_2017,higgs_2016,SMS_TChiHZ_HToGG_m127,SMS_TChiHZ_HToGG_m150,SMS_TChiHZ_HToGG_m175,SMS_TChiHZ_HToGG_m200,SMS_TChiHZ_HToGG_m225_2017,SMS_TChiHZ_HToGG_m225,SMS_TChiHZ_HToGG_m250_2017,SMS_TChiHZ_HToGG_m250,SMS_TChiHZ_HToGG_m275,SMS_TChiHZ_HToGG_m275_2017,SMS_TChiHZ_HToGG_m300,SMS_TChiHZ_HToGG_m300_2017,SMS_TChiHZ_HToGG_m325,SMS_TChiHZ_HToGG_m325_2017,SMS_TChiHZ_HToGG_m350,SMS_TChiHZ_HToGG_m350_2017,SMS_TChiHZ_HToGG_m375,SMS_TChiHZ_HToGG_m375_2017,SMS_TChiHZ_HToGG_m400,SMS_TChiHZ_HToGG_m400_2017,SMS_TChiHZ_HToGG_m425,SMS_TChiHZ_HToGG_m425_2017,SMS_TChiHZ_HToGG_m450,SMS_TChiHZ_HToGG_m450_2017,SMS_TChiHZ_HToGG_m475,SMS_TChiHZ_HToGG_m475_2017,SMS_TChiHZ_HToGG_m500,SMS_TChiHZ_HToGG_m500_2017" #,SMS_TChiHZ_HToGG_m525,SMS_TChiHZ_HToGG_m525_2017" #,SMS_TChiHZ_HToGG_m550,SMS_TChiHZ_HToGG_m550_2017,SMS_TChiHZ_HToGG_m575,SMS_TChiHZ_HToGG_m575_2017,SMS_TChiHZ_HToGG_m600,SMS_TChiHZ_HToGG_m600_2017,SMS_TChiHZ_HToGG_m625,SMS_TChiHZ_HToGG_m625_2017,SMS_TChiHZ_HToGG_m650,SMS_TChiHZ_HToGG_m650_2017,SMS_TChiHZ_HToGG_m675,SMS_TChiHZ_HToGG_m675_2017,SMS_TChiHZ_HToGG_m700,SMS_TChiHZ_HToGG_m700_2017,SMS_TChiHZ_HToGG_m725,SMS_TChiHZ_HToGG_m725_2017,SMS_TChiHZ_HToGG_m750,SMS_TChiHZ_HToGG_m750_2017,SMS_TChiHZ_HToGG_m775,SMS_TChiHZ_HToGG_m775_2017,SMS_TChiHZ_HToGG_m800,SMS_TChiHZ_HToGG_m800_2017,SMS_TChiHZ_HToGG_m825,SMS_TChiHZ_HToGG_m825_2017,SMS_TChiHZ_HToGG_m850,SMS_TChiHZ_HToGG_m850_2017,SMS_TChiHZ_HToGG_m875,SMS_TChiHZ_HToGG_m875_2017,SMS_TChiHZ_HToGG_m900,SMS_TChiHZ_HToGG_m900_2017,SMS_TChiHZ_HToGG_m925,SMS_TChiHZ_HToGG_m925_2017,SMS_TChiHZ_HToGG_m950,SMS_TChiHZ_HToGG_m950_2017,SMS_TChiHZ_HToGG_m1000,SMS_TChiHZ_HToGG_m1000_2017"
fi




#use
if [[ $whichSig == "HH" ]]; then

#    PROCS="higgs_2017,higgs_2016" #,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m175_2017"
    
    PROCS="higgs_2017,higgs_2016,SMS_TChiHH_HToGG_m127,SMS_TChiHH_HToGG_m127_2017,SMS_TChiHH_HToGG_m275,SMS_TChiHH_HToGG_m275_2017,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m175_2017"
    
   # PROCS="higgs_2017,SMS_TChiHH_HToGG_m127_2017,SMS_TChiHH_HToGG_m150_2017,SMS_TChiHH_HToGG_m175_2017,SMS_TChiHH_HToGG_m200_2017,higgs_2016,SMS_TChiHH_HToGG_m127,SMS_TChiHH_HToGG_m150,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m200,SMS_TChiHH_HToGG_m225_2017,SMS_TChiHH_HToGG_m225,SMS_TChiHH_HToGG_m250_2017,SMS_TChiHH_HToGG_m250,SMS_TChiHH_HToGG_m275,SMS_TChiHH_HToGG_m275_2017,SMS_TChiHH_HToGG_m300,SMS_TChiHH_HToGG_m300_2017,SMS_TChiHH_HToGG_m325,SMS_TChiHH_HToGG_m325_2017,SMS_TChiHH_HToGG_m350,SMS_TChiHH_HToGG_m350_2017,SMS_TChiHH_HToGG_m375,SMS_TChiHH_HToGG_m375_2017,SMS_TChiHH_HToGG_m400,SMS_TChiHH_HToGG_m400_2017,SMS_TChiHH_HToGG_m425,SMS_TChiHH_HToGG_m425_2017,SMS_TChiHH_HToGG_m450,SMS_TChiHH_HToGG_m450_2017,SMS_TChiHH_HToGG_m475,SMS_TChiHH_HToGG_m475_2017,SMS_TChiHH_HToGG_m500,SMS_TChiHH_HToGG_m500_2017,SMS_TChiHH_HToGG_m525,SMS_TChiHH_HToGG_m525_2017" #,SMS_TChiHH_HToGG_m550,SMS_TChiHH_HToGG_m550_2017,SMS_TChiHH_HToGG_m575,SMS_TChiHH_HToGG_m575_2017,SMS_TChiHH_HToGG_m600,SMS_TChiHH_HToGG_m600_2017,SMS_TChiHH_HToGG_m625,SMS_TChiHH_HToGG_m625_2017,SMS_TChiHH_HToGG_m650,SMS_TChiHH_HToGG_m650_2017,SMS_TChiHH_HToGG_m675,SMS_TChiHH_HToGG_m675_2017,SMS_TChiHH_HToGG_m700,SMS_TChiHH_HToGG_m700_2017,SMS_TChiHH_HToGG_m725,SMS_TChiHH_HToGG_m725_2017,SMS_TChiHH_HToGG_m750,SMS_TChiHH_HToGG_m750_2017,SMS_TChiHH_HToGG_m775,SMS_TChiHH_HToGG_m775_2017,SMS_TChiHH_HToGG_m800,SMS_TChiHH_HToGG_m800_2017,SMS_TChiHH_HToGG_m825,SMS_TChiHH_HToGG_m825_2017,SMS_TChiHH_HToGG_m850,SMS_TChiHH_HToGG_m850_2017,SMS_TChiHH_HToGG_m875,SMS_TChiHH_HToGG_m875_2017,SMS_TChiHH_HToGG_m900,SMS_TChiHH_HToGG_m900_2017,SMS_TChiHH_HToGG_m925,SMS_TChiHH_HToGG_m925_2017,SMS_TChiHH_HToGG_m950,SMS_TChiHH_HToGG_m950_2017,SMS_TChiHH_HToGG_m1000,SMS_TChiHH_HToGG_m1000_2017"
fi



#PROCS="higgs_2017,SMS_TChiWH_HToGG_127_1_2017,SMS_TChiWH_HToGG_150_1_2017,SMS_TChiWH_HToGG_150_24_2017,higgs_2016,SMS_TChiWH_HToGG_127_1,SMS_TChiWH_HToGG_150_1,SMS_TChiWH_HToGG_150_24"




#PROCS="higgs,SMS_TChiHH_HToGG_m127,SMS_TChiHH_HToGG_m150,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m200,SMS_TChiHH_HToGG_m225,SMS_TChiHH_HToGG_m250,SMS_TChiHH_HToGG_m275,SMS_TChiHH_HToGG_m300,SMS_TChiHH_HToGG_m325,SMS_TChiHH_HToGG_m350,SMS_TChiHH_HToGG_m375,SMS_TChiHH_HToGG_m400,SMS_TChiHH_HToGG_m425,SMS_TChiHH_HToGG_m450,SMS_TChiHH_HToGG_m475,SMS_TChiHH_HToGG_m500,SMS_TChiHH_HToGG_m525,SMS_TChiHH_HToGG_m550,SMS_TChiHH_HToGG_m575,SMS_TChiHH_HToGG_m600,SMS_TChiHH_HToGG_m625,SMS_TChiHH_HToGG_m650,SMS_TChiHH_HToGG_m675,SMS_TChiHH_HToGG_m700,SMS_TChiHH_HToGG_m725,SMS_TChiHH_HToGG_m750,SMS_TChiHH_HToGG_m775,SMS_TChiHH_HToGG_m800,SMS_TChiHH_HToGG_m825,SMS_TChiHH_HToGG_m850,SMS_TChiHH_HToGG_m875,SMS_TChiHH_HToGG_m900,SMS_TChiHH_HToGG_m925,SMS_TChiHH_HToGG_m950,SMS_TChiHH_HToGG_m975,SMS_TChiHH_HToGG_m1000"







#CATS="j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2"

CATS="j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j1to3_b0_pT2_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT2_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j1to3_b1_pT2_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT2_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT2_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT2_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j1to3_b0_pT2_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j4toInf_b0_pT2_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j1to3_b1_pT2_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j4toInf_b1_pT2_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j1to3_b2toInf_pT2_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT2_mt2_30,is1El_pT0_mt2_0,is1Mu_pT0_mt2_0,is1El_pT0_mt2_30,is1Mu_pT0_mt2_30,is1El_pT1_mt2_0,is1Mu_pT1_mt2_0,is1El_pT1_mt2_30,is1Mu_pT1_mt2_30,is1El_pT2_mt2_0,is1Mu_pT2_mt2_0,is1El_pT2_mt2_30,is1Mu_pT2_mt2_30,diBBZ_pT0_mt2_0,diBBZ_pT1_mt2_0,diBBZ_pT2_mt2_0,diBBH_pT0_mt2_0,diBBH_pT1_mt2_0,diBBH_pT2_mt2_0,diBBZ_pT0_mt2_30,diBBZ_pT1_mt2_30,diBBZ_pT2_mt2_30,diBBH_pT0_mt2_30,diBBH_pT1_mt2_30,diBBH_pT2_mt2_30,diLepZ,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2"

#CATS="j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j1to3_b0_pT2_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT2_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j1to3_b1_pT2_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT2_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT2_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT2_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j1to3_b0_pT2_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j4toInf_b0_pT2_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j1to3_b1_pT2_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j4toInf_b1_pT2_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j1to3_b2toInf_pT2_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT2_mt2_30,is1El_pT0_mt2_0,is1Mu_pT0_mt2_0,is1El_pT0_mt2_30,is1Mu_pT0_mt2_30,is1El_pT1_mt2_0,is1Mu_pT1_mt2_0,is1El_pT1_mt2_30,is1Mu_pT1_mt2_30,is1El_pT2_mt2_0,is1Mu_pT2_mt2_0,is1El_pT2_mt2_30,is1Mu_pT2_mt2_30,diBBZ_pT0_mt2_0,diBBZ_pT1_mt2_0,diBBZ_pT2_mt2_0,diBBH_pT0_mt2_0,diBBH_pT1_mt2_0,diBBH_pT2_mt2_0,diBBZ_pT0_mt2_30,diBBZ_pT1_mt2_30,diBBZ_pT2_mt2_30,diBBH_pT0_mt2_30,diBBH_pT1_mt2_30,diBBH_pT2_mt2_30,diLepZ,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2"

#CATS="j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,is1El_pT0_mt2_0,is1Mu_pT0_mt2_0,is1El_pT0_mt2_30,is1Mu_pT0_mt2_30,is1El_pT1_mt2_0,is1Mu_pT1_mt2_0,is1El_pT1_mt2_30,is1Mu_pT1_mt2_30,diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,diLepZ,j0_b0toInf_pT0,j0_b0toInf_pT1"


SCALES=""
#SCALES="HighR9EE,LowR9EE,HighR9EB,LowR9EB"
#SCALESCORR="MaterialCentral,MaterialForward,FNUFEE,FNUFEB,ShowerShapeHighR9EE,ShowerShapeHighR9EB,ShowerShapeLowR9EE,ShowerShapeLowR9EB"
SCALESCORR=""
#SCALESCORR="MaterialCentral,MaterialForward"
#SCALESGLOBAL="NonLinearity:0:2.6"
SCALESGLOBAL="NonLinearity,Geant4,LightYield,Absolute"
SMEARS="HighR9EE,LowR9EE,HighR9EB,LowR9EB" #DRY RUN
MASSLIST="120,125,130"
FTESTONLY=0
CALCPHOSYSTONLY=0
SIGFITONLY=0
SIGPLOTSONLY=0
INTLUMI=0.001
BATCH="T3"
DEFAULTQUEUE=""
BS=""

usage(){
	echo "The script runs three signal scripts in this order:"
		echo "signalFTest --> determines number of gaussians to use for fits of each Tag/Process"
		echo "calcPhotonSystConsts --> scale and smear ets of photons systematic variations"
		echo "SignalFit --> actually determine the number of gaussians to fit"
		echo "options:"
		echo "-h|--help) "
		echo "-i|--inputFile) "
		echo "-p|--procs) "
		echo "-f|--flashggCats) (default UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,UntaggedTag_4,VBFTag_0,VBFTag_1,VBFTag_2,TTHHadronicTag,TTHLeptonicTag,VHHadronicTag,VHTightTag,VHLooseTag,VHEtTag)"
		echo "--ext)  (default auto)"
		echo "--fTestOnly) "
		echo "--calcPhoSystOnly) "
		echo "--sigFitOnly) "
		echo "--sigPlotsOnly) "
		echo "--intLumi) specified in fb^-{1} (default $INTLUMI)) "
		echo "--batch) which batch system to use (None (''),LSF,IC) (default '$BATCH')) "
}


#------------------------------ parsing


# options may be followed by one colon to indicate they have a required argument
if ! options=$(getopt -u -o hi:p:f: -l help,inputFile:,procs:,bs:,smears:,massList:,scales:,scalesCorr:,scalesGlobal:,flashggCats:,ext:,fTestOnly,calcPhoSystOnly,sigFitOnly,sigPlotsOnly,intLumi:,batch: -- "$@")
then
# something went wrong, getopt will put out an error message for us
exit 1
fi
set -- $options

while [ $# -gt 0 ]
do
case $1 in
-h|--help) usage; exit 0;;
-i|--inputFile) FILE=$2; shift ;;
-p|--procs) PROCS=$2; shift ;;
--massList) MASSLIST=$2; shift ;;
--smears) SMEARS=$2; shift ;;
--scales) SCALES=$2; shift ;;
--scalesCorr) SCALESCORR=$2; shift ;;
--scalesGlobal) SCALESGLOBAL=$2; shift ;;
--bs) BS=$2; shift ;;
-f|--flashggCats) CATS=$2; shift ;;
--ext) EXT=$2 ; shift ;;
--fTestOnly) FTESTONLY=1 ;;
--calcPhoSystOnly) CALCPHOSYSTONLY=1;;
--sigFitOnly) SIGFITONLY=1;;
--sigPlotsOnly) SIGPLOTSONLY=1;;
--intLumi) INTLUMI=$2; shift ;;
--batch) BATCH=$2; shift;;

(--) shift; break;;
(-*) usage; echo "$0: [ERROR] - unrecognized option $1" 1>&2; usage >> /dev/stderr; exit 1;;
(*) break;;
esac
shift
done

echo "[INFO] processing signal model for INTLUMI $INTLUMI"

OUTDIR="outdir_$EXT"
echo "[INFO] outdir is $OUTDIR" 
if [[ $FILE == "" ]];then
echo "[ERROR], input file (--inputFile or -i) is mandatory!"
exit 0
fi

if [ $FTESTONLY == 0 -a $CALCPHOSYSTONLY == 0 -a $SIGFITONLY == 0 -a $SIGPLOTSONLY == 0 ]; then
#IF not particular script specified, run all!
FTESTONLY=1
CALCPHOSYSTONLY=1
SIGFITONLY=1
SIGPLOTSONLY=1
fi

if [[ $BATCH == "IC" ]]; then
DEFAULTQUEUE=hep.q
fi
if [[ $BATCH == "LSF" ]]; then
DEFAULTQUEUE=1nh
fi
if [[ $BATCH == "T3" ]]; then
DEFAULTQUEUE=short.q
fi
BSOPT=""

if [[ $BS == "" ]]; then
echo "[INFO] NO BeamSpot SIZE SPECIFIED - DEFAULT FROM MC WILL BE USED"
else
echo "[INFO] BeamSpot Size is to be reweighted to $BS"
BSOPT=" --bs $BS"
fi

####################################################
################## SIGNAL F-TEST ###################
####################################################
#ls dat/newConfig_${EXT}.dat
if [ -e dat/newConfig_${EXT}.dat ]; then
  echo "[INFO] sigFTest dat file $OUTDIR/dat/copy_newConfig_${EXT}.dat already exists, so SKIPPING SIGNAL FTEST"
else
  if [ $FTESTONLY == 1 ]; then
    mkdir -p $OUTDIR/fTest
    echo "=============================="
    echo "Running Signal F-Test"
    echo "-->Determine Number of gaussians"
    echo "=============================="
    if [ -z $BATCH ]; then
	echo "./bin/signalFTest -i $FILE -d dat/newConfig_$EXT.dat -p $PROCS -f $CATS -o $OUTDIR"
	./bin/signalFTest -i $FILE -d dat/newConfig_$EXT.dat -p $PROCS -f $CATS -o $OUTDIR
    else
        echo "./python/submitSignaFTest.py --procs $PROCS --flashggCats $CATS --outDir $OUTDIR --i $FILE --batch $BATCH -q $DEFAULTQUEUE"
	./python/submitSignaFTest.py --procs $PROCS --flashggCats $CATS --outDir $OUTDIR --i $FILE --batch $BATCH -q $DEFAULTQUEUE



	PEND=`ls -l $OUTDIR/fTestJobs/sub*| grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" |grep -v "\.log"  |wc -l`
	echo "PEND $PEND"
	while (( $PEND > 0 )) ; do
            PEND=`ls -l $OUTDIR/fTestJobs/sub* | grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" | grep -v "\.log" |wc -l`
            RUN=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.run" |wc -l`
            FAIL=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.fail" |wc -l`
            DONE=`ls -l $OUTDIR/fTestJobs/sub* | grep "\.done" |wc -l`
            (( PEND=$PEND-$RUN-$FAIL-$DONE ))
            echo " PEND $PEND - RUN $RUN - DONE $DONE - FAIL $FAIL"
            if (( $RUN > 0 )) ; then PEND=1 ; fi
            if (( $FAIL > 0 )) ; then 
		echo "[ERROR] at least one job failed :"
		ls -l $OUTDIR/fTestJobs/sub* | grep "\.fail"
		exit 1
            fi
            sleep 10
	    done
    fi
    mkdir -p $OUTDIR/dat
    cat $OUTDIR/fTestJobs/outputs/* > dat/newConfig_${EXT}_temp.dat
    sort -u dat/newConfig_${EXT}_temp.dat  > dat/tmp_newConfig_${EXT}_temp.dat 
    mv dat/tmp_newConfig_${EXT}_temp.dat dat/newConfig_${EXT}_temp.dat
    cp dat/newConfig_${EXT}_temp.dat $OUTDIR/dat/copy_newConfig_${EXT}_temp.dat
    rm -rf $OUTDIR/sigfTest
    mv $OUTDIR/fTest $OUTDIR/sigfTest
  fi
  echo "[INFO] SUCCESS sigFTest jobs completed, check output and do:"
  echo "cp $PWD/dat/newConfig_${EXT}_temp.dat $PWD/dat/newConfig_${EXT}.dat"
  echo "and manually amend chosen number of gaussians using the output pdfs here:"
	echo "Signal/outdir_${EXT}/sigfTest/"
  echo "then re-run the same command to continue !"
  CALCPHOSYSTONLY=0
  SIGFITONLY=0
  SIGPLOTSONLY=0
	exit 1
fi
####################################################
################## CALCPHOSYSTCONSTS ###################
####################################################

if [ $CALCPHOSYSTONLY == 1 ]; then

  echo "=============================="
  echo "Running calcPho"
  echo "-->Determine effect of photon systematics"
  echo "=============================="

#  echo "./bin/calcPhotonSystConsts -i $FILE -o dat/photonCatSyst_$EXT.dat -p $PROCS -s $SCALES -S $SCALESCORR -g $SCALESGLOBAL -r $SMEARS -D $OUTDIR -f $CATS"
 # ./bin/calcPhotonSystConsts -i $FILE -o dat/photonCatSyst_$EXT.dat -p $PROCS -s $SCALES -S $SCALESCORR -g $SCALESGLOBAL -r $SMEARS -D $OUTDIR -f $CATS 
  #cp dat/photonCatSyst_$EXT.dat $OUTDIR/dat/copy_photonCatSyst_$EXT.dat
fi
####################################################
####################### SIGFIT #####################
####################################################
if [ $SIGFITONLY == 1 ]; then

    echo "=============================="
    echo "Running SignalFit"
    echo "-->Create actual signal model"
    echo "=============================="


    if [[ $BATCH == "" ]]; then
    	echo "./bin/SignalFit -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_mva_13TeV_sigfit.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI "
    	./bin/SignalFit -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_mva_13TeV_sigfit.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI --massList $MASSLIST #--pdfWeights 26

    else
	
	# echo "./python/submitSignalFit.py -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_sigfit_$EXT.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI --batch $BATCH --massList $MASSLIST -q $DEFAULTQUEUE $BSOPT "
    	# ./python/submitSignalFit.py -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_sigfit_$EXT.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI --batch $BATCH --massList $MASSLIST -q $DEFAULTQUEUE $BSOPT 

    	# PEND=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub*| grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" |grep -v "\.log"  |wc -l`
    	# echo "PEND $PEND"
    	# while (( $PEND > 0 )) ; do
    	#     PEND=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" | grep -v "\.log" |wc -l`
    	#     RUN=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.run" |wc -l`
    	#     FAIL=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.fail" |wc -l`
    	#     DONE=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.done" |wc -l`
    	#     (( PEND=$PEND-$RUN-$FAIL-$DONE ))
    	#     echo " PEND $PEND - RUN $RUN - DONE $DONE - FAIL $FAIL"
    	#     if (( $RUN > 0 )) ; then PEND=1 ; fi
    	#     if (( $FAIL > 0 )) ; then 
    	# 	echo "ERROR at least one job failed :"
    	# 	ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.fail"
    	# 	exit 1
    	#     fi
    	#     sleep 30
	    
    	#     done


	if [[ $whichSig == "WH" ]]; then  
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*m200_m1*.root > out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*m175_m1*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root >> out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*m225_m50*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root >> out.txt"
	fi


	if [[ $whichSig == "HZ" ]]; then
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*127*.root > out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*175*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root >> out.txt"
	   # ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_higgs*.root >> out.txt
	   # echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_higgs*.root > out.txt"
	fi

	if [[ $whichSig == "HH" ]]; then
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*127*.root > out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*175*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root >> out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*275*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root >> out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_higgs*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_higgs*.root >> out.txt"
	fi

	if [[ $whichSig == "T2bH" ]]; then
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom600_mLSP1_*.root > out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom600_mLSP1_*.root > out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom450_mLSP1_*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom450_mLSP1_*.root >> out.txt"
	    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom450_mLSP300_*.root >> out.txt
	    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_SMS_T2bH_mSbottom450_mLSP300_*.root >> out.txt"
	fi

    counter=0
    while read p ; do
	if (($counter==0)); then
	    SIGFILES="$p"
	else
	    SIGFILES="$SIGFILES,$p"
	fi
	((counter=$counter+1))
    done < out.txt
    echo "SIGFILES $SIGFILES"

    #./makeSlides.sh $OUTDIR
    #scp fullslides.pdf lcorpe@lxplus.cern.ch:www/scratch/fullslides.pdf
    #exit 1

    echo "packaging"
    echo "./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_$EXT.root"
    ./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_$EXT.root > package.out

    fi

fi

#case ### #  in
    

# #####################################################
# #################### SIGNAL PLOTS ###################
# #####################################################

if [ $SIGPLOTSONLY == 1 ]; then

    echo "=============================="
    echo "Make Signal Plots"
    echo "-->Create Validation plots"
    echo "=============================="

    echo " ./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR -p $PROCS -f $CATS"
# #./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR/sigplots -p $PROCS -f $CATS 
    ./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR/sigplots -p $PROCS -f $CATS > signumbers_${EXT}.txt
# #mv $OUTDIR/sigfit/initialFits $OUTDIR/initialFits

# ./makeSlides.sh $OUTDIR
# mv fullslides.pdf $OUTDIR/fullslides_${EXT}.pdf
fi



# if [ $USER == "lcorpe" ]; then
# cp -r $OUTDIR ~/www/.
# cp ~lcorpe/public/index.php ~/www/$OUTDIR/sigplots/.
# cp ~lcorpe/public/index.php ~/www/$OUTDIR/systematics/.
# cp ~lcorpe/public/index.php ~/www/$OUTDIR/sigfit/.
# cp ~lcorpe/public/index.php ~/www/$OUTDIR/sigfTest/.

# echo "plots available at: "
# echo "https://lcorpe.web.cern.ch/lcorpe/$OUTDIR"

# fi

# if [ $USER == "lc1113" ]; then
# cp -r $OUTDIR ~lc1113/public_html/.
# cp ~lc1113/index.php ~lc1113/public_html/$OUTDIR/sigplots/.
# cp ~lc1113/index.php ~lc1113/public_html/$OUTDIR/systematics/.
# cp ~lc1113/index.php ~lc1113/public_html/$OUTDIR/sigfit/.
# cp ~lc1113/index.php ~lc1113/public_html/$OUTDIR/sigfTest/.
# echo "plots available at: "
# echo "http://www.hep.ph.imperial.ac.uk/~lc1113/$OUTDIR"
# echo "~lc1113/public_html/$OUTDIR/sigfTest/."
# echo " if you want the plots on lxplus, fill in your password!"
# echo " scp -r ~lc1113/public_html/$OUTDIR lcorpe@lxplus.cern.ch:~/www/. "
# scp -r ~lc1113/public_html/$OUTDIR lcorpe@lxplus.cern.ch:~/www/. 
# echo "https://lcorpe.web.cern.ch/lcorpe/$OUTDIR"
# fi
