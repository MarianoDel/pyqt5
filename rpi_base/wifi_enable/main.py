import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor



"""
        Test for WiFiDialog

"""

from wifi_enable_cls import WiFiDialog

class Dialog(QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        self.FirstDialogScreen()
        self.close()
        sys.exit(0)
        
    def FirstDialogScreen (self):
        a = WiFiDialog()
        a.setModal(True)
        a.exec_()

        
### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
w = Dialog()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
w.show()
sys.exit(app.exec_())
# app.exec_()


### End of File ###
