import cv2
import numpy as np
template = cv2.imread('bb.JPG',0)
w, h = template.shape[::-1]
cam = cv2.VideoCapture(0)
while(cam.isOpened):
    state,img = cam.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    cv2.imshow('Camera',img_gray)
    k = cv2.waitKey(27)
    if(k == 27):
        break
