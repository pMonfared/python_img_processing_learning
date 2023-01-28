# Video Cam

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    # Convert every BGR frame to HSV color channels
    frame_hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_red = np.array([0,50, 50])
    upper_red = np.array([6,255,180])

    
    lower_blue = np.array([100,50, 50])
    upper_blue = np.array([116,255,180])

    mask_red = cv.inRange(frame_hsv,lower_red,upper_red)
    mask_blue = cv.inRange(frame_hsv,lower_blue,upper_blue)

    frame_masked_blue = cv.bitwise_and(frame, frame, mask=mask_blue)

    cv.imshow('frame',frame)
    # cv.imshow('mask_red',mask_red)
    # cv.imshow('mask_blue',mask_blue)
    cv.imshow('frame_masked_blue',frame_masked_blue)
    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()


