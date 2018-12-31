import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)
white_color = (255, 255, 255)
img[::] = white_color
p = 290
cv.ellipse(img, (250,175), (100,100), 125, 0, p, (0,0,255), -1)
cv.ellipse(img, (250,175), (50,50), 125, 0, p, white_color, -1)
cv.ellipse(img, (125,350), (100,100), 10, 0, p, (0,255,0), -1)
cv.ellipse(img, (125,350), (50,50), 10, 0, p, white_color, -1)
cv.ellipse(img, (375,350), (100,100), 305, 0, p, (255,0,0), -1)
cv.ellipse(img, (375,350), (50,50), 305, 0, p, white_color, -1)
cv.imshow('My Image', img)

edges = cv.Canny(img, 100, 200)
cv.imshow('Edges', edges)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', img)



key = cv.waitKey(0) & 0xFF
if key == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
