# Hand Gesture

import numpy as np
import cv2 as cv
# run it in CMD: pip install cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon = 0.5, maxHands = 2)

while(True):
    rec, frame = cap.read()
    frame_gray= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hands, img = detector.findHands(frame)

    if hands:
        hand1 = hands[0]
        # Please check the land_marks_hand.jpg for find more detail
        land_marks_list1 = hand1["lmList"]
        length, info, frame = detector.findDistance(land_marks_list1[4][:-1],land_marks_list1[8][:-1], frame)

    
    cv.imshow('frame',frame)

    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()


