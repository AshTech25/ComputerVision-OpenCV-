
import numpy as np
import imutils
import cv2

image1=cv2.imread("bryce_left_02.png")
image2=cv2.imread("bryce_right_02.png")
from KeyPoints import KeyPoints
import cv2
import imutils
import numpy as np

image1=cv2.imread("bryce_left_02.png")
image2=cv2.imread("bryce_right_02.png")
imageA=imutils.resize(image1,width=400)
imageB=imutils.resize(image2,width=400)
sticher=KeyPoints()
(res,vis)=sticher.stitch([imageA,imageB],showMatches=True)
cv2.imshow("Unstiched",np.hstack([imageA,imageB]))
cv2.imshow("Result",res)
cv2.imshow("Visual",vis)
cv2.waitKey(0)