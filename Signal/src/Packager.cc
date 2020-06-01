#include "TCanvas.h"
#include "TGraph.h"

#include "RooAddition.h"
#include "RooAddPdf.h"
#include "RooDataSet.h"
#include "RooExtendPdf.h"
#include "RooArgList.h"
#include "RooRealVar.h"
#include "RooPlot.h"
#include "HiggsAnalysis/CombinedLimit/interface/RooSpline1D.h"

#include "../interface/Packager.h"

#include <algorithm>

using namespace std;
using namespace RooFit;

Packager::Packager(WSTFileWrapper *ws, RooWorkspace *wsSave  , vector<string> procs, int nCats, int mhLow, int mhHigh, vector<int> skipMasses, int sqrts, bool skipPlots, string outDir, 
		   RooWorkspace *wsMerge, const vector<int>& cats, const vector<string>& flashggCats):
  WS(ws),
  mergeWS(wsMerge),
  saveWS(wsSave),
  procs_(procs),
  nCats_(nCats),
  cats_(cats),
  flashggCats_(flashggCats),
  mhLow_(mhLow),
  mhHigh_(mhHigh),
  skipPlots_(skipPlots),
  outDir_(outDir),
  sqrts_(sqrts),
  skipMasses_(skipMasses)
{
  normalization = new Normalization_8TeV();
  normalization->Init(sqrts_);
}

Packager::~Packager(){}

bool Packager::skipMass(int mh){
  for (vector<int>::iterator it=skipMasses_.begin(); it!=skipMasses_.end(); it++) {
    if (*it==mh) return true;
  }
  return false;
}

