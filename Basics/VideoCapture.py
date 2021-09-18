# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:15:27 2021

@author: Prem Ranjan
"""
import cv2

## VIDEO CAPTURE FROM CAMERA
# set video capturing device  (0 for primary device)
cap = cv2.VideoCapture(0);

# seting the video write format = xvid
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
       # 1. ret is a boolean variable that returns true if the frame is available.
       # 2. frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)  # saving 'frame' video into folder
        
        # changinng the color to Gray scale color
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
        # cv2.imshow('frmae', frame)   # for exact image from cam
        cv2.imshow('frmae', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
