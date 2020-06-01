#!/usr/bin/env python

import os
import fnmatch
import sys
import time
import operator

sqrts=13
lumi=0.

from math import log10, floor
def round_to_nice(x):
  if( float(x)==0 ):
    return '0.0'
  elif( abs(x)>100):
    return str('%.0f' %(float(x)))
  elif( abs(x)>1):
    return str('%.1f' %(float(x)))
  elif( abs(x)<0.01):
    return str('%.1g' %(float(x)))
  else:
    return str('%.2f' %(float(x)))


#  if( x==0 ):
#    return 0
#  elif(x>1000):
#    return  round(x, -int(floor(log10(x))) + (4 - 1))
#  elif(x>100):
#    return  round(x, -int(floor(log10(x))) + (3 - 1))
#  elif(x>1):
#    return  round(x, -int(floor(log10(x))) + (3 - 1))
#  elif(x<0.99):
#    return  round(x, -int(floor(log10(x))) + (2 - 1))
#  else:
#    return  round(x, -int(floor(log10(x))) + (1 - 1))
  

def roundTogether(x, y):
#function to round the yield and it's uncertainty togther, as it's nicer to have the same amount of digits after the . for both
  if( float(x)==0 ):
    return '0.0 $\pm$ 0.0 '
  elif( x>100):
    return str('%.0f $\pm$ %.0f ' %(float(x), float(y)))
#  elif( x>10):
#    return str('%.1f $\pm$ %1.f ', %(float(x), float(y)))
  elif( x>1):
    return str('%.1f $\pm$ %.1f ' %(float(x), float(y)))
  elif( x<0.01):
    return str('%.2g $\pm$ %.1g ' %(float(x), float(y)))
  else:
    return str('%.2f $\pm$ %.2f ' %(float(x), float(y)))


#python yieldsTable_MT2.py -i Background/CMS-HGG_multipdf_data_mar20.root -s Signal/signumbers_HH_mar20.txt -u Background/CMS-HGG_multipdf_data_mar20.root 

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
#parser.add_option("-f","--flashggCats",default="UntaggedTag_0,UntaggedTag_1,UntaggedTag_2,UntaggedTag_3,UntaggedTag_4,VBFTag_0,VBFTag_1,VBFTag_2,TTHHadronicTag,TTHLeptonicTag,VHHadronicTag,VHTightTag,VHLooseTag,VHEtTag")
#parser.add_option("-f","--flashggCats",default="diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,diLepZ",help="Flashgg Categories (default: %default)")


#parser.add_option("-f","--flashggCats",default="diLepZ,diBBZ_pT0,diBBZ_pT1,diBBH_pT0,diBBH_pT1,is1El_pT0_mt2_0,is1El_pT0_mt2_30,is1El_pT1_mt2_0,is1El_pT1_mt2_30,is1Mu_pT0_mt2_0,is1Mu_pT0_mt2_30,is1Mu_pT1_mt2_0,is1Mu_pT1_mt2_30,j0_b0toInf_pT0,j0_b0toInf_pT1,j1to3_b0_pT0_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_0,j1to3_b0_pT1_mt2_30,j1to3_b1_pT0_mt2_0,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_0,j1to3_b1_pT1_mt2_30,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT1_mt2_30,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT1_mt2_30,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT1_mt2_30,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT1_mt2_30",help="Flashgg Categories (default: %default)")

parser.add_option("-f","--flashggCats",default="diLepZ,diBBZ_pT0_mt2_0,diBBZ_pT1_mt2_0,diBBZ_pT2_mt2_0,diBBZ_pT0_mt2_30,diBBZ_pT1_mt2_30,diBBZ_pT2_mt2_30,diBBH_pT0_mt2_0,diBBH_pT1_mt2_0,diBBH_pT2_mt2_0,diBBH_pT0_mt2_30,diBBH_pT1_mt2_30,diBBH_pT2_mt2_30,is1El_pT0_mt2_0,is1El_pT0_mt2_30,is1El_pT1_mt2_0,is1El_pT1_mt2_30,is1El_pT2_mt2_0,is1El_pT2_mt2_30,is1Mu_pT0_mt2_0,is1Mu_pT0_mt2_30,is1Mu_pT1_mt2_0,is1Mu_pT1_mt2_30,is1Mu_pT2_mt2_0,is1Mu_pT2_mt2_30,j0_b0toInf_pT0,j0_b0toInf_pT1,j0_b0toInf_pT2,j1to3_b0_pT0_mt2_0,j1to3_b0_pT1_mt2_0,j1to3_b0_pT2_mt2_0,j4toInf_b0_pT0_mt2_0,j4toInf_b0_pT1_mt2_0,j4toInf_b0_pT2_mt2_0,j1to3_b1_pT0_mt2_0,j1to3_b1_pT1_mt2_0,j1to3_b1_pT2_mt2_0,j4toInf_b1_pT0_mt2_0,j4toInf_b1_pT1_mt2_0,j4toInf_b1_pT2_mt2_0,j1to3_b2toInf_pT0_mt2_0,j1to3_b2toInf_pT1_mt2_0,j1to3_b2toInf_pT2_mt2_0,j4toInf_b2toInf_pT0_mt2_0,j4toInf_b2toInf_pT1_mt2_0,j4toInf_b2toInf_pT2_mt2_0,j1to3_b0_pT0_mt2_30,j1to3_b0_pT1_mt2_30,j1to3_b0_pT2_mt2_30,j4toInf_b0_pT0_mt2_30,j4toInf_b0_pT1_mt2_30,j4toInf_b0_pT2_mt2_30,j1to3_b1_pT0_mt2_30,j1to3_b1_pT1_mt2_30,j1to3_b1_pT2_mt2_30,j4toInf_b1_pT0_mt2_30,j4toInf_b1_pT1_mt2_30,j4toInf_b1_pT2_mt2_30,j1to3_b2toInf_pT0_mt2_30,j1to3_b2toInf_pT1_mt2_30,j1to3_b2toInf_pT2_mt2_30,j4toInf_b2toInf_pT0_mt2_30,j4toInf_b2toInf_pT1_mt2_30,j4toInf_b2toInf_pT2_mt2_30",help="Flashgg Categories (default: %default)")

#parser.add_option("-c","--cats",default="",help="Flashgg Categories (default: %default)")


(options,args) = parser.parse_args()

if not (options.workspaces ==""):
  print "execute"
  if (len(options.workspaces.split(","))>1) :
    os.system("./Signal/bin/SignalFit -i %s --checkYield 1 | grep _mass_m125_ > %s"%(options.workspaces,options.input))
  else:
    os.system("./Background/bin/workspaceTool -i %s --print 1 | grep RooData | grep it > %s"%(options.workspaces,options.input))
    #os.system("./Background/bin/workspaceTool -i %s --print 1 | grep intLumi >> %s"%(options.workspaces,options.input))

  if (len(options.workspaces.split(","))>1) :
    os.system("./Signal/bin/SignalFit -i %s --checkYield 1 | grep _mass_m125_ > %s"%(options.workspaces,options.input))
  else:
    os.system("./Background/bin/workspaceTool -i %s --print 1 | grep RooData | grep it > %s"%(options.workspaces,options.input))
   # os.system("./Background/bin/workspaceTool -i %s --print 1 | grep intLumi >> %s"%(options.workspaces,options.input))



names = ['$\PZ_{\Pl\PAl}$','$\PZ_{\cPqb\cPaqb} ~ \pt^{0}, ~ \mttwo^{0} ~ $','$\PZ_{\cPqb\cPaqb} ~ \pt^{75}, ~ \mttwo^{0} ~ $','$\PZ_{\cPqb\cPaqb} ~ \pt^{125}, ~ \mttwo^{0} ~ $','$\PZ_{\cPqb\cPaqb} ~ \pt^{0}, ~ \mttwo^{30} ~ $','$\PZ_{\cPqb\cPaqb} ~ \pt^{75}, ~ \mttwo^{30} ~ $','$\PZ_{\cPqb\cPaqb} ~ \pt^{125}, ~ \mttwo^{30} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{0}, ~ \mttwo^{0} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{75}, ~ \mttwo^{0} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{125}, ~ \mttwo^{0} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{0}, ~ \mttwo^{30} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{75}, ~ \mttwo^{30} ~ $','$\PH_{\cPqb\cPaqb} ~ \pt^{125}, ~ \mttwo^{30} ~ $','$1\Pe ~ \pt^{0}, ~ \mttwo^{0} ~ $','$1\Pe ~ \pt^{0}, ~ \mttwo^{30} ~ $','$1\Pe ~ \pt^{75}, ~ \mttwo^{0} ~ $','$1\Pe ~ \pt^{75}, ~ \mttwo^{30} ~ $','$1\Pe ~ \pt^{125}, ~ \mttwo^{0} ~ $','$1\Pe ~ \pt^{125}, ~ \mttwo^{30} ~ $','$1\PGm ~ \pt^{0}, ~ \mttwo^{0} ~ $','$1\PGm ~ \pt^{0}, ~ \mttwo^{30} ~ $','$1\PGm ~ \pt^{75}, ~ \mttwo^{0} ~ $','$1\PGm ~ \pt^{75}, ~ \mttwo^{30} ~ $','$1\PGm ~ \pt^{125}, ~ \mttwo^{0} ~ $','$1\PGm ~ \pt^{125}, ~ \mttwo^{30} ~ $',' $0\text{j}, ~ \ge 0\cPqb,  ~ \pt^{0} ~ $',' $0\text{j}, ~ \ge 0\cPqb,  ~ \pt^{75} ~ $',' $0\text{j}, ~ \ge 0\cPqb,  ~ \pt^{125} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 0\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ 1\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $','$1$--$3\text{j}, ~ \ge 2\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 0\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ 1\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{0}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{0}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{75}, ~ \mttwo^{0} ~ $','$\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{75}, ~ \mttwo^{30} ~ $','$\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{125}, ~ \mttwo^{0} ~ $',' $\ge 4\text{j}, ~ \ge 2\cPqb, ~ \pt^{125}, ~ \mttwo^{30} ~ $']