void Packager::packageOutput(bool split, string process , string tag){

  std::cout << "Print the saveWS" << std::endl;
  //  saveWS->Print();

  vector<string> expectedObjectsNotFound;
  bool split_=split;
  // sum datasets first
  for (int mh=mhLow_; mh<=mhHigh_; mh+=5){
    if (skipMass(mh)) continue;
    RooDataSet *allDataThisMass = 0;
    for (int cat=0; cat<nCats_; cat++) {
      string catname;
      if (sqrts_==8 || sqrts_==7) catname=Form("cat%d",cat);
      if (sqrts_ ==13) catname = Form("%s",flashggCats_[cat].c_str());
      RooDataSet *allDataThisCat = 0;

      RooDataSet *allDataThisCat_higgs = 0;
      RooDataSet *allDataThisCat_sig = 0;
      //      RooDataSet *allDataThisCat = NULL;
      bool merge = mergeWS != 0 && ( find(cats_.begin(),cats_.end(),cat) == cats_.end() );
      for (vector<string>::iterator proc=procs_.begin(); proc!=procs_.end(); proc++){
  	RooDataSet *tempData = 0;

  	if( merge ) { 
	  //  	  std::cout << "DO MERGE" << std::endl;
  	  tempData = (RooDataSet*)mergeWS->data(Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()));
  	  if(tempData && !saveWS->data(Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()))) 
  	    saveWS->import(*tempData); //FIXME
  	} else {
	  //	  std::cout << "DO NOT MERGE" << std::endl;
  	  tempData = (RooDataSet*)WS->data(Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()));
	  //  	  std::cout << "IS temp data " << tempData << std::endl;
	  //  	  std::cout << "IS saved yet " << Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()) << std::endl;

  	  if(tempData && !saveWS->data(Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()) ) ) {
	    //  	    std::cout << "IMPORTING " << Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()) << std::endl;
  	    saveWS->import(*tempData); //FIXME 

	    //	    tempData->Print();

  	  }
  	}

  	if (!tempData) {
	  //  	  std::cout << "not tempData" << std::endl;

  	  if (!split_)	
  	    cerr << "[WARNING] -- dataset: " << Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()) << " not found. It will be skipped (ignore this warning if just running one tag/proc)" << endl;
  	  expectedObjectsNotFound.push_back(Form("sig_%s_mass_m%d_%s",proc->c_str(),mh,catname.c_str()));
  	  continue;
  	}

  	if (!split_){
	  //  	  std::cout << "not Split" << std::endl;
  	  if ( cat==0 && proc==procs_.begin()) {
	    //	    std::cout << "not Split 0" << std::endl;
  	    allDataThisMass = (RooDataSet*)tempData->Clone(Form("sig_mass_m%d_AllCats",mh));
	    //	    std::cout << " " << std::endl;
	    //	    allDataThisMass->Print();
  	  } else {
	    //	    std::cout << "not Split 2" << std::endl;
  	    allDataThisMass->append(*tempData);
	    //	    std::cout << " " << std::endl;
	    //	    allDataThisMass->Print();
	  }
	}

	//to determine if we put it in the sum off SM-Higgs or Signal 
	std::string tempStrg = proc->c_str();

	//	std::cout << "done not split " << std::endl;
	if (proc==procs_.begin()){
	  allDataThisCat = (RooDataSet*)tempData->Clone(Form("sig_mass_m%d_%s",mh,catname.c_str()));


	  if( tempStrg.find("higgs") != std::string::npos )
	    allDataThisCat_higgs = (RooDataSet*)tempData->Clone(Form("higgs_mass_m%d_%s",mh,catname.c_str()));

	  if( tempStrg.find("SMS_T") != std::string::npos )
	    allDataThisCat_sig = (RooDataSet*)tempData->Clone(Form("signal_mass_m%d_%s",mh,catname.c_str()));

	  //	  std::cout << " added 0th" << std::endl;
	  //	  allDataThisCat->Print();
	}


	if (!allDataThisCat){ 
          allDataThisCat = (RooDataSet*)tempData->Clone(Form("sig_mass_m%d_%s",mh,catname.c_str()));
	}
	else if(proc!=procs_.begin())
	  allDataThisCat->append(*tempData);

	if (!allDataThisCat_higgs){ 
	  if( tempStrg.find("higgs") != std::string::npos )
          allDataThisCat_higgs = (RooDataSet*)tempData->Clone(Form("higgs_mass_m%d_%s",mh,catname.c_str()));
	}
	else if(proc!=procs_.begin())
	  if( tempStrg.find("higgs") != std::string::npos )
	    allDataThisCat_higgs->append(*tempData);

	if (!allDataThisCat_sig){ 
	  if( tempStrg.find("SMS_T") != std::string::npos )
          allDataThisCat_sig = (RooDataSet*)tempData->Clone(Form("signal_mass_m%d_%s",mh,catname.c_str()));
	}
	else if(proc!=procs_.begin())
	  if( tempStrg.find("SMS_T") != std::string::npos )
	    allDataThisCat_sig->append(*tempData);


	//	std::cout << "  otherwise appended it " << std::endl;
	//	allDataThisCat->Print();
	//	std::cout << "is it allDataThisCat???2" << std::endl;

      }//end loop over procs

      if (!allDataThisCat) {

	//       	std::cout << "is it allDataThisCat???3" << std::endl;

       	if (!split_)	cerr << "[WARNING] -- allData for cat " << catname.c_str() << " is NULL. Probably because the relevant datasets couldn't be found. Skipping.. (ignore this warning if just running one tag/proc)" << endl;
       	continue;
      }

      //      std::cout << "is it allDataThisCat???4" << std::endl;
      saveWS->import(*allDataThisCat);

      if (allDataThisCat_higgs)
	saveWS->import(*allDataThisCat_higgs);
      if (allDataThisCat_sig)
	saveWS->import(*allDataThisCat_sig);
      //      std::cout << "is it allDataThisCat???5" << std::endl;

    }

    if (!allDataThisMass) {

      //      std::cout << "is it allDataThisMass???" << std::endl;

      if (!split_)	cerr << "[WARNING] -- allData for mass " << mh << " is NULL. Probably because the relevant datasets couldn't be found. Skipping.. (ignore this warning if just running one tag/proc)" << endl;
      continue;
    }
    saveWS->import(*allDataThisMass);

  }
  //  std::cout << "Ok got some stuff now again get the stuff in the stuff" << std::endl;


  RooRealVar *MH = (RooRealVar*)WS->var("MH");
  // now create pdf sums (these don't the relative amounts as just used for plotting so can use ThisLum versions)
  RooArgList *sumPdfs = new RooArgList();
  RooArgList *runningNormSum = new RooArgList();
  double runningNormSumVal=0;
  for (int cat=0; cat<nCats_; cat++){
    RooRealVar *intLumi = (RooRealVar*)WS->var("IntLumi");
    string catname;
    if (sqrts_ == 13) catname=Form("%s",flashggCats_[cat].c_str());
    else if (sqrts_==7 || sqrts_==8) catname=Form("cat%d",cat);
    bool merge = mergeWS != 0 && ( find(cats_.begin(),cats_.end(),cat) == cats_.end() );
    //RooWorkspace * inWS = ( merge ? mergeWS : WS );
    if (merge){
      std::cout << "[ERROR] -  sorry, 'merge' functionailty is disabled in this release because of incompatibility between RooWorkspace and WSTFileWrapper. Exiting"<< std::cout ;
      exit(1);
    }
    RooArgList *sumPdfsThisCat = new RooArgList();
    for (vector<string>::iterator proc=procs_.begin(); proc!=procs_.end(); proc++){

      // sum eA
      //WS->Print();
      RooSpline1D *norm = (RooSpline1D*)/*in*/WS->function(Form("hggpdfsmrel_%dTeV_%s_%s_norm",sqrts_,proc->c_str(),catname.c_str()));

      if (!norm) {
	cerr << "[WARNING] -- ea: " << Form("hggpdfsmrel_%dTeV_%s_%s_norm",sqrts_,proc->c_str(),catname.c_str()) << " not found. It will be skipped (ignore this warning if just running one tag/proc)" << endl;
      }

      if (!norm) {
	if (!split_)	cerr << "[WARNING] -- ea: " << Form("hggpdfsmrel_%dTeV_%s_%s_norm",sqrts_,proc->c_str(),catname.c_str()) << " not found. It will be skipped (ignore this warning if just running one tag/proc)" << endl;
      }
      else {
        for (int m =120; m<131; m=m+5){
	  MH->setVal(m);norm->getVal(); 
        }
	//	runningNormSum->add(*norm);
	//        runningNormSumVal+= norm->getVal();
	//	std::cout << "[INFO] runningNormSum: adding "<< norm->getVal() << ", total " << runningNormSumVal << std::endl;
        //runningNormSum->Print();
      }

      // sum pdf
      RooExtendPdf *tempPdf = (RooExtendPdf*)/*in*/WS->pdf(Form("extendhggpdfsmrel_%dTeV_%s_%sThisLumi",sqrts_,proc->c_str(),catname.c_str()));
      if (!tempPdf) {
	if (!split_)	cerr << "[WARNING] -- pdf: " << Form("extendhggpdfsmrel_%dTeV_%s_%s",sqrts_,proc->c_str(),catname.c_str()) << " not found. It will be skipped (ignore this warning if just running one tag/proc)" << endl;
	expectedObjectsNotFound.push_back(Form("extendhggpdfsmrel_%dTeV_%s_%s",sqrts_,proc->c_str(),catname.c_str()));
	continue;
      }

      //saveWS->import(*norm); //FIXME
      saveWS->import(*tempPdf,RecycleConflictNodes()); //FIXME

      if( merge ) {
	saveWS->import(*norm); //FIXME
	saveWS->import(*tempPdf,RecycleConflictNodes()); //FIXME
      }
      sumPdfsThisCat->add(*tempPdf);
      sumPdfs->add(*tempPdf);
    }
    if (sumPdfsThisCat->getSize()==0){
      if (!split_)	cerr << "[WARNING] -- sumPdfs for cat " << catname.c_str() << " is EMPTY. Probably because the relevant pdfs couldn't be found. Skipping.. (ignore this warning if just running one tag/proc) " << endl;
      continue;
    }
    // Dont put sqrts here as combine never uses this (but our plotting scripts do)
    RooAddPdf *sumPdfsPerCat = new RooAddPdf(Form("sigpdfrel%s_allProcs",catname.c_str()),Form("sigpdfrel%s_allProcs",catname.c_str()),*sumPdfsThisCat);
    saveWS->import(*sumPdfsPerCat,RecycleConflictNodes());

  }

  if (sumPdfs->getSize()==0){
    if (!split_) cerr << "[WARNING] -- sumAllPdfs is EMPTY. Probably because the relevant pdfs couldn't be found. Skipping.. (ignore this warning if just running one tag/proc) " << endl;
  }
  else {
    // Dont put sqrts here as combine never uses this (but our plotting scripts do)
    RooAddPdf *sumPdfsAllCats = new RooAddPdf("sigpdfrelAllCats_allProcs","sigpdfrelAllCats_allProcs",*sumPdfs);
    saveWS->import(*sumPdfsAllCats,RecycleConflictNodes());
  }

  if (runningNormSum->getSize()==0){
    cerr << "[WARNING] -- runningNormSum is EMPTY. Probably because the relevant normalizations couldn't be found. Skipping.. (ignore this warning if just running one tag/proc) " << endl;
  }	else {
    {
      RooAddition *normSum = new RooAddition("normSumTotal","normSumTotal",*runningNormSum);
      saveWS->import(*normSum); //FIXME
    }

    if (!skipPlots_) {
      RooRealVar *MH = (RooRealVar*)WS->var("MH");
      RooRealVar *intLumi = (RooRealVar*)WS->var("IntLumi");
      RooAddition *norm = (RooAddition*)WS->function("normSumTotal");

      if (MH) saveWS->import(*MH);
      if(intLumi) saveWS->import(*intLumi);
      if (norm) saveWS->import(*norm);
      TGraph *effAccGraph = new TGraph();
      TGraph *expEventsGraph = new TGraph();
      int p=0;
      for (double mh=mhLow_; mh<mhHigh_+0.5; mh+=1){
	double intLumiVal = 0.;
	if (intLumi){
	  intLumiVal = intLumi->getVal();//FIXME
	  //std::cout << "[INFO] (packager) intlumi value is " << intLumiVal << std::endl;
	} else {
	  std::cout  << "[ERROR] IntLumi missing from workspace, exit "<< std::endl;
	  //intLumiVal = 1000;
	  return ;
	}
	MH->setVal(mh);
	float XS_value = 0;
	if (split_){//fixme
	  XS_value=normalization->GetXsection(125,process); // in this case get proc-specific eff*acc
	  //	  XS_value=normalization->GetXsection(mh,process); // in this case get proc-specific eff*acc
	} else {//fixme
	  XS_value=normalization->GetXsection(125); // or else, get the one for all processes!
	  //	  XS_value=normalization->GetXsection(mh); // or else, get the one for all processes!
	}

	//	expEventsGraph->SetPoint(p,mh,intLumiVal*normSum->getVal());
	//	effAccGraph->SetPoint(p,mh,normSum->getVal()/(XS_value*normalization->GetBR(125))); //fixme
	//	effAccGraph->SetPoint(p,mh,normSum->getVal()/(XS_value*normalization->GetBR(mh)));
	//std::cout << " [INFO] (Packager) expected events  " << intLumiVal*normSum->getVal() << std::endl;
	//std::cout << " [INFO] (Packager) eff*acc " << normSum->getVal()/(XS_value*normalization->GetBR(mh)) << std::endl;
	//std::cout << " [INFO] (Packager) eff*acc for " << mh << " (where normSum  " << normSum->getVal() << " (XS_value " << XS_value << " normalization->GetBR(mh)) " << normalization->GetBR(mh) << std::endl;

	// if (normSum->getVal()/(XS_value*normalization->GetBR(mh)) <0){
	//   std::cout << "ERROR eff*acc < 0 !!! exit!" << std::endl;
	//   exit(1);
	// }

	//expEventsGraph->SetPoint(p,mh,intLumiVal*norm->getVal());
	//effAccGraph->SetPoint(p,mh,norm->getVal()/(XS_value*normalization->GetBR(mh)));
	//std::cout << " [INFO] eff*acc " << norm->getVal()/(XS_value*normalization->GetBR(mh)) << std::endl;
	p++;
      } 
      string extension="";
      if (split_){
	extension=Form("_%s_%s",process.c_str(),tag.c_str());
      } else {
	extension=Form("_all");
      }
      TCanvas *canv = new TCanvas();
      effAccGraph->SetLineWidth(3);
      effAccGraph->SetName("effAccGraph");
      effAccGraph->GetXaxis()->SetTitle("m_{H} (GeV)");
      effAccGraph->GetYaxis()->SetTitle("efficiency #times acceptance");
      effAccGraph->Draw("AL");
      canv->Print(Form("%s/effAccCheck%s.pdf",outDir_.c_str(),extension.c_str()));
      canv->Print(Form("%s/effAccCheck%s.png",outDir_.c_str(),extension.c_str()));
      effAccGraph->SaveAs(Form("%s/effAccCheck%s.root",outDir_.c_str(),extension.c_str()));
      expEventsGraph->SetLineWidth(3);
      expEventsGraph->GetXaxis()->SetTitle("m_{H} (GeV)");
      double intLumiVal = 1000;
      if (intLumi){
	intLumiVal = intLumi->getVal();
	std::cout << "[INFO] intlumi value is " << intLumiVal << std::endl;
      } else {
	std::cout  << "[ERROR] could not find IntLumi var. Exit "<< std::endl;
	return ;
      }
      
      // expEventsGraph->GetYaxis()->SetTitle(Form("Expected Events for %4.1ffb^{-1}",intLumiVal/1000.));
      // expEventsGraph->Draw("AL");
      // canv->Print(Form("%s/expEventsCheck%s.pdf",outDir_.c_str(),extension.c_str()));
      // canv->Print(Form("%s/expEventsCheck%s.png",outDir_.c_str(),extension.c_str()));
      // //      makePlots();

    }
  }
}


