# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:08:21 2019

@author: rdayala
"""

import cv2

# load the image, convert it to grayscale
image = cv2.imread("images/beach.png")
# image = cv2.imread("images/horseshoe_bend.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization to stretch the contrast of our image
eq = cv2.equalizeHist(image)

print(eq[272,146])
# show our images -- notice how the contrast of the second image has
# been stretched
cv2.imshow("Original", image)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)
cv2.destroyAllWindows()