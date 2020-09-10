import cv2
import imutils
from VideoStream import VideoStream
import time,datetime
import numpy as np
from KeyClipWrite import KeyClipWriter
fourcc="MJPG"
fps=20
vs=VideoStream(src=0).start()
kcw=KeyClipWriter(bufSize=32,timeout=1.0)
time.sleep(15.0)
init_frame=None
Min_Area=500
output="New1"
while True:
    text="Unoccupied"
    frame=vs.read()
    if frame is None:
        break
    frame=imutils.resize(frame,width=500)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    reduc=cv2.GaussianBlur(gray,(21,21),0)
    if init_frame is None :
        init_frame=reduc
        continue
    diff=cv2.absdiff(init_frame,reduc)
    thresh=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,iterations=2)
    cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<Min_Area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        text="Occupied"
        cv2.putText(frame,"Room Status:{} ".format(text),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),1)
        cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(int(frame.shape[1]-50),int(frame.shape[0]-50)),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0,255,255),1)
        
        kcw.update(frame)
        if not kcw.Recording:
            kcw.start("{}.avi".format(output),cv2.VideoWriter_fourcc(*fourcc),fps)

    cv2.imshow("Security",frame)
    #cv2.imshow("Processing",init_frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
vs.stop()
kcw.finish()
cv2.destroyAllWindows()
