import cv2 as cv
import threading
import urllib2
import numpy as np
import sys
class CameraN(threading.Thread):
    def __init__(self,Source,Type=0):
        threading.Thread.__init__(self)
        self.isRunning = True
        self.Cap = None
        self.Host = Source
        self.bytes=''
        self.Type = Type
        self.Image = None
        self.bytes=''
        if(self.Type == 0):
            self.Cap = cv.VideoCapture(self.Host)
            self.isRunning = self.Cap.isOpened
            self.Image = self.Cap.read()
        else:
            self.Cap=urllib2.urlopen(self.Host)
            self.isRunning = True
    def get_image(self):
            return self.Image
    def run(self):
        if(self.Type == 0):
            while(self.Cap.isOpened and self.isRunning):
                state,self.Image = self.Cap.read()
                k = cv.waitKey(1)
        else:
            while(self.isRunning):
                self.bytes+=self.Cap.read(1024)
                a = self.bytes.find('\xff\xd8')
                b = self.bytes.find('\xff\xd9')
                if a!=-1 and b!=-1:
                    jpg = self.bytes[a:b+2]
                    self.bytes= self.bytes[b+2:]
                    self.Image = cv.imdecode(np.fromstring(jpg, dtype=np.uint8),cv.CV_LOAD_IMAGE_COLOR)
                if cv.waitKey(1) ==27:
                    exit(0)

