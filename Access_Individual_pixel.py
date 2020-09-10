import cv2
import imutils

image=cv2.imread("finding_shapes_example.png")
(w,h,d)=image.shape
#image[20,20]=(50,100,0)
#(B,G,R)=image[20,20]
#print("Red={} Blue={} Green={}".format(R,G,B))
i=0
j=0
for i in range(w):
    for j in range(h):
        (B,G,R)=image[i,j]
        if (B,G,R)==(0,0,0):
            image[i,j]=(0,255,126)
cv2.imshow("IP",image)

cv2.imwrite("OUTPUT",image)
cv2.waitKey(0)

