import cv2


image=cv2.imread("IM.jpg")
(h,w,d)=image.shape
radius=100
processed_img=cv2.circle(image.copy(),(100,50),radius,(255,2,20),2)
cv2.imshow("Image",processed_img)
cv2.waitKey(0)
