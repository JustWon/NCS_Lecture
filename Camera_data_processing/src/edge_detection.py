import cv2 as cv

img = cv.imread('../data/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

edge = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', edge)

cv.waitKey(0)