#names = ['$Z_{ll}$ ','$Z_{bb} ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$Z_{bb} ~ p_T^{75}, ~ \mttwo^{0} ~ $  ','$Z_{bb} ~ p_T^{125}, ~ \mttwo^{0} ~ $  ','$Z_{bb} ~ p_T^{0}, ~ \mttwo^{30} ~ $  ','$Z_{bb} ~ p_T^{75}, ~ \mttwo^{30} ~ $  ','$Z_{bb} ~ p_T^{125}, ~ \mttwo^{30} ~ $  ','$H_{bb} ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$H_{bb} ~ p_T^{75}, ~ \mttwo^{0} ~ $  ','$H_{bb} ~ p_T^{125}, ~ \mttwo^{0} ~ $  ','$H_{bb} ~ p_T^{0}, ~ \mttwo^{30} ~ $  ','$H_{bb} ~ p_T^{75}, ~ \mttwo^{30} ~ $  ','$H_{bb} ~ p_T^{125}, ~ \mttwo^{30} ~ $  ','$1el ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$1el ~ p_T^{0}, ~ \mttwo^{30} ~ $  ','$1el ~ p_T^{75}, ~ \mttwo^{0} ~ $  ','$1el ~ p_T^{75}, ~ \mttwo^{30} ~ $  ','$1el ~ p_T^{125}, ~ \mttwo^{0} ~ $  ','$1el ~ p_T^{125}, ~ \mttwo^{30} ~ $  ','$1\mu ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$1\mu ~ p_T^{0}, ~ \mttwo^{30} ~ $  ','$1\mu ~ p_T^{75}, ~ \mttwo^{0} ~ $  ','$1\mu ~ p_T^{75}, ~ \mttwo^{30} ~ $   ','$1\mu ~ p_T^{125}, ~ \mttwo^{0} ~ $  ','$1\mu ~ p_T^{125}, ~ \mttwo^{30} ~ $   ','$0\\text{j}, ~ 0\\text{-}\infty ~ \\text{b}, ~ p_T^{0} ~ $  ','$0\\text{j}, ~ 0\\text{-}\infty ~ \\text{b}, ~ p_T^{75} ~ $','$0\\text{j}, ~ 0\\text{-}\infty ~ \\text{b}, ~ p_T^{125} ~ $','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $  ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $  ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $  ', '$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $  ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $ ', '$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{0}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{0}, ~ \mttwo^{30} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{75}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{75}, ~ \mttwo^{30} ~ $','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{125}, ~ \mttwo^{0} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{125}, ~ \mttwo^{30} ~ $']


# names = ['$Z_{ll}$   ',# '$Z_{bb} ~ p_T^{lo}, ~ \mttwo^{hi} ~ $  ','$Z_{bb} ~ p_T^{hi}, ~ \mttwo^{hi} ~ $  ',# '$H_{bb} ~ p_T^{lo}, ~ \mttwo^{hi} ~ $  ','$H_{bb} ~ p_T^{hi}, ~ \mttwo^{hi} ~ $  ',# '$1el ~ p_T^{lo}, ~ \mttwo^{lo} ~ $  ','$1el ~ p_T^{lo}, ~ \mttwo^{hi} ~ $  ','$1el ~ p_T^{hi}, ~ \mttwo^{lo} ~ $  ','$1el ~ p_T^{hi}, ~ \mttwo^{hi} ~ $  ','$1\mu ~ p_T^{lo}, ~ \mttwo^{lo} ~ $  ','$1\mu ~ p_T^{lo}, ~ \mttwo^{hi} ~ $  ','$1\mu ~ p_T^{hi}, ~ \mttwo^{lo} ~ $  ','$1\mu ~ p_T^{hi}, ~ \mttwo^{hi} ~ $   ','$0\\text{j}, ~ 0\\text{-}\infty ~ \\text{b}, ~ p_T^{lo} ~ $  ','$0\\text{j}, ~ 0\\text{-}\infty ~ \\text{b}, ~ p_T^{hi} ~ $','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $  ','$1\\text{-}3\\text{j}, ~ 0\\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $  ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $  ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $ ','$1\\text{-}3\\text{j}, ~ 1\\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $ ','$1\\text{-}3\\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $  ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 0\\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 1\\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{lo}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{lo}, ~ \mttwo^{hi} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{hi}, ~ \mttwo^{lo} ~ $ ','$4\\text{-}\infty ~ \\text{j}, ~ 2\\text{-}\infty ~ \\text{b}, ~ p_T^{hi}, ~ \mttwo^{hi} ~ $']



#tableData/higgsTHX_comb_mt2_30.txt              
#tableData/higgsggH_comb_mt2_30.txt















readJECFiles2016= "tableData/higgsSyst_2016_JECdn_comb_mt2_30_SMHDonly.txt"
#tableData/higgsSyst_2016_JECup_comb_mt2_30.txt
readJECFiles2017= "tableData/higgsSyst_2017_JECdn_comb_mt2_30_SMHDonly.txt"
#tableData/higgsSyst_2017_JECup_comb_mt2_30.txt

jecUncerts_SMH_2016={}
jecUncerts_SMH_2017={}

with open(readJECFiles2016) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    #      print line
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      jecUncerts_T2bH_tmp = words
      #      print words
      jecUncerts_SMH_2016[words[0]]=abs(float(words[1]))

#print jecUncerts_SMH_2016

with open(readJECFiles2017) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    #      print line
      line=line.replace("  "," ")
      line=line.replace("  "," ")
      line=line.replace("\n","")
      words=line.split(" ")  
      jecUncerts_T2bH_tmp = words
      #      print words
      jecUncerts_SMH_2017[words[0]]=abs(float(words[1]))

#print jecUncerts_SMH_2017





smH_uncert = {'j1to3_b0_pT0_mt2_0': 1.0730616178304313, 'j1to3_b0_pT1_mt2_0': 1.082716382899641, 'j1to3_b0_pT2_mt2_0': 1.0939787209957659, 'j4toInf_b0_pT0_mt2_0': 1.1231015840677934, 'j4toInf_b0_pT1_mt2_0': 1.129460418661458, 'j4toInf_b0_pT2_mt2_0': 1.1430594282107962, 'j1to3_b1_pT0_mt2_0': 1.0688839603971783, 'j1to3_b1_pT1_mt2_0': 1.0748197834800395, 'j1to3_b1_pT2_mt2_0': 1.0831324244804637, 'j4toInf_b1_pT0_mt2_0': 1.0849588135510377, 'j4toInf_b1_pT1_mt2_0': 1.0920108689231875, 'j4toInf_b1_pT2_mt2_0': 1.1050761628534274, 'j1to3_b2toInf_pT0_mt2_0': 1.1019754872506133, 'j1to3_b2toInf_pT1_mt2_0': 1.101316336293808, 'j1to3_b2toInf_pT2_mt2_0': 1.1043791166852834, 'j4toInf_b2toInf_pT0_mt2_0': 1.0663098786004017, 'j4toInf_b2toInf_pT1_mt2_0': 1.0742832417170924, 'j4toInf_b2toInf_pT2_mt2_0': 1.0892468486838611, 'j1to3_b0_pT0_mt2_30': 1.0734914961066926, 'j1to3_b0_pT1_mt2_30': 1.0836899038116308, 'j1to3_b0_pT2_mt2_30': 1.0978621479429103, 'j4toInf_b0_pT0_mt2_30': 1.1310152662860324, 'j4toInf_b0_pT1_mt2_30': 1.1394094688319267, 'j4toInf_b0_pT2_mt2_30': 1.1494991638772605, 'j1to3_b1_pT0_mt2_30': 1.0670745853509358, 'j1to3_b1_pT1_mt2_30': 1.0731231837381279, 'j1to3_b1_pT2_mt2_30': 1.084035706696618, 'j4toInf_b1_pT0_mt2_30': 1.0879829528942966, 'j4toInf_b1_pT1_mt2_30': 1.0951997899157346, 'j4toInf_b1_pT2_mt2_30': 1.1072240644631604, 'j1to3_b2toInf_pT0_mt2_30': 1.0921466222929521, 'j1to3_b2toInf_pT1_mt2_30': 1.0951419991381304, 'j1to3_b2toInf_pT2_mt2_30': 1.1008811181539935, 'j4toInf_b2toInf_pT0_mt2_30': 1.0658710862214977, 'j4toInf_b2toInf_pT1_mt2_30': 1.0741822081094923, 'j4toInf_b2toInf_pT2_mt2_30': 1.0899944442729659, 'is1El_pT0_mt2_0': 1.0748064168370601, 'is1Mu_pT0_mt2_0': 1.0774015503720693, 'is1El_pT0_mt2_30': 1.0790632658065682, 'is1Mu_pT0_mt2_30': 1.0773886296557833, 'is1El_pT1_mt2_0': 1.0752263251794212, 'is1Mu_pT1_mt2_0': 1.0828794304999738, 'is1El_pT1_mt2_30': 1.0798561206170194, 'is1Mu_pT1_mt2_30': 1.0849117188614152, 'is1El_pT2_mt2_0': 1.0888538125237177, 'is1Mu_pT2_mt2_0': 1.0968607247546702, 'is1El_pT2_mt2_30': 1.090188691087076, 'is1Mu_pT2_mt2_30': 1.0983310734203586, 'diBBZ_pT0_mt2_0': 1.0961405221537723, 'diBBZ_pT1_mt2_0': 1.093792323779721, 'diBBZ_pT2_mt2_0': 1.1012620363216146, 'diBBH_pT0_mt2_0': 1.0925310758610316, 'diBBH_pT1_mt2_0': 1.0951997899157344, 'diBBH_pT2_mt2_0': 1.1054466689848474, 'diBBZ_pT0_mt2_30': 1.0904930936591295, 'diBBZ_pT1_mt2_30': 1.0950789145920379, 'diBBZ_pT2_mt2_30': 1.1050428484000694, 'diBBH_pT0_mt2_30': 1.0934184136024583, 'diBBH_pT1_mt2_30': 1.0967057392298925, 'diBBH_pT2_mt2_30': 1.1092565787492907, 'diLepZ': 1.1011484058203589, 'j0_b0toInf_pT0': 1.0619758017293845, 'j0_b0toInf_pT1': 1.0728491592264455, 'j0_b0toInf_pT2': 1.0778331548891602}

