# setting of camera or video

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

cap.set(10,100)# 10 is key to set brightness
cap.set(3,640)# width key 3
cap.set(4,480)#height key 4

while(True):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xff ==ord('q'):
        break  
cap.release()
cv.destroyAllWindows()