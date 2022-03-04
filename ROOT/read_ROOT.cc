// Standard library
#include<cstdio>
#include<cstring>
#include<iostream>

// ROOT
#include<TFile.h>
#include<TTree.h>
#include<TROOT.h>
#include<TRandom.h>

int main() {

    // Read the input ROOT file
    TFile f("tree.root");

    // We will read the tree from the file
    // and store a new local variable
    TTree* input_tree = (TTree*)f.Get("t1");

    Float_t met; // Define the Missing energy in trasverse direction
    Int_t n_jets; // Define the number of jets

    // Set the branch address for the variables - assume we have 
    // a maximum of 16 jets
    Float_t jet_pt[16];
    Float_t jet_eta[16];
    Float_t jet_phi[16];

    // Assign variables to specific branch addresses
    input_tree->SetBranchAddress("met", &met);
    input_tree->SetBranchAddress("n_jets", &n_jets);
    input_tree->SetBranchAddress("jet_pt", jet_pt);
    input_tree->SetBranchAddress("jet_eta", jet_eta);
    input_tree->SetBranchAddress("jet_phi", jet_phi);

    // Lets get the number of entries in the file
    Int_t n_events = input_tree->GetEntries();

    // Loop over the events
    for (Int_t i=0;i<n_events;i++) {

        // Get value of i'th event and fill our local variables assigen 
        // to the branch addresses
        input_tree->GetEntry(i);

        // Print the number of jets in the event
        printf("Event %d has %d jets\n",i ,n_jets);

        // Print the momentum of each jet in the event
        for (Int_t j=0;j<n_jets;j++) {
            printf("Jet %d has momentum %f and eta %f and phi %f\n", j, jet_pt[j], jet_eta[j], jet_phi[j]);
        }
    }

    return 0;
}
