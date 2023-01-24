import numpy as np
import cv2 as cv

img_colored = cv.imread('city_thumb.jpg', cv.IMREAD_COLOR)

cv.line(img_colored, (100,150),(250,150),(0,0,255),10)
cv.rectangle(img_colored,(100,100),(250,170),(0,255,140),8)

cv.circle(img_colored,(250,170),30, (225,200,100), 10)
cv.circle(img_colored,(100,170),30, (225,200,100), 10)


points = np.array([[30,50],[300,200],[480,350],[120,50]], np.int32)
cv.polylines(img_colored,[points],True,(255,0,0),5)



cv.imshow('City', img_colored)
cv.waitKey(0)
cv.destroyAllWindows()