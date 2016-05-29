import wx
class Centre(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.Centre()
        self.Show(True)
app = wx.App()
Centre(None, -1, 'Centre')
app.MainLoop()