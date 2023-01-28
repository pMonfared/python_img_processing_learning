# Face Detection

import numpy as np
import cv2 as cv

# XML source:
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv.CascadeClassifier('frontfacedefault.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
cap = cv.VideoCapture(0)


while(True):
    rec, frame = cap.read()
    frame_gray= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame_gray,1.3,5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h), (255,0,255), 2)
        # cropped face detected area
        frame_gr_roi = frame_gray[y:y+h,x:x+w]
        frame_roi = frame[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(frame_gr_roi)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(frame_roi,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)

        smiles = smile_cascade.detectMultiScale(frame_gr_roi, 1.8, 20)
        for (sx,sy,sw,sh) in smiles:
            cv.rectangle(frame_roi,(sx,sy),(sx+sw, sy+sh),(0,0,255),2)

    cv.imshow('frame',frame)

    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()


