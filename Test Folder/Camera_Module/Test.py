import CameraN as cam1
import Camera as cam2
import cv2 as cv
import time

cam = cam1.CameraN('http://192.168.173.169:8080/video',1)
cam.start()
time.sleep(3)
while(True):
    img = cam.get_image()
    cv.imshow('Owww',img)
    cv.waitKey(2)