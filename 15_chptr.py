# Resolution of camera
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
#resolation HD (1280x720)


# function for HD
def hd_resolution():
    cap.set(3,1280)# width
    cap.set(4,720)#height
# hd_resolution()
# Function for full HD
def fhd_resolution():
    cap.set(3,1920)# width
    cap.set(4,1080)#height
fhd_resolution()
while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Camera", frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
