# Basic functions or manipulation in open cv
# import library
import numpy as np
import cv2 as cv
#original image
img=cv.imread("resources/amir.png")
# print(img.shape)
img=cv.resize(img,(400,800))
# print(img.shape)
#resied
resize_img=cv.resize(img,(400,400))

#gray image
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# black and white
(thresh,binary)=cv.threshold(img,127,255,cv.THRESH_BINARY)

#blurred image
blurr_img=cv.GaussianBlur(img,(23,23),0)# blurr matlb hai k dhudla pan 

# Edge detection
edge_img=cv.Canny(img,53,53)

#thickness of lines
mat_karnal=np.ones((3,3),np.uint8)
dilated_img=cv.dilate(edge_img,(mat_karnal),iterations=1)
# dilated_img=cv.dilate(edge_img,(7,7),iterations=1)

#make thinner outline
ero_img=cv.erode(dilated_img,mat_karnal,iterations=1)

#cropping we will use numpy library not open cv
print("The size or your image is :",img.shape)
cropped_img=img[0:400,50:500]

cv.imshow("Original",img)
cv.imshow("Cropped",cropped_img)
cv.imshow("Eroad",ero_img)
cv.imshow("Resize",resize_img)
cv.imshow("Gray",gray_img)
cv.imshow("Blurr",blurr_img)
cv.imshow("Edge",edge_img)
cv.imshow("Dilate",dilated_img)
cv.imshow("Black and White",binary)
cv.waitKey(0)
cv.destroyAllWindows()