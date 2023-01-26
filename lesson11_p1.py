# featureMatching
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread("super-luxury-cars.jpg",1)

# SIFT
sift = cv.SIFT_create()

# SURF

# surf = cv.SURF_create()

# ORB

orb = cv.ORB_create(nfeatures=1000)

sift_keypoints, descriptors = sift.detectAndCompute(image,None)
orb_keypoints, descriptors2 = orb.detectAndCompute(image,None)

image_sift =  cv.drawKeypoints(image,sift_keypoints, None)
image_orb =  cv.drawKeypoints(image,orb_keypoints, None)
 
plt.imshow(image_orb, 'gray')
plt.show()