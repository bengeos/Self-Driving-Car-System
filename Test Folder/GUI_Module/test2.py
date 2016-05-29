import wx
class MyPanel(wx.Panel):

   def __init__(self, parent):
      super(MyPanel, self).__init__(parent)

      b = wx.Button(self, label = 'Btn', pos = (100,100))
      b.Bind(wx.EVT_BUTTON, self.btnclk)
      self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)


   def OnButtonClicked(self, e):
      print 'Panel received click event. propagated to Frame class'
      e.Skip()

   def btnclk(self,e):
      print "Button received click event. propagated to Panel class"
      e.Skip()
class Example(wx.Frame):

   def __init__(self, *args, **kw):
      super(Example, self).__init__(*args, **kw)
      self.InitUI()

   def InitUI(self):
      self.Bind(wx.EVT_MOVE, self.OnMove)
      self.SetSize((1000, 600))
      self.SetTitle('Move event')
      self.Centre()
      self.Show(True)
      self.Maximize(True)
   def OnMove(self, e):
      x, y = e.GetPosition()
      print "current window position x = ",x," y= ",y

ex = wx.App()
Example(None)
ex.MainLoop()