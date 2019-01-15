import os
import numpy as np
import pandas as pd

dataDir = '../data'
train_fldr = 'train_imgs1'

data = pd.read_excel('{}/{}.csv.xlsx'.format(dataDir, train_fldr))
data['FileName'] = [name.split('\\')[1] for name in data['FileName']]

imgNames, gcpString = [], []
imgNamesOS = os.listdir('{}/{}'.format(dataDir, train_fldr))

for name, loc in zip(data['FileName'], data['GCPLocation']):
    if name in imgNamesOS:
        imgNames.append(name)
        gcpString.append(loc)        

gcpString = [loc.split(',') for loc in gcpString]
gcpLoc = []

for loc in gcpString:
    temp = []
    for tup in zip(*[iter(loc)]*2):
        temp.append([np.int(np.float32(tup[0].strip(' [  ] '))), 
                     np.int(np.float32(tup[1].strip(' [  ] ')))])
    gcpLoc.append(temp)
