import cv2 as cv

img = cv.imread('../data/park.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
cv.imshow('YUV', yuv)

cv.waitKey(0)