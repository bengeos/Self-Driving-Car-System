import MLP as net
import IP_Camera as cam
import cv2
import numpy as np
import serial as sp
import threading
import time

class SDC_Mode(object):
    def __init__(self,NetLayers,ip_camera_host,capture_image_size,serialport):
        self.MyNet = net.MLP(NetLayers)
        self.Port = serialport
        self.SerialPort = sp.Serial(self.Port)
        self.Camera = cam.Camera(ip_camera_host)
        self.Host = ip_camera_host
        self.Frame = None
        self.Image = None
        self.Size = capture_image_size
        self.Speed = 1
        self.SerialThread = threading.Thread(target=self.ReadWriteSerial,args=())
        self.SerialWrite = None
        self.SerialRead = None
        self.WheelState = "Stopped"
        self.SerialThread.start()
    def Update_WheelState(self,val):
        if(val == 0):
            self.WheelState = "Stopped"
        if(val == 1):
            self.WheelState = "Moving Forward"
        if(val == 2):
            self.WheelState = "Moving Backward"
        if(val == 3):
            self.WheelState = "Moving Right"
        if(val == 4):
            self.WheelState = "Moving Left"
    def Disconnect_Serial(self):
        self.SerialPort.close()
    def ChangeSpeed(self,new_speed):
        self.Speed = new_speed
        self.SerialPort.write(new_speed)
    def ReadWriteSerial(self):
        prev = ''
        while(self.SerialPort.isOpen()):
            self.SerialRead = self.SerialPort.readline()
            print self.SerialRead
            time.sleep(0.01)

    def Send_Serial(self,data):
        print 'Sending Serial Data: '+str(data)
        self.SerialPort.write(str(data))
        #self.SerialWrite = str(data)
    def Load_Trained_MLP(self,mlp_xml_file):
        print 'Loading trained data'
        self.MyNet.Load_From(mlp_xml_file)
        print self.MyNet.Weights
    def Drive_Serial(self,data):
        if(data == 1):
            self.Send_Serial('W')
        elif (data == 2):
            self.Send_Serial('Z')
        elif(data == 3):
            self.Send_Serial('D')
        elif(data == 4):
            self.Send_Serial('A')
        elif(data == 5):
            self.Send_Serial('S')
        else:
            self.Send_Serial('S')
    def Start_Driving(self):
        self.Camera.start()
        self.isRunning = True
        while(self.isRunning):
            self.Frame = self.Camera.get_image()
            x = np.size(self.Frame)
            if(x >= self.Size[0]*self.Size[1]):
                try:
                    self.Image = cv2.resize(self.Frame,self.Size)
                    ImageArray = self.Image.reshape(-1,self.MyNet.Network_Shape[0]).astype(np.float32)
                    _TrainingData = []
                    _TestingData = []
                    _TestingData.append(1)
                    _TrainingData.append(ImageArray)
                    TestingData = [np.reshape(x, (self.MyNet.Network_Shape[0], 1)) for x in _TrainingData]
                    TestingResult = [np.reshape(x, (1, 1)) for x in _TestingData]
                    TestData = zip(TestingData,TestingResult)
                    res = self.MyNet.Evaluate_Data(TestData)
                    print 'Process Result: '+str(res[0])
                    self.Update_WheelState(res[0])
                    self.Drive_Serial(res[0])
                    cv2.imshow('IP Camera '+self.Host,self.Frame)
                finally:
                    pass
            k = cv2.waitKey(1000)
            self.Update_WheelState(0)
            if(k == 27):
                self.Update_WheelState(0)
                self.Camera.Stop()
                break
        cv2.destroyAllWindows()

