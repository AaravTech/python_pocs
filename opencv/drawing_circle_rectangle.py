import cv2 as cv
import numpy as np
import math

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
filled = -1
ix,iy = -1,-1
img = np.zeros((512,512,3), np.uint8)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    #elif event == cv.EVENT_MOUSEMOVE:
    #    if drawing == True:
    #        if mode == True:
    #            cv.rectangle(img,(ix,iy),(x,y),(0,0,255),1)
    #        else:
    #            cv.circle(img,(x,y),5,(0,0,255),1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),filled)
        else:
            r = int(math.sqrt((x - ix)**2 + (y - iy)**2) / 2)
            x,y = (x+ix)/2, (y+iy)/2
            cv.circle(img,(x,y),r,(0,0,255),filled)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('f'):
        if filled == 1:
            filled = -1
        else:
            filled = 1 
    elif k == 27:
        break
cv.destroyAllWindows()
