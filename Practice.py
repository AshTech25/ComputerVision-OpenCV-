
import cv2
image = cv2.imread("Im.jpg")
(h,w,d)=image.shape
print("width={},hieght={},depth={}".format(w,h,d))
cv2.imshow("Image",image)

(B,G,R)=image[100,50]
print("R={},G={},B={}".format(R,G,B))
cv2.waitKey(0)