SMS_T2bH_mSbottom450_mLSP1_uncert = {'j1to3_b0_pT0_mt2_0': 1.1204574613712244, 'j1to3_b0_pT1_mt2_0': 1.1941494269885953, 'j1to3_b0_pT2_mt2_0': 1.2019504889818293, 'j4toInf_b0_pT0_mt2_0': 1.2620381651591996, 'j4toInf_b0_pT1_mt2_0': 1.248060476497164, 'j4toInf_b0_pT2_mt2_0': 1.1987913479002545, 'j1to3_b1_pT0_mt2_0': 1.1459588983241515, 'j1to3_b1_pT1_mt2_0': 1.1016956242913136, 'j1to3_b1_pT2_mt2_0': 1.1153776408148477, 'j4toInf_b1_pT0_mt2_0': 1.1593486742963368, 'j4toInf_b1_pT1_mt2_0': 1.14422205101856, 'j4toInf_b1_pT2_mt2_0': 1.1439722195425213, 'j1to3_b2toInf_pT0_mt2_0': 1.1154729405531876, 'j1to3_b2toInf_pT1_mt2_0': 1.1079536937765446, 'j1to3_b2toInf_pT2_mt2_0': 1.1199333148045196, 'j4toInf_b2toInf_pT0_mt2_0': 1.1023327904437281, 'j4toInf_b2toInf_pT1_mt2_0': 1.100359354322355, 'j4toInf_b2toInf_pT2_mt2_0': 1.0863712915267567, 'j1to3_b0_pT0_mt2_30': 1.2409937758532366, 'j1to3_b0_pT1_mt2_30': 1.178969271105405, 'j1to3_b0_pT2_mt2_30': 1.2031944881142203, 'j4toInf_b0_pT0_mt2_30': 1.2131056076221365, 'j4toInf_b0_pT1_mt2_30': 1.198831587027816, 'j4toInf_b0_pT2_mt2_30': 1.1987058126980688, 'j1to3_b1_pT0_mt2_30': 1.1821263297823799, 'j1to3_b1_pT1_mt2_30': 1.1065833007557937, 'j1to3_b1_pT2_mt2_30': 1.118033893437436, 'j4toInf_b1_pT0_mt2_30': 1.127679285712288, 'j4toInf_b1_pT1_mt2_30': 1.1629232948353305, 'j4toInf_b1_pT2_mt2_30': 1.1576832267554162, 'j1to3_b2toInf_pT0_mt2_30': 1.0951525091629224, 'j1to3_b2toInf_pT1_mt2_30': 1.0900111104253247, 'j1to3_b2toInf_pT2_mt2_30': 1.1085541339608953, 'j4toInf_b2toInf_pT0_mt2_30': 1.0976831612920057, 'j4toInf_b2toInf_pT1_mt2_30': 1.112791843676748, 'j4toInf_b2toInf_pT2_mt2_30': 1.092854725243253, 'is1El_pT0_mt2_0': 1.0719722168617865, 'is1Mu_pT0_mt2_0': 1.081338797630651, 'is1El_pT0_mt2_30': 1.062609903369994, 'is1Mu_pT0_mt2_30': 1.0848410278108414, 'is1El_pT1_mt2_0': 1.0647147587494536, 'is1Mu_pT1_mt2_0': 1.074605629814378, 'is1El_pT1_mt2_30': 1.0772528316633116, 'is1Mu_pT1_mt2_30': 1.078689262291624, 'is1El_pT2_mt2_0': 1.0831624915451672, 'is1Mu_pT2_mt2_0': 1.0862670273047588, 'is1El_pT2_mt2_30': 1.0739729680356276, 'is1Mu_pT2_mt2_30': 1.0789683480895988, 'diBBZ_pT0_mt2_0': 1.0819023809177732, 'diBBZ_pT1_mt2_0': 1.0678085540326587, 'diBBZ_pT2_mt2_0': 1.0669178600972866, 'diBBH_pT0_mt2_0': 1.0727873615403114, 'diBBH_pT1_mt2_0': 1.080882631015565, 'diBBH_pT2_mt2_0': 1.0739864852523755, 'diBBZ_pT0_mt2_30': 1.1078888316740891, 'diBBZ_pT1_mt2_30': 1.0873040663428686, 'diBBZ_pT2_mt2_30': 1.0765375724726098, 'diBBH_pT0_mt2_30': 1.1008166652890288, 'diBBH_pT1_mt2_30': 1.0909505360072165, 'diBBH_pT2_mt2_30': 1.0780128194593683, 'diLepZ': 1.1352405264704335, 'j0_b0toInf_pT0': 1.033970575502926, 'j0_b0toInf_pT1': 1.033970575502926, 'j0_b0toInf_pT2': 1.033970575502926}



SMS_T2bH_mSbottom450_mLSP300_uncert = {'j1to3_b0_pT0_mt2_0': 1.1204574613712244, 'j1to3_b0_pT1_mt2_0': 1.1941494269885953, 'j1to3_b0_pT2_mt2_0': 1.2019504889818293, 'j4toInf_b0_pT0_mt2_0': 1.2620381651591996, 'j4toInf_b0_pT1_mt2_0': 1.248060476497164, 'j4toInf_b0_pT2_mt2_0': 1.1987913479002545, 'j1to3_b1_pT0_mt2_0': 1.1459588983241515, 'j1to3_b1_pT1_mt2_0': 1.1016956242913136, 'j1to3_b1_pT2_mt2_0': 1.1153776408148477, 'j4toInf_b1_pT0_mt2_0': 1.1593486742963368, 'j4toInf_b1_pT1_mt2_0': 1.14422205101856, 'j4toInf_b1_pT2_mt2_0': 1.1439722195425213, 'j1to3_b2toInf_pT0_mt2_0': 1.1154729405531876, 'j1to3_b2toInf_pT1_mt2_0': 1.1079536937765446, 'j1to3_b2toInf_pT2_mt2_0': 1.1199333148045196, 'j4toInf_b2toInf_pT0_mt2_0': 1.1023327904437281, 'j4toInf_b2toInf_pT1_mt2_0': 1.100359354322355, 'j4toInf_b2toInf_pT2_mt2_0': 1.0863712915267567, 'j1to3_b0_pT0_mt2_30': 1.2409937758532366, 'j1to3_b0_pT1_mt2_30': 1.178969271105405, 'j1to3_b0_pT2_mt2_30': 1.2031944881142203, 'j4toInf_b0_pT0_mt2_30': 1.2131056076221365, 'j4toInf_b0_pT1_mt2_30': 1.198831587027816, 'j4toInf_b0_pT2_mt2_30': 1.1987058126980688, 'j1to3_b1_pT0_mt2_30': 1.1821263297823799, 'j1to3_b1_pT1_mt2_30': 1.1065833007557937, 'j1to3_b1_pT2_mt2_30': 1.118033893437436, 'j4toInf_b1_pT0_mt2_30': 1.127679285712288, 'j4toInf_b1_pT1_mt2_30': 1.1629232948353305, 'j4toInf_b1_pT2_mt2_30': 1.1576832267554162, 'j1to3_b2toInf_pT0_mt2_30': 1.0951525091629224, 'j1to3_b2toInf_pT1_mt2_30': 1.0900111104253247, 'j1to3_b2toInf_pT2_mt2_30': 1.1085541339608953, 'j4toInf_b2toInf_pT0_mt2_30': 1.0976831612920057, 'j4toInf_b2toInf_pT1_mt2_30': 1.112791843676748, 'j4toInf_b2toInf_pT2_mt2_30': 1.092854725243253, 'is1El_pT0_mt2_0': 1.0719722168617865, 'is1Mu_pT0_mt2_0': 1.081338797630651, 'is1El_pT0_mt2_30': 1.062609903369994, 'is1Mu_pT0_mt2_30': 1.0848410278108414, 'is1El_pT1_mt2_0': 1.0647147587494536, 'is1Mu_pT1_mt2_0': 1.074605629814378, 'is1El_pT1_mt2_30': 1.0772528316633116, 'is1Mu_pT1_mt2_30': 1.078689262291624, 'is1El_pT2_mt2_0': 1.0831624915451672, 'is1Mu_pT2_mt2_0': 1.0862670273047588, 'is1El_pT2_mt2_30': 1.0739729680356276, 'is1Mu_pT2_mt2_30': 1.0789683480895988, 'diBBZ_pT0_mt2_0': 1.0819023809177732, 'diBBZ_pT1_mt2_0': 1.0678085540326587, 'diBBZ_pT2_mt2_0': 1.0669178600972866, 'diBBH_pT0_mt2_0': 1.0727873615403114, 'diBBH_pT1_mt2_0': 1.080882631015565, 'diBBH_pT2_mt2_0': 1.0739864852523755, 'diBBZ_pT0_mt2_30': 1.1078888316740891, 'diBBZ_pT1_mt2_30': 1.0873040663428686, 'diBBZ_pT2_mt2_30': 1.0765375724726098, 'diBBH_pT0_mt2_30': 1.1008166652890288, 'diBBH_pT1_mt2_30': 1.0909505360072165, 'diBBH_pT2_mt2_30': 1.0780128194593683, 'diLepZ': 1.1352405264704335, 'j0_b0toInf_pT0': 1.033970575502926, 'j0_b0toInf_pT1': 1.033970575502926, 'j0_b0toInf_pT2': 1.033970575502926 }


