import cv2
import imutils
import numpy as np
image=cv2.imread("MUNA.jpg")
npdata=np.arange(0,360,15)
for angle in npdata:
    rotate=imutils.rotate(image,angle)
    cv2.imshow("Image",image)
    cv2.waitKey(0)