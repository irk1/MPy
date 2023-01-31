import cv2
video_capture = cv2.VideoCapture(0)
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, frame = video_capture.read()

    cv2.imshow('Video', frame,)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
