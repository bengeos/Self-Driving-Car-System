import cv2
import urllib2
import numpy as np
import sys
import time
import csv
class IP_Cam(object):
    def __init__(self,host):
        self.Host = host
        self.Stream = urllib2.urlopen(self.Host)
        self.Folder = 'C:\Images'
        self.csvPath = 'C:\Users\BENGEOS-PC\Documents\SDC-DAs\Tests\BEN\Neural Network\TrainingData.csv'
        self.isRunning = False
        self.ShowImage = False
        self.Frame = None
        self.Image = None
        self.Size = (100,100)
        self.Data = []

    def Start(self):
        bytes=''
        self.isRunning = False
        while(not self.isRunning):
            bytes+=self.Stream.read(10024)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+2:]
                self.Frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                self.Image = cv2.resize(self.Frame,self.Size)
                if(self.ShowImage):
                    cv2.imshow('IP Camera '+self.Host,self.Image)
                k = cv2.waitKey(1) - 48
    def Stop(self):
        self.isRunning = True
    def Take(self,label):
        imgPath = self.Folder+'\\'+str(time.time())+'.jpg'
        size = np.shape(self.Image)
        data = [imgPath,label,size[0],size[1]]
        cv2.imwrite(imgPath,self.Image)
        self.Data.append(data)
    def SaveCSV(self):
        for data in self.Data:
            self.WriteCSV(data)
    def getFrame(self):
        return self.Frame
    def getImage(self):
        return self.Image
    def WriteCSV(self,row):
        with open(self.csvPath,'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
