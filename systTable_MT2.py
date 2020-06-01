#!/usr/bin/env python

import os
import fnmatch
import sys
import time
import operator

import glob

sqrts=13
lumi=0.


#python yieldsTable_MT2.py -i Background/CMS-HGG_multipdf_data_nov23_pTbin.root -s Signal/signumbers_HZ_nov23_pTbin.txt -u Background/CMS-HGG_multipdf_data_nov23_pTbin.root

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-d","--dir")
parser.add_option("--factor",default=1.)
parser.add_option("-i","--input",default="numbers.txt")
parser.add_option("-s","--siginput",default="signumbers.txt")
parser.add_option("-w","--workspaces",default="")
parser.add_option("-v","--sigworkspaces",default="")
parser.add_option("-u","--bkgworkspaces",default="")
parser.add_option("-o","--order",default="",help="tell the script what order to print tags and procs in. Usage proc1,proc2,proc3..:tag1,tag2,tag3...")


parser.add_option("-f","--flashggCats",default="diLepZ,diBBZ_pT0_mt2_0,diBBZ_pT1_mt2_0,diBBZ_pT2_mt2_0,diBBZ_pT0_mt2_30,diBBZ_pT1_mt2_30,diBBZ_pT2_mt2_30,diBBH_pT0_mt2_0,diBBH_pT1_mt2_0,diBBH_pT2_mt2_0,diBBH_pT0_mt2_30,diBBH_pT1_mt2_30,diBBH_pT2_mt2_30,is1El_pT0_mt2_0,is1El_pT0_mt2_30,is1El_pT1_mt2_0,is1El_pT1_mt2_30,is1El_pT2_mt2_0,is1El_pT2_mt2_30,is1Mu_pT0_mt2_0,is1Mu_pT0_mt2_30,is1Mu_pT1_mt2_0,is1Mu_pT1_mt2_30,is1Mu_pT2_mt2_0,is1Mu_pT2_mt2_30,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2,j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j1to3_b0_pT2_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT2_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j1to3_b1_pT2_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT2_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT2_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT2_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j1to3_b0_pT2_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j4toInf_b0_pT2_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j1to3_b1_pT2_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j4toInf_b1_pT2_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j1to3_b2toInf_pT2_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT2_mt2_30",help="Flashgg Categories (default: %default)")


#order or regions in makeDC
regionOrder=["j1to3_b0_pT0_mt2_0","j1to3_b0_pT1_mt2_0","j1to3_b0_pT2_mt2_0","j4toInf_b0_pT0_mt2_0","j4toInf_b0_pT1_mt2_0","j4toInf_b0_pT2_mt2_0","j1to3_b1_pT0_mt2_0","j1to3_b1_pT1_mt2_0","j1to3_b1_pT2_mt2_0","j4toInf_b1_pT0_mt2_0","j4toInf_b1_pT1_mt2_0","j4toInf_b1_pT2_mt2_0","j1to3_b2toInf_pT0_mt2_0","j1to3_b2toInf_pT1_mt2_0","j1to3_b2toInf_pT2_mt2_0","j4toInf_b2toInf_pT0_mt2_0","j4toInf_b2toInf_pT1_mt2_0","j4toInf_b2toInf_pT2_mt2_0","j1to3_b0_pT0_mt2_30","j1to3_b0_pT1_mt2_30","j1to3_b0_pT2_mt2_30","j4toInf_b0_pT0_mt2_30","j4toInf_b0_pT1_mt2_30","j4toInf_b0_pT2_mt2_30","j1to3_b1_pT0_mt2_30","j1to3_b1_pT1_mt2_30","j1to3_b1_pT2_mt2_30","j4toInf_b1_pT0_mt2_30","j4toInf_b1_pT1_mt2_30","j4toInf_b1_pT2_mt2_30","j1to3_b2toInf_pT0_mt2_30","j1to3_b2toInf_pT1_mt2_30","j1to3_b2toInf_pT2_mt2_30","j4toInf_b2toInf_pT0_mt2_30","j4toInf_b2toInf_pT1_mt2_30","j4toInf_b2toInf_pT2_mt2_30","is1El_pT0_mt2_0","is1Mu_pT0_mt2_0","is1El_pT0_mt2_30","is1Mu_pT0_mt2_30","is1El_pT1_mt2_0","is1Mu_pT1_mt2_0","is1El_pT1_mt2_30","is1Mu_pT1_mt2_30","is1El_pT2_mt2_0","is1Mu_pT2_mt2_0","is1El_pT2_mt2_30","is1Mu_pT2_mt2_30","diBBZ_pT0_mt2_0","diBBZ_pT1_mt2_0","diBBZ_pT2_mt2_0","diBBH_pT0_mt2_0","diBBH_pT1_mt2_0","diBBH_pT2_mt2_0","diBBZ_pT0_mt2_30","diBBZ_pT1_mt2_30","diBBZ_pT2_mt2_30","diBBH_pT0_mt2_30","diBBH_pT1_mt2_30","diBBH_pT2_mt2_30","diLepZ","j0_b0toInf_pT0","j0_b0toInf_pT1","j0_b0toInf_pT2"]

