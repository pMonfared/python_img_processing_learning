import numpy as np
import cv2 as cv

img_colored = cv.imread('city_thumb.jpg', cv.IMREAD_COLOR)

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img_colored,'Hello World!',(50,100),font,2,(255,255,255),3, cv.LINE_AA)



cv.imshow('City', img_colored)
cv.waitKey(0)
cv.destroyAllWindows()