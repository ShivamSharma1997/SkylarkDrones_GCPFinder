import os
import cv2
import numpy as np
import pandas as pd

from sift import SIFT
from tqdm import tqdm

dataDir = '../data'
train1_fldr = 'train_imgs1'
train2_fldr = 'train_imgs2'
BnW_fldr1 = 'BnW_imgs1'
BnW_fldr2 = 'BnW_imgs2'
            
data = pd.read_excel('{}/{}.csv.xlsx'.format(dataDir, train1_fldr))
data['FileName'] = [name.split('\\')[1] for name in data['FileName']]

imgNames, gcpString = [], []
imgNamesOS = os.listdir('{}/{}'.format(dataDir, train2_fldr))

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

sift = SIFT(alphaMin = 0.2, alphaMax = 0.45)
res = []
saveFile = open('../data/results.csv', 'w')

for name in tqdm(imgNamesOS):
    matchPoints = sift.getPoints('{}/{}/{}'.format(dataDir, train2_fldr, name),
                                 '{}/templates'.format(dataDir), writeImg=True,
                                 writeDir='../data/results/')
    saveFile.write(str(name) + ',' + str(matchPoints) + '\n')

saveFile.close()