// void Packager::makePlots(){
//   RooRealVar *mass = (RooRealVar*)saveWS->var("h_mass");
//   //  RooRealVar *mass = (RooRealVar*)saveWS->var("CMS_hgg_mass");
//   RooRealVar *MH = (RooRealVar*)saveWS->var("MH");
//   //  RooAddPdf *sumPdfsAllCats = (RooAddPdf*)saveWS->pdf("sigpdfrelAllCats_allProcs");
//   map<int,RooDataSet*> dataSets;
//   for (int m=mhLow_; m<=mhHigh_; m+=5){
//     if (skipMass(m)) continue;
//     //    RooDataSet *data = (RooDataSet*)saveWS->data(Form("sig_mass_m%d_AllCats",m));
//     //    if (data) {
//     //  dataSets.insert(make_pair(m,data));
//       //data->Print();
//     // } else {
//     //   //      std::cout << "[WARNING] could not get dataset " << Form("sig_mass_m%d_AllCats",m) <<" (ignore this warning if just running one tag/proc)"<<   std::endl;
//     // }

//   }

//   // if (sumPdfsAllCats){
//   //   makePlot(mass,MH,sumPdfsAllCats,dataSets,"all");
//   // } else {
//   //   std::cout << "[WARNING] sumPdfsAllCats missing or not generated, skipping it " <<std::endl;
//   // }

