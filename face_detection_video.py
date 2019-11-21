# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:17:34 2019

@author: rdayala
"""

# import the necessary packages
import cv2

# load the face detector
detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
 
# grab the reference to the webcam
camera = cv2.VideoCapture(0)

# keep looping
while True:
    
    # grab the current frame
    (grabbed, frame) = camera.read()
    
    # if we are viewing a video and we did not grab a
    # frame, then we have reached the end of the video
    if not grabbed:
        break
    
    # resize
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # handle face detection
    faceRects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,
			minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # loop over the faces and draw a rectangle around each
    for (x, y, w, h) in faceRects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # show the frame to our screen
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
 
# clean up the camera and close any open windows
camera.release()
cv2.destroyAllWindows()