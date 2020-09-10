import numpy as np
import cv2
import imutils

source=cv2.imread("1d7eb759ffa3f19c03dc2cbfe9653d85676f.jpg")
target=cv2.imread("UsmanT.jpg")

def color_transfer(source,target):
    source=cv2.cvtColor(source,cv2.COLOR_BGR2LAB).astype("float")
    target=cv2.cvtColor(target,cv2.COLOR_BGR2LAB).astype("float")

    (lMeanTar,lStdTar,aMeanTar,aStdTar,bMeanTar,bStdTar)=image_stats(target)
    (lMeanSrc,lStdSrc,aMeanSrc,aStdSrc,bMeanSrc,bStdSrc)=image_stats(source)

    (l,a,b)=cv2.split(target)
    l=l-lMeanTar
    a=a-aMeanTar
    b=b-bMeanTar

    l=(lStdTar/lStdSrc)*l
    a=(aStdTar/aStdSrc)*a
    b=(bStdTar/bStdSrc)*b

    l=l+lMeanSrc
    a=a+aMeanSrc
    b=b+bMeanSrc

    l=np.clip(l,0,255)
    a=np.clip(a,0,255)
    b=np.clip(b,0,255)

    transfer=cv2.merge([l,a,b])
    transfer=cv2.cvtColor(transfer.astype("uint8"),cv2.COLOR_LAB2BGR)
    return transfer


def image_stats(img):
    (l,a,b)=cv2.split(img)
    (lMean,lStd)=(l.mean(),l.std())
    (aMean,aStd)=(a.mean(),a.std())
    (bMean,bStd)=(b.mean(),b.std())
    return (lMean,lStd,aMean,aStd,bMean,bStd)

def Aspect_Ratio(img):
    (h,w,d)=img.shape
    nw=600
    aR=w/h
    nh=int(nw/aR)
    img=cv2.resize(img,(nw,nh))
    return img


aesthetic=color_transfer(source,target)
aesthetic=Aspect_Ratio(aesthetic)
(h,w,d)=aesthetic.shape
source=cv2.resize(source,(w,h))
target=cv2.resize(target,(w,h))
#(h,w,d)=aesthetic.shape
#nw=400
#aR=(w/h)
#nh=int(nw/aR)
#aesthetic=cv2.resize(aesthetic,(nw,nh))

cv2.imshow("Color Transfer",np.hstack([source,target,aesthetic]))
cv2.waitKey(0)