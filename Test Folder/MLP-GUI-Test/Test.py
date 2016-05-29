import wx
import serial as sp
import cv, cv2
import time
class Test(wx.Frame):
    def __init__(self):
        self.Port = sp.Serial('COM6',9600)
        wx.Frame.__init__(self,None,wx.ID_ANY,"BENGEOS")
        panel = wx.Panel(self,wx.ID_ANY)
        btn = wx.Button(panel,label="OK")

        bb = wx.Button(panel,label="Button")
        btn.Bind(wx.EVT_KEY_DOWN,self.OnKeyPressed)
        btn.Bind(wx.EVT_KEY_UP,self.OnKeyReLeased)

    def ben(self,evt):
        print('bemgeos')
        evt.Skip()
    def OnKeyPressed(self,event):
        keyCode = event.GetKeyCode()
        print(keyCode)
        if(keyCode == 73):
            self.Port.write('P\r\n')
            time.sleep(0.1)
            self.Port.write('I\r\n')
        if(keyCode == 79):
            self.Port.write('O\r\n')
        if(keyCode == 80):
            self.Port.write('I\r\n')
            time.sleep(0.1)
            self.Port.write('P\r\n')
        if(keyCode == 76):
            self.Port.write('L\r\n')
        if(keyCode == 77):
            self.Port.write('M\r\n')
    def OnKeyReLeased(self,event):
        keyCode = event.GetKeyCode()
       # self.Port.write('M\r\n')
class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=100):
        wx.Panel.__init__(self, parent, wx.ID_ANY, (0,0), (800,500))
        self.capture = capture
        ret, frame = self.capture.read()
        height, width = frame.shape[:2]
        parent.SetSize((width, height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.BitmapFromBuffer(width, height, frame)
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()


capture = cv2.VideoCapture(0)

app = wx.PySimpleApp()
frame = Test()
frame.Show()
app.MainLoop()