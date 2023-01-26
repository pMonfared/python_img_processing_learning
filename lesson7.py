import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Edge Detection

img = cv.imread('road.jpg', 0)
# cv.imshow('Origin', img)

img_noise_removed = cv.GaussianBlur(img,(7,7),0)
# Laplacian
laplacian = cv.Laplacian(img_noise_removed,cv.CV_64F)
# cv.imshow('laplacian', laplacian)

# Sobelx
sobelx = cv.Sobel(img_noise_removed,cv.CV_64F,1,0,ksize=5)
# cv.imshow('sobelx', sobelx)

# Sobely

sobely = cv.Sobel(img_noise_removed,cv.CV_64F,0,1,ksize=5)
# cv.imshow('sobely', sobely)

# Canny Edge Detection

canny = cv.Canny(img_noise_removed,10, 250)
cv.imshow('canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()