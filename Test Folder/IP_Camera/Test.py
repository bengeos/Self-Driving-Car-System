import IP_Camera
import time
import cv2 as cv

Cam = IP_Camera.Camera('http://192.168.43.1:8080/video')
Cam.start()
time.sleep(1)
while(1):
    img = Cam.get_image()
    cv.imshow('Camera',img)
    k = cv.waitKey(100)
    if(k == 27):
        break
