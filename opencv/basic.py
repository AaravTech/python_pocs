import numpy as np
import cv2 as cv
import math
import os
import time

# Load two images
img1 = cv.imread('images/django-thumb.jpg')
img2 = cv.imread('test.png')
img2 = img2[0:200,2:200]
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('image2 fg',img2_fg)
cv.imshow('image1 bg',img1_bg)
cv.imshow('mask', mask)
cv.imshow('roi', roi)
cv.waitKey(0)
cv.destroyAllWindows()
