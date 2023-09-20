import cv2
import numpy as np

#image import
img = cv2.imread("moon.jpg")
cv2.imshow("Original", img)

#Horizontal
hor = np.hstack((img,img))
cv2.imshow("horizontal", hor)

#Vertical
ver = np.vstack((img,img))
cv2.imshow("vertical", ver)


cv2.waitKey()