SMS_TChiWH_200_1_uncert =  {'j1to3_b0_pT0_mt2_0': 1.110995495404093, 'j1to3_b0_pT1_mt2_0': 1.0859767410408185, 'j1to3_b0_pT2_mt2_0': 1.192223827867411, 'j4toInf_b0_pT0_mt2_0': 1.1101907437128908, 'j4toInf_b0_pT1_mt2_0': 1.1024890238025518, 'j4toInf_b0_pT2_mt2_0': 1.2021781392732658, 'j1to3_b1_pT0_mt2_0': 1.1105621996886819, 'j1to3_b1_pT1_mt2_0': 1.0743908596535892, 'j1to3_b1_pT2_mt2_0': 1.17476269624837, 'j4toInf_b1_pT0_mt2_0': 1.1152562362737912, 'j4toInf_b1_pT1_mt2_0': 1.0656201188660914, 'j4toInf_b1_pT2_mt2_0': 1.1863491346907735, 'j1to3_b2toInf_pT0_mt2_0': 1.1701058493997192, 'j1to3_b2toInf_pT1_mt2_0': 1.1542206211892556, 'j1to3_b2toInf_pT2_mt2_0': 1.2761702373537018, 'j4toInf_b2toInf_pT0_mt2_0': 1.3677145632144585, 'j4toInf_b2toInf_pT1_mt2_0': 1.113947356265953, 'j4toInf_b2toInf_pT2_mt2_0': 1.530445096122115, 'j1to3_b0_pT0_mt2_30': 1.1122408125416066, 'j1to3_b0_pT1_mt2_30': 1.091203070123763, 'j1to3_b0_pT2_mt2_30': 1.1787512237720346, 'j4toInf_b0_pT0_mt2_30': 1.1179830496300212, 'j4toInf_b0_pT1_mt2_30': 1.1103358509279735, 'j4toInf_b0_pT2_mt2_30': 1.227081483172891, 'j1to3_b1_pT0_mt2_30': 1.1100636179670649, 'j1to3_b1_pT1_mt2_30': 1.0771232779386353, 'j1to3_b1_pT2_mt2_30': 1.1786393013869008, 'j4toInf_b1_pT0_mt2_30': 1.1058583959825576, 'j4toInf_b1_pT1_mt2_30': 1.0818168686763308, 'j4toInf_b1_pT2_mt2_30': 1.2241561955423048, 'j1to3_b2toInf_pT0_mt2_30': 1.1845318400710294, 'j1to3_b2toInf_pT1_mt2_30': 1.119958326097024, 'j1to3_b2toInf_pT2_mt2_30': 1.2722755956746767, 'j4toInf_b2toInf_pT0_mt2_30': 1.36156603822815, 'j4toInf_b2toInf_pT1_mt2_30': 1.0925958962373603, 'j4toInf_b2toInf_pT2_mt2_30': 1.274892706341947, 'is1El_pT0_mt2_0': 1.1178388730428122, 'is1Mu_pT0_mt2_0': 1.105242576935383, 'is1El_pT0_mt2_30': 1.1531665759883662, 'is1Mu_pT0_mt2_30': 1.1102905254316981, 'is1El_pT1_mt2_0': 1.0866717947200817, 'is1Mu_pT1_mt2_0': 1.0874299719775775, 'is1El_pT1_mt2_30': 1.1042976509802593, 'is1Mu_pT1_mt2_30': 1.085743804440904, 'is1El_pT2_mt2_0': 1.1918541112408072, 'is1Mu_pT2_mt2_0': 1.1949102357496908, 'is1El_pT2_mt2_30': 1.2085233799841157, 'is1Mu_pT2_mt2_30': 1.1961224107541004, 'diBBZ_pT0_mt2_0': 1.1738505104968058, 'diBBZ_pT1_mt2_0': 1.1384990974699836, 'diBBZ_pT2_mt2_0': 1.235469743279259, 'diBBH_pT0_mt2_0': 1.158309822815895, 'diBBH_pT1_mt2_0': 1.2169008990299486, 'diBBH_pT2_mt2_0': 1.1928419041598584, 'diBBZ_pT0_mt2_30': 1.1521315220458928, 'diBBZ_pT1_mt2_30': 1.1619259089830902, 'diBBZ_pT2_mt2_30': 1.204308590127777, 'diBBH_pT0_mt2_30': 1.125690095075149, 'diBBH_pT1_mt2_30': 1.1444645285182489, 'diBBH_pT2_mt2_30': 1.2569708154635464, 'diLepZ': 1.033970575502926, 'j0_b0toInf_pT0': 1.1008166652890286, 'j0_b0toInf_pT1': 1.0858254041645012, 'j0_b0toInf_pT2': 1.1379782591570138 } 



SMS_TChiHH_175_uncert = {'j1to3_b0_pT0_mt2_0': 1.1617714437099453, 'j1to3_b0_pT1_mt2_0': 1.108986237663294, 'j1to3_b0_pT2_mt2_0': 1.1675171632997645, 'j4toInf_b0_pT0_mt2_0': 1.1727136358253163, 'j4toInf_b0_pT1_mt2_0': 1.1277732366342812, 'j4toInf_b0_pT2_mt2_0': 1.2068187612379495, 'j1to3_b1_pT0_mt2_0': 1.1561985915429456, 'j1to3_b1_pT1_mt2_0': 1.0966850557221746, 'j1to3_b1_pT2_mt2_0': 1.156709923106356, 'j4toInf_b1_pT0_mt2_0': 1.1177794549146838, 'j4toInf_b1_pT1_mt2_0': 1.1229471431144293, 'j4toInf_b1_pT2_mt2_0': 1.2032633759436264, 'j1to3_b2toInf_pT0_mt2_0': 1.1540324641106543, 'j1to3_b2toInf_pT1_mt2_0': 1.0918585869693191, 'j1to3_b2toInf_pT2_mt2_0': 1.1783872192731306, 'j4toInf_b2toInf_pT0_mt2_0': 1.1106164544721986, 'j4toInf_b2toInf_pT1_mt2_0': 1.3022780177254045, 'j4toInf_b2toInf_pT2_mt2_0': 1.2302563788475793, 'j1to3_b0_pT0_mt2_30': 1.1631441080762648, 'j1to3_b0_pT1_mt2_30': 1.1188528501972084, 'j1to3_b0_pT2_mt2_30': 1.1649848477891225, 'j4toInf_b0_pT0_mt2_30': 1.1610155272015716, 'j4toInf_b0_pT1_mt2_30': 1.1160430954430292, 'j4toInf_b0_pT2_mt2_30': 1.2244192505111806, 'j1to3_b1_pT0_mt2_30': 1.1523614124376644, 'j1to3_b1_pT1_mt2_30': 1.102752128931716, 'j1to3_b1_pT2_mt2_30': 1.1577085920297305, 'j4toInf_b1_pT0_mt2_30': 1.1206896847290606, 'j4toInf_b1_pT1_mt2_30': 1.0859418407994617, 'j4toInf_b1_pT2_mt2_30': 1.213255715046514, 'j1to3_b2toInf_pT0_mt2_30': 1.1542011673107568, 'j1to3_b2toInf_pT1_mt2_30': 1.107619700798692, 'j1to3_b2toInf_pT2_mt2_30': 1.1786952713420253, 'j4toInf_b2toInf_pT0_mt2_30': 1.317512204489843, 'j4toInf_b2toInf_pT1_mt2_30': 1.193380454027805, 'j4toInf_b2toInf_pT2_mt2_30': 1.2207034209068812, 'is1El_pT0_mt2_0': 1.2785031418135173, 'is1Mu_pT0_mt2_0': 1.1603558542741736, 'is1El_pT0_mt2_30': 1.2558397936209298, 'is1Mu_pT0_mt2_30': 1.1637986568931504, 'is1El_pT1_mt2_0': 1.2424994845355346, 'is1Mu_pT1_mt2_0': 1.1294835896938296, 'is1El_pT1_mt2_30': 1.1781179384565181, 'is1Mu_pT1_mt2_30': 1.1171921499077475, 'is1El_pT2_mt2_0': 1.1997848843131032, 'is1Mu_pT2_mt2_0': 1.1636276260293477, 'is1El_pT2_mt2_30': 1.224882191380287, 'is1Mu_pT2_mt2_30': 1.1734819875376115, 'diBBZ_pT0_mt2_0': 1.1652029055434558, 'diBBZ_pT1_mt2_0': 1.0992471662063958, 'diBBZ_pT2_mt2_0': 1.1619382598399772, 'diBBH_pT0_mt2_0': 1.154103861080766, 'diBBH_pT1_mt2_0': 1.098934321648253, 'diBBH_pT2_mt2_0': 1.1875739854030938, 'diBBZ_pT0_mt2_30': 1.1526433752247374, 'diBBZ_pT1_mt2_30': 1.1207890723534213, 'diBBZ_pT2_mt2_30': 1.1638291793301792, 'diBBH_pT0_mt2_30': 1.1513406752991409, 'diBBH_pT1_mt2_30': 1.1010544407732783, 'diBBH_pT2_mt2_30': 1.1959948978927768, 'diLepZ': 1.1465946793031723, 'j0_b0toInf_pT0': 1.157905034751904, 'j0_b0toInf_pT1': 1.1388452375848737,'j0_b0toInf_pT2': 1.1024109369159367 }


SMS_TChiHZ_175_uncert = {'j1to3_b0_pT0_mt2_0': 1.161245154965971, 'j1to3_b0_pT1_mt2_0': 1.1021273714534943, 'j1to3_b0_pT2_mt2_0': 1.1708332520325007, 'j4toInf_b0_pT0_mt2_0': 1.1608415369237686, 'j4toInf_b0_pT1_mt2_0': 1.1161292383510717, 'j4toInf_b0_pT2_mt2_0': 1.2036369318173892, 'j1to3_b1_pT0_mt2_0': 1.1432340741583509, 'j1to3_b1_pT1_mt2_0': 1.0924662100445346, 'j1to3_b1_pT2_mt2_0': 1.1675350709553078, 'j4toInf_b1_pT0_mt2_0': 1.1262061805142678, 'j4toInf_b1_pT1_mt2_0': 1.075352504935138, 'j4toInf_b1_pT2_mt2_0': 1.1880585015360912, 'j1to3_b2toInf_pT0_mt2_0': 1.1868421793921275, 'j1to3_b2toInf_pT1_mt2_0': 1.0919999999999996, 'j1to3_b2toInf_pT2_mt2_0': 1.1672602762164406, 'j4toInf_b2toInf_pT0_mt2_0': 1.304200591715401, 'j4toInf_b2toInf_pT1_mt2_0': 1.0646065012208523, 'j4toInf_b2toInf_pT2_mt2_0': 1.198443946745674, 'j1to3_b0_pT0_mt2_30': 1.1571877857850283, 'j1to3_b0_pT1_mt2_30': 1.1093800713110025, 'j1to3_b0_pT2_mt2_30': 1.17200581385523, 'j4toInf_b0_pT0_mt2_30': 1.1362204096308626, 'j4toInf_b0_pT1_mt2_30': 1.1161722858516607, 'j4toInf_b0_pT2_mt2_30': 1.2179128266073387, 'j1to3_b1_pT0_mt2_30': 1.147695632975386, 'j1to3_b1_pT1_mt2_30': 1.0984479557939117, 'j1to3_b1_pT2_mt2_30': 1.1611707169432464, 'j4toInf_b1_pT0_mt2_30': 1.1385640646055102, 'j4toInf_b1_pT1_mt2_30': 1.0641716448285377, 'j4toInf_b1_pT2_mt2_30': 1.191426225998425, 'j1to3_b2toInf_pT0_mt2_30': 1.1463010594630128, 'j1to3_b2toInf_pT1_mt2_30': 1.1333791587917692, 'j1to3_b2toInf_pT2_mt2_30': 1.1705637710652528, 'j4toInf_b2toInf_pT0_mt2_30': 1.1366235704408283, 'j4toInf_b2toInf_pT1_mt2_30': 1.3047753270853795, 'j4toInf_b2toInf_pT2_mt2_30': 1.273334959344757, 'is1El_pT0_mt2_0': 1.1868903421795787, 'is1Mu_pT0_mt2_0': 1.1593423986263542, 'is1El_pT0_mt2_30': 1.2151232205039708, 'is1Mu_pT0_mt2_30': 1.1617838063589803, 'is1El_pT1_mt2_0': 1.0889044430835715, 'is1Mu_pT1_mt2_0': 1.1295762323885057, 'is1El_pT1_mt2_30': 1.1012620363216146, 'is1Mu_pT1_mt2_30': 1.1185411321018994, 'is1El_pT2_mt2_0': 1.1896259475915678, 'is1Mu_pT2_mt2_0': 1.1593800489396338, 'is1El_pT2_mt2_30': 1.1565183695289472, 'is1Mu_pT2_mt2_30': 1.1661445154075212, 'diBBZ_pT0_mt2_0': 1.1619876538505325, 'diBBZ_pT1_mt2_0': 1.1085725563851199, 'diBBZ_pT2_mt2_0': 1.1743559577416267, 'diBBH_pT0_mt2_0': 1.1713125798066213, 'diBBH_pT1_mt2_0': 1.1481890684227416, 'diBBH_pT2_mt2_0': 1.1795717126943996, 'diBBZ_pT0_mt2_30': 1.1616415788094139, 'diBBZ_pT1_mt2_30': 1.1247477454706098, 'diBBZ_pT2_mt2_30': 1.176589920437153, 'diBBH_pT0_mt2_30': 1.148128322747542, 'diBBH_pT1_mt2_30': 1.1167133240037315, 'diBBH_pT2_mt2_30': 1.187717873416465, 'diLepZ': 1.126585939187573, 'j0_b0toInf_pT0': 1.162751344080471, 'j0_b0toInf_pT1': 1.1138156404014843,'j0_b0toInf_pT2': 1.1374263439082914 }




glugluTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsGluGlu_comb_mt2_30_SMHDonly.txt"
VBFTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsVBF_comb_mt2_30_SMHDonly.txt"
ttHTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsttH_comb_mt2_30_SMHDonly.txt"
VHTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsVH_comb_mt2_30_SMHDonly.txt"
bbHTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsbbH_comb_mt2_30_SMHDonly.txt"
#THXTxt= "/work/mschoene/CMSSW_7_4_7_gg/src/flashggFinalFit/tableData/higgsTHX_comb_mt2_30_SMHDonly.txt"
 


glugluYield={}
with open(glugluTxt) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    line=line.replace("  "," ")
    line=line.replace("  "," ")
    words=line.split(" ")  
    glugluYield[words[0]]=words[1]

VBFYield={}
with open(VBFTxt) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    line=line.replace("  "," ")
    line=line.replace("  "," ")
    words=line.split(" ")  
    VBFYield[words[0]]=words[1]

ttHYield={}
with open(ttHTxt) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    line=line.replace("  "," ")
    line=line.replace("  "," ")
    words=line.split(" ")  
    ttHYield[words[0]]=words[1]

VHYield={}
with open(VHTxt) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    line=line.replace("  "," ")
    line=line.replace("  "," ")
    words=line.split(" ")  
    VHYield[words[0]]=words[1]

bbHYield={}
with open(bbHTxt) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    line=line.replace("  "," ")
    line=line.replace("  "," ")
    words=line.split(" ")  
    bbHYield[words[0]]=words[1]

#THXYield={}
#with open(THXTxt) as i:
#  lines  = i.readlines()
#  for n,line in enumerate(lines):
#    line=line.replace("\n","")
#    line=line.replace("  "," ")
#    line=line.replace("  "," ")
#    words=line.split(" ")  
#    THXYield[words[0]]=words[1]

# print glugluYield, "             "
# print VBFYield, "             "
# print ttHYield, "             "
# print bbHYield, "             "
# print VHYield, "             "
# print THXYield, "             "



rankingT2bH_450_1 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_mar30/AsymptoticRanking_SMS_T2bH_mSbottom_450_1.txt"
rankingT2bH_600_1 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_mar30/AsymptoticRanking_SMS_T2bH_mSbottom_600_1.txt"
rankingT2bH_450_300 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_T2bH_mar30/AsymptoticRanking_SMS_T2bH_mSbottom_450_300.txt"

rankingWH_200_1 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_WH_mar30/AsymptoticRanking_SMS_TChiWH_HToGG_200_1.txt"
#rankingWH_175_49 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_WH_mar30/AsymptoticRanking_SMS_TChiWH_175_49.txt"
rankingWH_225_50 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_WH_mar30/AsymptoticRanking_SMS_TChiWH_HToGG_225_50.txt"

rankingHH_127 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HH_mar30/AsymptoticRanking_SMS_TChiHH_HToGG_127.txt"
rankingHH_275 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HH_mar30/AsymptoticRanking_SMS_TChiHH_HToGG_275.txt"
rankingHZ_127 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HZ_mar30_corrSumGenMET/AsymptoticRanking_SMS_TChiHZ_HToGG_127.txt"  
rankingHZ_175 = "/work/mschoene/CMSSW_7_4_7_gg/src/HiggsAnalysis/CombinedLimit/dataCards_HZ_mar30_corrSumGenMET/AsymptoticRanking_SMS_TChiHZ_HToGG_175.txt"



rank_HZ_175_exp={}
rank_HZ_175_obs={}
sorted_rank_HZ_175_exp=[]

with open(rankingHZ_175) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_HZ_175_exp[words[0]]=words[1]
    rank_HZ_175_obs[words[0]]=words[2]
    sorted_rank_HZ_175_exp.append(words[1])
   
sorted_rank_HZ_175_exp = sorted(sorted_rank_HZ_175_exp, key=float)

#########################

rank_HZ_127_exp={}
rank_HZ_127_obs={}
sorted_rank_HZ_127_exp=[]

with open(rankingHZ_127) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_HZ_127_exp[words[0]]=words[1]
    rank_HZ_127_obs[words[0]]=words[2]
    sorted_rank_HZ_127_exp.append(words[1])
   
sorted_rank_HZ_127_exp = sorted(sorted_rank_HZ_127_exp, key=float)

#########################

rank_HH_275_exp={}
rank_HH_275_obs={}
sorted_rank_HH_275_exp=[]

with open(rankingHH_275) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_HH_275_exp[words[0]]=words[1]
    rank_HH_275_obs[words[0]]=words[2]
    sorted_rank_HH_275_exp.append(words[1])
   
sorted_rank_HH_275_exp = sorted(sorted_rank_HH_275_exp, key=float)

#########################

rank_HH_127_exp={}
rank_HH_127_obs={}
sorted_rank_HH_127_exp=[]

with open(rankingHH_127) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_HH_127_exp[words[0]]=words[1]
    rank_HH_127_obs[words[0]]=words[2]
    sorted_rank_HH_127_exp.append(words[1])
   
sorted_rank_HH_127_exp = sorted(sorted_rank_HH_127_exp, key=float)

#########################

rank_WH_225_50_exp={}
rank_WH_225_50_obs={}
sorted_rank_WH_225_50_exp=[]

with open(rankingWH_225_50) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_WH_225_50_exp[words[0]]=words[1]
    rank_WH_225_50_obs[words[0]]=words[2]
    sorted_rank_WH_225_50_exp.append(words[1])
   
sorted_rank_WH_225_50_exp = sorted(sorted_rank_WH_225_50_exp, key=float)

#########################

# rank_WH_175_49_exp={}
# rank_WH_175_49_obs={}
# sorted_rank_WH_175_49_exp=[]

# with open(rankingWH_175_49) as i:
#   lines  = i.readlines()
#   for n,line in enumerate(lines):
#     line=line.replace("\n","")
#     words=line.split(" ")  
#     rank_WH_175_49_exp[words[0]]=words[1]
#     rank_WH_175_49_obs[words[0]]=words[2]
#     sorted_rank_WH_175_49_exp.append(words[1])
   
# sorted_rank_WH_175_49_exp = sorted(sorted_rank_WH_175_49_exp, key=float)

#########################

rank_WH_200_1_exp={}
rank_WH_200_1_obs={}
sorted_rank_WH_200_1_exp=[]

with open(rankingWH_200_1) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_WH_200_1_exp[words[0]]=words[1]
    rank_WH_200_1_obs[words[0]]=words[2]
    sorted_rank_WH_200_1_exp.append(words[1])
   
sorted_rank_WH_200_1_exp = sorted(sorted_rank_WH_200_1_exp, key=float)

#########################

rank_T2bH_450_1_exp={}
rank_T2bH_450_1_obs={}
sorted_rank_T2bH_450_1_exp=[]

with open(rankingT2bH_450_1) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_T2bH_450_1_exp[words[0]]=words[1]
    rank_T2bH_450_1_obs[words[0]]=words[2]
    sorted_rank_T2bH_450_1_exp.append(words[1])
   
sorted_rank_T2bH_450_1_exp = sorted(sorted_rank_T2bH_450_1_exp, key=float)

#########################

rank_T2bH_450_300_exp={}
rank_T2bH_450_300_obs={}
sorted_rank_T2bH_450_300_exp=[]

with open(rankingT2bH_450_300) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_T2bH_450_300_exp[words[0]]=words[1]
    rank_T2bH_450_300_obs[words[0]]=words[2]
    sorted_rank_T2bH_450_300_exp.append(words[1])
   
sorted_rank_T2bH_450_300_exp = sorted(sorted_rank_T2bH_450_300_exp, key=float)


rank_T2bH_600_1_exp={}
rank_T2bH_600_1_obs={}
sorted_rank_T2bH_600_1_exp=[]

with open(rankingT2bH_600_1) as i:
  lines  = i.readlines()
  for n,line in enumerate(lines):
    line=line.replace("\n","")
    words=line.split(" ")  
    rank_T2bH_600_1_exp[words[0]]=words[1]
    rank_T2bH_600_1_obs[words[0]]=words[2]
    sorted_rank_T2bH_600_1_exp.append(words[1])
   
sorted_rank_T2bH_600_1_exp = sorted(sorted_rank_T2bH_600_1_exp, key=float)




#lumi2016=36.814
lumi2016=35.922
lumi2017=41.529

#lumi2016=35.9
#lumi2017=41.37

lumi=77.5
procs=["higgs2016","higgs2017","HZ 2016","HZ 2017","HH 2016","HH 2017","WH 127 1 2016","WH 127 1 2017"]
#procs=["higgs2016","higgs2017","HZ 2016","HZ 2017","HH 2016","HH 2017","WH 150 1 2016","WH 150 1 2017","WH 150 24 2016","WH 150 24 2017"]
#procs=[]
tags=[]
_tags=options.flashggCats.split(",")
weights=[]
entries=[]
yields=[]
perTagYields={}
perProcYields={}
matrix1={}
matrix2={} 
Arr={}


