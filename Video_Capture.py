from VideoStream import VideoStream
import cv2
import imutils
import numpy as np
import time
fps=20
fourcc='MJPG'
write=None

vs=VideoStream().start()
time.sleep(10.0)
output='VideoforAttendance'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(frame,gray):
    epsilon=50
    myframe=frame
    faces= face_cascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(myframe,(x-epsilon,y-epsilon),(x+w+epsilon,y+h+epsilon),(255,0,0),2)
            
    return myframe

while True:
    frame=vs.read()
    frame=imutils.resize(frame,height=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
    canvas = detect(frame, gray) # We get the output of our detect function.
    (h,w)=frame.shape[:2]
    if write is None:
        out="{}.avi".format(output)
        write=cv2.VideoWriter(out,cv2.VideoWriter_fourcc(*fourcc),fps,(w,h),True)
        #zeros=np.zero
        
    
    #if not kcw.Recording:
     #   kcw.start(out,cv2.VideoWriter_fourcc(*fourcc),fps)
    #kcw.update(output)
    #cv2.imshow("VideoRecording",output)
    cv2.imshow("Frames",canvas)
    
    write.write(frame)
    key=cv2.waitKey(1) or 0xFF
    if key == ord("q"):
        break
#kcw.finish()
cv2.destroyAllWindows()
vs.stop()
write.release()




    