(options,args) = parser.parse_args()

# if not (options.workspaces ==""):
#   print "execute"
#   if (len(options.workspaces.split(","))>1) :
#     os.system("./Signal/bin/SignalFit -i %s --checkYield 1 | grep _mass_m125_ > %s"%(options.workspaces,options.input))
#   else:
#     os.system("./Background/bin/workspaceTool -i %s --print 1 | grep RooData | grep it > %s"%(options.workspaces,options.input))
#     #os.system("./Background/bin/workspaceTool -i %s --print 1 | grep intLumi >> %s"%(options.workspaces,options.input))

#   if (len(options.workspaces.split(","))>1) :
#     os.system("./Signal/bin/SignalFit -i %s --checkYield 1 | grep _mass_m125_ > %s"%(options.workspaces,options.input))
#   else:
#     os.system("./Background/bin/workspaceTool -i %s --print 1 | grep RooData | grep it > %s"%(options.workspaces,options.input))
#    # os.system("./Background/bin/workspaceTool -i %s --print 1 | grep intLumi >> %s"%(options.workspaces,options.input))





#datacard_T2bH_600_1 = "/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_dec01/Datacard_13TeV_SMS_T2bH_mSbottom600_mLSP1.txt"

#datacard_T2bH_600_1 = "/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_dec01/Datacard_13TeV_SMS_T2bH_mSbottom450_mLSP1.txt"






#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_dec01_full/Datacard_13TeV_SMS_T2bH_mSbottom450_mLSP1.txt")

#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_dec01_full/Datacard_13TeV_SMS_T2bH_mSbottom450_mLSP300.txt")

#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_WH_dec01_full/Datacard_13TeV_SMS_TChiWH_HToGG_175_1.txt")

#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HH_dec01/Datacard_13TeV_SMS_TChiHH_HToGG_m175.txt")

#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HZ_mar30_corrSumGenMET/Datacard_13TeV_SMS_TChiHZ_HToGG_m175.txt")

#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HZ_mar30_corrSumGenMET/Datacard_13TeV_SMS_TChiHZ_HTo*.txt")
#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HH_mar30/Datacard_13TeV_SMS*.txt")
#read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_WH_mar30/Datacard_13TeV_SMS*.txt")

