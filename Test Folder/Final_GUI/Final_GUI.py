from PyQt4 import QtCore, QtGui
import SDC_GUI as My_GUI
import sys
import time

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = My_GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.SentPrev = 0
        self.LastPressed = 0
    def keyReleaseEvent(self, ev):
        if(self.ui.Driving_Mode > -1):
            if(ev.key() == 16777235 and (self.SentPrev != 1 or self.ui.Driving_Mode == 1)):
                print 'Up'
                self.SentPrev = 1
                self.ui.SDCDriving.Send_Serial('W')
                if(self.ui.Driving_Mode == 1):
                    self.ui.Camera.Take(1)
                    time.sleep(0.1)
                    self.ui.SDCDriving.Send_Serial('S')
            if(ev.key() == 16777237 and (self.SentPrev != 2 or self.ui.Driving_Mode == 1)):
                print 'Down'
                self.SentPrev = 2
                self.ui.SDCDriving.Send_Serial('Z')
                if(self.ui.Driving_Mode == 1):
                    self.ui.Camera.Take(2)
                    time.sleep(0.1)
                    self.ui.SDCDriving.Send_Serial('S')
            if(ev.key() == 16777236 and (self.SentPrev != 3 or self.ui.Driving_Mode == 1)):
                print 'Right'
                self.SentPrev = 3
                self.ui.SDCDriving.Send_Serial('D')
                if(self.ui.Driving_Mode == 1):
                    self.ui.Camera.Take(3)
                    time.sleep(0.1)
                    self.ui.SDCDriving.Send_Serial('S')
            if(ev.key() == 16777234 and (self.SentPrev != 4 or self.ui.Driving_Mode == 1)):
                print 'Left'
                self.SentPrev = 4
                self.ui.SDCDriving.Send_Serial('A')
                if(self.ui.Driving_Mode == 1):
                    self.ui.Camera.Take(4)
                    time.sleep(0.1)
                    self.ui.SDCDriving.Send_Serial('S')
            if(ev.key() == 16777249 and (self.SentPrev != 5 or self.ui.Driving_Mode == 1)):
                print 'Stop'
                self.SentPrev = 5
                self.ui.SDCDriving.Send_Serial('S')
                if(self.ui.Driving_Mode == 1):
                    self.ui.Camera.Take(5)
                    time.sleep(0.1)
                    self.ui.SDCDriving.Send_Serial('S')
            print ev.key()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())