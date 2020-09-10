from threading import Thread
import cv2
class VideoStream:
    def __init__(self,src=0):
        self.stream=cv2.VideoCapture(src)
        (self.grabbed,self.frame)=self.stream.read()
        self.stopped=False
    def start(self):
        Thread(target=self.update,args=()).start()
        return self
    def update(self):
        while True:
            if self.stopped==True:
                return self
            (self.grabbed,self.frame)=self.stream.read()
    def read(self):
        return self.frame

    def stop(self):
        self.stopped=True
