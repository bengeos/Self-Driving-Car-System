import cv2 as cv
import numpy as np
import time
cam = cv.VideoCapture(0)
img = np.zeros((512,512,3), np.uint8)


def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.imwrite('shanti'+str(time.time())+'.png',img)
        print("Image saved")
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(cam.isOpened):
    st,img = cam.read()
    cv.imshow('image',img)
    cv.waitKey(10)
