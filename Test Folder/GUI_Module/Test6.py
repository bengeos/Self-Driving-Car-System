import wx
import cv2

class LiveFrame(wx.Frame):

  fps = 30


  def __init__(self, parent):
    wx.Frame.__init__(self, parent, -1, title="Live Camera Feed")

    self.SetDoubleBuffered(True)
    self.capture = None
    self.bmp = None
    #self.displayPanel = wx.Panel(self,-1)

    #set up camaera init
    self.capture = cv2.VideoCapture(0)
    state,frame = self.capture.read()
    if state:
      cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      h, w = frame.shape[:2]
      wxbmp = wx.BitmapFromBuffer(w, h, frame)
      self.bmp = frame
      self.SetSize((w,h))
    self.displayPanel = wx.Panel(self,-1)

    self.fpstimer = wx.Timer(self)
    self.fpstimer.Start(1000/self.fps)
    self.Bind(wx.EVT_TIMER, self.onNextFrame, self.fpstimer)
    self.Bind(wx.EVT_PAINT, self.onPaint)

    self.Show(True)

  def updateVideo(self):
    state,frame = self.capture.read()
    cv2.imshow('bb',frame)
    if state:
      cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      h, w = frame.shape[:2]
      wxbmp = wx.BitmapFromBuffer(w, h, frame)
      self.bmp = wxbmp
      self.Refresh()


  def onNextFrame(self,evt):
    self.updateVideo()
    #self.Refresh()
    #evt.Skip()

  def onPaint(self,evt):
    #if self.bmp:
    wx.BufferedPaintDC(self.displayPanel, self.bmp)
    #evt.Skip()

if __name__=="__main__":
    app = wx.App()
    app.RestoreStdio()
    LiveFrame(None)
    app.MainLoop()