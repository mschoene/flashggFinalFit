#!/bin/bash


#./bin/SignalFit -i /shome/mschoene/9_2_4_gg/src/myMT2Analysis/analysis/EventYields_data_diPhoton_Apr19_Mgg/WS/ws_SMS_T2bH_mSbottom450_mLSP1.root -d dat/newConfig_Sep16.dat  --mhLow=120 --mhHigh=130 -s systConfig.dat --procs higgs,SMS_T2bH_mSbottom250_mLSP100,SMS_T2bH_mSbottom250_mLSP1,SMS_T2bH_mSbottom250_mLSP50,SMS_T2bH_mSbottom300_mLSP100,SMS_T2bH_mSbottom300_mLSP150,SMS_T2bH_mSbottom300_mLSP1,SMS_T2bH_mSbottom300_mLSP50,SMS_T2bH_mSbottom350_mLSP100,SMS_T2bH_mSbottom350_mLSP150,SMS_T2bH_mSbottom350_mLSP1,SMS_T2bH_mSbottom350_mLSP200,SMS_T2bH_mSbottom350_mLSP50,SMS_T2bH_mSbottom400_mLSP100,SMS_T2bH_mSbottom400_mLSP150,SMS_T2bH_mSbottom400_mLSP1,SMS_T2bH_mSbottom400_mLSP200,SMS_T2bH_mSbottom400_mLSP250,SMS_T2bH_mSbottom400_mLSP50,SMS_T2bH_mSbottom450_mLSP1,SMS_T2bH_mSbottom450_mLSP100,SMS_T2bH_mSbottom450_mLSP150,SMS_T2bH_mSbottom450_mLSP200,SMS_T2bH_mSbottom450_mLSP250,SMS_T2bH_mSbottom450_mLSP300,SMS_T2bH_mSbottom450_mLSP50,SMS_T2bH_mSbottom500_mLSP100,SMS_T2bH_mSbottom500_mLSP150,SMS_T2bH_mSbottom500_mLSP1,SMS_T2bH_mSbottom500_mLSP200,SMS_T2bH_mSbottom500_mLSP250,SMS_T2bH_mSbottom500_mLSP300,SMS_T2bH_mSbottom500_mLSP50,SMS_T2bH_mSbottom600_mLSP1,SMS_T2bH_mSbottom600_mLSP100,SMS_T2bH_mSbottom600_mLSP200,SMS_T2bH_mSbottom600_mLSP300       -o CMS-HGG_13TeV_sigfit_sep17.root -p outdir_sep17/sigfit -f HT0toInf_j0_b0_pT0,HT0toInf_j0_b0_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j0_b1toInf_pT0,HT0toInf_j0_b1toInf_pT1,HT0toInf_j1to3_b1toInf_pT0,HT0toInf_j1to3_b1toInf_pT1,HT0toInf_j4toInf_b1toInf_pT0,HT0toInf_j4toInf_b1toInf_pT1 --changeIntLumi 1 -v 1


#bash variables
FILE="";
#EXT="oct10_b012V2"; #extensiom for all folders and files created by this script
#EXT="oct03_b012V2_HH"; #extensiom for all folders and files created by this script
#EXT="oct27_T2bH_b012ISR"; #extensiom for all folders and files created by this script
#EXT="oct24_T2bH_llbb"; #extensiom for all folders and files created by this script
#EXT="oct15_HZ_LLbin"; #extensiom for all folders and files created by this script
#EXT="oct04_mt2bin_HH"; #extensiom for all folders and files created by this script
#EXT="sep27_b012"; #extensiom for all folders and files created by this script
#EXT="sep25_lowPtCut"; #extensiom for all folders and files created by this script
#PROCS="higgs"

EXT="nov07_bb"; #extensiom for all folders and files created by this script



#PROCS="higgs,SMS_TChiHH_HToGG_m127,SMS_TChiHH_HToGG_m150,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m200,SMS_TChiHH_HToGG_m225,SMS_TChiHH_HToGG_m250,SMS_TChiHH_HToGG_m275,SMS_TChiHH_HToGG_m300,SMS_TChiHH_HToGG_m325,SMS_TChiHH_HToGG_m350,SMS_TChiHH_HToGG_m375,SMS_TChiHH_HToGG_m400,SMS_TChiHH_HToGG_m425,SMS_TChiHH_HToGG_m450,SMS_TChiHH_HToGG_m475,SMS_TChiHH_HToGG_m500,SMS_TChiHH_HToGG_m525,SMS_TChiHH_HToGG_m550,SMS_TChiHH_HToGG_m575,SMS_TChiHH_HToGG_m600,SMS_TChiHH_HToGG_m625,SMS_TChiHH_HToGG_m650,SMS_TChiHH_HToGG_m675,SMS_TChiHH_HToGG_m700,SMS_TChiHH_HToGG_m725,SMS_TChiHH_HToGG_m750,SMS_TChiHH_HToGG_m775,SMS_TChiHH_HToGG_m800,SMS_TChiHH_HToGG_m825,SMS_TChiHH_HToGG_m850,SMS_TChiHH_HToGG_m875,SMS_TChiHH_HToGG_m900,SMS_TChiHH_HToGG_m925,SMS_TChiHH_HToGG_m950,SMS_TChiHH_HToGG_m975,SMS_TChiHH_HToGG_m1000"