#to get all
read_files = glob.glob("/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_mar30/Datacard*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())


datacard_T2bH= "/mnt/t3nfs01/data01/shome/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/result.txt"

lumiUncerts_SMH_2016=[]
lumiUncerts_SMH_2017=[]
lumiUncerts_T2bH_2016=[]
lumiUncerts_T2bH_2017=[]

lepsfUncerts_SMH_2016=[]
lepsfUncerts_SMH_2017=[]
lepsfUncerts_T2bH_2016=[]
lepsfUncerts_T2bH_2017=[]

gammasfUncerts_SMH_2016=[]
gammasfUncerts_SMH_2017=[]
gammasfUncerts_T2bH_2016=[]
gammasfUncerts_T2bH_2017=[]

isrUncerts_T2bH_2016=[]
isrUncerts_T2bH_2017=[]

genMETUncerts_T2bH_2016=[]
genMETUncerts_T2bH_2017=[]

btagsf_heavyUncerts_SMH_2016=[]
btagsf_heavyUncerts_SMH_2017=[]
btagsf_heavyUncerts_T2bH_2016=[]
btagsf_heavyUncerts_T2bH_2017=[]

btagsf_lightUncerts_SMH_2016=[]
btagsf_lightUncerts_SMH_2017=[]
btagsf_lightUncerts_T2bH_2016=[]
btagsf_lightUncerts_T2bH_2017=[]


#btagsf_heavy_syst

smHiggs_lepsf_2016=[]
smHiggs_lepsf_2017=[]

smHiggs_lumi_2016=[]
smHiggs_lumi_2017=[]

smHiggs_gammasf_2016=[]
smHiggs_gammasf_2017=[]

smHiggs_btagsf_heavy_2016=[]
smHiggs_btagsf_heavy_2017=[]

smHiggs_btagsf_light_2016=[]
smHiggs_btagsf_light_2017=[]

signal_lepsf_2016=[]
signal_lepsf_2017=[]

signal_isr_2016=[]
signal_isr_2017=[]

signal_genMET_2016=[]
signal_genMET_2017=[]
                              
signal_lumi_2016=[]
signal_lumi_2017=[]
                              
signal_gammasf_2016=[]
signal_gammasf_2017=[]

signal_btagsf_heavy_2016=[]
signal_btagsf_heavy_2017=[]

signal_btagsf_light_2016=[]
signal_btagsf_light_2017=[]



with open(datacard_T2bH) as i:
#with open(datacard_T2bH) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):

      
    if "isr" in line:
        #print line
        line=line.replace("isr","")
        line=line.replace("lnN","")
        line=line.replace("-","")
        line=line.replace("    "," ")
        line=line.replace("   "," ")
        line=line.replace("  "," ")
        line=line.replace("  "," ")
        line=line.replace("\n","")
        words=line.split(" ")  
        isrUncerts_T2bH_tmp = words
        del isrUncerts_T2bH_tmp[-1]
        del isrUncerts_T2bH_tmp[0:2]
  #      isrUncerts_T2bH_2016 =   isrUncerts_T2bH_2016.add( isrUncerts_T2bH_tmp[::4] )
        #print isrUncerts_T2bH_tmp
        #print isrUncerts_T2bH_tmp[1::2]
        isrUncerts_T2bH_2016.extend( isrUncerts_T2bH_tmp[::2] )
        isrUncerts_T2bH_2017.extend( isrUncerts_T2bH_tmp[1::2] )
        
        signal_isr_2016.extend(isrUncerts_T2bH_tmp[::2])
        signal_isr_2017.extend(isrUncerts_T2bH_tmp[1::2])

    if "genMET" in line:
        #print line
        line=line.replace("genMET","")
        line=line.replace("lnN","")
        line=line.replace("-","")
        line=line.replace("    "," ")
        line=line.replace("   "," ")
        line=line.replace("  "," ")
        line=line.replace("  "," ")
        line=line.replace("\n","")
        words=line.split(" ")  
        genMETUncerts_T2bH_tmp = words
        del genMETUncerts_T2bH_tmp[-1]
        del genMETUncerts_T2bH_tmp[0:2]
  #      genMETUncerts_T2bH_2016 =   genMETUncerts_T2bH_2016.add( genMETUncerts_T2bH_tmp[::4] )
        #print genMETUncerts_T2bH_tmp
        #print genMETUncerts_T2bH_tmp[1::2]
        genMETUncerts_T2bH_2016.extend( genMETUncerts_T2bH_tmp[::2] )
        genMETUncerts_T2bH_2017.extend( genMETUncerts_T2bH_tmp[1::2] )
        
        signal_genMET_2016.extend(genMETUncerts_T2bH_tmp[::2])
        signal_genMET_2017.extend(genMETUncerts_T2bH_tmp[1::2])

    if "lumi" in line:
      # print line
      line=line.replace("lumi_13TeV","")
      line=line.replace("lnN","")
      line=line.replace("-","")
      line=line.replace("    "," ")
      line=line.replace("   "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      lumiUncerts_T2bH_tmp = words
      del lumiUncerts_T2bH_tmp[-1]
      del lumiUncerts_T2bH_tmp[0:1]
      lumiUncerts_SMH_2016.extend(       lumiUncerts_T2bH_tmp[::4] )
      lumiUncerts_SMH_2017.extend(     lumiUncerts_T2bH_tmp[1::4] )
      lumiUncerts_T2bH_2016.extend(     lumiUncerts_T2bH_tmp[2::4] )
      lumiUncerts_T2bH_2017.extend(     lumiUncerts_T2bH_tmp[3::4] )

      signal_lumi_2016.extend(lumiUncerts_T2bH_tmp[2::4])
      signal_lumi_2017.extend(lumiUncerts_T2bH_tmp[3::4])

      smHiggs_lumi_2016.extend(lumiUncerts_T2bH_tmp[::4])
      smHiggs_lumi_2017.extend(lumiUncerts_T2bH_tmp[1::4])

      # print        len(signal_lumi_2016)
      # print        len(signal_lumi_2017)

      # print        (signal_lumi_2016)
      # print        (signal_lumi_2017)


    if "lepsf" in line:
      # print line
      line=line.replace("lepsf","")
      line=line.replace("lnN","")
      line=line.replace("-","")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      lepsfUncerts_T2bH_tmp = words
      del lepsfUncerts_T2bH_tmp[-1]
      del lepsfUncerts_T2bH_tmp[0:2]
      lepsfUncerts_SMH_2016.extend(     lepsfUncerts_T2bH_tmp[::4] )
      lepsfUncerts_SMH_2017.extend(     lepsfUncerts_T2bH_tmp[1::4] )
      lepsfUncerts_T2bH_2016.extend(     lepsfUncerts_T2bH_tmp[2::4] )
      lepsfUncerts_T2bH_2017.extend(     lepsfUncerts_T2bH_tmp[3::4] )

      smHiggs_lepsf_2016.extend(lepsfUncerts_T2bH_tmp[::4])
      smHiggs_lepsf_2017.extend(lepsfUncerts_T2bH_tmp[1::4])

      signal_lepsf_2016.extend(lepsfUncerts_T2bH_tmp[2::4])
      signal_lepsf_2017.extend(lepsfUncerts_T2bH_tmp[3::4])

    if "gammasf" in line:
      # print line
      line=line.replace("gammasf","")
      line=line.replace("lnN","")
      line=line.replace("-","")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      gammasfUncerts_T2bH_tmp = words
      del gammasfUncerts_T2bH_tmp[-1]
      del gammasfUncerts_T2bH_tmp[0:2]
      gammasfUncerts_SMH_2016.extend(     gammasfUncerts_T2bH_tmp[::4] )
      gammasfUncerts_SMH_2017.extend(     gammasfUncerts_T2bH_tmp[1::4] )
      gammasfUncerts_T2bH_2016.extend(     gammasfUncerts_T2bH_tmp[2::4] )
      gammasfUncerts_T2bH_2017.extend(     gammasfUncerts_T2bH_tmp[3::4] )

      smHiggs_gammasf_2016.extend(gammasfUncerts_T2bH_tmp[::4])
      smHiggs_gammasf_2017.extend(gammasfUncerts_T2bH_tmp[1::4])

      signal_gammasf_2016.extend(gammasfUncerts_T2bH_tmp[2::4])
      signal_gammasf_2017.extend(gammasfUncerts_T2bH_tmp[3::4])

    if "btagsf_heavy" in line:
      # print line
      line=line.replace("btagsf_heavy","")
      line=line.replace("lnN","")
      line=line.replace("-","")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      btagsf_heavyUncerts_T2bH_tmp = words
      del btagsf_heavyUncerts_T2bH_tmp[-1]
      del btagsf_heavyUncerts_T2bH_tmp[0:2]
      btagsf_heavyUncerts_SMH_2016.extend(     btagsf_heavyUncerts_T2bH_tmp[::4] )
      btagsf_heavyUncerts_SMH_2017.extend(     btagsf_heavyUncerts_T2bH_tmp[1::4] )
      btagsf_heavyUncerts_T2bH_2016.extend(     btagsf_heavyUncerts_T2bH_tmp[2::4] )
      btagsf_heavyUncerts_T2bH_2017.extend(     btagsf_heavyUncerts_T2bH_tmp[3::4] )

      smHiggs_btagsf_heavy_2016.extend(btagsf_heavyUncerts_T2bH_tmp[::4])
      smHiggs_btagsf_heavy_2017.extend(btagsf_heavyUncerts_T2bH_tmp[1::4])

      signal_btagsf_heavy_2016.extend(btagsf_heavyUncerts_T2bH_tmp[2::4])
      signal_btagsf_heavy_2017.extend(btagsf_heavyUncerts_T2bH_tmp[3::4])

    if "btagsf_light" in line:
      # print line
      line=line.replace("btagsf_light","")
      line=line.replace("lnN","")
      line=line.replace("-","")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      btagsf_lightUncerts_T2bH_tmp = words
      del btagsf_lightUncerts_T2bH_tmp[-1]
      del btagsf_lightUncerts_T2bH_tmp[0:2]
      btagsf_lightUncerts_SMH_2016.extend(     btagsf_lightUncerts_T2bH_tmp[::4] )
      btagsf_lightUncerts_SMH_2017.extend(     btagsf_lightUncerts_T2bH_tmp[1::4] )
      btagsf_lightUncerts_T2bH_2016.extend(     btagsf_lightUncerts_T2bH_tmp[2::4] )
      btagsf_lightUncerts_T2bH_2017.extend(     btagsf_lightUncerts_T2bH_tmp[3::4] )

      smHiggs_btagsf_light_2016.extend(btagsf_lightUncerts_T2bH_tmp[::4])
      smHiggs_btagsf_light_2017.extend(btagsf_lightUncerts_T2bH_tmp[1::4])

      signal_btagsf_light_2016.extend(btagsf_lightUncerts_T2bH_tmp[2::4])
      signal_btagsf_light_2017.extend(btagsf_lightUncerts_T2bH_tmp[3::4])


print " "





totalUncert_lumi = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(smHiggs_lumi_2016, smHiggs_lumi_2017)]
totalUncert_lepsf = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(smHiggs_lepsf_2016, smHiggs_lepsf_2017)]
totalUncert_gammasf = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(smHiggs_gammasf_2016, smHiggs_gammasf_2017)]
totalUncert_btagsf_heavy = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(smHiggs_btagsf_heavy_2016, smHiggs_btagsf_heavy_2017)]
totalUncert_btagsf_light = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(smHiggs_btagsf_light_2016, smHiggs_btagsf_light_2017)]



totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(totalUncert_lumi, totalUncert_lepsf)]
totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(totalUncert, totalUncert_gammasf)]
totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(totalUncert, totalUncert_btagsf_heavy)]
totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(totalUncert, totalUncert_btagsf_light)]




signal_totalUncert_lumi = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_lumi_2016, signal_lumi_2017)]
signal_totalUncert_lepsf = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_lepsf_2016, signal_lepsf_2017)]
signal_totalUncert_gammasf = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_gammasf_2016, signal_gammasf_2017)]
signal_totalUncert_btagsf_heavy = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_btagsf_heavy_2016, signal_btagsf_heavy_2017)]
signal_totalUncert_btagsf_light = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_btagsf_light_2016, signal_btagsf_light_2017)]
signal_totalUncert_isr = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_isr_2016, signal_isr_2017)]

signal_totalUncert_genMET = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_genMET_2016, signal_genMET_2017)]


signal_totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_totalUncert_lumi, signal_totalUncert_lepsf)]
signal_totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_totalUncert, signal_totalUncert_gammasf)]
signal_totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_totalUncert, signal_totalUncert_btagsf_heavy)]
signal_totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_totalUncert, signal_totalUncert_btagsf_light)]
signal_totalUncert = [ 1.+( abs(1.-float(x))**2 + abs(1.-float(y))**2 )**(1./2) for x, y in zip(signal_totalUncert, signal_totalUncert_isr)]



