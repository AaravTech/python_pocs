import numpy as np
import cv2 as cv
import math


def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((500,712,3), np.uint8)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
o_switch = '0 : Cricle \n1 : Rectangle'
m_switch = '0 : Filled \n1 : Not Filled'
cv.createTrackbar(o_switch, 'image',0,1,nothing)
cv.createTrackbar(m_switch, 'image',0,1,nothing)

color = (0,0,0)
obj = 'circle'
filled = -1

def draw_object(event, x, y, flags, param):
    global ix, iy, obj, filled
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
    elif event == cv.EVENT_LBUTTONUP:
        if obj == 'rectangle':
            cv.rectangle(img,(ix,iy),(x,y),color,filled)
        else:
            r = int(math.sqrt((x - ix)**2 + (y - iy)**2) / 2)
            x,y = (x+ix)/2, (y+iy)/2
            cv.circle(img,(x,y),r,color,filled)

    
cv.setMouseCallback('image',draw_object)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    o = cv.getTrackbarPos(o_switch,'image')
    m = cv.getTrackbarPos(m_switch,'image')
    color = (b,g,r)
    temp = img.copy()
    cv.rectangle(temp,(100,100),(150,150),color,filled)
    cv.imshow('image_color',temp)
    if o == 1:
        obj = 'rectangle'
    else:
        obj = 'circle'

    if m == 0:
        filled = -1
    else:
        filled = 1
    
cv.destroyAllWindows()
