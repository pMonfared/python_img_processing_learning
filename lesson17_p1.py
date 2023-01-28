# QR Code Detection
import numpy as np
import cv2 as cv

# pip install qrcode
import qrcode


### Detect Qr Code
qrcode_img = cv.imread("QrCode1.jpg")

detector = cv.QRCodeDetector()

value, box, _ = detector.detectAndDecode(qrcode_img)

print(value)
# print(box)
box_int16 = box.astype(np.int16)

pt1= (box_int16[0][0][0], box_int16[0][0][1])
pt2= (box_int16[0][2][0], box_int16[0][2][1])

cv.rectangle(qrcode_img, pt1,pt2,(255,255,0),2)


### Generate QR Code
generated_qr_code = qrcode.make("Doset Daram!")
generated_qr_code.save('qrcode2.png')
 
cv.imshow('qrcode_img',qrcode_img)
cv.waitKey()
cv.destroyAllWindows()