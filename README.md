# SkylarkDrones_GCPFinder

This repository contains the my solution to the coding assignment for Skylark Drones. 
The assignment was to find 'L' shaped white Ground Control Points (GCPs) from the given images.

# Method Used

The method I have used to solve this problem is using Scale-Invariant Feature Transform (SIFT) method along with Blunt Force Matching. 

-> First the Image is converted to binary so as to remove major noise and extra features.<br />
-> Then it is passed through the SIFT function.<br />
-> The resulting image is matched using KNN with Blunt Force Method with GCP at 4 different angles kept in the template folder in                 data.<br />
-> The resulting matched points are returned. Please note that the array obtained is first checked for similar points or points in same area.<br />

A point to be noted is that the results can be improved by changing the feature extraction and matching methods, but the main idea is the same.

# Results

The following is a correctly placed marker by the method mentioned above.

![True Positive](data/results/DJI_0036_1.JPG)

The following is an image containing a GCP without a marker because of obstruction from tree. 

![False Negetive](data/results/DJI_0050_1.JPG)

The following is an image without a GCP with a marker. 

![False Positive](data/results/DJI_0064_4.JPG)


The following is an image with multiple GCP but the result shows only one. This can be improved by a little more processing and changing methods. (I am sure I will be able to imrpove this but could not because lack of time.) 

![Result](data/results/DJI_0084_4.JPG)
