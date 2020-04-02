from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from time import time
from threading import Timer
from datetime import datetime
import platform
import os


#get the UI from here
from ui_diagnostics_dlg import Ui_DiagnosticsDialog
from dlg_rtc_cls import RtcDialog
from dlg_pwr_ctrl_cls import PowerControlDialog

## what to do with the RTC info
USE_RTC_STRING_FOR_PRINT = 1
USE_RTC_STRING_FOR_COMMAND = 0


#####################################################################
# DiagnosticsDialog Class - Secondary window for diagnostics checks #
#####################################################################
class DiagnosticsDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()

    def __init__(self, ser_instance, treatment_instance):
        super(DiagnosticsDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_DiagnosticsDialog()
        self.ui.setupUi(self)

        # get the close event and connect the buttons        
        self.ui.doneButton.clicked.connect(self.accept)
        self.ui.rtcButton.clicked.connect(self.RtcScreen)
        self.ui.max_powerButton.clicked.connect(self.PowerScreen)

        self.ser = ser_instance
        self.t = treatment_instance

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # to start 1 second timer
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)

        if self.ser.port_open == False:
            self.ui.hardwareLabel.setText("No port  ")
            self.ui.firmwareLabel.setText("No port  ")
        else:
            self.ui.hardwareLabel.setText("Waiting...  ")
            self.ui.firmwareLabel.setText("Waiting...  ")
            self.ser.Write("voltage\n")
            # ser_instance.Write("get data\n")
            
        #recupero informacion del sistema
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        os_text = "--" + distname + version + "-- "
        self.ui.osLabel.setText(os_text)

        (system, node, release, version, machine, processor) = platform.uname()
        self.ui.kernelLabel.setText(release)
        self.ui.softLabel.setText(self.t.current_version)


    def UpdateDateTime(self, new_date_time):
        date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
        self.ui.date_timeLabel.setText(date_str)


        """ QTimer callback emit a signal to not upset the timer interval """
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

            
    ## RtcScreen
    def RtcScreen (self):
        a = RtcDialog()
        a.setModal(True)

        date_now = datetime.today()
        a.ui.dayButton.setText(date_now.strftime("%d"))
        a.ui.monthButton.setText(date_now.strftime("%m"))
        a.ui.yearButton.setText(date_now.strftime("%y"))

        a.ui.hourButton.setText(date_now.strftime("%H"))
        a.ui.minuteButton.setText(date_now.strftime("%M"))            

        a.exec_()
        new_day = a.ui.dayButton.text()
        new_month = a.ui.monthButton.text()
        new_year = a.ui.yearButton.text()
        new_hour = a.ui.hourButton.text()
        new_minute = a.ui.minuteButton.text()
        myCmd1 = "sudo date -s {0}/{1}/20{2}".format(new_day, new_month, new_year)
        myCmd2 = "sudo date -s {0}:{1}:00".format(new_hour, new_minute)
        myCmd3 = "sudo hwclock -w"        #guardo info del date en hwclock
        if USE_RTC_STRING_FOR_PRINT:
            print(myCmd1)
            print(myCmd2)
            print(myCmd3)            

        if USE_RTC_STRING_FOR_COMMAND:
            os.system(myCmd1)
            os.system(myCmd2)            
            os.system(myCmd3)

        # do a UI update
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)



    ## PowerScreen
    def PowerScreen (self):
        a = PowerControlDialog(self.t)
        a.setModal(True)
        a.exec_()
        
        
### end of file ###

