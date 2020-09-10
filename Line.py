import cv2
image=cv2.imread("finding_shapes_example.png")
cv2.line(image,(0,0),(200,200),(255,0,0),2)
cv2.putText(image,"YO BRO", (0,200),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
