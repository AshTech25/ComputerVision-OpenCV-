import cv2
import imutils
from imutils import paths
import imutils
import numpy as np
imagePath="E:/KU 4th Year Work/Computer Vision/scottsdale"
imagePath=sorted(list(paths.list_images(imagePath)))
images=[]
crop=1
for imageP in imagePath:
    image=cv2.imread(imageP)
    images.append(image)
stitcher=cv2.createStitcher() if imutils.is_cv3()  else cv2.Stitcher_create()
(status,stitched)=stitcher.stitch(images)
if status==0:
    #cv2.imwrite("E:/KU 4th Year Work/Computer Vision/Fika.jpg",stitched)
    if crop>1:
        stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,
			cv2.BORDER_CONSTANT, 0)

        gray=cv2.cvtColor(stitched,cv2.COLOR_BGR2GRAY)
#lur=cv2.GaussianBlur(gray,(11,11),0)
        thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY)[1]
        cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(cnts)
        c=max(cnts,key=cv2.contourArea)
        (x,y,w,h)=cv2.boundingRect(c)
        mask=np.zeros(thresh.shape,dtype="uint8")
        cv2.rectangle(mask,(x,y),(x+w,y+h),255,-1)
        minRec=mask.copy()
        sub=mask.copy()
        while cv2.countNonZero(sub)>0:
            minRec=cv2.erode(minRec,None)
            sub=cv2.subtract(minRec,thresh)
        cv2.imshow("thresh",minRec)
        cv2.waitKey(0)
#minRec=cv2.threshold(minRec,0,255,cv2.THRESH_BINARY)[1]
        cnts=cv2.findContours(minRec.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(cnts)
        c=max(cnts,key=cv2.contourArea)
        (x,y,w,h)=cv2.boundingRect(c)
        stitch=stitched[y:y+h,x:x+w]
        cv2.imshow("Processed Image",stitch)
        cv2.waitKey(0)
    else:
        cv2.imshow("Stiched Image",stitched)
        cv2.waitKey(0)
else:
    print("Cannot do it-tick")


           

