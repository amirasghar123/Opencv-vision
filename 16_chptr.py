# saving HD recording of cam steming
# only code include chptr no 15 and 11 add aur hamy chptr no 16 mil gya alhamdolilah very happy hans k wakha dy
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

# writing format ,codec, voideo writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter('resources/cam_video.avi',cv.VideoWriter_fourcc('M','J','P','G'),30,(frame_width,frame_height))

while(True):
  
    ret,frame=cap.read()
    # gray frame k kye 
    # grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # (thresh,binary)=cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
   # to show in player
    if ret==True:
        out.write(frame)
        cv.imshow("vidio",frame)
        # to quit with q key
        if cv.waitKey(1) & 0xff ==ord('q'):
            break       
    else:
        break
    
cap.release()
out.release()
cv.destroyAllWindows()