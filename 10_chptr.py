# gray camera
# from tkinter import Frame
#converted video into gray and black and white
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)

    cv.imshow("originalCam",frame)
    cv.imshow("grayCam",gray_frame)
    cv.imshow("BlackandwhiteCam",binary)
    if cv.waitKey(1) & 0xff ==ord('q'):
        break 
cap.release()
cv.destroyAllWindows()