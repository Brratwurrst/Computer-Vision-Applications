
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    start_time = time.time()
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Find the brightest spot in the image
   # (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    
    # Find the reddest spot
    # Split the frame into R, G, B channels
    b, g, r = cv2.split(frame)
    
    for i in frame
    # Find the reddest spot in the R channel
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(r)
    
    # Draw a circle around the reddest spot
    cv2.circle(frame, maxLoc, 20, (0, 255, 0), 2)
    

    # Draw a circle around the brightest spot
    #cv2.circle(frame, maxLoc, 20, (255, 0, 0), 2)
    
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

