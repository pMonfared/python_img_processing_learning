import numpy as np
import cv2 as cv

img_colored = cv.imread('blobs.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_colored,cv.COLOR_BGR2GRAY)



img_gray_croped = img_gray [50:200, 50:300]


cv.imshow('Blobs colored', img_colored)
cv.imshow('Blobs gray', img_gray)
cv.imshow('Blobs gray croped', img_gray_croped)

# It means, Hey Python wait for press any key then close the opened page, 
cv.waitKey(0) # 0 => any keys
cv.destroyAllWindows()