#print list(zip(regionOrder,smHiggs_lepsf_2017))


smHiggs_totalUncert = list(zip(regionOrder,totalUncert))

#print [[regionOrder], [signal_totalUncert]]


#print regionOrder
#print signal_totalUncert


signal_totalUncert = list(zip(regionOrder,signal_totalUncert))

print smHiggs_totalUncert
print signal_totalUncert



diff_isrUncerts_T2bH_2016 = [abs(1-float(x)) for x in isrUncerts_T2bH_2016 ]
max_isr_T2bH_2016 = max([abs(1-float(x)) for x in isrUncerts_T2bH_2016])
average_isr_T2bH_2016 = sum(diff_isrUncerts_T2bH_2016)/ len(diff_isrUncerts_T2bH_2016)
diff_isrUncerts_T2bH_2017 = [abs(1-float(x)) for x in isrUncerts_T2bH_2017]
max_isr_T2bH_2017 = max([abs(1-float(x)) for x in isrUncerts_T2bH_2017])
average_isr_T2bH_2017 = sum(diff_isrUncerts_T2bH_2017)/ len(diff_isrUncerts_T2bH_2017)

diff_genMETUncerts_T2bH_2016 = [abs(1-float(x)) for x in genMETUncerts_T2bH_2016 ]
max_genMET_T2bH_2016 = max([abs(1-float(x)) for x in genMETUncerts_T2bH_2016])
average_genMET_T2bH_2016 = sum(diff_genMETUncerts_T2bH_2016)/ len(diff_genMETUncerts_T2bH_2016)
diff_genMETUncerts_T2bH_2017 = [abs(1-float(x)) for x in genMETUncerts_T2bH_2017]
max_genMET_T2bH_2017 = max([abs(1-float(x)) for x in genMETUncerts_T2bH_2017])
average_genMET_T2bH_2017 = sum(diff_genMETUncerts_T2bH_2017)/ len(diff_genMETUncerts_T2bH_2017)


