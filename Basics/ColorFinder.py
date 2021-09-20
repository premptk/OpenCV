import cv2
import numpy as np

def click_event(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x,y), 4, (0,255,255),-1)
        color_base = np.zeros((512,512,3), np.uint8)
        color_base[:] = [blue, green, red]
        cv2.imshow('color', color_base)
        
img = cv2.imread('demon.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
