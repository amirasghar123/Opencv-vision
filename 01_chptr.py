# import library
import cv2 as cv
# from matplotlib.pyplot import imshow
img=cv.imread("resources/image.png")
cv.imshow("phali image",img)
cv.waitKey(5000)