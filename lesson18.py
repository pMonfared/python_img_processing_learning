# Moving Object Detector
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import modules.qr_code_util as qrutil
import modules.video_util as videoutil

cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()

    resized_frame = videoutil.rescale_frame(frame, 30)
    cv.imshow('frame',resized_frame)

    keyexist = cv.waitKey(5) & 0xFF
    if keyexist == 27:
        break

cv.destroyAllWindows()
cap.release()

