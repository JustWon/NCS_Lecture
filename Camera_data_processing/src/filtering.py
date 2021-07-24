import cv2 as cv

img = cv.imread('../data/cats.jpg')
cv.imshow('Cats', img)

average = cv.blur(img, (10,10))
cv.imshow('Average Blur', average)

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

cv.waitKey(0)