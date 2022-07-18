# how to capture a webcam inside python
# from tkinter import Frame
#import libraries
import cv2 as cv
import numpy as np
#road the frame from camera
 
cap=cv.VideoCapture(0) # webcam no 1 chal gye ga agr ()my 1 likhty to webcam no 2 chal jata i'm right
# if(cap.isopened()==False):
#     print("There is an error")# only check karny k lye k ya hamra webcam chal rha hai k nai

# read until the end
while(True):
# while(cap.isOpened()):
#Capture frame by frame
    ret,frame=cap.read()
    # if ret==True:
         # to display the frame
    cv.imshow("originalCam",frame)
         # to quit with q key
    if cv.waitKey(1) & 0xff ==ord('q'):
        break 
    # else:
    #     break
    #release and close window
cap.release()
cv.destroyAllWindows()
# yar mary ghar my to camera he nai laga huwa my asy chalny ke try my ho hahaha
