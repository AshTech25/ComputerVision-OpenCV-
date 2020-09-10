import cv2
import imutils
import numpy as np
from imutils.perspective import four_point_transform

def sort_contours(c,order="left-to-right"):
    reverse=False
    i=0
    if order=="top-to-bottom" or order=="bottom-to-top":
        i=1
    if order=="right-to-left" or order=="bottom-to-top":
        reverse=True
    
    bounding=[cv2.boundingRect(i) for i in c]
    #print(sorted(zip(c,bounding),key=lambda b:b[1][i],reverse=reverse))
    (c,bounding)=zip(*sorted(zip(c,bounding),key=lambda b:b[1][i],reverse=reverse))
    return (c,bounding)
AnswerKey={0:1, 1: 2, 2: 0, 3: 3, 4: 1}

image=cv2.imread("OMR.png")
before=image.copy()
cv2.putText(before,"BEFORE",(50,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(120,50,250),2)
cv2.imshow("Before",before)
cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)

edged=cv2.Canny(blur,75,200)
cnts=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sorted(cnts,key=cv2.contourArea)[:5]
for c in cnts:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True)
    if len(approx)==4:
        scr=approx
        break
#cv2.drawContours(image,[scr],-1,255,2)
warped=four_point_transform(image,scr.reshape(4,2))
paper=four_point_transform(gray,scr.reshape(4,2))
after=warped.copy()
cv2.putText(after,"AFTER",(50,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(120,50,250),2)
cv2.imshow("After",after)
cv2.waitKey(0)

#blur=cv2.GaussianBlur(warped,(5,5),0)
#gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
#edged=cv2.Canny(gray,70,135)
thresh = cv2.threshold(paper, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
qst_cnt=[]
for c in cnts:
    (x,y,w,h)=cv2.boundingRect(c)
    ar=w/float(h)
    if w>=20 and h>=20 and ar>=0.9 and ar<=1.1:
        qst_cnt.append(c)
#for i in qst_cnt:
    #cv2.drawContours(warped,[i],-1,255,3)
qst_cnt=sort_contours(qst_cnt,order="top-to-bottom")[0]
correct=0
#print(np.arange(0,26,5))
#print(len(qst_cnt))
for (q,i) in enumerate(np.arange(0,len(qst_cnt),5)):
    cnt=sort_contours(qst_cnt[i:i+5])[0]
    bubble=None
    for (c,j) in enumerate(cnt):
        mask=np.zeros(thresh.shape,dtype="uint8")
        cv2.drawContours(mask,[j],-1,255,-1)
        new=cv2.bitwise_and(thresh,thresh,mask=mask)
        total=cv2.countNonZero(new)
        if bubble is None  or  bubble[0]<total:
            bubble=(total,c)  
    my_ans=bubble[1]
    answer=AnswerKey[q]
    color=[0,0,255]

    if my_ans==answer:
        color=[255,0,0]
        correct+=1
    cv2.drawContours(warped,[cnt[answer]],-1,color,2)

score=(correct/5)*100
print(score)
cv2.putText(warped,"{:.2f}%".format(score),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,120,50),2)
cv2.imshow("Final Result",warped)
before=imutils.resize(before,height=after.shape[0])
cv2.imwrite("OMR.jpg",np.hstack([before,after,warped]))
#cv2.imshow("OMR gray",thresh)
cv2.waitKey(0)
