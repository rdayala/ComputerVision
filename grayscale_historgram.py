# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:27:07 2019

@author: rdayala
"""

# import the necessary packages
# We’ll make use of the matplotlib  package to make 
# plotting our 'images' and histograms easier.
# Why matplotlib library? because of compatibility in macOS. 
from matplotlib import pyplot as plt
import cv2

# load the image, convert it to grayscale
image = cv2.imread("images/beach.png")
# image = cv2.imread("images/horseshoe_bend.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# construct a grayscale histogram
# [image] - only one image, it should be wrapped as a list
# [0] - grayscale image - so only one channel
# None - there is no mask provided
# [256] - 256 bins - only one channel, so one value in list
# [0, 256] - pixel intensity value ranges
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
 
# matplotlib expects RGB images so convert and then display the image
# with matplotlib to avoid GUI conflicts/errors (mainly on macOS)
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)) # Grayscale to RGB
 
# plot the histogram - unnormalized
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# normalize the histogram
hist /= hist.sum()
 
# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


"""
Notes:
We can see that our first parameter is the grayscale image. 
A grayscale image has only one channel, so we have a value of [0]  for channels. 
We don’t have a mask, so we set the mask value to None . We will use 256 bins 
in our histogram, and the possible values range from 0 to 255. 
"""
