from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from time import time
from threading import Timer
from datetime import datetime
import platform
import os


#get the UI from here
from ui_diagnostics_dlg import Ui_DiagnosticsDialog
from dlg_rtc_cls import RtcDialog


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

        self.ser = ser_instance
        self.t = treatment_instance

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # to start 1 second timer
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

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


        """ This runs in other thread is a better idea to use a signal to change the UI """
    def TimerOneSec(self, lapse):
        self.next_call = self.next_call + 1        
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()
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
        myCmd = "sudo date -s {0}/{1}/20{2} {3}:{4}".format(new_day, new_month, new_year, new_hour, new_minute)
        print(myCmd)
        # os.system(myCmd)
        
        
### end of file ###