#PROCS="higgs,SMS_TChiHZ_HToGG_m127,SMS_TChiHZ_HToGG_m150,SMS_TChiHZ_HToGG_m175,SMS_TChiHZ_HToGG_m200"

#PROCS="higgs,SMS_TChiHH_HToGG_m127,SMS_TChiHH_HToGG_m150,SMS_TChiHH_HToGG_m175,SMS_TChiHH_HToGG_m200"

PROCS="higgs,SMS_TChiWH_HToGG_127_1,SMS_TChiWH_HToGG_150_1,SMS_TChiWH_HToGG_150_24,SMS_TChiWH_HToGG_175_1,SMS_TChiWH_HToGG_175_25,SMS_TChiWH_HToGG_175_49,SMS_TChiWH_HToGG_200_1,SMS_TChiWH_HToGG_200_25,SMS_TChiWH_HToGG_200_50,SMS_TChiWH_HToGG_200_74"

#PROCS="higgs,SMS_TChiHZ_HToGG_m127"

#PROCS="higgs,SMS_TChiHZ_HToGG_m127,SMS_TChiHZ_HToGG_m150,SMS_TChiHZ_HToGG_m175,SMS_TChiHZ_HToGG_m200,SMS_TChiHZ_HToGG_m225,SMS_TChiHZ_HToGG_m250,SMS_TChiHZ_HToGG_m275,SMS_TChiHZ_HToGG_m300,SMS_TChiHZ_HToGG_m325,SMS_TChiHZ_HToGG_m350,SMS_TChiHZ_HToGG_m375,SMS_TChiHZ_HToGG_m400,SMS_TChiHZ_HToGG_m425,SMS_TChiHZ_HToGG_m450,SMS_TChiHZ_HToGG_m475,SMS_TChiHZ_HToGG_m500,SMS_TChiHZ_HToGG_m525,SMS_TChiHZ_HToGG_m550,SMS_TChiHZ_HToGG_m575,SMS_TChiHZ_HToGG_m600,SMS_TChiHZ_HToGG_m625,SMS_TChiHZ_HToGG_m650,SMS_TChiHZ_HToGG_m675,SMS_TChiHZ_HToGG_m700,SMS_TChiHZ_HToGG_m725,SMS_TChiHZ_HToGG_m750,SMS_TChiHZ_HToGG_m775,SMS_TChiHZ_HToGG_m800,SMS_TChiHZ_HToGG_m825,SMS_TChiHZ_HToGG_m850,SMS_TChiHZ_HToGG_m875,SMS_TChiHZ_HToGG_m900,SMS_TChiHZ_HToGG_m925,SMS_TChiHZ_HToGG_m950,SMS_TChiHZ_HToGG_m975,SMS_TChiHZ_HToGG_m1000"

#PROCS="higgs,SMS_T2bH_mSbottom250_mLSP100,SMS_T2bH_mSbottom250_mLSP1,SMS_T2bH_mSbottom250_mLSP50,SMS_T2bH_mSbottom300_mLSP100,SMS_T2bH_mSbottom300_mLSP150,SMS_T2bH_mSbottom300_mLSP1,SMS_T2bH_mSbottom300_mLSP50,SMS_T2bH_mSbottom350_mLSP100,SMS_T2bH_mSbottom350_mLSP150,SMS_T2bH_mSbottom350_mLSP1,SMS_T2bH_mSbottom350_mLSP200,SMS_T2bH_mSbottom350_mLSP50,SMS_T2bH_mSbottom400_mLSP100,SMS_T2bH_mSbottom400_mLSP150,SMS_T2bH_mSbottom400_mLSP1,SMS_T2bH_mSbottom400_mLSP200,SMS_T2bH_mSbottom400_mLSP250,SMS_T2bH_mSbottom400_mLSP50,SMS_T2bH_mSbottom450_mLSP1,SMS_T2bH_mSbottom450_mLSP100,SMS_T2bH_mSbottom450_mLSP150,SMS_T2bH_mSbottom450_mLSP200,SMS_T2bH_mSbottom450_mLSP250,SMS_T2bH_mSbottom450_mLSP300,SMS_T2bH_mSbottom450_mLSP50,SMS_T2bH_mSbottom500_mLSP100,SMS_T2bH_mSbottom500_mLSP150,SMS_T2bH_mSbottom500_mLSP1,SMS_T2bH_mSbottom500_mLSP200,SMS_T2bH_mSbottom500_mLSP250,SMS_T2bH_mSbottom500_mLSP300,SMS_T2bH_mSbottom500_mLSP50,SMS_T2bH_mSbottom600_mLSP1,SMS_T2bH_mSbottom600_mLSP100,SMS_T2bH_mSbottom600_mLSP200,SMS_T2bH_mSbottom600_mLSP300"





