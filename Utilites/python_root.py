import ROOT

file = "root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD2NanoAODOutreachTool/GluGluToHToTauTau.root"

f = ROOT.TFile.Open(file)

tree = f.Get("Events")

nevents = tree.GetEntries()

print("Number of events: ", nevents)

for i in range(nevents):
    tree.GetEntry(i)
    print(tree.run, tree.event)

    print(i)
