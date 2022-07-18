#image an saving and writing
import cv2 as cv
img=cv.imread("resources/amir.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)

binary=cv.resize(binary,(300,400))

cv.imwrite('resources/image_gray.png',gray)
cv.imwrite('resources/image_bw.png',binary)

# cv.waitKey(500)
# cv.destroyAllWindows()