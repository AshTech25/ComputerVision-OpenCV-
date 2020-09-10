import cv2
import imutils 
import numpy as np
from colorDetect import colorDetect
from shape_detector import ShapeDetector

image=cv2.imread('shapes_and_colors.jpg')
resize=imutils.resize(image,width=300)
ratio=image.shape[0]/float(resize.shape[0])


blur=cv2.GaussianBlur(resize,(5,5),0)
gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)
thresh=cv2.threshold(gray,60,255,cv2.THRESH_BINARY)[1]
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
sd=ShapeDetector()
cd=colorDetect()
for c in cnts:
    M=cv2.moments(c)
    cX=int(M["m10"]/M["m00"]*ratio)
    cY=int(M["m01"]/M["m00"]*ratio)
    shape=sd.detect_shape(c)
    color=cd.label(lab,c)
    c=c.astype("float")
    c=c*ratio
    c=c.astype("int")
    cv2.drawContours(image,[c],-1,(0,255,0),2)
    text="{} {}".format(shape,color)
    cv2.putText(image,text,(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)