//   for (int cat=0; cat<nCats_; cat++){
//     string catname;
//     if (sqrts_ == 13) catname=Form("%s",flashggCats_[cat].c_str());
//     else if (sqrts_==7 || sqrts_==8) catname=Form("cat%d",cat);
//     //    RooAddPdf *sumPdfsCat = (RooAddPdf*)saveWS->pdf(Form("sigpdfrel%s_allProcs",catname.c_str()));

//     map<int,RooDataSet*> dataSetsCat;
//     for (int m=mhLow_; m<=mhHigh_; m+=5){
//       if (skipMass(m)) continue;
//       RooDataSet *data = (RooDataSet*)saveWS->data(Form("sig_mass_m%d_%s",m,catname.c_str()));
//       if (data) {
// 	dataSetsCat.insert(make_pair(m,data));
//       }
//     }
//     if (sumPdfsCat){
//       // makePlot(mass,MH,sumPdfsCat,dataSetsCat,Form("%s",catname.c_str()));
//     } else {
//       std::cout << "[WARNING] sumPdfsCat missing or not generated, skipping it " <<std::endl;
//     }
//   }
// }

// void Packager::makePlot(RooRealVar *mass, RooRealVar *MH, RooAddPdf *pdf, map<int,RooDataSet*> data, string name){

