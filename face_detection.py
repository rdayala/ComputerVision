# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 07:43:45 2019

@author: rdayala
"""

import cv2

# load the image, convert it to grayscale
# image = cv2.imread("images/messi.png")
image = cv2.imread("images/obama.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

faceRects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,
        minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
  
print("I found {} face(s)".format(len(faceRects)))
  
# loop over the faces and draw a rectangle around each
for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
# show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()