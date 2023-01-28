# Color Spaces
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread("book1.jpg")

# OpenCV imread function returns BRG channel as default
blue_ch, green_ch, red_ch = cv.split(image)
img_rgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)

# RGB 
# BGR openCV
# BGRA / RGBA => 4 channel alpha opacity

# HSV [20, 100, 50]
# =>  [HUE, Saturation, Value]
# Please check the RGBvsHSV.jpg in project's root folder to understand more detail about it


img_hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
 
plt.imshow(img_hsv)
plt.show()