//   TCanvas *canv = new TCanvas();
//   RooPlot *dataPlot = mass->frame(Title(name.c_str()),Range(110,140));
//   for (map<int,RooDataSet*>::iterator it=data.begin(); it!=data.end(); it++){
//     int mh = it->first;
//     RooDataSet *dset = it->second;
//     dset->plotOn(dataPlot,Binning(320));
//     MH->setVal(mh);
//     pdf->plotOn(dataPlot);
//   }
//   dataPlot->Draw();
//   canv->Print(Form("%s/%s_fits.pdf",outDir_.c_str(),name.c_str()));
//   canv->Print(Form("%s/%s_fits.png",outDir_.c_str(),name.c_str()));

//   RooPlot *pdfPlot = mass->frame(Title(name.c_str()),Range(100,160));
//   pdfPlot->GetYaxis()->SetTitle(Form("Pdf projection / %2.1f GeV",(mass->getMax()-mass->getMin())/160.));
//   for (int mh=mhLow_; mh<=mhHigh_; mh++){
//     MH->setVal(mh);
//     // to get correct normlization need to manipulate with bins and range
//     pdf->plotOn(pdfPlot,Normalization(mass->getBins()/160.*(mass->getMax()-mass->getMin())/60.,RooAbsReal::RelativeExpected));
//   }
//   pdfPlot->Draw();
//   canv->Print(Form("%s/%s_interp.pdf",outDir_.c_str(),name.c_str()));
//   canv->Print(Form("%s/%s_interp.png",outDir_.c_str(),name.c_str()));
//   delete canv;
// }
 
