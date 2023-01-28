import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import modules.qr_code_util as qrutil





cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    frame_gray= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    qrutil.displayOnCam(frame,im=frame_gray)
    
    cv.imshow('frame',frame)

    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()