#CATS="HT0toInf_j1to3_b0_pT0_loMT2,HT0toInf_j1to3_b0_pT0_hiMT2,HT0toInf_j1to3_b0_pT1_loMT2,HT0toInf_j1to3_b0_pT1_hiMT2,HT0toInf_j1to3_b1_pT0_loMT2,HT0toInf_j1to3_b1_pT0_hiMT2,HT0toInf_j1to3_b1_pT1_loMT2,HT0toInf_j1to3_b1_pT1_hiMT2,HT0toInf_j4toInf_b0_pT0_loMT2,HT0toInf_j4toInf_b0_pT0_hiMT2,HT0toInf_j4toInf_b0_pT1_loMT2,HT0toInf_j4toInf_b0_pT1_hiMT2,HT0toInf_j0_b0toInf_pT0_loPt,HT0toInf_j0_b0toInf_pT0_hiPt,HT0toInf_j0_b0toInf_pT1_loPt,HT0toInf_j0_b0toInf_pT1_hiPt,HT0toInf_j1to3_b2toInf_pT0_loMT2,HT0toInf_j1to3_b2toInf_pT0_hiMT2,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b1toInf_pT0_loMT2,HT0toInf_j4toInf_b1toInf_pT0_hiMT2,HT0toInf_j4toInf_b1toInf_pT1_loMT2,HT0toInf_j4toInf_b1toInf_pT1_hiMT2"

#CATS="is1El_pT1,is1Mu_pT1,is1El_pT0,is1Mu_pT0,diLepZ,diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,HT0toInf_j1to3_b0_pT0_loMT2,HT0toInf_j1to3_b0_pT0_hiMT2,HT0toInf_j1to3_b0_pT1_loMT2,HT0toInf_j1to3_b0_pT1_hiMT2,HT0toInf_j1to3_b1_pT0_loMT2,HT0toInf_j1to3_b1_pT0_hiMT2,HT0toInf_j1to3_b1_pT1_loMT2,HT0toInf_j1to3_b1_pT1_hiMT2,HT0toInf_j4toInf_b0_pT0_loMT2,HT0toInf_j4toInf_b0_pT0_hiMT2,HT0toInf_j4toInf_b0_pT1_loMT2,HT0toInf_j4toInf_b0_pT1_hiMT2,HT0toInf_j4toInf_b1_pT0_loMT2,HT0toInf_j4toInf_b1_pT0_hiMT2,HT0toInf_j4toInf_b1_pT1_loMT2,HT0toInf_j4toInf_b1_pT1_hiMT2,HT0toInf_j0_b0toInf_pT0_loPt,HT0toInf_j0_b0toInf_pT0_hiPt,HT0toInf_j0_b0toInf_pT1_loPt,HT0toInf_j0_b0toInf_pT1_hiPt,HT0toInf_j1to3_b2toInf_pT0_loMT2,HT0toInf_j1to3_b2toInf_pT0_hiMT2,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b2toInf_pT0,HT0toInf_j4toInf_b2toInf_pT1"

#CATS="is1El_pT0,is1Mu_pT0,is1El_pT1,is1Mu_pT1,diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,diLepZ,HT0toInf_j0_b0toInf_pT0,HT0toInf_j0_b0toInf_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j1to3_b1_pT0,HT0toInf_j1to3_b1_pT1,HT0toInf_j4toInf_b1_pT0,HT0toInf_j4toInf_b1_pT1,HT0toInf_j1to3_b2toInf_pT0,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b2toInf_pT0,HT0toInf_j4toInf_b2toInf_pT1"

#CATS="is1El,is1Mu,diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,diLepZ,HT0toInf_j0_b0toInf_pT0,HT0toInf_j0_b0toInf_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j1to3_b1_pT0,HT0toInf_j1to3_b1_pT1,HT0toInf_j4toInf_b1_pT0,HT0toInf_j4toInf_b1_pT1,HT0toInf_j1to3_b2toInf_pT0,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b2toInf_pT0,HT0toInf_j4toInf_b2toInf_pT1"

CATS="HT0toInf_j0_b0toInf_pT0,HT0toInf_j0_b0toInf_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j1to3_b1_pT0,HT0toInf_j1to3_b1_pT1,HT0toInf_j4toInf_b1_pT0,HT0toInf_j4toInf_b1_pT1,HT0toInf_j1to3_b2toInf_pT0,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b2toInf_pT0,HT0toInf_j4toInf_b2toInf_pT1"

