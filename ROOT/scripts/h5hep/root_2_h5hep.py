import sys
import numpy as np
import ROOT

filename = sys.argv[1]
file = ROOT.TFile(filename)

tree = file.Get("T")
branch_names = []
branch_list = tree.GetListOfBranches();
n_branches = branch_list.GetEntries();

for i in range(0,n_branches):
    branch_name = branch_list[i].GetName()
    branch_type = branch_list[i].GetLeaf(branch_name).GetTypeName()
    branch_names.append((branch_name,branch_type))

print(branch_names)
