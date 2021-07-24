import cv2 as cv
import numpy as np

img = cv.imread('../data/park.jpg')

def rotate(img, angle):
    (height, width) = img.shape[:2]

    image_center = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)

cv.imshow('Rotated', rotated)

cv.waitKey(0)