import MLP as net
import cv2 as cv
import numpy as np
import csv

class NeuralNetwork(object):
    def __init__(self,NetLayers,ImageSize):
        self.MyNet = net.MLP(NetLayers)
        self.TrainingData = []
        self.TrainingResult = []
        self.Size = ImageSize
        self.Iteration = 50
        self.BatchTask = 10
        self.Epselom = 0.5
        self.Count = 0
        if((ImageSize[0]*ImageSize[1]) != NetLayers[0]):
            print '>> Image Size and Input layer should Match'
            exit()
    def setBatch_Number(self,number):
        print 'Batch Number set to be '+str(number)
        self.BatchTask = number
    def setIterationNumber(self,number):
        print 'Iteration Number set to be '+str(number)
        self.Iteration = number
    def setEpselom(self,number):
        print 'Epselom Number set to be '+str(number)
        self.Epselom = number
    def getVector(self,val,size):
        vec = np.zeros((size, 1))
        vec[val] = 1.0
        return vec
    def LoadTrainigData(self,filePath):
        print 'Resetting mlp ...'
        self.MyNet.init_Biases()
        self.MyNet.init_Weight()
        print 'Loading Trainig Files'
        print filePath
        self.TrainingData = []
        self.TrainingResult = []
        with open(filePath) as csvFile:
            self.Count = 0
            spread = csv.reader(csvFile)
            for row in spread:
                if(int(row[2]) == self.Size[0] and int(row[3]) == self.Size[1]):
                    img = cv.imread(row[0])
                    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                    img_shape = np.shape(img)
                    arrayData = img.reshape(-1,img_shape[0]*img_shape[1]).astype(np.float32)
                    print 'Loading Data:'
                    print arrayData
                    self.TrainingData.append(arrayData)
                    self.TrainingResult.append(int(row[1]))
                    self.Count = self.Count + 1
    def ResetData(self):
        self.Count = 0
        for xx in range(len(self.TrainingData)):
            self.TrainingData.pop()
        for xx in range(len(self.TrainingResult)):
            self.TrainingResult.pop()
    def TrainMLP(self):
        #Orcustrting Training Data
        Training_Input = [np.reshape(x,(int(self.MyNet.Network_Shape[0]),1)) for x in self.TrainingData]
        Training_Result = [self.getVector(x,10) for x in self.TrainingResult]
        #Orcustriting Testing Data
        Test_Input = [np.reshape(x,(self.MyNet.Network_Shape[0],1)) for x in self.TrainingData]
        Test_Result = [np.reshape(x,(1,1)) for x in self.TrainingResult]
        #Orcustrating Data for Learning
        TrainingData = zip(Training_Input,Training_Result)
        TestingData = zip(Test_Input,Test_Result)
        #Start Training from Data
        self.MyNet.Evaluate_Network(TrainingData,self.Iteration,self.BatchTask,self.Epselom,TestingData)
    def EvaluateImg(self,img):
        ImageArray = img.reshape(-1,self.MyNet.Network_Shape[0]).astype(np.float32)
        _TrainingData = []
        _TestingData = []
        _TestingData.append(1)
        _TrainingData.append(ImageArray)
        TestingData = [np.reshape(x, (self.MyNet.Network_Shape[0], 1)) for x in _TrainingData]
        TestingResult = [np.reshape(x, (1, 1)) for x in _TestingData]
        TestData = zip(TestingData,TestingResult)
        Result = self.MyNet.Evaluate_Data(TestData)
        return Result
    def StopLearning(self):
        self.MyNet.StopTraining()
    def Learn(self,csvFIle='TrainingData.csv'):
        self.LoadTrainigData(csvFIle)
        self.TrainMLP()
    def Save_To(self,path):
        self.MyNet.Save_To(path)
    def Load_From(self,path):
        self.MyNet.Load_From(path)
bb = NeuralNetwork([2500,500,10],(50,50))
