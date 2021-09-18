# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:15:27 2021

@author: Prem Ranjan
"""
import cv2
import numpy as np

img = cv2.imread('demon.jpg', 1)
# img = np.zeros([700,700,3],np.uint8)


# creating geometric shapes on image
# (image object, Point1, Point2, BGR color, thickness)

img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)
img = cv2.rectangle(img, (100,450),(800, 650), (0, 0, 255), 5)  # -1 in thickness for filled rectange
img = cv2.circle(img, (500, 450), 75, (0,255,0), 10)

# add text
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'OpenCV', (200,600), font, 4, (0, 255, 255), cv2.LINE_AA)

print(img.shape)
cv2.imshow('frame', img)

k = cv2.waitKey(0)

if k == 27:  # 27 -> "q" : closes the window
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lines.jpg',img)
    cv2.destroyAllWindows()
    
cv2.destroyAllWindows()
