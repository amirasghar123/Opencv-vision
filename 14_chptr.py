#How to draw lines, and shape in python

import cv2 as cv
import numpy as np
# Draw a canvas 0 is for black
img=np.zeros((600,600))
# Draw a canvas 1 is for whiteq
img1=np.ones((600,600))

#print shape size
print("The size of our canvas is: ",img.shape)
# print(img)

# Adding colors to the canvas
colored_img=np.zeros((600,600,3),np.uint8)#color channel addition
colored_img[:]=255,170,210  #complete image color     # color code sy koi b color pasad kr k laga sakty ho
colored_img[150:200,100:500]=255,10,0  # image k kasi b part ko color k sakty hai like kasi b hesy ko

#Adding lines
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)# puri line lagny k lye ya function use kr sakty hai
cv.line(colored_img,(100,100),(300,300),(255,255,100),3)# part line 300,300,length hai esko thora ghnna kr sakty ho

# Adding rectangles
cv.rectangle(colored_img,(40,60),(300,400),(155,55,34),3)# drew a rectangles
cv.rectangle(colored_img,(40,60),(300,400),(155,55,34),cv.FILLED)# fill the rectangles

# Adding circle
cv.circle(colored_img,(400,300),50,(255,100,250),5)# drew a circle
cv.circle(colored_img,(400,300),50,(255,100,250),cv.FILLED)#fill th circle

# Adding Text
cv.putText(colored_img,("My name is Aamir.I'm very sad now a \n day yr pta nai qu mary sath he sb kuch huta hai"),(200,500),cv.ADAPTIVE_THRESH_GAUSSIAN_C,1,(123,142,231),3)

# cv.imshow("Black Image",img)
# cv.imshow("White Image",img1)
cv.imshow("Color Image",colored_img)
cv.waitKey(0)
cv.destroyAllWindows() 