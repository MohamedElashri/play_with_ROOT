import sys
import ROOT

tdir = "root://eospublic.cern.ch//eos/opendata/cms/"

print("To list the contents of any subdirectories of\n")
print("{0}\n".format(tdir))
print("just add them to the commandline options.\n")
print("Example: ")
print("python ls_dir.py")
print("python ls_dir.py Run2011A")
print("python ls_dir.py Run2011A/SingleMu")
print("\n")

if len(sys.argv) > 1:
    tdir += sys.argv[1]
dir = ROOT.TSystemDirectory(tdir, tdir)

files = dir.GetListOfFiles()

print("List of files in {0}:\n".format(tdir))
for f in files:
    print(f.GetName())


