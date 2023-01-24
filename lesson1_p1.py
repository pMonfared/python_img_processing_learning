import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img_gray = cv.imread('city_thumb.jpg', cv.IMREAD_GRAYSCALE)
img_colored = cv.imread('city_thumb.jpg', cv.IMREAD_COLOR)

img_origin = cv.imread('city_thumb.jpg', cv.IMREAD_UNCHANGED)

# cv.IMREAD_GRAYSCALE   0
# cv.IMREAD_COLOR  1
# cv.IMREAD_UNCHANGED  -1


cv.imshow('City gray', img_gray)
cv.imshow('City colored', img_colored)
cv.imshow('City origin', img_origin)

# It means, Hey Python wait for press any key then close the opened page, 
cv.waitKey(0) # 0 => any keys
cv.destroyAllWindows()

# Colors categories in OpenCV library

# RGB (34, 45, 56) other libraries
# in OpenCV:
# BGR
# RGBA, BGRA

# Save a image
cv.imwrite('city_t_1_saved.jpg',img_gray)


