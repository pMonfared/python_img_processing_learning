import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread("xray1.jpg", 0)

histogram = cv.calcHist([image], [0], None, [256], [0, 256])

plt.subplot(121), plt.imshow(image, 'gray')
plt.subplot(122), plt.plot(histogram)
plt.show()