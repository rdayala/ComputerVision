# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:40:24 2019

@author: rdayala
"""

# bitwise with 2 color images
import numpy as np
import cv2

image1 = cv2.imread("images/messi.png")
image2 = cv2.imread("images/obama.png")

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)

cv2.waitKey(0)

# both images should be of same size
(h1, w1) = image1.shape[:2]
(h2, w2) = image2.shape[:2]

ratio = w2 / float(h2)

resize1 = cv2.resize(image1, (w2, h2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resize Image1", resize1)
cv2.waitKey(0)

bitwiseAnd = cv2.bitwise_and(resize1, image2)
cv2.imshow("Bitwise And", bitwiseAnd)
cv2.waitKey(0)

colorImage1 = np.ones((300,300, 3), dtype = "uint8") * 127
cv2.imshow("Color Image 1", colorImage1)
cv2.waitKey(0)

colorImage2 = np.ones((300,300, 3), dtype = "uint8") * 200
cv2.imshow("Color Image 2", colorImage2)
cv2.waitKey(0)

bitwiseAnd2 = cv2.bitwise_and(colorImage1, colorImage2)
cv2.imshow("Bitwise And 2", bitwiseAnd2)
cv2.waitKey(0)

# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = colorImage1[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = colorImage2[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = bitwiseAnd2[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

cv2.destroyAllWindows()