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


#####################################################################
# DiagnosticsDialog Class - Secondary window for diagnostics checks #
#####################################################################
class DiagnosticsDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()

    def __init__(self, ser_instance, treatment_instance, parent=None):
        super(DiagnosticsDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_DiagnosticsDialog()
        self.ui.setupUi(self)

        # get the close event and connect the buttons        
        self.ui.doneButton.clicked.connect(self.accept)
        self.ui.rtcButton.clicked.connect(self.RtcScreen)
        self.ui.max_powerButton.clicked.connect(self.PowerScreen)

        # get the parent reference and data
        self.parent = parent
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

        # progress timer, these ones are qt
        self.init_timer = QTimer()
        

        # CONNECT SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)

        self.ui.highVLabel.setText("--")
        self.ui.lowVLabel.setText("--")

        if self.ser.port_open == False:
            self.ui.hardwareLabel.setText("No port  ")
            self.ui.firmwareLabel.setText("No port  ")
        else:
            self.ui.hardwareLabel.setText("Waiting...  ")
            self.ui.firmwareLabel.setText("Waiting...  ")
            
        # recupero informacion del sistema
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        os_text = "--" + distname + version + "-- "
        self.ui.osLabel.setText(os_text)

        (system, node, release, version, machine, processor) = platform.uname()
        self.ui.kernelLabel.setText(release)
        self.ui.softLabel.setText(self.t.current_version)

        # recupero informacion de la placa power si el puerto esta OK
        self.comm_progress = 'clean'        
        if self.ser.port_open == True:
            self.GetPowerInfoSM()


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


    def GetPowerInfoSM (self):
        if self.comm_progress == 'clean':
            # limpio el puerto y luego la configuracion
            self.ser.Write("keepalive,\r\n")
            
            self.comm_progress = 'voltage'
            self.init_timer.singleShot(100, self.GetPowerInfoSM)

        elif self.comm_progress == 'voltage':
            self.ser.Write("voltage\r\n")

            self.comm_progress = 'hardware_and_software'
            self.init_timer.singleShot(100, self.GetPowerInfoSM)

        elif self.comm_progress == 'hardware_and_software':
            self.ser.Write("hard_soft\r\n")

            self.comm_progress = 'device_id'
            self.init_timer.singleShot(100, self.GetPowerInfoSM)

        elif self.comm_progress == 'device_id':
            self.ser.Write("serial num\r\n")
            

    def SerialDataCallback (self, rcv):
        if rcv.startswith("High Supply:"):
            h_voltage = rcv[12:]
            self.ui.highVLabel.setText(h_voltage)

        if rcv.startswith("Low Supply:"):
            l_voltage = rcv[11:]
            self.ui.lowVLabel.setText(l_voltage)

        if rcv.startswith("Hardware Version:"):
            hs = rcv[17:]
            self.ui.hardwareLabel.setText(hs)

        if rcv.startswith("Software Version:"):
            hs = rcv[17:]
            self.ui.firmwareLabel.setText(hs)

        if rcv.startswith("Device Id:"):
            hs = rcv[10:]
            self.ui.deviceLabel.setText(hs)
            
        


    ###############
    # Screens     #
    ###############
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
        myCmd1 = "sudo date -s {1}/{0}/20{2}".format(new_day, new_month, new_year)
        myCmd2 = "sudo date -s {0}:{1}:00".format(new_hour, new_minute)
        myCmd3 = "sudo hwclock -w"        #guardo info del date en hwclock
        if self.t.GetCurrentSystem() == 'slackware':
            print(myCmd1)
            print(myCmd2)
            print(myCmd3)            

        elif self.t.GetCurrentSystem() == 'raspbian':
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

