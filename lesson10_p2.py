import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img_origin = cv.imread("art.png")
img = cv.cvtColor(img_origin,cv.COLOR_BGR2GRAY)

img_hist = cv.calcHist([img], [0], None, [256], [0, 256])


equalized_histogram = cv.equalizeHist(img)
img_equalized_histogram = cv.calcHist([equalized_histogram], [0], None, [256], [0, 256])


clahe = cv.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cl1_equalized_histogram = cv.calcHist([cl1], [0], None, [256], [0, 256])


plt.subplot(321), plt.imshow(img)
plt.subplot(322), plt.plot(img_hist)

plt.subplot(323), plt.imshow(equalized_histogram)
plt.subplot(324), plt.plot(img_equalized_histogram)

plt.subplot(325), plt.imshow(cl1)
plt.subplot(326), plt.plot(cl1_equalized_histogram)
plt.show()