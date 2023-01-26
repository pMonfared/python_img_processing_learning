#Template Matching

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread("sunflowers.jpg", 0)
template = cv.imread("sunflower.jpg",0)
template1 = cv.imread("sunflower1.jpg",0)

w, h = template.shape
w1, h1 = template1.shape

result = cv.matchTemplate(image,template, cv.TM_CCOEFF_NORMED)
result1 = cv.matchTemplate(image,template1, cv.TM_CCOEFF_NORMED)

# This is for find the matches items) => higher amount = find Less number but most similarity) , lower amount = find more number but less similarity)
threshold = 0.55
threshold1 = 0.65

# return detail of founded location(s) which are bigger than threshold amount
locations = np.where(result >= threshold)

for point in zip(*locations[::-1]):
    cv.rectangle(image, point, (point[0]+ h,point[1]+w), (255,255,255),1)



locations1 = np.where(result1 >= threshold1)

for point in zip(*locations1[::-1]):
    cv.rectangle(image, point, (point[0]+ h1,point[1]+w1), (255,255,0),1)


plt.imshow(image)
plt.show()