import cv2 as cv
import numpy as np

img = cv.imread('../data/park.jpg')

flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

cv.waitKey(0)