import wx
class Centre(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self,-1)
        box = wx.BoxSizer(wx.VERTICAL)
        self.Centre()
        self.Show(True)
class MyGUI(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.Center()
        self.Show(True)
app = wx.App()
MyGUI(None, -1, 'Center')
app.MainLoop()
