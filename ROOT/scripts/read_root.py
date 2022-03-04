import sys
import ROOT

chain = ROOT.TChain("T")
files = sys.argv[1:]

for file in files:
    print("Adding file:", file)
    chain.Add(file)

# Event loop
nev = chain.GetEntries()

energies = []

for n in range (nev):
    chain.GetEntry(n)
    
    if n % 100000 == 0:
        print("Processing event", n)

        '''
        print(tree.nmuon)

        for i in range(tree.nmuon):
            print(tree.muon_pt[i])
        '''

        energies += chain.jets

print(len(energies))


