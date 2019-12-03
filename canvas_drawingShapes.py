# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:05:46 2019

@author: rdayala
"""

import numpy as np
import cv2

# creating a black canvas
canvas = np.zeros((450, 600, 3), dtype="uint8")

cv2.imshow("Black Canvas", canvas)
cv2.waitKey(0)

# cv2.line(srcImage, startPoint, endPoint, lineColor, thickness)
cv2.line(canvas, (30,30), (300, 300), (0, 255, 0), 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw another rectangle, this time we'll make it red and 5 pixels thick
red = (0, 0, 255)
cv2.rectangle(canvas, (0, 200), (200, 400), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
 
# let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
cv2.circle(canvas, (centerX, centerY), 100, white, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# random circles
# let's go crazy and draw 25 random circles
for i in range(0, 25):
	# randomly generate a radius size between 5 and 200, generate a random
	# color, and then pick a random point on our canvas where the circle
	# will be drawn
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size = (3,)).tolist()
	pt = np.random.randint(0, high=300, size = (2,))
 
	# draw our random circle
	cv2.circle(canvas, tuple(pt), radius, color, -1)
 
# Show our masterpiece
cv2.imshow("Random circles", canvas)
cv2.waitKey(0)

# change the canvas color to green
canvas[:] = (0, 255, 0)
cv2.imshow("Green canvas", canvas)
cv2.waitKey(0)

# Using NumPy full method to fill the canvas with a color intensity values
redCanvas = np.full((450, 600, 3), (0, 0, 255), dtype="uint8")
cv2.imshow("Red Canvas", redCanvas)
cv2.waitKey(0)

# drawing concentric circles
# create canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(h, w) = canvas.shape[:2]
(cX, cY) = (w // 2, h // 2)
white = (255, 255, 255)
 
for r in range(0, 175, 25):
	cv2.circle(canvas, (cX, cY), r, white)
 
# show our work of art
cv2.imshow("Concentric circles", canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()
