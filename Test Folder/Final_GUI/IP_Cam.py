import cv2
import urllib2
import numpy as np
import sys
import time
import csv
class IP_Cam(object):
    def __init__(self,host):
        self.Host = host
        self.Folder = 'C:\Images'
        self.csvPath = 'C:\TrainingData.csv'
        self.isRunning = True
        self.ShowImage = True
        self.Frame = None
        self.Image = None
        self.Size = (500,800)
        self.Data = []
    def setImageSize(self,image_size):
        self.Size = image_size
    def setFolder(self,folder_name):
        self.Folder = folder_name
    def setCSVPath(self,csv_path):
        self.csvPath = csv_path
    def getImageSize(self):
        return self.Size
    def Start(self):
        self.Stream = urllib2.urlopen(self.Host)
        bytes=''
        self.isRunning = True
        while(self.isRunning):
            bytes+=self.Stream.read(512)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+2:]
                self.Frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                x = np.size(self.Frame)
                if(x>= self.Size[0]*self.Size[1]):
                    try:
                        cv2.imshow('IP Camera '+self.Host,self.Frame)
                    finally:
                        x = 0
                k = cv2.waitKey(1) - 48
        cv2.destroyAllWindows()
    def Stop(self):
        self.isRunning = False
    def Take(self,label):
        print 'This is the label: '+str(label)
        self.Stream = urllib2.urlopen(self.Host)
        bytes=''
        self.isRunning = True
        trail = 100;
        while(trail > 0):
            bytes+=self.Stream.read(512)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+2:]
                self.Frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                self.Frame = cv2.cvtColor(self.Frame,cv2.COLOR_BGR2GRAY)
                x = np.size(self.Frame)
                if(x>= self.Size[0]*self.Size[1]):
                    try:
                        self.Image = cv2.resize(self.Frame,self.getImageSize())
                        trail = 0
                    finally:
                        x = 0
                k = cv2.waitKey(1) - 48
        print 'Taking Picture'
        imgPath = str(self.Folder+'\\'+str(time.time())+'.jpg')
        print imgPath
        size = np.shape(self.Image)
        print size
        data = [imgPath,label,size[0],size[1]]
        cv2.imwrite(imgPath,self.Image)
        self.Data.append(data)
        self.WriteCSV(data)
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
