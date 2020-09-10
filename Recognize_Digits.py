import cv2
import imutils
import numpy as np
from imutils.perspective import four_point_transform
from imutils import contours

DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}

image=cv2.imread("example.jpg")
image=imutils.resize(image,height=500)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edge=cv2.Canny(blur,50,200,255)
cnts=cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
dispcnt=None
cn=sorted(cnts,key=cv2.contourArea,reverse=True)
for c in  cn:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx)==4:
        dispcnt=approx
        break
transform=four_point_transform(image,dispcnt.reshape(4,2)) 
warp=four_point_transform(gray,dispcnt.reshape(4,2))
thresh=cv2.threshold(warp,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow("th",thresh)
cv2.waitKey(0)
cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cn=sorted(cnts,key=cv2.contourArea,reverse=True)
Nums=[]
for c in cn:
    (x,y,w,h)=cv2.boundingRect(c)
    if w>=10 and (h>=30 and h<=40):
        Nums.append(c)

cv2.drawContours(transform,Nums,-1,(255,0,0),2)

Nums=contours.sort_contours(Nums,method="left-to-right")[0]
digits=[]

for c in Nums:
    (x,y,w,h)=cv2.boundingRect(c)
    roi=thresh[y:y+h,x:x+w]
    (roih,roiw)=roi.shape[:2]
    (dw,dh)=(int(roiw*0.25),int(roih*0.15))
    dhC=int(roih*0.05)
    segments=[
        ((0,0),(w,dh)),
        ((0,0),(dw,h//2)),
        ((w-dw,0),(w,h//2)),
        ((0,(h//2-dhC)),(w,(h//2+dhC))),
        ((0,h//2),(dw,h)),
        ((w-dw,h//2),(w,h)),
        ((0,h-dh),(w,h))
    ]
    on=[0]*len(segments)
    for (i,((rx,ry),(dx,dy))) in enumerate(segments):
        region=roi[ry:dy,rx:dx]
        #cv2.rectangle(region,(rx,ry),(rx+dx,ry+dy),(255,0,0),-1)
        nonzeros=cv2.countNonZero(region)
        area=(dx-rx)*(dy-ry)
        if nonzeros/area>0.5:
            on[i]=1
    if (tuple(on) in DIGITS_LOOKUP):
        digit=DIGITS_LOOKUP[tuple(on)] 
    else: 
        digit=0   
    digits.append(digit)
print(digits)




cv2.imshow("Image",transform)
cv2.waitKey(0)