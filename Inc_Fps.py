from FPS import FPS
from VideoStream import VideoStream
import cv2
import imutils

limit=500
display=True
video=cv2.VideoCapture(0)
fps=FPS().start()
while (fps._numframes<limit):
    (grab,frames)=video.read()
    frames = imutils.resize(frames, width=400)

    if (display):
        cv2.imshow("Frames",frames)
        key=cv2.waitKey(1) & 0xFF
    fps.update()
fps.stop()
calc=fps.fps()
print("Elapsed time is : {:2f}".format(fps.elapsed()))
print("Total fps is : {:2f}".format(calc))

tvideo=VideoStream(src=0).start()
tfps=FPS().start()
while (tfps._numframes<limit):
    frame=tvideo.read()
    frame = imutils.resize(frame, width=400)

    if (display):
        cv2.imshow("TFrame",frame)
        key=cv2.waitKey(1) & 0xFF
    tfps.update()
tfps.stop()

calc=tfps.fps()
print("Elapsed time is : {:2f}".format(tfps.elapsed()))
print("Total fps is : {:2f}".format(calc))