diff_lumiUncerts_SMH_2016 = [abs(1-float(x)) for x in lumiUncerts_SMH_2016]
max_lumi_SMH_2016 = max([abs(1-float(x)) for x in lumiUncerts_SMH_2016])
average_lumi_SMH_2016 = sum(diff_lumiUncerts_SMH_2016)/ len(diff_lumiUncerts_SMH_2016)
diff_lumiUncerts_SMH_2017 = [abs(1-float(x)) for x in lumiUncerts_SMH_2017]
max_lumi_SMH_2017 = max([abs(1-float(x)) for x in lumiUncerts_SMH_2017])
average_lumi_SMH_2017 = sum(diff_lumiUncerts_SMH_2017)/ len(diff_lumiUncerts_SMH_2017)
diff_lumiUncerts_T2bH_2016 = [abs(1-float(x)) for x in lumiUncerts_T2bH_2016]
max_lumi_2016 = max([abs(1-float(x)) for x in lumiUncerts_T2bH_2016])
average_lumi_2016 = sum(diff_lumiUncerts_T2bH_2016)/ len(diff_lumiUncerts_T2bH_2016)
diff_lumiUncerts_T2bH_2017 = [abs(1-float(x)) for x in lumiUncerts_T2bH_2017]
max_lumi_2017 = max([abs(1-float(x)) for x in lumiUncerts_T2bH_2017])
average_lumi_2017 = sum(diff_lumiUncerts_T2bH_2017)/ len(diff_lumiUncerts_T2bH_2017)


diff_lepsfUncerts_SMH_2016 = [abs(1-float(x)) for x in lepsfUncerts_SMH_2016]
max_lepsf_SMH_2016 = max([abs(1-float(x)) for x in lepsfUncerts_SMH_2016])
average_lepsf_SMH_2016 = sum(diff_lepsfUncerts_SMH_2016)/ len(diff_lepsfUncerts_SMH_2016)
diff_lepsfUncerts_SMH_2017 = [abs(1-float(x)) for x in lepsfUncerts_SMH_2017]
max_lepsf_SMH_2017 = max([abs(1-float(x)) for x in lepsfUncerts_SMH_2017])
average_lepsf_SMH_2017 = sum(diff_lepsfUncerts_SMH_2017)/ len(diff_lepsfUncerts_SMH_2017)
diff_lepsfUncerts_T2bH_2016 = [abs(1-float(x)) for x in lepsfUncerts_T2bH_2016]
max_lepsf_2016 = max([abs(1-float(x)) for x in lepsfUncerts_T2bH_2016])
average_lepsf_2016 = sum(diff_lepsfUncerts_T2bH_2016)/ len(diff_lepsfUncerts_T2bH_2016)
diff_lepsfUncerts_T2bH_2017 = [abs(1-float(x)) for x in lepsfUncerts_T2bH_2017]
max_lepsf_2017 = max([abs(1-float(x)) for x in lepsfUncerts_T2bH_2017])
average_lepsf_2017 = sum(diff_lepsfUncerts_T2bH_2017)/ len(diff_lepsfUncerts_T2bH_2017)


