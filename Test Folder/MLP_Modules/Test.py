import cv2 as cv
import Camera as cam
import time

Cam = cam.Camera(0)
Cam.start()
time.sleep(1)
while(1):
    img = Cam.get_image()
    cv.imshow('Camera',img)
    k = cv.waitKey(1)
    if(k == 27):
        cv.destroyAllWindows()
        break