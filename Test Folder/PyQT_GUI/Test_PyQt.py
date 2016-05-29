from PyQt4 import QtCore, QtGui
class Dialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(Dialog,self).__init__(parent)
        self.resize(300,200)
    def keyPressEvent(self, event):
        print event.key()
    def keyReleaseEvent(self, *args, **kwargs):
        print 'fdfdf'
    def mouseDoubleClickEvent(self, *args, **kwargs):
        print 'Doyble clicked'+ str(args)
    def eventFilter(self, QObject, QEvent):
        print 'some even'

if __name__ == "__main__":
    app = QtGui.QApplication([])
    d = Dialog()
    d.show()
    d.raise_()
    app.exec_()
