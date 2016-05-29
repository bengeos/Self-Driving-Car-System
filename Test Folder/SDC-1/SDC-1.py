import wx
import cv, cv2

class MainWindow(wx.Panel):
    def __init__(self, parent,capture):
        wx.Panel.__init__(self, parent)
        panel = wx.Panel(self,wx.ID_ANY)
        btn = wx.Button(panel,label="OK")
        videoFrame = wx.Panel(self)
        ShowCapture(videoFrame, capture)
        videoFrame.Bind(wx.EVT_KEY_DOWN,self.OnKeyPressed)
        M1 = wx.BoxSizer(wx.HORIZONTAL)
        M1.Add(videoFrame,wx.ALIGN_CENTER)
        self.SetSizerAndFit(M1)
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
app = wx.App(False)
frame = wx.Frame(None,-1,'Self Driving Car',size=(800, 400))
panel = MainWindow(frame,capture)
frame.Show()
app.MainLoop()