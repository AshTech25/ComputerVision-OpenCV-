import cv2
import imutils

class Motion:
    def __init__(self,delta_thresh=5,accumWeight=0.5,minArea=5000):
        self.delta=delta_thresh
        self.accumWeight=accumWeight
        self.avg=None
        self.minArea=5000
    def update(self,image):
        locs=[]
        if self.avg is None:
            self.avg=image.astype("float")
            return locs
        cv2.accumWeighted(image,self.avg,self.accumWeight)
        diff=cv2.absdiff(image,cv2.convertScaleAbs(self.avg))
        thresh=cv2.threshold(image,self.delta,255,cv2.THRESH_BINARY)[1]
        thresh=cv2.dilate(thresh,None,iterations=2)
        cnts=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            if cv2.ContourArea(c)>self.minArea:
                locs.append(c)
        return locs