#for n,p in enumerate(_tags):
#  line= str('%s' %(p.replace("_","\_") ) )  
 # print  names[ n ]



hmSigma={}
bkgYield={}
bkgReso_up={}
bkgReso_dn={}

dataYield={}

effSigmaSM={}
hmSigmaSM={}
bkgYieldSM={}

hmSigma_2017={}
bkgYield_2017={}

effSigmaSM_2017={}
hmSigmaSM_2017={}
bkgYieldSM_2017={}

effSigmaHZ_127={}
effSigmaHZ_127_2017={}
effSigmaHZ_175={}
effSigmaHZ_175_2017={}

effSigmaHH_127={}
effSigmaHH_127_2017={}
effSigmaHH_275={}
effSigmaHH_275_2017={}
effSigmaHH_175={}
effSigmaHH_175_2017={}

#effSigmaWH_127_1={}
#effSigmaWH_127_1_2017={}

effSigmaWH_200_1={}
effSigmaWH_200_1_2017={}
#effSigmaWH_175_49={}
#effSigmaWH_175_49_2017={}
#effSigmaWH_175_1={}
#effSigmaWH_175_1_2017={}
effSigmaWH_225_50={}
effSigmaWH_225_50_2017={}

effSigmaT2bH_450_1={}
effSigmaT2bH_450_1_2017={}

effSigmaT2bH_600_1={}
effSigmaT2bH_600_1_2017={}
effSigmaT2bH_450_300={}
effSigmaT2bH_450_300_2017={}

sigInputHZ=options.siginput.replace("HH","HZ")
sigInputWH=options.siginput.replace("HH","WH")
sigInputT2bH=options.siginput.replace("HH","T2bH")

#SM higgs
with open(options.siginput) as i:
#with open(sigInputHH) as i:
#with open(sigInputT2bH) as i:
  lines  = i.readlines()
  for line in lines:
    if not "[For MT2 MC integral]" in line: continue
    if not "MT2" in line: continue
    if not "higgs" in line: continue # only do Higgs here
    line=line.replace("m125_","=")
#    line=line.replace("AllCats","Total")
    line=line.replace("mass_","")
    line=line.replace("sig_","")
    line=line.replace("2017_","2017")
    line=line.replace("\n","")
    words=line.split("=")  
    if "2017" in line:
      effSigmaSM_2017[words[1]]=words[2]
    else:
      effSigmaSM[words[1]]=words[2]
      
#HZ
#with open(options.siginput) as i:
with open(sigInputHZ) as i:
  lines  = i.readlines()
  for line in lines:
    #  print line
    if not "[For MT2 MC integral]" in line: continue
 #   if not "150" or "higgs"  in line: continue #only doing the higgs bg and the signal at 150GeV mchi
    if not "sig_" in line: continue
    if not "TChi" in line: continue
    line=line.replace("m125_","=")
    line=line.replace("mass_","")
    line=line.replace("sig_","")
    line=line.replace("2017_","2017")
    line=line.replace("\n","")
    words=line.split("=")  
    if "m127" in line:
      if "2017" in line:
        effSigmaHZ_127_2017[words[1]]=words[2]
      else:
        effSigmaHZ_127[words[1]]=words[2]
    elif "m175" in line:
      if "2017" in line:
        effSigmaHZ_175_2017[words[1]]=words[2]
      else:
        effSigmaHZ_175[words[1]]=words[2]


#HH
with open(options.siginput) as i:
#with open(sigInputHH) as i:
  lines  = i.readlines()
  for line in lines:
    if not "[For MT2 MC integral]" in line: continue
  #  if not "150" or "higgs"  in line: continue #only doing the higgs bg and the signal at 150GeV mchi
    if not "sig_" in line: continue
    if not "TChi" in line: continue
    line=line.replace("m125_","=")
    line=line.replace("mass_","")
    line=line.replace("sig_","")
    line=line.replace("2017_","2017")
    line=line.replace("\n","")
    words=line.split("=")  
    if "m127" in line:
      if "2017" in line:
        effSigmaHH_127_2017[words[1]]=words[2]
      else:
        effSigmaHH_127[words[1]]=words[2]
    elif "m275" in line:
      if "2017" in line:
        effSigmaHH_275_2017[words[1]]=words[2]
      else:
        effSigmaHH_275[words[1]]=words[2]
    elif "m175" in line:
      if "2017" in line:
        effSigmaHH_175_2017[words[1]]=words[2]
      else:
        effSigmaHH_175[words[1]]=words[2]

#WH    
with open(sigInputWH) as i:
  lines  = i.readlines()
  for line in lines:
    if not "[For MT2 MC integral]" in line: continue
 #   if not "150" or "higgs"  in line: continue #only doing the higgs bg and the signal at 150GeV mchi
    if not "sig_" in line: continue
    if not "TChi" in line: continue
    line=line.replace("m125_","=")
    line=line.replace("mass_","")
    line=line.replace("sig_","")
    line=line.replace("2017_","2017")
    line=line.replace("\n","")
    words=line.split("=")  
    if "m200_m1" in line:
#      print line
      if "2017" in line:
        effSigmaWH_200_1_2017[words[1]]=words[2]
      else:
        effSigmaWH_200_1[words[1]]=words[2]
#    elif "175_49" in line:
#      if "2017" in line:
#        effSigmaWH_175_49_2017[words[1]]=words[2]
#      else:
#        effSigmaWH_175_49[words[1]]=words[2]
#    elif "175_1" in line:
#      if "2017" in line:
#        effSigmaWH_175_1_2017[words[1]]=words[2]
#      else:
#        effSigmaWH_175_1[words[1]]=words[2]
    elif "m225_m50" in line:
      if "2017" in line:
        effSigmaWH_225_50_2017[words[1]]=words[2]
      else:
        effSigmaWH_225_50[words[1]]=words[2]

#T2bH
with open(sigInputT2bH) as i:
  lines  = i.readlines()
  for line in lines:
    if not "[For MT2 MC integral]" in line: continue
    if not "450" or "higgs"  in line: continue #only doing the higgs bg and the signal at 150GeV mchi
    if not "sig_" in line: continue
    if not "T2b" in line: continue
    line=line.replace("m125_","=")
    line=line.replace("mass_","")
    line=line.replace("sig_","")
    line=line.replace("2017_","2017")
    line=line.replace("mLSP","")
    line=line.replace("\n","")
    words=line.split("=")  

    if "450_1" in line:
      if "2017" in line:
        effSigmaT2bH_450_1_2017[words[1]]=words[2]
      else:
        effSigmaT2bH_450_1[words[1]]=words[2]
    elif "450_300" in line:
      if "2017" in line:
        effSigmaT2bH_450_300_2017[words[1]]=words[2]
      else:
        effSigmaT2bH_450_300[words[1]]=words[2]
    elif "600_1" in line:
      if "2017" in line:
        effSigmaT2bH_600_1_2017[words[1]]=words[2]
      else:
        effSigmaT2bH_600_1[words[1]]=words[2]


#xsec_EW = 0.111E+01;
 
 
#print effSigmaT2bH_450_1_2017[ _tags[1] ] 


flashggCats=""
for x in effSigmaHZ_127.keys():
  if (flashggCats==""):
    flashggCats=x
  else:
    flashggCats=flashggCats+","+x


xsec_EW_450 = 1.110
xsec_EW_600 = 0.205
#def round_to_nice(x):

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{c c c c c c}"
print line
#print "[\\cmsTabSkip]"
print "Category & HH 175 & HZ 175 & WH 175,1 & T2bH 450,1 & T2bH 450,300     \\\\ "
#print "Category & Data (122-129) & SM Higgs & HZ & HH & WH 150 1  & WH 150 24   \\\\ "
print "[\\cmsTabSkip]"

for n,p in enumerate(_tags):
#for p in _tags:
#  line= str('%s' %(p.replace("_","\_") ) )  
  line= names[ n ]
#  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])))
 # line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1f ^{%.1f}_{%.1f}' %( float(bkgYield[ str(p) ])*(129.-122), float(bkgReso_up[ str(p) ]), float(bkgReso_dn[ str(p) ]) )) 
 # line= line + " & " + str('%.1f $\pm$ %.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) *  abs(1. -float(smH_uncert[ str(p) ]) )) ) 

  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  

  
#  line= line + " & " + str('%s $\pm$ %s' %(round_to_nice(float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017)), round_to_nice((float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHH_175_uncert[ str(p) ]) )    ))  ) 
#  line= line + " & " + str('%s $\pm$ %s' %(round_to_nice(float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017)), round_to_nice((float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHZ_175_uncert[ str(p) ]) )    ) ) )  
#  line= line + " & " + str('%s $\pm$ %s' %(round_to_nice(float(effSigmaWH_175_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_175_1_2017[ str(p) ])*(lumi2017)), round_to_nice((float(effSigmaWH_175_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_175_1_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiWH_175_1_uncert[ str(p) ]) )    ) ) )  
#  line= line + " & " + str('%s $\pm$ %s' %(round_to_nice(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017) ), round_to_nice((float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) )    ) ) )
#  line= line + " & " + str('%s $\pm$ %s' %(round_to_nice(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017)), round_to_nice((float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) ) )   ) )  + " \\\\"

  
  line= line + " & " + roundTogether( float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017), (float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHH_175_uncert[ str(p) ]) )    )

  line= line + " & " + roundTogether( (float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017)), (float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHZ_175_uncert[ str(p) ]) )     )

  line= line + " & " + roundTogether( (float(effSigmaWH_200_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017)), (float(effSigmaWH_200_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiWH_200_1_uncert[ str(p) ]) )   
  ) 
  line= line + " & " + roundTogether( (float(  effSigmaT2bH_450_300[ str(p) ])*(lumi2016) *xsec_EW_450  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017)  *xsec_EW_450), (float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016) *xsec_EW_450  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017) *xsec_EW_450)* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) )  ) 

  line= line + " & " + roundTogether( (float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) *xsec_EW_450  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017) *xsec_EW_450), (float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) *xsec_EW_450  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017)  *xsec_EW_450)* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) ) )   + " \\\\"


