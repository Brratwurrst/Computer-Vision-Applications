
import cv2
import time
import numpy as np

cap = cv2.VideoCapture('http://192.168.1.76:8080/video?type=some.mjpeg')

while(True):
    start_time = time.time()
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Find the brightest spot in the image
    (minValb, maxValb, minLocb, maxLocb) = cv2.minMaxLoc(gray)
    
#    # Initialize maximum brightness and redness values and their corresponding locations
#     max_brightness = 0
#     max_brightness_loc = (0, 0)
#     max_redness = 0
#     max_redness_loc = (0, 0)
    
#     # Iterate over each pixel in the frame
#     for y in range(frame.shape[0]):
#         for x in range(frame.shape[1]):
#             # Calculate brightness as the sum of the B, G, R values
#             brightness = int(frame[y, x, 0]) + int(frame[y, x, 1]) + int(frame[y, x, 2])
            
#             # Update maximum brightness value and location
#             if brightness > max_brightness:
#                 max_brightness = brightness
#                 max_brightness_loc = (x, y)
            
#             # Calculate redness as the R value minus the average of the B and G values
#             redness = int(frame[y, x, 2]) - (int(frame[y, x, 0]) + int(frame[y, x, 1])) / 2
            
#             # Update maximum redness value and location
#             if redness > max_redness:
#                 max_redness = redness
#                 max_redness_loc = (x, y)
    
#     # Draw circles around the brightest and reddest spots
#     cv2.circle(gray, max_brightness_loc, 20, (0, 255, 0), 2)
#     cv2.circle(frame, max_redness_loc, 20, (255, 0, 0), 2)


    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range for red color
    lower_red = np.array([-40, 100, 100])
    upper_red = np.array([40, 255, 255])
    
    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Convert the result to grayscale
    graymask = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    
    # Find the brightest spot in the grayscale image
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(graymask)
    
    # Draw a circle around the brightest spot
    cv2.circle(frame, maxLoc, 20, (0, 255, 0), 2)

    # Draw a circle around the brightest spot
    cv2.circle(gray, maxLocb, 20, (255, 0, 0), 2)
    
    # Calculate FPS
    fps = 1.0 / (time.time() - start_time)
    
    # Display FPS on the frame
    cv2.putText(frame, "FPS : " + str(round(fps,2)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(gray, "FPS : " + str(round(fps,2)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('frame', gray)
    
    cv2.imshow('colour', frame)
    
   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

