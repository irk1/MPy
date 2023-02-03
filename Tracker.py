import cv2
import numpy as np
import time

# Define the color range for orange in HSV color space
lower_orange = np.array([10, 125, 125])
upper_orange = np.array([13, 255, 255])

# Load the video capture
cap = cv2.VideoCapture(0) # 0 for default camera

while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the frame to get only orange pixels
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Find the moments of the thresholded image
    moments = cv2.moments(mask)

    # Check if moments have been found (i.e. there's an orange object in the frame)
    if moments["m00"] != 0:
        # Calculate the x,y coordinates of the center of the object
        x = int(moments["m10"] / moments["m00"])
        y = int(moments["m01"] / moments["m00"])

        # Divide the screen into a 9x9 grid and find which grid the object is in
        grid_x = x // (frame.shape[1] // 3)
        grid_y = y // (frame.shape[0] // 3)

        # Print the result
        print("Object is in grid: ", (grid_x, grid_y))
        if grid_x == 0 and grid_y == 0:
            print("right,down")
        elif grid_x == 1 and grid_y == 0:
            print("down")
        elif grid_x == 2 and grid_y == 0:
            print("left,down")
            ###
        elif grid_x == 0 and grid_y == 1:
            print("right")
        elif grid_x == 1 and grid_y == 1:
            print(" ")
        elif grid_x == 2 and grid_y == 1:
            print("left")
            ###
        elif grid_x == 0 and grid_y == 2:
            print("right,up")
        elif grid_x == 1 and grid_y == 2:
            print("up")
        elif grid_x == 2 and grid_y == 2:
            print("left,up")





    #   00 10 20
    #   01 11 21
    #   02 12 22
        time.sleep(0.1)

    cv2.imshow("masked",mask)
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()
cv2.destroyAllWindows()
