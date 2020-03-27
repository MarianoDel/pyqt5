from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from time import time
from threading import Timer
from datetime import datetime
import platform
import os


#get the UI from here
from ui_stretcher_diag import Ui_DiagnosticsDialog

## This Interface Software version
CURRENT_VERSION = "Stretcher ver_3_1"

#####################################################################
# DiagnosticsDialog Class - Secondary window for diagnostics checks #
#####################################################################
class DiagDialog(QDialog):
    def __init__(self, ser_instance):
        super(DiagDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_DiagnosticsDialog()
        self.ui.setupUi(self)

        self.ui.doneButton.clicked.connect(self.accept)

        self.ser = ser_instance

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
        self.ui.softLabel.setText(CURRENT_VERSION)

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
    
        
        
### end of file ###

