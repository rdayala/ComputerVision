# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:33:59 2019

@author: rdayala
"""
import numpy as np
import cv2

def displayConnectedComponents(im):
    
    imLabels = im
    
    # The following line finds the min and max pixel values
    # and their locations in an image.
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imLabels)
    
    # Normalize the image so the min value is 0 and max value is 255.
    imLabels = 255 * (imLabels - minVal)/(maxVal-minVal)
    
    # Convert image to 8-bits unsigned type
    imLabels = np.uint8(imLabels)
    
    # Apply a color map
    imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_JET)
    
    # Display colormapped labels
    cv2.imshow("Labels", imColorMap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# load the image, convert it to grayscale
image = cv2.imread("images/truth.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold Image
th, imThresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", imThresh)
cv2.waitKey(0)

# Find connected components
_, imLabels = cv2.connectedComponents(imThresh)

# Display the labels
displayConnectedComponents(imLabels)
