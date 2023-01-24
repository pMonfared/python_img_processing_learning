import numpy as np
import cv2 as cv

img_colored = cv.imread('blobs.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_colored,cv.COLOR_BGR2GRAY)


# BGR
print(img_colored.shape) # => (294, 553, 3)
                         # => ( x , y  , Count of Colors Channel)

b = img_colored[:,:,0] # Blue
g = img_colored[:,:,1] # Green
r = img_colored[:,:,2] # Red

# Or we can use a openCV funtion for retrive the BGR channel amount
img_blue, img_green, img_red = cv.split(img_colored)






cv.imshow('Blobs colored', img_colored)
cv.imshow('Blobs Blue', b)
cv.imshow('Blobs Green', g)
cv.imshow('Blobs Red', r)

# Remove Red Color Channel from Image
img_colored[:,:,2] = 0

cv.imshow('Blobs after removed the Red Channel', img_colored)

cv.waitKey(0)
cv.destroyAllWindows()