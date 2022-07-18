#image into black and white
import cv2 as cv
img=cv.imread("resources/amir.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow("Original",img)
cv.imshow("Gray",gray)
cv.imshow("Black And White",binary)
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.waitKey(5000)
cv.destroyAllWindows()