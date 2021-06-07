import cv2
import imutils
#doc anh mau vao bien image
image = cv2.imread("Sample.PNG")
cv2.imshow("anh mau", image)
cv2.waitKey()

#convert anh xam
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image,threshold1=50, threshold2=100)
cv2.imshow("anh edges", edges)
cv2.waitKey()
