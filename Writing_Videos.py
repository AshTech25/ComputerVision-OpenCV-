import cv2
import imutils
import numpy as np
from VideoStream import VideoStream
from KeyClipWrite import KeyClipWriter
outputfile="Ash"
write=None
vs=VideoStream(src=0).start()
fourcc="MJPG"
fps=20
(h,w)=(None,None)
#kcw=KeyClipWriter(32,1.0)
#frame=vs.read()
#frame=imutils.resize(frame,width=600)

#kcw.update(frame)
while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=300)
    
    
    if write is None:
        out="{}.avi".format(outputfile)
        (h,w)=frame.shape[:2]
        write=cv2.VideoWriter(out,cv2.VideoWriter_fourcc(*fourcc),fps,(w*2,h*2),True)
        
    zeros=np.zeros(frame.shape[:2],dtype="uint8")
    (B,G,R)=cv2.split(frame)
    R=cv2.merge([zeros,zeros,R])
    G=cv2.merge([zeros,G,zeros])
    B=cv2.merge([B,zeros,zeros])
        #R=(zeros,zeros,R)
        #G=(zeros,G,zeros)
        #B=(B,zeros,zeros)
    output=np.zeros((h*2,w*2,3),dtype="uint8")
    output[0:h,0:w]=frame

    output[h:h*2,0:w]=R
    output[0:h,w:w*2]=G
    output[h:h*2,w:w*2]=B
    write.write(output)
    
    #if not kcw.Recording:
     #   kcw.start(out,cv2.VideoWriter_fourcc(*fourcc),fps)
    #kcw.update(output)
    cv2.imshow("VideoRecording",output)
    cv2.imshow("Frames",frame)
    key=cv2.waitKey(1) or 0xFF
    if key == ord("q"):
        break
#kcw.finish()
cv2.destroyAllWindows()
vs.stop()
write.release()

