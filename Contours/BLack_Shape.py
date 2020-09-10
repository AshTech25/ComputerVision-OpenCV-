import cv2
import imutils
import numpy 
import argparse

ap= argparse.ArgumentParser()
ap.add_argument("-i","--input",required=True,help="Insert input path")
ap.add_argument("-o","--output",required=True,help="Insert output path")
args=vars(ap.parse_args())

image=cv2.imread(args["input"])

lower=numpy.array([0,0,0])
upper=numpy.array([15,15,15])

new=cv2.inRange(image,lower,upper)

cnts=cv2.findContours(new.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
text = "I found {} shapes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
		(0, 0, 255), 2)

for c in cnts:
    cv2.drawContours(image,[c],-1,(255,0,0),2)

cv2.imwrite(args["output"], image)
cv2.imshow("Image",new)
cv2.waitKey(0)