diff_gammasfUncerts_SMH_2016 = [abs(1-float(x)) for x in gammasfUncerts_SMH_2016]
max_gammasf_SMH_2016 = max([abs(1-float(x)) for x in gammasfUncerts_SMH_2016])
average_gammasf_SMH_2016 = sum(diff_gammasfUncerts_SMH_2016)/ len(diff_gammasfUncerts_SMH_2016)
diff_gammasfUncerts_SMH_2017 = [abs(1-float(x)) for x in gammasfUncerts_SMH_2017]
max_gammasf_SMH_2017 = max([abs(1-float(x)) for x in gammasfUncerts_SMH_2017])
average_gammasf_SMH_2017 = sum(diff_gammasfUncerts_SMH_2017)/ len(diff_gammasfUncerts_SMH_2017)
diff_gammasfUncerts_T2bH_2016 = [abs(1-float(x)) for x in gammasfUncerts_T2bH_2016]
max_gammasf_2016 = max([abs(1-float(x)) for x in gammasfUncerts_T2bH_2016])
average_gammasf_2016 = sum(diff_gammasfUncerts_T2bH_2016)/ len(diff_gammasfUncerts_T2bH_2016)
diff_gammasfUncerts_T2bH_2017 = [abs(1-float(x)) for x in gammasfUncerts_T2bH_2017]
max_gammasf_2017 = max([abs(1-float(x)) for x in gammasfUncerts_T2bH_2017])
average_gammasf_2017 = sum(diff_gammasfUncerts_T2bH_2017)/ len(diff_gammasfUncerts_T2bH_2017)

diff_btagsf_heavyUncerts_SMH_2016 = [abs(1-float(x)) for x in btagsf_heavyUncerts_SMH_2016]
max_btagsf_heavy_SMH_2016 = max([abs(1-float(x)) for x in btagsf_heavyUncerts_SMH_2016])
average_btagsf_heavy_SMH_2016 = sum(diff_btagsf_heavyUncerts_SMH_2016)/ len(diff_btagsf_heavyUncerts_SMH_2016)
diff_btagsf_heavyUncerts_SMH_2017 = [abs(1-float(x)) for x in btagsf_heavyUncerts_SMH_2017]
max_btagsf_heavy_SMH_2017 = max([abs(1-float(x)) for x in btagsf_heavyUncerts_SMH_2017])
average_btagsf_heavy_SMH_2017 = sum(diff_btagsf_heavyUncerts_SMH_2017)/ len(diff_btagsf_heavyUncerts_SMH_2017)
diff_btagsf_heavyUncerts_T2bH_2016 = [abs(1-float(x)) for x in btagsf_heavyUncerts_T2bH_2016]
max_btagsf_heavy_2016 = max([abs(1-float(x)) for x in btagsf_heavyUncerts_T2bH_2016])
average_btagsf_heavy_2016 = sum(diff_btagsf_heavyUncerts_T2bH_2016)/ len(diff_btagsf_heavyUncerts_T2bH_2016)
diff_btagsf_heavyUncerts_T2bH_2017 = [abs(1-float(x)) for x in btagsf_heavyUncerts_T2bH_2017]
max_btagsf_heavy_2017 = max([abs(1-float(x)) for x in btagsf_heavyUncerts_T2bH_2017])
average_btagsf_heavy_2017 = sum(diff_btagsf_heavyUncerts_T2bH_2017)/ len(diff_btagsf_heavyUncerts_T2bH_2017)

diff_btagsf_lightUncerts_SMH_2016 = [abs(1-float(x)) for x in btagsf_lightUncerts_SMH_2016]
max_btagsf_light_SMH_2016 = max([abs(1-float(x)) for x in btagsf_lightUncerts_SMH_2016])
average_btagsf_light_SMH_2016 = sum(diff_btagsf_lightUncerts_SMH_2016)/ len(diff_btagsf_lightUncerts_SMH_2016)
diff_btagsf_lightUncerts_SMH_2017 = [abs(1-float(x)) for x in btagsf_lightUncerts_SMH_2017]
max_btagsf_light_SMH_2017 = max([abs(1-float(x)) for x in btagsf_lightUncerts_SMH_2017])
average_btagsf_light_SMH_2017 = sum(diff_btagsf_lightUncerts_SMH_2017)/ len(diff_btagsf_lightUncerts_SMH_2017)
diff_btagsf_lightUncerts_T2bH_2016 = [abs(1-float(x)) for x in btagsf_lightUncerts_T2bH_2016]
max_btagsf_light_2016 = max([abs(1-float(x)) for x in btagsf_lightUncerts_T2bH_2016])
average_btagsf_light_2016 = sum(diff_btagsf_lightUncerts_T2bH_2016)/ len(diff_btagsf_lightUncerts_T2bH_2016)
diff_btagsf_lightUncerts_T2bH_2017 = [abs(1-float(x)) for x in btagsf_lightUncerts_T2bH_2017]
max_btagsf_light_2017 = max([abs(1-float(x)) for x in btagsf_lightUncerts_T2bH_2017])
average_btagsf_light_2017 = sum(diff_btagsf_lightUncerts_T2bH_2017)/ len(diff_btagsf_lightUncerts_T2bH_2017)



