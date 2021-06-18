from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
# from PyQt5.QtGui import QMovie
# from time import time
# from threading import Timer
# from datetime import datetime


#get the UI from here
from ui_steps_dlg import Ui_StepsDialog


#################################################
# FirstDialog Class - to get the system running #
#################################################
class StepsDialog(QDialog):

    # signal to update in 10 second
    ten_seconds_signal = pyqtSignal()

    def __init__(self, parent):
        super(StepsDialog, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_StepsDialog()
        self.ui.setupUi(self)

        # get the parent reference and data
        self.parent = parent

        # Setup signals
        self.ui.doneButton.clicked.connect(self.accept)
        self.ui.buzzButton.clicked.connect(self.Buzzer)

        # self.ui.doneButton.setStyleSheet("background-color: rgba(255, 255, 255, 0); \
        #                                   border: 0px");
        
        # to start 10 seconds timer
        self.t10seg = QTimer()
        self.t10seg.timeout.connect(self.TimerTenSecs)
        self.t10seg.start(10000)

        #SIGNALS
        # connect the timer signal to the Update
        self.ten_seconds_signal.connect(self.UpdateTenSecs)


        """ QTimer callback emit a signal to not upset the timer interval """
    def TimerTenSecs(self):
        self.ten_seconds_signal.emit()


    def UpdateTenSecs (self):
        # self.parent
        pass


    def Buzzer (self):
        self.parent.SendBuzzerCmd(1)

        


        
### end of file ###
