import cv2 as cv
img = cv.imread('../data/cat.jpg')
cv.imshow('Cat', img) 
cv.waitKey(0)