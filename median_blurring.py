# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:18:58 2019

@author: rdayala
"""

import cv2

# load the image, display it, and initialize the list of kernel sizes
image = cv2.imread("images/Rana1.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", image)
cv2.waitKey(0)

kernelSizes = [(3, 3), (5, 5), (9, 9), (15, 15)]
 
# loop over the kernel sizes and apply a "Median" blur to the image
for k in (3, 5, 7, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)
    
blurred_7 = cv2.medianBlur(image, 7)
cv2.imwrite("images/Rana1_smooth.jpg", blurred_7)
    
cv2.destroyAllWindows()