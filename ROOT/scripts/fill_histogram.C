{

    // Read the input file
    TFile f(tree.root);

    // Make the output file to save the histogram
    TFile fout(out.root, "recreate");

    // Define the histogram
    TH1F h1("h1", "Jet pT (GeV/c)", 50, 0, 150);

    // Get the tree
    TTree *input_file = (TTree*)f.Get("t1");

    // Define the variables
    Float_t met; // Missing transverse energy
    Int_t njets; // Number of jets

    // Set the branch address
    // The branch address is set to the variable
    Float_t pt[16]; // Jet pT
    Float_t eta[16]; // Jet eta
    Float_t phi[16]; // Jet phi

    // Assign the branch address
    input_file->SetBranchAddress("met", &met);
    input_file->SetBranchAddress("njets", &njets);
    input_file->SetBranchAddress("pt", pt);
    input_file->SetBranchAddress("eta", eta);
    input_file->SetBranchAddress("phi", phi);

    // Get the total number of events
    Int_t n_events = input_file->GetEntries();

    // Loop over the events
    for (Int_t i=0; i<n_events; i++) {

        // Get i'th event and fill the variables
        input_file->GetEntry(i);

        // Print the number of jets in each event
        printf("%d\n", njets);

        // Print momentum and other quantites for each jet
        for (Int_t j=0; j<njets; j++) {
            printf("%d %f %f %f\n", j, pt[j], eta[j], phi[j]);
        // Fill the histogram
        h1.Fill(pt[j]);
        }
    }

    // lets work with TCanvas
    // Create a canvas with following arguments
    // name, title, width, height
    TCanvas *c1 = new TCanvas("c1", "Jet pT", 800, 600);

    c1->cd();
    h1.Draw();
    c1->SaveAs("jet_pt.png");

    fout->cd();
    h1.Write();
    fout->Close();

}



