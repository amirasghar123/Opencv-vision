# How to change the perspective of an image

import cv2 as cv
from cv2 import imread
import numpy as np
 
img=cv.imread("resources/amir.png")
print(img.shape)
#defining point
point1=np.float32([[233,196],[82,471],[522,169],[715.482]])
width=480
height=1000
width,height=480,1000
point2=np.float32([[0,0],[800,0],[0,height],[width,height]])
matrix=cv.getPerspectiveTransform(point1,point2)
out_img=cv.warpPerspective(img,matrix,(width,height))

cv.imshow("original",img)
# cv.imshow("Transformed",out_img)
cv.waitKey(0)
cv.destroyAllWindows()