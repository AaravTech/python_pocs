import numpy as np
import cv2 as cv
import math
import os
import time

images = []
for image_path in os.listdir('images/'):
    images.append('images/' + image_path)

i = 0
total = len(images)
img = cv.imread(images[i])

def load_next_image():
    global i, img
    if i != total - 1:
        img1 = cv.imread(images[i])
        img2 = cv.imread(images[i+1])
        x,y = 1,0
        while int(y) != 1:
            img = cv.addWeighted(img1,x,img2,y,0)
            x -= 0.005
            y += 0.005
            cv.imshow('image', img)
            cv.waitKey(1) & 0xFF
        i += 1

def load_previous_image():
    global i, img
    if i != 0:
        img1 = cv.imread(images[i])
        img2 = cv.imread(images[i-1])
        x,y = 1,0
        while int(y) != 1:
            img = cv.addWeighted(img1,x,img2,y,0)
            x -= 0.02
            y += 0.02
            cv.imshow('image', img)
            cv.waitKey(1) & 0xFF
        i -= 1

def auto_slideshow():
    global i, img
    while(1):
        cv.imshow('image', img)
        k = cv.waitKey(1)
        if k == 115:
            break
        time.sleep(1)
        if i == total - 1:
            break
        load_next_image()

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == 83:
        load_next_image()
    elif k == 81:
        load_previous_image()
    elif k == 97:
        auto_slideshow()
