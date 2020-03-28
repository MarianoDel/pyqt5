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

        
        #activo el timer de 2 segundos, la primera vez, luego se autollama
        if self.ser.port_open == False:
            self.ui.hardwareLabel.setText("No port  ")
            self.ui.firmwareLabel.setText("No port  ")
        else:
            self.ui.hardwareLabel.setText("Waiting...  ")
            self.ui.firmwareLabel.setText("Waiting...  ")
            self.ser.Write("voltage\n")
            # ser_instance.Write("get data\n")
            self.next_call = time()
            self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()

        #recupero informacion del sistema
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        # print(f"distname: {distname} version: {version} id: {nid}")
        os_text = "--" + distname + version + "-- "
        self.ui.osLabel.setText(os_text)

        (system, node, release, version, machine, processor) = platform.uname()
        # print(f"system: {system}, node: {node}, release: {release}, version: {version}, machine: {machine}, processor: {processor}")
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

            
    def TimerThreeSec (self, lapse):
        """ 
            aca tengo que resolver todo lo que se mueve 
            lo hago tipo por estados del programa con treatmet_state
        """
        self.next_call = self.next_call + lapse
        # #esto corre en otro thread entonces mando una senial para hacer update de la interface
        # self.one_second_signal.emit()        
        #antes de volver hago la proxima llamada
        self.t3seg = Timer(self.next_call - time(), self.TimerThreeSec, [3]).start()
        arrow = self.ser.Read()
        print(arrow)
        


    #     self.intfreq = 0

    #     # # # Connect up the buttons.
    #     self.ui.pushButton1.clicked.connect(self.UPFreq)
    #     self.ui.pushButton2.clicked.connect(self.DWNFreq)
    #     self.ui.endButton.clicked.connect(self.accept)


    # def UPFreq (self, event=None):
    #     if (self.intfreq < 10):
    #         self.intfreq += 1

    #     self.changeFreqLabel(self.intfreq)

    # def DWNFreq (self, event=None):
    #     if (self.intfreq > 1):
    #         self.intfreq -= 1

    #     self.changeFreqLabel(self.intfreq)

    # def changeFreqLabel(self, new_f):
    #     self.intfreq = new_f
    #     self.ui.whatfreqLabel.setText(str(self.intfreq))
    
    ## RtcScreen
    def RtcScreen (self):
        print("rtc button presed!!!")
        a = RtcDialog()
        a.setModal(True)

        date_now = datetime.today()
        a.ui.dayButton.setText(date_now.strftime("%d"))
        a.ui.monthButton.setText(date_now.strftime("%m"))
        a.ui.yearButton.setText(date_now.strftime("%y"))

        a.ui.hourButton.setText(date_now.strftime("%H"))
        a.ui.minuteButton.setText(date_now.strftime("%M"))            

        a.exec_()
        
        
### end of file ###

