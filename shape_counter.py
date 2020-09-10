import cv2
import argparse
import imutils
import numpy

ap=argparse.ArgumentParser()
ap.add_argument("-i","--input",required=True,help="insert input path")
ap.add_argument("-o","--output",required=True,help="output path")
args=vars(ap.parse_args())

image=cv2.imread(args["input"])
#gray=cv2.cvtColor(image,cv2.BGR2GRAY())
#blur=cv2.GaussianBlur(gray,(5,5),0)
#thresh=cv2.threshold(blur,(60,255),cv2.THRESH_BINARY)[1]
lower=numpy.array([0,0,0])
upper=numpy.array([255,255,255])
thresh=cv2.inRange(image,lower,upper)
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL(),cv2.CHAIN_APPROX_SIMPLE())
cnts=imutils.grab_contours(cnts)

for c in cnts:
    cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
    
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
		(0, 0, 255), 2)
 
# write the output image to disk
cv2.imwrite(args["output"], image)
cv2.imshow("Image",thresh)
