import numpy as np
import cv2 as cv

img_brain_mri_scan = cv.imread('BRAIN.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_brain_mri_scan,cv.COLOR_BGR2GRAY)

ret, tresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY)
#OTSU Thresholding
ret2,thresh2 = cv.threshold(img_gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)


thresh_adaptive = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY , 15, 1)



cv.imshow('brain mri scan', img_brain_mri_scan)
cv.imshow('brain mri scan thresh2', thresh2)
cv.imshow('brain mri scan adaptive', thresh_adaptive)



cv.waitKey(0)
cv.destroyAllWindows()