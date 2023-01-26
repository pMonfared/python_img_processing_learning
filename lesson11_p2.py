# featureMatching
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image1 = cv.imread("book1.jpg")
image2 = cv.imread("library.jpg")


# ORB

orb = cv.ORB_create(nfeatures=1000)

orb_keypoints1, descriptors1 = orb.detectAndCompute(image1,None)
orb_keypoints2, descriptors2 = orb.detectAndCompute(image2,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck =True)

matches = bf.match(descriptors1, descriptors2)
matches = sorted(matches, key= lambda x:x.distance)

image_matches = cv.drawMatches(image1,orb_keypoints1, image2, orb_keypoints2, matches[:20], None, flags=2)
 
 
plt.imshow(image_matches, 'gray')
plt.show()