#  line= line + " & " + str('%.2g $\pm$ %.2g' %(float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017), (float(effSigmaHH_175[ str(p) ])*(lumi2016)  + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHH_175_uncert[ str(p) ]) )    ) ) 
 # line= line + " & " + str('%.1f $\pm$ %.1f' %(float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017), (float(effSigmaHZ_175[ str(p) ])*(lumi2016)  + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiHZ_175_uncert[ str(p) ]) )    ) ) 
  #line= line + " & " + str('%.1f $\pm$ %.1f' %(float(effSigmaWH_175_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_175_1_2017[ str(p) ])*(lumi2017), (float(effSigmaWH_175_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_175_1_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_TChiWH_175_1_uncert[ str(p) ]) )    ) ) 
 # line= line + " & " + str('%.1f $\pm$ %.1f' %(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017), (float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) )    ) ) 
  #line= line + " & " + str('%.1f $\pm$ %.1f' %(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017), (float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017))* abs(1. -float( SMS_T2bH_mSbottom450_mLSP1_uncert[ str(p) ]) )    ) )  + " \\\\"


#  line= line + " & " + str('%.1f' %(float(effSigmaHZ_175[ str(p) ])*(lumi2016) + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017)  ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaHH_175[ str(p) ])*(lumi2016)        + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017)  ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaWH_200_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017)) ) 
# line= line + " & " + str('%.1f' %(float(effSigmaWH_150_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_150_1_2017[ str(p) ])*(lumi2017)) ) 
  # line= line + " & " + str('%.1f' %(float(effSigmaWH_150_24[ str(p) ])*(lumi2016) + float(effSigmaWH_150_24_2017[ str(p) ])*(lumi2017)) )  + " \\\\"
#  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017)) ) 
#  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017)) )  + " \\\\"

  if( n==0 or n==6 or n==12 or n==18 or n==24  or n==27  or n==45):
    line = line + "  [\\cmsTabSkip]"

  print line

#print "[\\cmsTabSkip]"
print "\\end{tabular}"
print "\\caption{Expected background and EW signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up.}"
print "\\label{tab:res_ew}"
print "\\end{table*}"
print " "





print " "


 
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%% SMH split into processes %%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{c|c|c|c|c|c||c}"
print line
#print "[\\cmsTabSkip]"
print "Category & ggH & ttH & VBF & VH & bbH & Total    \\\\ "

print "[\\cmsTabSkip]"

for n,p in enumerate(_tags):
#for p in _tags:
#  line= str('%s' %(p.replace("_","\_") ) )  
  line= names[ n ]
#  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])))

  line= line + " & " + round_to_nice(float(glugluYield[ str(p) ]))
  line= line + " & " + round_to_nice(float(ttHYield[ str(p) ]))  
  line= line + " & " + round_to_nice(float(VBFYield[ str(p) ]))  
  line= line + " & " + round_to_nice(float(VHYield[ str(p) ]))  
  line= line + " & " + round_to_nice(float(bbHYield[ str(p) ])) 


#  line= line + " & " + str('%.1g' %(float(glugluYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1g' %(float(ttHYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1g' %(float(VBFYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1g' %(float(VHYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1g' %(float(bbHYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1f' %(float(THXYield[ str(p) ])) ) 

#just as a check, remove this column afterwards#
 # line= line + " & " + str('%.1f' %(float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) + float(THXYield[ str(p) ]) )  )

  #  line= line + " & " + str('%.1f' %(float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )  )
 # line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  

  #print line
  #print smH_uncert[ str(p) ]

#add the jec uncert here for now in this ugly manner...and just taking the average here...
  averageHere= (float ( jecUncerts_SMH_2016[ str(p) ]) +float ( jecUncerts_SMH_2016[ str(p) ]) ) 
  
  errorHere =  ( (1-float(smH_uncert[ str(p) ]))**2 + averageHere**2        )**(1./2)
  smhUncertHere = abs( errorHere )

  line= line + " & " + roundTogether( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) * smhUncertHere  )   + " \\\\"
# line= line + " & " + str('%.1f $\pm$ %.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) * smhUncertHere  ) )  + " \\\\"
  

  #  line= line + " & " + str('%.1f $\pm$ %.1f' %( float(effSigmaSM[ str(p) ])*(lumi2016) + float(effSigmaSM_2017[ str(p) ])*(lumi2017), (float(effSigmaSM[ str(p) ])*(lumi2016)+ float(effSigmaSM_2017[ str(p) ])*(lumi2017) )*  abs(1. -float(smH_uncert[ str(p) ]) )) )  + " \\\\"



  if( n==0 or n==6 or n==12 or n==18 or n==24  or n==27  or n==45):
    line = line + "  [\\cmsTabSkip]"

  print line

#print "[\\cmsTabSkip]"
print "\\end{tabular}"
print "\\caption{Expected standard model Higgs boson background in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up.}"
print "\\label{tab:smh_split}"
print "\\end{table*}"
print " "





counter=0;
for x in effSigmaHZ_127.keys():
  exec_line='$CMSSW_BASE/src/flashggFinalFit/Background/bin/makeBkgPlots -b %s -o tmp.root -d tmp -c %d --sqrts 13 --intLumi 77.5 --massStep 1.000 --nllTolerance 0.050 -L 125 -H 125  --higgsResolution %f --isMultiPdf  --verbose --unblind --useBinnedData --doBands -f %s| grep TABLE > bkg.tmp'%(options.bkgworkspaces,counter,float(effSigmaHZ_127[x]),flashggCats.replace("Tag ","Tag_").replace(" Tag","Tag").replace("TTH ","TTH"))
#exec_line='$CMSSW_BASE/src/flashggFinalFit/Background/bin/makeBkgPlots -b %s -o tmp.root -d tmp -c %d --sqrts 13 --intLumi 77.5 --massStep 1.000 --nllTolerance 0.050 -L 125 -H 125  --higgsResolution %f --isMultiPdf  --verbose --unblind --useBinnedData --doBands -f %s| grep TABLE > bkg.tmp'%(options.bkgworkspaces,counter,float(effSigmaHZ_127[x]),flashggCats.replace("Tag ","Tag_").replace(" Tag","Tag").replace("TTH ","TTH"))
  print exec_line
  os.system(exec_line)
  counter=counter+1

#  exec_line='$CMSSW_BASE/src/flashggFinalFit/Background/bin/makeBkgPlots -b %s -o tmp.root -d tmp -c %d --sqrts 13 --intLumi 77.5 --massStep 1.000 --nllTolerance 0.050 -L 125 -H 125  --higgsResolution %f --isMultiPdf  --verbose --unblind --useBinnedData --doBands -f %s| grep TABLE > bkg.tmp'%(options.bkgworkspaces,counter,float(effSigmaHZ_127[x]),flashggCats.replace("Tag ","Tag_").replace(" Tag","Tag").replace("TTH ","TTH"))
 # os.system(exec_line)
# -s Signal/CMS-HGG_13TeV_sigfit_2018dec01_HH.root

  with open('bkg.tmp') as i:
    lines  = i.readlines()
    for line in lines:
#      print line
      if not "TABLE" in line: continue

      if not "Unblind" in line:
        line=line.replace("Tag_","Tag ")
        line=line.replace("Tag"," Tag")
        line=line.replace("TTH","TTH ")
        line=line.replace("\n","")
        line=line.replace(" assuming resolution of ","")
        words=line.split(',')

        bkgYield[words[1]]=float(words[3])
#        dataYield[words[1]]=float(words[3])

        if "Bkg" in line:
          bkgYield[words[1]]=float(words[2])
          bkgReso_up[words[1]]=float(words[3])
          bkgReso_dn[words[1]]=float(words[4])

      else:
        line=line.replace("Tag_","Tag ")
        line=line.replace("Tag"," Tag")
        line=line.replace("TTH","TTH ")
        line=line.replace("\n","")
        line=line.replace(" assuming resolution of ","")
        words=line.split(',')
        print line
        print words
        dataYield[words[1]]=float(words[3])
 

#      print "LCDEBUG ", bkgYield
#bkgAllYield=0
#for x in bkgYield.values(): bkgAllYield=bkgAllYield+x
#bkgYield["Total"]=bkgAllYield

#print "DEBUG bkg YIELD"
#print bkgYield
#print bkgReso_up
#print bkgReso_dn
print dataYield






print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{c c c c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data (122-129) & Data Fit (122-129) & SM Higgs   \\\\ "
#print "Category & Data (122-129) & SM Higgs & HZ & HH & WH 150 1  & WH 150 24   \\\\ "
print "[\\cmsTabSkip]"

for n,p in enumerate(_tags):
#for p in _tags:
#  line= str('%s' %(p.replace("_","\_") ) )  
  line= names[ n ]
#  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])))
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
#  line= line + " & " + str('%.1f $\pm$ %.1f ' %( float(bkgYield[ str(p) ])*(129.-122), float(bkgReso_up[ str(p) ]) )) 
  line= line + " & " + roundTogether( float(bkgYield[ str(p) ])*(129.-122), float(bkgReso_up[ str(p) ]) ) 
#asym errors  line= line + " & " + str('%.1f ^{%.1f}_{%.1f}' %( float(bkgYield[ str(p) ])*(129.-122), float(bkgReso_up[ str(p) ]), float(bkgReso_dn[ str(p) ]) )) 

#add the jec uncert here for now in this ugly manner...and just taking the average here...
  averageHere= (float ( jecUncerts_SMH_2016[ str(p) ]) +float ( jecUncerts_SMH_2016[ str(p) ]) ) 
  
  errorHere =  ( (1-float(smH_uncert[ str(p) ]))**2 + averageHere**2        )**(1./2)
  smhUncertHere = abs( errorHere )

  line= line + " & " + roundTogether( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) * smhUncertHere  )   + " \\\\"
#  line= line + " & " + str('%.1f $\pm$ %.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) * smhUncertHere  ) )  + " \\\\"

#  line= line + " & " + str('%.1f $\pm$ %.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) ) , (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ])) *  abs(1. -float(smH_uncert[ str(p) ]) )) )   + " \\\\"

  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  

  

#  line= line + " & " + str('%.1f' %(float(effSigmaHZ_175[ str(p) ])*(lumi2016) + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017)  ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaHH_175[ str(p) ])*(lumi2016)        + float(effSigmaHH_175_2017[ str(p) ])*(lumi2017)  ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaWH_200_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017)) ) 
# line= line + " & " + str('%.1f' %(float(effSigmaWH_150_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_150_1_2017[ str(p) ])*(lumi2017)) ) 
  # line= line + " & " + str('%.1f' %(float(effSigmaWH_150_24[ str(p) ])*(lumi2016) + float(effSigmaWH_150_24_2017[ str(p) ])*(lumi2017)) )  + " \\\\"
