import cv2 as cv

img = cv.imread('sudoku-original.jpg',0)


_,th1 = cv.threshold(img, 127, 255,cv.THRESH_BINARY)  # global threshold
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 6)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 6)
cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th2', th2)
    
cv.waitKey(0)
cv.destroyAllWindows()
