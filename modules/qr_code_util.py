import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
from matplotlib import pyplot as plt 

font = cv2.FONT_HERSHEY_SIMPLEX

def decode(im) : 
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decodedObjects
 
# Display barcode and QR code location  
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points
        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
    # Display results 
    #cv2.imshow("Results", im);
    #cv2.waitKey(0);
    return im

def displayOnCam(frame,im):
    decodedObjects = decode(im)

    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
     
        # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points
         
        # Number of points in the convex hull
        n = len(hull)     
        # Draw the convext hull
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

        x = decodedObject.rect.left
        y = decodedObject.rect.top

        print(x, y)

        print('Type : ', decodedObject.type)
        print('Data : ', decodedObject.data,'\n')

        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
    
    return frame