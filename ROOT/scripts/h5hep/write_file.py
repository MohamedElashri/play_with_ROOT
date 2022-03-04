import numpy as np
import sys
from numpy.random import beta
import h5hep as h5
import ROOT 
def calc_energy(m,px,py,pz):
    return np.sqrt(m**2+px**2+py**2+pz**2)

##############################################################################

data = h5.initialize()

h5.create_group(data,'jet',counter='njet')
h5.create_dataset(data,['e','px','py','pz','btag'],group='jet',dtype=float)

h5.create_group(data,'muon',counter='nmuon')
h5.create_dataset(data,['e','px','py','pz','q'],group='muon',dtype=float)

h5.create_group(data,'electron',counter='nelectron')
h5.create_dataset(data,['e','px','py','pz','q'],group='electron',dtype=float)

h5.create_group(data,'photon',counter='nphoton')
h5.create_dataset(data,['e','px','py','pz'],group='photon',dtype=float)

h5.create_group(data,'met',counter='nmet')
h5.create_dataset(data,['pt','phi'],group='MET',dtype=float)

event = h5.create_single_event(data)

n_events = 1000
if len(sys.argv) > 1:
    n_events = int(sys.argv[1])

tag = None
if len(sys.argv) > 2:
    tag = sys.argv[2]

for i in range(0,n_events):
    if i%1000 == 0:
        print(i)
    h5.clear_event(event)

    njet = np.random.randint(16)
    event['jet/njet'] = njet
    for n in range(njet):
        px = 300*beta(2,9)
        py = 300*beta(2,9)
        pz = 300*beta(2,9)
        m  =  5*beta(2,9)
        energy = calc_energy(m,px,py,pz)
        event['jet/e'].append(energy)
        event['jet/px'].append(px)
        event['jet/py'].append(py)
        event['jet/pz'].append(pz)
      
    nmuon = np.random.randint(16)
    event['muon/nmuon'] = nmuon
    for n in range(nmuon):
        px = 300*beta(2,9)
        py = 300*beta(2,9)
        pz = 300*beta(2,9)
        m  =  0.105
        energy = calc_energy(m,px,py,pz)
        event['muon/e'].append(energy)
        event['muon/px'].append(px)
        event['muon/py'].append(py)
        event['muon/pz'].append(pz)
        event['muon/q'].append(2*np.random.randint(2)-1)
      
    nelectron = np.random.randint(16)
    event['electron/nelectron'] = nelectron
    for n in range(nelectron):
        px = 300*beta(2,9)
        py = 300*beta(2,9)  
        pz = 300*beta(2,9)
        m  =  0.000511
        energy = calc_energy(m,px,py,pz)
        event['electron/e'].append(energy)
        event['electron/px'].append(px)
        event['electron/py'].append(py)
        event['electron/pz'].append(pz)
        event['electron/q'].append(2*np.random.randint(2)-1)
    
    nphoton = np.random.randint(16)
    event['photon/nphoton'] = nphoton
    for n in range(nphoton):
        px = 300*beta(2,9)
        py = 300*beta(2,9)
        pz = 300*beta(2,9)
        m  =  0.0
        energy = calc_energy(m,px,py,pz)
        event['photon/e'].append(energy)
        event['photon/px'].append(px)
        event['photon/py'].append(py)
        event['photon/pz'].append(pz)
    
    h5.pack(data,event) 

name = 'HEP_file_n_%d.hdf5' % (n_events)
if tag is not None:
    name = 'HEP_file_tag%s_n%d.hdf5' % (tag,n_events)
print('Writing the file ...%s' % (name))
hdfile = h5.write_to_file(name,data,comp_type='gzip',comp_opts=9)




