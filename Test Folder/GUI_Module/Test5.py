import wx
import cv2

class MyFrame(wx.Frame):
    def _init_(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition, size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame, self)._init_(parent, id, title,pos, size, style, name)
        # Attributes
        self.panel = wx.Panel(self)
        img = cv2.imread("ben.jpg")
        img = cv2.cvtColor(img, cv2.cv.CV_BGR2RGB)
        h, w = img.shape[:2]
        wxbmp = wx.BitmapFromBuffer(w, h, img)
        wx.StaticBitmap(self.panel, bitmap=wx.BitmapFromImage(wx.ImageFromBitmap(wxbmp).Scale(w/6, h/6)))

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="The Main Frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
