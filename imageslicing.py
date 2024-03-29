# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:33:40 2019

@author: rdayala
"""

# this program, we try to display different parts of an image
# Using NumPy array slicing to break down the image into different parts
import numpy as np
import cv2

image = cv2.imread("images/messi.png");

cv2.imshow("Original", image)
cv2.waitKey(0)

# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

(h, w) = image.shape[:2]

# compute center of the image
(cX, cY) = (w // 2, h // 2)

# top left corner of an image
tl = image[0:cY, 0:cX]

# top right of the image
tr = image[0:cY, cX:w]

# bottom left of the image
bl = image[cY:h, 0:cX]

# bottom right corner of the image
br = image[cY:h, cX:w]

cv2.imshow("Top left", tl)
cv2.imshow("Top right", tr)
cv2.imshow("Bottom left", bl)
cv2.imshow("Bottom right", br)

cv2.waitKey(0)

# top of the image
top_image = image[0:cY]

# bottom of the image
bottom_image = image[cY:h]

cv2.imshow("Top image", top_image)
cv2.imshow("Bottom image", bottom_image)
cv2.waitKey(0)

# left of the image
left = image[:, 0:cX]

#right of the image
right = image[:, cX:w]

cv2.imshow("Left", left)
cv2.imshow("Right", right)
cv2.waitKey(0)

# copy an image using numpy
copy_image = np.copy(image)
cv2.imshow("Copy image", copy_image)
cv2.waitKey(0)

# change color of the top left of the image
copy_image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated image", copy_image)
cv2.waitKey(0)

cv2.destroyAllWindows()