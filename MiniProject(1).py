import cv2
import numpy as np
import imutils

image=cv2.imread("pill.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 20, 100)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
mask=np.zeros(gray.shape,dtype="int8")
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	c = max(cnts, key=cv2.contourArea)
	#mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)
#for angle in np.arange(0, 360, 15):
	##	cv2.imshow("Rotated (Problematic)", rotated)
	#	cv2.waitKey(0)
	# loop over the rotation angles again, this time ensure the
	# entire pill is still within the ROI after rotation
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(imageROI, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(0)