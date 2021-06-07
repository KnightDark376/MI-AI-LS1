import cv2
camera_id = 0
# Kai bao doi tuong video
video = cv2.VideoCapture(camera_id)

while True :
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR5552BGR)
        cv2.imshow("Anh tu wecam",frame)
    if cv2.waitKey(1) == ord(" "):
        break
video.release()
cv2.destroyAllWindows()