#  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017)) ) 
#  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017)) )  + " \\\\"

  if( n==0 or n==6 or n==12 or n==18 or n==24  or n==27  or n==45):
    line = line + "  [\\cmsTabSkip]"

  print line

#print "[\\cmsTabSkip]"
print "\\end{tabular}"
print "\\caption{Observed and expected }"
print "\\label{tab:res_ew}"
print "\\end{table*}"
print " "





#HZ 175

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{c|c|c|c|c||c|c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_HZ_175_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_HZ_175_exp.keys()[ rank_HZ_175_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))

  #print line 

  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  
  #line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaHZ_175[ str(p) ])*(lumi2016) + float(effSigmaHZ_175_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_HZ_175_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_HZ_175_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiHZ(175): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_hz175}"
print "\\end{table*}"
print " "

#HZ 127

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c| |c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_HZ_127_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_HZ_127_exp.keys()[ rank_HZ_127_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaHZ_127[ str(p) ])*(lumi2016) + float(effSigmaHZ_127_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_HZ_127_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_HZ_127_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiHZ(127): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_hz127}"
print "\\end{table*}"
print " "



#HH 127

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c|| c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_HH_127_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_HH_127_exp.keys()[ rank_HH_127_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaHH_127[ str(p) ])*(lumi2016) + float(effSigmaHH_127_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_HH_127_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_HH_127_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiHH(127): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_hh127}"
print "\\end{table*}"
print " "


#HH 275

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c|| c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_HH_275_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_HH_275_exp.keys()[ rank_HH_275_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
#  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaHH_275[ str(p) ])*(lumi2016) + float(effSigmaHH_275_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_HH_275_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_HH_275_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiHH(275): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_hh275}"
print "\\end{table*}"
print " "





# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "\\begin{table*}[htb]"
# line="\\begin{tabular}{ c | c | c | c  || c| c}"
# print line
# #print "[\\cmsTabSkip]"
# print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
# print "[\\cmsTabSkip]"

# countToTen=0
# for lim in sorted_rank_WH_175_1_exp:
#   countToTen=countToTen+1
#   if( countToTen > 10):
#     continue
#   p= rank_WH_175_1_exp.keys()[ rank_WH_175_1_exp.values().index(lim)]
#   n = _tags.index(p)
#   line= names[ n ] 
#   line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
#   line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
#   line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
#   #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
#   line= line + " & " + str('%.1f' %(float(effSigmaWH_175_1[ str(p) ])*(lumi2016) + float(effSigmaWH_175_1_2017[ str(p) ])*(lumi2017)) )
#   line = line +  " & " + str('%.1f' %(float( rank_WH_175_1_exp[ str(p) ]) ))
#   line = line +  " & " + str('%.1f' %(float( rank_WH_175_1_obs[ str(p) ]) ))  + " \\\\"
#   print line

# print "\\end{tabular}"
# print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiWH(175,1): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
# print "\\label{tab:ranking_wh175_49}"
# print "\\end{table*}"
# print " "


print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  || c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_WH_225_50_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_WH_225_50_exp.keys()[ rank_WH_225_50_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaWH_225_50[ str(p) ])*(lumi2016) + float(effSigmaWH_225_50_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_WH_225_50_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_WH_225_50_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiWH(200,1): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_wh225_50}"
print "\\end{table*}"
print " "











print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  || c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_WH_200_1_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_WH_200_1_exp.keys()[ rank_WH_200_1_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaWH_200_1[ str(p) ])*(lumi2016) + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017)) )
  line = line +  " & " + str('%.1f' %(float( rank_WH_200_1_exp[ str(p) ]) ))
  line = line +  " & " + str('%.1f' %(float( rank_WH_200_1_obs[ str(p) ]) ))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for TChiWH(200,1): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_wh200_1}"
print "\\end{table*}"
print " "





print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  || c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"

countToTen=0
for lim in sorted_rank_T2bH_450_1_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_T2bH_450_1_exp.keys()[ rank_T2bH_450_1_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) *xsec_EW_450 + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017) *xsec_EW_450) )
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_450_1_exp[ str(p) ]) /xsec_EW_450 ))
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_450_1_obs[ str(p) ])  /xsec_EW_450))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for T2bH(450,1): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_t2bh450_1}"
print "\\end{table*}"
print " "



print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c| |c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"


countToTen=0
for lim in sorted_rank_T2bH_450_300_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_T2bH_450_300_exp.keys()[ rank_T2bH_450_300_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016) *xsec_EW_450 + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017) *xsec_EW_450) )
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_450_300_exp[ str(p) ]) /xsec_EW_450 ))
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_450_300_obs[ str(p) ])  /xsec_EW_450))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for T2bH(450,300): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_t2bh450_300}"
print "\\end{table*}"
print " "



print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "\\begin{table*}[htb]"
line="\\begin{tabular}{ c | c | c | c  | c| |c| c}"
print line
#print "[\\cmsTabSkip]"
print "Category & Data & Data Fit & SM Higgs & Sig & exp & obs \\\\ "
print "[\\cmsTabSkip]"


countToTen=0
for lim in sorted_rank_T2bH_600_1_exp:
  countToTen=countToTen+1
  if( countToTen > 10):
    continue
  p= rank_T2bH_600_1_exp.keys()[ rank_T2bH_600_1_exp.values().index(lim)]
  n = _tags.index(p)
  line= names[ n ] 
  line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
  line= line + " & " + str('%.1f' %( (float(glugluYield[ str(p) ]) + float(ttHYield[ str(p) ]) + float(VBFYield[ str(p) ]) + float(VHYield[ str(p) ]) + float(bbHYield[ str(p) ]) )   ) )  
  #  line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
  line= line + " & " + str('%.1f' %(float(effSigmaT2bH_600_1[ str(p) ])*(lumi2016) *xsec_EW_600 + float(effSigmaT2bH_600_1_2017[ str(p) ])*(lumi2017) *xsec_EW_600) )
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_600_1_exp[ str(p) ]) /xsec_EW_600 ))
  line = line +  " & " + str('%.1f' %(float( rank_T2bH_600_1_obs[ str(p) ])  /xsec_EW_600))  + " \\\\"
  print line

print "\\end{tabular}"
print "\\caption{The ten regions leading by expected upper limit on the signal strength for T2bH(600,1): Expected non-resonant and resonant background,and expected signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up per region and their corresponding expected and observed upper limit on the signal strenght.}"
print "\\label{tab:ranking_t2bh600_1}"
print "\\end{table*}"
print " "


 



# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "\\begin{table*}[htb]"
# line="\\begin{tabular}{c|c|c|c|c|c|c}"
# print line
# #print "[\\cmsTabSkip]"
# print "Category & Data (122-129) & Data Fit (122-129) & SM Higgs & HZ & HH & WH 200,1    \\\\ "
# #print "Category & Data (122-129) & SM Higgs & HZ & HH & WH 150 1  & WH 150 24   \\\\ "
# print "[\\cmsTabSkip]"

# for n,p in enumerate(_tags):
# #for p in _tags:
# #  line= str('%s' %(p.replace("_","\_") ) )  
#   line= names[ n ]
# #  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])))
#   line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
# #  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
#   line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
#   line= line + " & " + str('%.1f' %(float(effSigmaHZ_127[ str(p) ])*(lumi2016)          + float(effSigmaHZ_127_2017[ str(p) ])*(lumi2017)  ) )  
#   line= line + " & " + str('%.1f' %(float(effSigmaHH_127[ str(p) ])*(lumi2016)        + float(effSigmaHH_127_2017[ str(p) ])*(lumi2017)  ) )  
#   line= line + " & " + str('%.1f' %(float(effSigmaWH_200_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_200_1_2017[ str(p) ])*(lumi2017)) ) + " \\\\"
#   # line= line + " & " + str('%.1f' %(float(effSigmaWH_150_1[ str(p) ])*(lumi2016)  + float(effSigmaWH_150_1_2017[ str(p) ])*(lumi2017)) ) 
#   # line= line + " & " + str('%.1f' %(float(effSigmaWH_150_24[ str(p) ])*(lumi2016) + float(effSigmaWH_150_24_2017[ str(p) ])*(lumi2017)) )  + " \\\\"

#   if( n==0 or n==6 or n==12 or n==18 or n==24  or n==27  or n==45):
#     line = line + "  [\\cmsTabSkip]"

#   print line

# #print "[\\cmsTabSkip]"
# print "\\end{tabular}"
# print "\\caption{Expected background and EW signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up.}"
# print "\\label{tab:res_ew}"
# print "\\end{table*}"
# print " "





# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
# print "\\begin{table*}[htb]"
# line="\\begin{tabular}{ c | c | c | c  | c| c}"
# print line
# #print "[\\cmsTabSkip]"
# print "Category & Data & Data Fit & SM Higgs & T2bH 450,300 & T2bH 600,1  \\\\ "
# print "[\\cmsTabSkip]"


# for n,p in enumerate(_tags):
#   line=  names[ n ] 
# #  line= str('%s' %(p.replace("_","\_") ) )  
#   line= line + " & " + str('%.0f' %(float(dataYield[ str(p) ])) ) 
# #  line= line + " & " + str('%.1f' %(float(bkgYield[ str(p) ])*(129.-122)))
#   line= line + " & " + str('%.1f' %(float(effSigmaSM[ str(p) ])*(lumi2016)        + float(effSigmaSM_2017[ str(p) ])*(lumi2017)  ) )  
#   line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_300[ str(p) ])*(lumi2016)  + float(effSigmaT2bH_450_300_2017[ str(p) ])*(lumi2017)) ) 
#   line= line + " & " + str('%.1f' %(float(effSigmaT2bH_450_1[ str(p) ])*(lumi2016) + float(effSigmaT2bH_450_1_2017[ str(p) ])*(lumi2017)) )  + " \\\\"

#   if( n==0 or n==6 or n==12 or n==18 or n==24  or n==27  or n==45):
#     line = line + "  [\\cmsTabSkip]"

# #  if( n==0 or n==4 or n==12 or n==14  or n==26):
# #    line = line + "  [\\cmsTabSkip]"

#   print line
  

# #print "[\\cmsTabSkip]"
# print "\\end{tabular}"
# print "\\caption{Expected background and strongly produced signal yields in the di-photon invariant mass range 122-129 for 2016 and 2017 summed up.}"
# print "\\label{tab:res_t2bh}"
# print "\\end{table*}"
# print " "








