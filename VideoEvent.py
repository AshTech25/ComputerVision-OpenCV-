from KeyClipWrite import KeyClipWriter
import cv2
import imutils
import numpy as np
from VideoStream import VideoStream
import datetime
import time
import argparse

vid=VideoStream(0).start()
time.sleep(2.0)
output="AshirTestVid"
fourcc="MJPG"
fps=20
i=0
buffersize=64
kwc=KeyClipWriter(buffersize,1.0)
green1=(29,86,6)
green2=(64,255,255)
ap = argparse.ArgumentParser()
#ap.add_argument("-o", "--output", required=True,
	#help="path to output directory")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
	help="codec of output video")
args = vars(ap.parse_args())
frame=vid.read()
frame=imutils.resize(frame,width=600)
kwc.update(frame)

while True:
    
    frame=vid.read()
    
    updateConsecFrame=True
    frame=imutils.resize(frame,width=600)
    blur=cv2.GaussianBlur(frame,(11,11),0)
    
    #hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(blur,green1,green2)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)

    if len(cnts)>0:
        
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        updateConsecFrame=radius<=10
    

        if (radius>10):
            consecFrame=0
            cv2.circle(frame,(int(x),int(y)),int(radius),(255,0,0),1)
            if not kwc.Recording:
                timestamp=datetime.datetime.now()
                p="output.avi"
					#timestamp.strftime("%Y%m%d-%H%M%S"))
                kwc.start(p,cv2.VideoWriter_fourcc(*args["codec"]),fps)
                
                print("Started recording"+str(i))
                i=i+1
    if updateConsecFrame:
        consecFrame+=1
     
    kwc.update(frame)
    if kwc.Recording and consecFrame==buffersize:
        kwc.finish()
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
		
        

if kwc.Recording:
    kwc.finish()
cv2.destroyAllWindows()
vid.stop()