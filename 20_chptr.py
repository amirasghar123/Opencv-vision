# How to detect specific color inside python
# from cv2 import getTrackbarPos
import numpy as np
import cv2 as cv
# img=cv.imread("resources/image.png")

# Convert in HSV (Hue, Saturation, Value)
# hue_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)#rang barangi sakal my chla gye ga jb show kary gye


def slider():
    pass


path = "resources/image.png"

# new img or new window bnaye gye essy
cv.namedWindow("Bars")
cv.resizeWindow("Bars", 900, 300)

# Track Bar
# cv.createTrackbar("Hue","Bars",0,179,slider) yaha sy start krna hai slider bnana
cv.createTrackbar("Hue min", "Bars", 0, 179, slider)
cv.createTrackbar("Hue max", "Bars", 179, 179, slider)
cv.createTrackbar("Sat min", "Bars", 0, 255, slider)
cv.createTrackbar("Sat max", "Bars", 255, 255, slider)
cv.createTrackbar("Val min", "Bars", 0, 255, slider)
cv.createTrackbar("Val max", "Bars", 255, 255, slider)


img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hue_min=getTrackbarPos("Hue min","Bars")
# print(hue_min)
while True:

    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue min", "Bars")
    hue_max = cv.getTrackbarPos("Hue max", "Bars")
    sat_min = cv.getTrackbarPos("Sat min", "Bars")
    sat_max = cv.getTrackbarPos("Sat max", "Bars")
    val_min = cv.getTrackbarPos("Val min", "Bars")
    val_max = cv.getTrackbarPos("Val max", "Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    
 # To see these changes inside an image
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])

 # image mask
    mask_img=cv.inRange(hsv_img,lower,upper)
    out_img=cv.bitwise_and(img,img,mask=mask_img)


    cv.imshow("original",img)
    cv.imshow("HSV",hsv_img)
    cv.imshow("Mask",mask_img)
    cv.imshow("Final Output",out_img)
    
    if cv.waitKey(1) & 0xff ==ord('q'):
        break
cv.destroyAllWindows()
