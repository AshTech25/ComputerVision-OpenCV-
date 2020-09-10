import cv2
import imutils
from VideoStream import VideoStream
from MotionClass import Motion
import time
import numpy as np
import datetime

vs1=VideoStream(src=0).start()
vs2=VideoStream(src=1).start()
time.sleep(15.0)
motion1=Motion()
motion2=Motion()
image=cv2.imread("MUNA.jpg")
total=0
while True:
    frames=[]
    for (stream,motion) in zip((vs1,vs2),(motion1,motion2)):
        frame=stream.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)
        locs=motion.update(gray)
        if total>32:
            frames.append(frame)
        if len(locs)>0:
            (max_x,max_y)=(-np.inf,-np.inf)
            (min_x,min_y)=(np.inf,np.inf)
        for l in locs:
            (x,y,w,h)=cv2.boundingBox(l)
            (minx,maxx)=(min(min_x,x),max(max_x,x+w))
            (miny,maxy)=(min(min_y,y),max(max_y,y+h))
            cv2.rectangle(frame,(minx,miny),(maxx,maxy),(255,0,0),2)
        frames.append(frame)
        total=total+1
        timestamp=datetime.datetime.now()
        ts=timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        for (frame, name) in zip(frames, ("Webcam", "Picamera")):
            cv2.putText(frame, ts, (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.imshow(name,frame)
            #cv2.imshow(name[1],frame[1])
		
        key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	    if key == ord("q"):
		    break
cv2.destroyAllWindows()
vs1.stop()
vs2.stop()
    