# converted video to gray or black and white and asving
import cv2 as cv


cap=cv.VideoCapture('resources/video1.mp4')


# writing format ,codec, voideo writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter('resources/out_video.avi',cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)

while(True):
  
    ret,frame=cap.read()
    # gray frame k kye 
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # (thresh,binary)=cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
   # to show in player
    if ret==True:
        out.write(grayframe)
        cv.imshow("vidio",grayframe)
        # to quit with q key
        if cv.waitKey(1) & 0xff ==ord('q'):
            break       
    else:
        break
    
cap.release()
out.release()
cv.destroyAllWindows()