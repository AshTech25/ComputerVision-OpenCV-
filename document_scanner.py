import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local,try_all_threshold

imag=cv2.imread("Scan_this.png")
orig=imag.copy()
ratio=imag.shape[1]/500
image=imutils.resize(imag,width=500)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edge=cv2.Canny(blur,75,150)
cv2.imshow("edge",edge)
cv2.waitKey(0)
cnts=cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
max_cnt=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]
for c in max_cnt:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.05*peri,True)

    if len(approx)==4:
        scr=approx
        break
print(scr)
cv2.drawContours(image,[scr],-1,(0,255,0),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


def order_points(cnt):
    rect=np.zeros((4,2),dtype="float32")
    s=cnt.sum(axis=1)
    rect[0]=cnt[np.argmin(s)]
    rect[2]=cnt[np.argmax(s)]
    diff=np.diff(cnt,axis=1)
    rect[1]=cnt[np.argmin(diff)]
    rect[3]=cnt[np.argmax(diff)]
    return rect


def four_point_transform(image,pts):
 peck = order_points(pts)
 (tl, tr, br, bl) = peck
 widthA=np.sqrt(((tl[0]-tr[0])**2) + ((tl[1]-tr[1])**2))
 widthB=np.sqrt(((bl[0]-br[0])**2) + ((bl[1]-br[1])**2))
 heightA=np.sqrt(((tl[0]-bl[0])**2) + ((tl[1]-bl[1])**2))
 heightB=np.sqrt(((tr[0]-br[0])**2) + ((tr[1]-br[1])**2))
         
 max_width=max(int(widthA),int(widthB))
 max_height=max(int(heightA),int(heightB)) 

 dist=np.array([
         [0,0],
         [max_width-1,0],
         [max_width-1,max_height-1],
         [0,max_height-1]
 ],dtype="float32")
 M=cv2.getPerspectiveTransform(peck,dist)
 warped=cv2.warpPerspective(image,M,(max_width,max_height))
 return warped



warped=four_point_transform(orig,scr.reshape(4,2)*ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
arped = (warped > T).astype("uint8") * 255
marped=try_all_threshold(warped, figsize=(10, 6), verbose=True)
marped=imutils.resize(warped,width=650)

arped=imutils.resize(arped,width=650)
cv2.imshow("Orig",marped)

cv2.imshow("Image",arped)
cv2.waitKey(0)






