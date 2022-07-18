# import library
import numpy as np
import cv2 as cv
# from matplotlib.pyplot import imshow
img=cv.imread("resources/image.png")
img=cv.resize(img,(600,400))


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
# cv.imshow("dusri image",img)


cv.waitKey(0)
cv.destroyAllWindows()