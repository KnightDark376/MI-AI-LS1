import cv2
import imutils
camera_id = 0
# Kai bao doi tuong video
image = cv2.imread("Capture.PNG")
rotate = 0
while True :


    if rotate != 0:
        farme = imutils.rotate(frame,rotate)
        cv2.imshow("Anh tu wecam", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        rotate = 90
    elif key == ord('d'):
        rotate = -90
cv2.destroyAllWindows()
