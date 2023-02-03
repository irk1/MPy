import cv2 #downloads stuffs
import numpy as np
video_capture = cv2.VideoCapture(0) #hijacks webcam
while True: #stuffs go brrrrr
    if not video_capture.isOpened(): #makes stuffs stop brrrr
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, frame = video_capture.read() # (ret will return a true value if the frame exists otherwise False)

    into_hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    # changing the color format from BGr to HSV

#STUFF THAT FIND BLUE PIXELS GOES HERE

#100,45,25
#255,150,50

    L_limit=np.array([11,191,100]) # setting the color lower limit
    U_limit=np.array([21,205,255]) # setting the color upper limit
    b_mask=cv2.inRange(into_hsv,L_limit,U_limit) #creating the mask using inRange() function this will produce an image where the color of the objects falling in the range will turn white and rest will be black
    blue=cv2.bitwise_and(frame,frame,mask=b_mask) #makes the mask pretty
    cv2.imshow('Original', frame)#converts the yoinked frames into pretty pictures and displays them
    cv2.imshow('Color Detector',blue)
    cv2.imshow('Color',b_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'): #shuts up python program
        break
    if cv2.waitKey(1)==27: #SCRAM button for nuclear reactor located at 40.45400062787497, -74.05143604797301
        break

video_capture.release()
cv2.destroyAllWindows()
