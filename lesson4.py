import numpy as np
import cv2 as cv

img_eye_gray = cv.imread('eye_gray.jpg', cv.IMREAD_COLOR)
img_eye_brown = cv.imread('eye_brown.jpg', cv.IMREAD_COLOR)


added = img_eye_brown + img_eye_gray 
added_2 = cv.add(img_eye_brown, img_eye_gray)
added_3 = cv.addWeighted(img_eye_gray, 0.5, img_eye_brown, 0.5, 0)


img1gray = cv.cvtColor(img_eye_gray, cv.COLOR_BGR2GRAY)
ret, mask_img1gray = cv.threshold(img1gray, 150, 255,cv.THRESH_BINARY)
mask_img1gray_inverted = cv.bitwise_not(mask_img1gray)

img1_m = cv.bitwise_and(img_eye_gray,img_eye_gray, mask= mask_img1gray)
img2_m = cv.bitwise_and(img_eye_brown,img_eye_brown,mask= mask_img1gray_inverted)

image_added = cv.add(img1_m, img2_m)


# cv.imshow('eye gray', img_eye_gray)
# cv.imshow('eye brown', img_eye_brown)
# cv.imshow('Blobs added', added)
# cv.imshow('Blobs added_2', added_2)
cv.imshow('Blobs mask_img1gray', mask_img1gray)
cv.imshow('Blobs added_3', added_3)

cv.imshow('Blobs image_added', image_added)



cv.waitKey(0)
cv.destroyAllWindows()