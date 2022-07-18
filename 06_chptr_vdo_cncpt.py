# converted video to gray or black and white
import cv2 as cv

cap=cv.VideoCapture('resources/vidio2.mp4')
# cap=cv.cvtColor(cap,cv.COLOR_BGR2GRAY)
#indicator
# if (cap.isOpened() == False):

#     print("Error in reading video")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("vidio",frame)
        if cv.waitKey(1) & 0xff ==ord('q'):
            break       
    else:
        break
cap.release()
cv.destroyAllWindows()