#CATS="diBB,diLepZ,HT0toInf_j0_b0toInf_pT0,HT0toInf_j0_b0toInf_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j1to3_b1_pT0,HT0toInf_j1to3_b1_pT1,HT0toInf_j4toInf_b1toInf_pT0,HT0toInf_j4toInf_b1toInf_pT1,HT0toInf_j1to3_b2toInf_pT0,HT0toInf_j1to3_b2toInf_pT1" 
 
#CATS="HT0toInf_j0_b0toInf_pT0,HT0toInf_j0_b0toInf_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j1to3_b1_pT0,HT0toInf_j1to3_b1_pT1,HT0toInf_j4toInf_b1_pT0,HT0toInf_j4toInf_b1_pT1,HT0toInf_j1to3_b2toInf_pT0,HT0toInf_j1to3_b2toInf_pT1,HT0toInf_j4toInf_b2toInf_pT0,HT0toInf_j4toInf_b2toInf_pT1"
#CATS="HT0toInf_j0_b0_pT0,HT0toInf_j0_b0_pT1,HT0toInf_j1to3_b0_pT0,HT0toInf_j1to3_b0_pT1,HT0toInf_j4toInf_b0_pT0,HT0toInf_j4toInf_b0_pT1,HT0toInf_j0_b1toInf_pT0,HT0toInf_j0_b1toInf_pT1,HT0toInf_j1to3_b1toInf_pT0,HT0toInf_j1to3_b1toInf_pT1,HT0toInf_j4toInf_b1toInf_pT0,HT0toInf_j4toInf_b1toInf_pT1"

#CATS="UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,UntaggedTag_4,VBFTag_0,VBFTag_1,VBFTag_2"
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
    echo "./python/submitSignalFit.py -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_sigfit_$EXT.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI --batch $BATCH --massList $MASSLIST -q $DEFAULTQUEUE $BSOPT "
    ./python/submitSignalFit.py -i $FILE -d dat/newConfig_$EXT.dat  --mhLow=120 --mhHigh=130 -s dat/photonCatSyst_sep18.dat --procs $PROCS -o $OUTDIR/CMS-HGG_sigfit_$EXT.root -p $OUTDIR/sigfit -f $CATS --changeIntLumi $INTLUMI --batch $BATCH --massList $MASSLIST -q $DEFAULTQUEUE $BSOPT 

    PEND=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub*| grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" |grep -v "\.log"  |wc -l`
    echo "PEND $PEND"
    while (( $PEND > 0 )) ;do
      PEND=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep -v "\.run" | grep -v "\.done" | grep -v "\.fail" | grep -v "\.err" | grep -v "\.log" |wc -l`
      RUN=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.run" |wc -l`
      FAIL=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.fail" |wc -l`
      DONE=`ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.done" |wc -l`
      (( PEND=$PEND-$RUN-$FAIL-$DONE ))
      echo " PEND $PEND - RUN $RUN - DONE $DONE - FAIL $FAIL"
      if (( $RUN > 0 )) ; then PEND=1 ; fi
      if (( $FAIL > 0 )) ; then 
        echo "ERROR at least one job failed :"
        ls -l $OUTDIR/sigfit/SignalFitJobs/sub* | grep "\.fail"
        exit 1
      fi
      sleep 20
  
    done

    ls $PWD/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt
    echo "ls ../Signal/$OUTDIR/CMS-HGG_sigfit_${EXT}_*.root > out.txt"
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

#    echo "./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_$EXT.root"
#    ./bin/PackageOutput -i $SIGFILES --procs $PROCS -l $INTLUMI -p $OUTDIR/sigfit -W wsig_13TeV -f $CATS -L 120 -H 130 -o $OUTDIR/CMS-HGG_sigfit_$EXT.root > package.out

  fi

fi

#case ### #  in
    

# #####################################################
# #################### SIGNAL PLOTS ###################
# #####################################################

# if [ $SIGPLOTSONLY == 1 ]; then

# echo "=============================="
# echo "Make Signal Plots"
# echo "-->Create Validation plots"
# echo "=============================="

# echo " ./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR -p $PROCS -f $CATS"
# #./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR/sigplots -p $PROCS -f $CATS 
# ./bin/makeParametricSignalModelPlots -i $OUTDIR/CMS-HGG_sigfit_$EXT.root  -o $OUTDIR/sigplots -p $PROCS -f $CATS > signumbers_${EXT}.txt
# #mv $OUTDIR/sigfit/initialFits $OUTDIR/initialFits

# ./makeSlides.sh $OUTDIR
# mv fullslides.pdf $OUTDIR/fullslides_${EXT}.pdf
# fi



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
