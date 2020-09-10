import cv2
import imutils

image=cv2.imread("tetris.png")
(h,w,d)=image.shape
new_width=400
new_height=int(new_width*(h/w))
image=cv2.resize(image,(new_width,new_height))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
threshold=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cnt=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=imutils.grab_contours(cnt)
cv2.drawContours(image,cnt,-1,(255,0,0),2)
text="I found {} shapes".format(len(cnt))
cv2.putText(image,text,(10,25),cv2.FONT_HERSHEY_SIMPLEX, 1,(240, 0, 159), 2)
print(cnt)
cv2.imshow("Image",image)
cv2.waitKey(0)