import cv2
#Đọc ảnh
img = cv2.imread('Capture.PNG')
cv2.imshow("Anh_goc",img)
cv2.waitKey() == ord("1")
# Lấy cao, rộng
(h, w) = img.shape[:2]
# Tính tâm bức ảnh, góc quay và mức độ scale
center = (w / 2, h / 2)
angle90 = 45
scale = 1.0
# Quay ngược 90 độ
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))
samller_image = cv2.resize(rotated90,dsize=(500,500))
cv2.imshow("Rotate",samller_image)
cv2.waitKey() == ord("2")
samller_image1 = cv2.cvtColor(samller_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh_gray",samller_image1)
cv2.waitKey() == ord(" ")
cv2.destroyAllWindows()