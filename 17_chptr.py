#Joining the two image
import cv2 as cv
from cv2 import imshow
import numpy as np

img=cv.imread("resources/image.png")

#stacking same image

#1- horizontal stack      // braber us k sath attach ho jye ge

hor_img=np.hstack((img,img))

#2- Vertical stack        // nachy us k sath attach ho gye ge
ver_img=np.vstack((img,img))

cv.imshow("Horizontal",hor_img)
cv.imshow("Vertical",ver_img)

cv.waitKey(0)
cv.destroyAllWindows()

#you