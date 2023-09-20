import cv2

img = cv2.imread("moon.jpg")
print("img resize:", img.shape)
cv2.imshow("Originally", img)

#resized
imgResized = cv2.resize(img, (800,800))
print("Resized img shape", imgResized.shape)
cv2.imshow("img Resized", imgResized)

#Cropped
imgCropped = img[:200,:300]
cv2.imshow("Cropped img", imgCropped)

cv2.waitKey()










