# Face Detector

import numpy as np
import cv2 as cv
# run it in CMD: pip install cvzone
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv.VideoCapture(0)
detector = FaceDetector()
mesh_detector = FaceMeshDetector()

while(True):
    rec, frame = cap.read()
    frame_gray= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame, bbox = detector.findFaces(frame)
    frame, faces = mesh_detector.findFaceMesh(frame)

    if(bbox):
        center = bbox[0]['center']
        cv.circle(frame,center,5,(255,0,255), cv.FILLED)

    
    cv.imshow('frame',frame)

    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()


