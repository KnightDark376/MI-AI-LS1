import cv2
camera_id = 'Sample.mp4'
#mo camera
cap = cv2.VideoCapture(camera_id)
#doc anh tu camera
while True:
    # Doc tung frame
    ret, frame = cap.read()
    #hien anh
    cv2.imshow("Video",frame)
    # kiem tra neu bam Q thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#giai phong camera
cap.release()
cv2.destroyAllWindows()