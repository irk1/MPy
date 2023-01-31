import cv2 #downloads stuffs
video_capture = cv2.VideoCapture(0) #hijacks webcam
while True: #stuffs go brrrrr
    if not video_capture.isOpened(): #makes stuffs stop brrrr
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, frame = video_capture.read() #yoinks images from video

#STUFF THAT FIND ORANGE PIXELS GOES HERE
#



    cv2.imshow('Video', frame,)#converts the yoinked frames into pretty pictures and displays them
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
