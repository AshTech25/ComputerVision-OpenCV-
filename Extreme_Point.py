import cv2
import imutils
import numpy as np

def Aspect_Ratio(img):
    (h,w,d)=img.shape
    nw=600
    aR=w/h
    nh=int(nw/aR)
    img=cv2.resize(img,(nw,nh))
    return img


image=cv2.imread("palm.jpg")
image=Aspect_Ratio(image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
threshold=cv2.threshold(blur,60,255,cv2.THRESH_BINARY)[1]
thresh = cv2.erode(threshold, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
c=max(cnts,key=cv2.contourArea)
min_pointx=tuple(c[c[:,:,0].argmin()][0])
max_pointx=tuple(c[c[:,:,0].argmax()][0])
min_pointy=tuple(c[c[:,:,1].argmin()][0])
max_pointy=tuple(c[c[:,:,1].argmax()][0])
cv2.drawContours(image,[c],-1,(255,0,0),3)
cv2.circle(image,min_pointx,8,(0,0,255),-1)
cv2.circle(image,max_pointx,8,(0,255,255),-1)
cv2.circle(image,min_pointy,8,(0,255,0),-1)
cv2.circle(image,max_pointy,8,(255,0,255),-1)
print(max_pointy)
cv2.imshow("Current",image)
cv2.waitKey(0)