#lumi2016=36.814
lumi2016=35.922
lumi2017=41.529

#lumi2016=35.9
#lumi2017=41.37

lumi=77.5

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c }"
print line
print "Uncertainty Source & SM Higgs 2016 & SM Higgs 2017 & Signal 2016 & Signal 2017 &  \\\\ "
print "\\hline"


#print "Luminosity & " +  str('%.1f' %(100.* float(average_lumi_SMH_2016 )))+"/%   & " +  str('%.1f' %(100.* float(average_lumi_SMH_2017 )))+"/%  & " +  str('%.1f' %(100.* float(average_lumi_2016 )))+"/%   & " +  str('%.1f' %(100.* float(average_lumi_2017 )))+"/%"


print "Luminosity & " +  str('%.1f' %(100.* float(max_lumi_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_lumi_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(max_lumi_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_lumi_2017 )))+"\%"

print "ISR        & - & -  " +  str('%.1f' %(100.* float(max_isr_T2bH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_isr_T2bH_2017 )))+"\%"

print "GENMET        & - & -  " +  str('%.1f' %(100.* float(max_genMET_T2bH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_genMET_T2bH_2017 )))+"\%"

print "Lepton SF & " +  str('%.1f' %(100.* float(max_lepsf_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_lepsf_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(max_lepsf_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_lepsf_2017 )))+"\%"

print "Gamma SF & " +  str('%.1f' %(100.* float(max_gammasf_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_gammasf_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(max_gammasf_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_gammasf_2017 )))+"\%"

print "B-tag  SF & " +  str('%.1f' %(100.* float(max_btagsf_heavy_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_btagsf_heavy_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(max_btagsf_heavy_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_btagsf_heavy_2017 )))+"\%"

print "B-tag  SF & " +  str('%.1f' %(100.* float(max_btagsf_light_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_btagsf_light_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(max_btagsf_light_2016 )))+"\%   & " +  str('%.1f' %(100.* float(max_btagsf_light_2017 )))+"\%"

print ""



print "Luminosity & " +  str('%.1f' %(100.* float(average_lumi_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_lumi_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(average_lumi_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_lumi_2017 )))+"\%"

print "ISR & - & -  " +  str('%.1f' %(100.* float(average_isr_T2bH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_isr_T2bH_2017 )))+"\%"

print "GENMET & - & -  " +  str('%.1f' %(100.* float(average_genMET_T2bH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_genMET_T2bH_2017 )))+"\%"


print "Branching fraction       & {}_{2.0}^{2.1} \%  & {}_{2.0}^{2.1} \%  & {}_{2.0}^{2.1} \%  & {}_{2.0}^{2.1} \%   "


print "Lepton SF & " +  str('%.1f' %(100.* float(average_lepsf_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_lepsf_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(average_lepsf_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_lepsf_2017 )))+"\%"

print "Gamma SF & " +  str('%.1f' %(100.* float(average_gammasf_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_gammasf_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(average_gammasf_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_gammasf_2017 )))+"\%"

print "B-tag  SF heavy & " +  str('%.1f' %(100.* float(average_btagsf_heavy_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_btagsf_heavy_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(average_btagsf_heavy_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_btagsf_heavy_2017 )))+"\%"

print "B-tag  SF light & " +  str('%.1f' %(100.* float(average_btagsf_light_SMH_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_btagsf_light_SMH_2017 )))+"\%  & " +  str('%.1f' %(100.* float(average_btagsf_light_2016 )))+"\%   & " +  str('%.1f' %(100.* float(average_btagsf_light_2017 )))+"\%" 


#print "Lepton & " +  str('%.1f ' %(100.* float(average_lepsf_SMH_2016 ))) #(max_average_lepsf_SMH_2016) " & " average_lepsf_SMH_2017


# for lim in sorted_rank_HZ_175_exp:

#   p= rank_HZ_175_exp.keys()[ rank_HZ_175_exp.values().index(lim)]
#   n = _tags.index(p)
#   line= names[ n ] 

#   line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
#   line= line + " & " + str('%.2f' %(float(bkgYield[ str(p) ])*(129.-122)))

#   print line

print "\\end{tabular}"
print "\\caption{Systematic uncertainties.}"
print "\\label{tab:systs_MT2}"
print "\\end{table*}"
print " "

