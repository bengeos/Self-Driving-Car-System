__author__ = 'BENGEOS-PC'
import cv2 as cv
import threading
import urllib2
import numpy as np

class Camera(threading.Thread):
    def __init__(self,host):
        threading.Thread.__init__(self)
        self.Host = host
        self.Stream = urllib2.urlopen(self.Host)
        self.Image = None
        self.isRunning = True
    def cap_img(self):
        state,img = self.Cap.read()
        cv.waitKey(10)
        return img
    def run(self):
        bytes=''
        while(self.isRunning):
            bytes+=self.Stream.read(512)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+2:]
                self.Image = cv.imdecode(np.fromstring(jpg, dtype=np.uint8),cv.CV_LOAD_IMAGE_COLOR)
    def get_image(self):
        return self.Image
    def Stop(self):
        self.isRunning = False

