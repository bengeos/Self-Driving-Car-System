import cv2 as cv
import MLP as My_Net
import Camera_Module
import time
import numpy as np
import threading
class MLP_Module_1(threading.Thread):
    def __init__(self,Layers,Camera):
        threading.Thread.__init__(self)
        self.network = My_Net.MLP(Layers)
        #initilize Data Storages
        self.training_inputs = []
        self.training_result = []
        #initialise Camera Module
        self.cam = Camera_Module.Camera_Module(0)
        self.cam.Start()
        self.isRunning = False
        time.sleep(3)
        self.S_T = 0
        self.img_shp = 0
    def vectorized_result(Val,size):
        e = np.zeros((size, 1))
        e[Val] = 1.0
        return e

    def Reset_All(self):
        for xx in range(len(self.training_inputs)):
            self.training_inputs.pop()
        for xx in range(len(self.training_result)):
            self.training_result.pop()

    def append_Trianing(self,img,val):
        self.img_shp = np.shape(img)
        self._data_ = img.reshape(-1,self.img_shp[0]*self.img_shp[1]).astype(np.float32)
        self.training_inputs.append(self._data_)
        self.training_result.append(val)
    def Train_MLP(self):
        self.training_inputs1 = [np.reshape(x, (self.net2.Network_Shape[0], 1)) for x in self.training_inputs]
        self.training_result1 = [self.vectorized_result(y,10) for y in self.training_result]

        self.test_inputs = [np.reshape(x, (self.net2.Network_Shape[0], 1)) for x in self.training_inputs]
        self.test_result = [np.reshape(x, (1, 1)) for x in self.training_result]

        training_data = zip(self.training_inputs1, self.training_result1)
        test_data = zip(self.test_inputs,self.test_result)
        self.net2.Evaluate_Network(training_data,10,1,2.0,test_data)
    def run(self):
        while(self.isRunning):
            img = self.cam.get_NewImage((100,100),0)
            cv.imshow("BEN",cv.resize(img,(700,500)))
            k = cv.waitKey(100)
ben = MLP_Module_1([2500,100,10],0)
ben.isRunning = True
ben.start()
