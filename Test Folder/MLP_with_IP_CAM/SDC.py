import IP_Cam as cam
import cv2 as cv
from multiprocessing import Process,Value,Array
import MLP as ntk

Cam1 = cam.IP_Cam('http://192.168.43.12:8080/video')
Cam2 = cam.IP_Cam('http://192.168.43.1:8080/video')

def StartCam1():
    Cam1.Start()


def StartCam2():
    Cam2.ShowImage = True
    Cam2.Start()
def show():
    while(1):
        if(not Cam2.isRunning):
            cv.imshow('bengeos',Cam2.getImage())
            cv.waitKey(1)

if __name__ == '__main__':
    P1 = Process(target=StartCam2)
    P2 = Process(target=show)
    P1.start()
    P2.start()
