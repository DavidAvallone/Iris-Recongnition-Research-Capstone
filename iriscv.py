# David Avallone & Kelly Reynolds Computer Vision


import cv2
from matplotlib import pyplot as plt
import math
import numpy as np
import os



img = cv2.imread("archive/000/S6000S00.jpg", cv2.IMREAD_COLOR) 
  
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray,  cv2.HOUGH_GRADIENT, 1,20, param1 = 50, param2 = 50, minRadius = 1, maxRadius = 115) 
# Draw circles that are detected. 

if detected_circles is not None:
# Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
    max_radius_index = np.argmax(detected_circles[0, :, 2])
    a, b, r = detected_circles[0, max_radius_index]

    # Draw the circumference of the largest circle
    cv2.circle(img, (a, b), r, (0, 255, 0), 2)
    cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

    plt.imshow(img)
    plt.show()

else:
    print("Nothing detected")
'''
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 

        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 

        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
        plt.imshow(img) 
        plt.pause(0.1)

    plt.show()

else:
    print("No circles detected")
'''  

#This code only produces one circle but it isn't around the iris
#The circle is too far right and too far up (mostly on the eyelid)
'''
max_radius_index = np.argmax(detected_circles[0, :, 2])
    a, b, r = detected_circles[0, max_radius_index]

    # Draw the circumference of the largest circle
    cv2.circle(img, (a, b), r, (0, 255, 0), 2)
    cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

    plt.imshow(img)
    plt.show()
'''
