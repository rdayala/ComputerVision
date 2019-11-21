# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:14:05 2019

@author: rdayala
"""

# import the necessary packages
import cv2
 
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
 
	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# clean up the camera and close any open windows
camera.release()
cv2.destroyAllWindows()