import os

from sift import SIFT
from tqdm import tqdm

dataDir = '../data'
train_fldr = 'train_imgs1'

imgNames = os.listdir('{}/{}'.format(dataDir, train_fldr))

sift = SIFT(alphaMin = 0.2, alphaMax = 0.45)
saveFile = open('../data/results.csv', 'w')

for name in tqdm(imgNames):
    matchPoints = sift.getPoints('{}/{}/{}'.format(dataDir, train_fldr, name),
                                 '{}/templates'.format(dataDir), writeImg=True,
                                 writeDir='../data/results/')
    saveFile.write(str(name) + ',' + str(matchPoints) + '\n')

saveFile.close()