import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# Morphological Operations

original_img = cv.imread("Neuron.jpg")
img_gray = cv.cvtColor(original_img,cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)


cv.imshow('Neuron', img_gray)
cv.imshow('Neuron mask', mask)

# Erosion (سایش و فرسایش)

kernel_eroded = np.ones((2,2),np.uint8)
eroded_img = cv.erode(mask, kernel=kernel_eroded, iterations=1)

cv.imshow('Neuron eroded_img', eroded_img)

# Dilation (رشد دادن، افزایش دادن، حجیم کردن)

kernel_delated = np.ones((2,2),np.uint8)
delated_img = cv.dilate(mask, kernel=kernel_delated, iterations=1)

cv.imshow('Neuron delated_img', delated_img)

# Closing

kernel_closed = np.ones((5,5),np.uint8)
closed_img = cv.morphologyEx(delated_img,cv.MORPH_CLOSE,kernel=kernel_closed)

cv.imshow('Neuron closed_img', closed_img)

# Opening

kernel_opened = np.ones((10,5),np.uint8)
opened_img = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel=kernel_closed)

cv.imshow('Neuron opened_img', opened_img)

# Gradiant
kernel_gradiant = np.ones((3,3),np.uint8)

gradiant = cv.morphologyEx(original_img,cv.MORPH_GRADIENT,kernel=kernel_gradiant)
cv.imshow('Neuron gradiant', gradiant)





cv.waitKey(0)
cv.destroyAllWindows()