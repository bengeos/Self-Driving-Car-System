import cv2
import numpy as np
import time
img_rgb = cv2.imread('ben.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('ben1.JPG',0)
w, h = template.shape[::-1]
T1 = time.time()
print('Start Time: ',T1)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
T2 = time.time()
print('End Time: ',T2)
print('Ellpsed Time: ',T2-T1)
while(1):
    cv2.imshow('Detected',img_rgb)
    k = cv2.waitKey(27)