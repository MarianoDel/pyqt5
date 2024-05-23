# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QObject, QTimer, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from treatment_class import Treatment
import platform
from serialcomm import SerialComm


#Here import the UIs or classes that got the UIs
from main_cls import MainWindow


### GLOBALS FOR CONFIGURATION #########
CURRENT_VERSION = 'Micro Current ver 1.0'


### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()


############################
# Main Class - Main Window #
############################
class MyMainClass (QObject):

    #SIGNALS
    rcv_signal = pyqtSignal(str)
    one_second_signal = pyqtSignal()
    
    def __init__(self):
        super(MyMainClass, self).__init__()
        self.t = Treatment()

        self.distro = self.GetDistroName(True)
        # print ('distro: ' + self.distro + ' distro len: ' + str(len(self.distro)))
        print (self.distro)        
        
        self.t.SetCurrentVersion(CURRENT_VERSION)
        self.t.SetCurrentSystem(self.distro)
        
        #creo el evento y lo conecto al slot
        self.c = Communicate()

        ## PARA SLACKWARE
        if self.t.GetCurrentSystem() == 'Slackware ':
            # self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
            self.s = SerialComm(self.MyObjCallback, '/dev/ttyUSB0')
        ## PARA RASPBERRY
        elif self.t.GetCurrentSystem() == 'debian':
            self.s = SerialComm(self.MyObjCallback, '/dev/serial0')
            
        ### For last call to the first f*** dialog
        # if NO_CALL_FIRST_DLG == 0:
        #     self.FirstDialogScreen()

        self.MainScreen()
        self.closeEvent(self)

            
    def GetDistroName (self, show=False):
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        if show:
            os_text = "--" + distname + version + "-- "
            print("os: " + os_text)

        return distname

            
    def MyObjCallback (self, dataread):
        d = dataread.rstrip()
        self.rcv_signal.emit(d)

        
    #capturo el cierre
    def closeEvent (self, event):
        print("Closing, Please Wait...")
        self.s.Close()
        sleep(0.5)
        sys.exit()

        
####################################
# Different Screens Calls are here #
####################################

    ## Initial Screen
    # def FirstDialogScreen (self):
    #     self.screensaver_window = False
    #     a = FirstDialog(self.t.GetLocalization(), self.t.timeout_screensaver)
    #     a.setModal(True)
    #     a.exec_()

        
    ## Main Screen
    def MainScreen (self):
        debug = False
        a = MainWindow(self.distro, self.s, parent=self)
        a.show()
        sys.exit(app.exec_())
        # a.exec_()


        
### End of Dialog ###
    

############
# Main App #
############
app = QApplication(sys.argv)
w = MyMainClass()
#http://doc.qt.io/qt-5/qt.html#WindowType-enum
# w.setWindowFlags(Qt.CustomizeWindowHint)
# w.setWindowFlags(Qt.FramelessWindowHint)
print('Starting magnet app...')
# w.show()
sys.exit(app.exec_())


### End of File ###
    
