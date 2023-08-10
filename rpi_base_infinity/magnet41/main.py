import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime
from antenna_class import AntennaInTreatment
import platform


#para el timer de 1 segundo
from threading import Timer


"""
        GUI for Magnet - as a copy from stretcher
        Select if its running on Slackware or Raspberry
        Select the type of date-time
        Select the version of the GUI:
            - 3.1 original
"""

### GLOBALS FOR CONFIGURATION #########
CURRENT_VERSION = 'Magnet ver 4.1'
## No call the first Dialog - code empty presentation page -
NO_CALL_FIRST_DLG = False


## Import UIs classes used
from dlg_main_cls import Dialog
from first_dialog_cls import FirstDialog
# from screen_saver_cls import ScreenSaverDialog
# from wifi_enable_cls import WiFiDialog

#get the code for manager
from wifi_thread_manager import WiFiThreadManager


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
        if NO_CALL_FIRST_DLG == 0:
            self.FirstDialogScreen()

        self.MainDialogScreen()
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
    def FirstDialogScreen (self):
        self.screensaver_window = False
        a = FirstDialog(self.t.GetLocalization(), self.t.timeout_screensaver)
        a.setModal(True)
        a.exec_()

        
    ## Main Screen
    def MainDialogScreen (self):
        debug = False
        a = Dialog(debug, self.s, self.t, parent=self)
        a.setModal(True)
        a.exec_()


        
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
