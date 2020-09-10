import cv2
import imutils

image=cv2.imread("finding_shapes_example.png")
(h,w,d)=image.shape
print("Width={} Height={} Depth={}".format(w,h,d))
new_width=int(input())
Aspect_Ratio=w/h
dim=(new_width,int(new_width/Aspect_Ratio))
resize=cv2.resize(image,dim)
cv2.imshow("Image",resize)
cv2.waitKey(0)
