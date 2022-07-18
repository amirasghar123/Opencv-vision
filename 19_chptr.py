#coordinate of an image or video
# Step-1 import libraries
import cv2 as cv
from cv2 import imread
import numpy as np
# step-2 define a functiom
def find_coord(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        #lift mouse click
        print(x,'',y)
        # how to define or print on the same image or window
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x),+',',str(y),(x,y),font,1,(255,124,169),thickness=2)
        # show the text on the image and image itself
        cv.imshow("image",img)

# final function to read an display
        
if __name__=="__main__":
    #reading an image 
    img=imread("resources/image.png",1)
    # display the image
    cv.imshow("image",img)
    #setting call back function
    cv.setMouseCallback("image",find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()