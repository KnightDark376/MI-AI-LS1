import cv2
import numpy as np
import imutils
#doc anh xam vao bien image
image = cv2.imread("example1.png")
cv2.imshow("anh mau", image)
cv2.waitKey()
#convert thanh anh xam
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#threshold
#ret, thresh_binary = cv2.threshold(gray_image,127,127,cv2.THRESH_BINARY_INV)
thresh_binary = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,1 )
image, contours = cv2.findContours(thresh_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(image,contours, -1, (0, 255, 0), 2)


cv2.imshow("Anh", image)
cv2.waitKey()
cv2.destroyAllWindows()

