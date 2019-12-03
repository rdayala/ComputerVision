# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:07:36 2019

@author: rdayala
"""

# translation
import numpy as np
import cv2

image = np.zeros((300, 300, 3), dtype="uint8")
image[:] = (0, 255, 0)
cv2.imshow("Original Image", image)
cv2.waitKey(0)

(h, w) = image.shape[:2]

# define Translation matrix
# shift to right
M = np.float32([[1, 0, 150], [0, 1, 0]])
shiftedRight = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted Right", shiftedRight)
cv2.waitKey(0)

# shift to left
M = np.float32([[1, 0, -150], [0, 1, 0]])
shiftedLeft = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted Left", shiftedLeft)
cv2.waitKey(0)

# shift to top
M = np.float32([[1, 0, 0], [0, 1, -150]])
shiftedTop = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted Top", shiftedTop)
cv2.waitKey(0)

# shift to down
M = np.float32([[1, 0, 0], [0, 1, 150]])
shiftedDown = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted Down", shiftedDown)
cv2.waitKey(0)

# shift to right & down
M = np.float32([[1, 0, 100], [0, 1, 150]])
shiftedRightDown = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted Right & Down", shiftedRightDown)
cv2.waitKey(0)


cv2.destroyAllWindows()