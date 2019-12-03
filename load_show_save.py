# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:40:10 2019

@author: rdayala
"""

# load, display, save based on key pressed

import cv2

image = cv2.imread("images/messi.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image is not loaded")
    exit

cv2.imshow("Grayscale Image", image)

key = cv2.waitKey(0) # & 0xFF

# if ESC key is pressed
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    print("Saving file..")
    cv2.imwrite("images/messi_grayscale.jpg", image)
    cv2.destroyAllWindows()


