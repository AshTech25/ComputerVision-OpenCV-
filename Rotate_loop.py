import cv2
import imutils
import numpy as np
image=cv2.imread("MUNA.jpg")
(h,w,d)=image.shape
nw=400
nh=nw*(h/w)
new_image=cv2.resize(image,(nw,int(nh)))
npdata=np.arange(0,360,15)
for angle in npdata:
    rotate=imutils.rotate(new_image,angle)
    cv2.imshow("Image",rotate)
    cv2.waitKey(0)