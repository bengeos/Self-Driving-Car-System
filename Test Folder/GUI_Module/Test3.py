import wx
import serial as sp
class MyPanel(wx.Panel):

    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.MBR = 0;
        self.LRM = 0;
        self.BRM1 = 0;
        self.BRM2 = 0;
        self.KCN = 0;
        self.FAN1 = 0;
        self.FAN2 = 0;
        self.PWD = '123456'
        self.Port = sp.Serial('COM4',9600)

        LRM = wx.Button(self, label = 'Living Room', pos = (60,20),size = (100,30))
        MBR = wx.Button(self, label = 'Master Bed Room', pos = (60,60),size = (100,30))
        BRM1 = wx.Button(self, label = 'Bed  Room 1', pos = (60,100),size = (100,30))

        BRM2 = wx.Button(self, label = 'Bed Room 2', pos = (200,20),size = (100,30))
        KCN = wx.Button(self, label = 'Kitchen Room', pos = (200,60),size = (100,30))
        FAN1 = wx.Button(self, label = 'Fan', pos = (200,100),size = (100,30))

        LRM.Bind(wx.EVT_BUTTON, self.LRM_Clicked)
        MBR.Bind(wx.EVT_BUTTON, self.MBR_Clicked)
        BRM1.Bind(wx.EVT_BUTTON, self.BRM1_Clicked)
        BRM2.Bind(wx.EVT_BUTTON, self.BRM2_Clicked)
        BRM1.Bind(wx.EVT_BUTTON, self.BRM1_Clicked)
        KCN.Bind(wx.EVT_BUTTON, self.KCN_Clicked)
        FAN1.Bind(wx.EVT_BUTTON, self.FAN1_Clicked)
    def LRM_Clicked(self, e):
        if self.LRM == 0:
            self.sendSerial(1,'LRM')
            self.LRM = 1
        else:
            self.sendSerial(0,'LRM')
            self.LRM = 0
    def MBR_Clicked(self, e):
        if self.MBR == 0:
            self.sendSerial(1,'MBR')
            self.MBR = 1
        else:
            self.sendSerial(0,'MBR')
            self.MBR = 0
    def BRM1_Clicked(self, e):
        if self.BRM1 == 0:
            self.sendSerial(1,'BRM1')
            self.BRM1 = 1
        else:
            self.sendSerial(0,'BRM1')
            self.BRM1 = 0
    def BRM2_Clicked(self, e):
        if self.BRM2 == 0:
            self.sendSerial(1,'BRM2')
            self.BRM2 = 1
        else:
            self.sendSerial(0,'BRM2')
            self.BRM2 = 0
    def KCN_Clicked(self, e):
        if self.KCN == 0:
            self.sendSerial(1,'KCN')
            self.KCN = 1
        else:
            self.sendSerial(0,'KCN')
            self.KCN = 0
    def FAN1_Clicked(self, e):
        if self.FAN1 == 0:
            self.sendSerial(1,'FAN1')
            self.FAN1 = 1
        else:
            self.sendSerial(0,'FAN1')
            self.FAN1 = 0
    def FAN2_Clicked(self, e):
        if self.FAN2 == 0:
            self.sendSerial(1,'FAN2')
            self.FAN2 = 1
        else:
            self.sendSerial(0,'FAN2')
            self.FAN2 = 0
    def btnclk(self,e):
      print "Button received click event. propagated to Panel class | "+str(e)
    def sendSerial(self,SW_cmd,RM_cmd):
        self.Port.write('PWD='+str(self.PWD)+' SW='+str(SW_cmd)+'RM ='+str(RM_cmd)+'\r\n')
class Example(wx.Frame):

   def __init__(self,parent):
      super(Example, self).__init__(parent)

      self.InitUI()

   def InitUI(self):
      mpnl = MyPanel(self)
      self.SetTitle('Home Automation')
      self.Centre()
      self.Show(True)
ex = wx.App()
Example(None)
ex.MainLoop()