import cv2
import imutils
import numpy as np

def draw_contours(img,c,i):
    M=cv2.moments(c)
    cX=int(M["m10"]/M["m00"])
    cY=int(M["m01"]/M["m00"])
    cv2.putText(img,"#{}".format(i+1),(cX-20,cY),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,255,255),2)
    return img

def sort_contours(c,order="left-to-right"):
    reverse=False
    i=0
    if order=="top-to-bottom" or order=="bottom-to-top":
        i=1
    if order=="right-to-left" or order=="bottom-to-top":
        reverse=True
    
    bounding=[cv2.boundingRect(i) for i in c]
    print(sorted(zip(c,bounding),key=lambda b:b[1][i],reverse=reverse))
    (c,bounding)=zip(*sorted(zip(c,bounding),key=lambda b:b[1][i],reverse=reverse))
    return (c,bounding)

image=cv2.imread('sorted_contours.png')
accumEdged=np.zeros(image.shape[:2],dtype='uint8')

for chan in cv2.split(image):
    chan=cv2.medianBlur(chan,5)
    edge=cv2.Canny(chan,60,200)
    accumEdged = cv2.bitwise_or(accumEdged, edge)

cnts=cv2.findContours(accumEdged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:4]
#cv2.drawContours(image,cnts,-1,(255,0,0),3)
orig=image.copy()
for (i,c) in enumerate(cnts):
    orig=draw_contours(orig,c,i)


cv2.imshow('Image',orig)
cv2.waitKey(0)

orig=image.copy()
(cnts,bounding)=sort_contours(cnts,order="top-to-bottom")
for (i,c) in enumerate(cnts):
    orig=draw_contours(orig,c,i)


cv2.imshow('Image',orig)
cv2.waitKey(0)


