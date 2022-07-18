# converted video to gray or black and white 
import cv2 as cv


cap=cv.VideoCapture('resources/video1.mp4')


while(True):
    ret,frame=cap.read()
    # gray frame k kye 
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # black and white
    (thresh,binary)=cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    # to show with player
    if ret==True:
        # binary ke janga grayframe likhy gye to video gray ho gye ge
        cv.imshow("vidio",binary)
        # to quit with q key
        if cv.waitKey(1) & 0xff ==ord('q'):
            break       
    else:
        break
    
cap.release()
cv.destroyAllWindows()