import numpy as np
from hdf5_util import *

data = initilize_h5()

create_entry(data,'jets',dtype =float, index ='njet')
create_entry(data,'jetpx',dtype =float, index ='njet')
create_entry(data,'jetpy',dtype =float, index ='njet')
create_entry(data,'jetpz',dtype =float, index ='njet')
create_entry(data,'njet,dtype =int')

event = create_single_event(data)

for i in range(0,10000):

    clear_event(event)
    njet = 10
    event['njet'] = njet

    for n in range(njet):
        event['jets'].append(np.random.rand())
        event['jetpx'].append(np.random.rand())
        event['jetpy'].append(np.random.rand())
        event['jetpz'].append(np.random.rand())
    fill(data,event)

hdfile = write_to_file('out.hdf5',data)
