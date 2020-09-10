import cv2
import imutils

image=cv2.imread("tetris.png")
(h,w,d)=image.shape
new_width=400
new_height=int(new_width*(h/w))
image=cv2.resize(image,(new_width,new_height))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
threshold=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
mask=cv2.erode(threshold,None,iterations=5)
mask=cv2.dilate(threshold,None,iterations=5)
cv2.imshow("Image",mask)
cv2.waitKey(0)