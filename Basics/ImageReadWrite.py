# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:15:27 2021

@author: Prem Ranjan
"""
import cv2

## BASIC I/O
# Read image from the same folder and load into img variable
img = cv2.imread('demon.jpg', 0)

# prints the image in array format
print(img)  

print(img.shape)  # (224, 224, 3)

# shows the image in console
cv2.imshow('image', img)  
k = cv2.waitKey(0)  # takes input from keyboard

if k == 27:  # 27 -> "q" : closes the window
    cv2.destroyAllWindows()
    
elif k == ord('s'):   # 's' from keyboard will save the image in the same folder
    cv2.imwrite('lena_copy.jpg', img)
    cv2.destroyAllWindows()
