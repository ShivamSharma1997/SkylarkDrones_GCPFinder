import os
import cv2
import numpy as np

class SIFT:
    
    def __init__(self, alphaMin=0.25, alphaMax=0.4, thresh=250):
        
        self.alphaMin = alphaMin
        self.alphaMax = alphaMax
        self.thresh = thresh

    def getPoints(self, imgPath, tempPath, writeImg=False, writeDir='../data/'):
        
        bestMatchPoints = []
        
        img1 = cv2.imread(imgPath)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img1 = cv2.threshold(img1, self.thresh, 255, cv2.THRESH_BINARY)[1]
        
        sift = cv2.xfeatures2d.SIFT_create()
        
        kp1, des1 = sift.detectAndCompute(img1,None)
        img1 = cv2.imread(imgPath)
        
        for tempName in os.listdir(tempPath):
            
            img2 = cv2.imread('{}/{}'.format(tempPath, tempName))
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
            
            kp2, des2 = sift.detectAndCompute(img2,None)
           
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1,des2, k=2)
            
            good, res = [], []
            
            for m,n in matches:
                alpha = self.alphaMin
                while(len(good) == 0 and alpha <= self.alphaMax):
                    
                    if m.distance < alpha*n.distance:
                        x, y = kp1[m.queryIdx].pt
                        good.append([int(x), int(y)])
                        res.append([m])
                    alpha += 0.05
            
            bestMatchPoints.extend(good)
            if writeImg:
                imgName = imgPath.split('/')[-1][:-4]
                tempImgName = tempName.split('.')[0]
                writePath = writeDir+imgName+'_'+tempImgName+'.JPG'
                outImage = np.zeros(img1.shape)
                img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2, res, outImage, flags=2)
                cv2.imwrite(writePath,img3)
        
        out = []
        if len(bestMatchPoints) != 0:
            out.append(bestMatchPoints[0])
            
            for i in range(1, len(bestMatchPoints)):
                for fclPt in out:
                    tstX, tstY = bestMatchPoints[i]
                    fclX, fclY = fclPt
                    if (abs(tstX - fclX) > 50) and (abs(tstY - fclY) > 50):
                        out.append(bestMatchPoints[i])
        
        return out
    