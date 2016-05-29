import cv2
import urllib2
import numpy as np
import sys
import time
import csv
import NeuralNetwork as net

class IPCamera(object):
    def __init__(self,host):
        self.Host = host
        self.Stream = urllib2.urlopen(self.Host)
        self.Folder = 'C:\Images'
        self.csvPath = 'C:\Users\BENGEOS-PC\Documents\SDC-DAs\Tests\BEN\Neural Network\TrainingData.csv'
        self.MyNet = net.NeuralNetwork([2500,500,100,10],(50,50))
        self.MyNet.MyNet.ReadXML()
        self.isActive = False
    def Start(self):
        bytes=''
        while(True):
            bytes+=self.Stream.read(10240)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+2:]
                i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_GRAYSCALE)
                img = cv2.resize(i,(50,50))
                cv2.imshow('IP Camera',i)
                kk = cv2.waitKey(1)
                if(kk == 97):
                    if self.isActive:
                        self.isActive = False
                    else:
                        self.isActive = True
                k = kk - 48
                datas = []
                if(self.isActive):
                    val = self.MyNet.EvaluateImg(img)
                    print val
                else:
                    if(k>=0 and k<10):
                        print k,str(time.time())
                        imgPath = self.Folder+'\\'+str(time.time())+'.jpg'
                        size = np.shape(img)
                        data = [imgPath,k,size[0],size[1]]
                        datas.append(data)
                        cv2.imwrite(imgPath,img)
                        self.WriteCSV(data)
                if kk ==27:
                    exit(0)
    def WriteCSV(self,row):
        with open(self.csvPath,'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

bb = IPCamera('http://192.168.1.28:8080/video')
bb.Start()
