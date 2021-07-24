import cv2 as cv
img = cv.imread('../data/cat_large.jpg')

scale = 0.3
width = int(img.shape[1]*scale)
height = int(img.shape[0]*scale)

dimensions = (width, height)

resized_img = cv.resize(img, dimensions)

cv.imshow('Resized_cat', resized_img) 
cv.waitKey(0)