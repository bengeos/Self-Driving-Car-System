import cv2
import urllib2
import numpy as np
import threading

class Camera(threading.Thread):
    def __init__(self,Type,Host,Visible=False):
        threading.Thread.__init__(self)
        self.Host = Host
        self.Image = None
        self.isRunning = True
        self.Type = Type
        print 'initialising camera'+str(type(self.Type))
        if(type(self.Type) == int):
            print 'initialising Web/USB camera'
            self.Cap = cv2.VideoCapture(int(self.Host))
        else:
            print 'initialising IP camera'
            self.Stream = urllib2.urlopen(self.Host)
    def get_image(self):
        return self.Image
    def Stop(self):
        self.Cap.release()
        cv2.destroyAllWindows()
        self.isRunning = False
    def run(self):
        if(type(self.Type) == int):
            print 'WebCam Started ....'
            while(self.isRunning and self.Cap.isOpened):
                ret,self.Image_ = self.Cap.read()
                self.Image_ = cv2.cvtColor(self.Image_,cv2.COLOR_BGR2GRAY)
                self.Image = cv2.flip(self.Image_,1)
        else:
            bytes=''
            print 'IP Camera Started ....'
            while(self.isRunning):
                bytes+=self.Stream.read(2024)
                a = bytes.find('\xff\xd8')
                b = bytes.find('\xff\xd9')
                if a!=-1 and b!=-1:
                    jpg = bytes[a:b+2]
                    bytes= bytes[b+2:]
                    self.Image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_GRAYSCALE)