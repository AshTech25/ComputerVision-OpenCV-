import cv2


image=cv2.imread("MUNA.jpg")
(h,w,d)=image.shape
new_width=400
new_height=int(new_width*(h/w))
image=cv2.resize(image,(new_width,new_height))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,60,150)

cv2.imshow("Image",edge)
cv2.waitKey(0)
