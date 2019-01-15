import os

from sift import SIFT
from tqdm import tqdm

###################### DEFINING DATA PATH ######################

'''

-> Please change the following paths.

-> The "writeImg" option in sift.getPoints is to save images as processed
   by the SIFT function. Please update the "writeDir" option to change the path
   to save the processed images.

'''

dataDir = '../data'
train_fldr = 'train_imgs1'
resultFile = 'results.csv'

###################### GETTING POINTS AND SAVING RESULTS ######################

imgNames = os.listdir('{}/{}'.format(dataDir, train_fldr))

sift = SIFT(alphaMin = 0.2, alphaMax = 0.45)
saveFile = open('{}/{}'.format(dataDir, resultFile), 'w')

for name in tqdm(imgNames[0:1]):
    matchPoints = sift.getPoints('{}/{}/{}'.format(dataDir, train_fldr, name),
                                 '{}/templates'.format(dataDir), writeImg=True,
                                 writeDir='../data/results/')
    saveFile.write(str(name) + ',' + str(matchPoints) + '\n')

saveFile.close()