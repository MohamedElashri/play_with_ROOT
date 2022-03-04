// Standard Library:

#include <iostream>
#include <cstdio>
#include <cstdlib>

// ROOT Library:
#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TH1F.h>
#include <TRandom.h>

int main() {

    // Read the input file:
    TFile f("tree.root");

    // Make ouput file to save the histogram:
    TFile fout("hist.root","recreate");

    // We are going to make a histogram of the variable "pt"
    // which is the transverse momentum of the jets.
    TH1F h1("h1","jet pT (GeV/c)",50,0,150);
    // First argument is the name of the histogram,
    // second argument is the title of the histogram,
    // third argument is the number of bins,
    // fourth argument is the lower bound of the histogram,
    // fifth argument is the upper bound of the histogram.
    // The histogram will be saved in the file "hist.root".

    // Get the tree from the file:
    // We assume that the tree is named "t1"
    TTree *input_tree = (TTree*)f.Get("t1");

    // Define variables
    Float_t met; // Missing transverse energy
    Int_t njets; // Number of jets

    // Define jets quantities:
    Float_t pt[16]; // Transverse momentum of the jets
    Float_t eta[16]; // Pseudorapidity of the jets
    Float_t phi[16]; // Azimuthal angle of the jets

    // Set the branch address of the variables:
    input_tree->SetBranchAddress("met",&met);
    input_tree->SetBranchAddress("njets",&njets);
    input_tree->SetBranchAddress("pt",pt);
    input_tree->SetBranchAddress("eta",eta);
    input_tree->SetBranchAddress("phi",phi);

    // Get number of events in the file:
    Int_t n_events = input_tree->GetEntries();

    for (Int_t i=0;i<n_events;i++) {
        // Get the event:
        input_tree->GetEntry(i);

        // Print number of jets in the event:
        printf("Number of jets in the event: %d\n",njets);

        // Print the momentum of each jet in the event:
        for (Int_t j=0;j<njets;j++) {
            printf("Jet %d: pt = %f, eta = %f, phi = %f\n",j,pt[j],eta[j],phi[j]);
        

        
            // Fill the histogram:
            h1.Fill(pt[j]);
        }
    }
    
    fout.cd();
    h1.Write();
    fout.Close();

    return 0;
}
