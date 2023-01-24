import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img_gray = cv.imread('city_thumb.jpg', cv.IMREAD_GRAYSCALE)
img_colored = cv.imread('city_thumb.jpg', cv.IMREAD_COLOR)

img_origin = cv.imread('city_thumb.jpg', cv.IMREAD_UNCHANGED)


# Show img by matplotlip library

plt.imshow(img_colored, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()


