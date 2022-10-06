from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon


#get the UI from here
from wifi_test_thread_dlg_ui import Ui_WifiTestDialog

#get the code for manager
from wifi_thread_manager import WiFiThreadManager


########################
# KeyboardDialog Class #
########################
class WifiTestDialog(QDialog):

    #SIGNALS
    # signal to update in 2 seconds
    two_second_signal = pyqtSignal()

    def __init__(self):
        super(WifiTestDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_WifiTestDialog()
        self.ui.setupUi(self)

        # SIGNALS
        # connect the timer signal to the Update
        self.two_second_signal.connect(self.UpdateTwoSec)

        # connect common buttons

        # inits
        self.ui.wifiLabel1.setText('status:')

        ## setup wifi icons
        ## url(:/buttons/resources/Stop.png)
        self.wifi_act_Icon = QIcon(':/symbols/resources/wifi-symbol_act.png')
        self.wifi_err_Icon = QIcon(':/symbols/resources/wifi-symbol_err.png')
        self.wifi_disa_Icon = QIcon(':/symbols/resources/wifi-symbol_disa.png')
        self.wifi_emit_Icon = QIcon(':/symbols/resources/wifi-symbol_emit.png')
        

        # to start 2 second timer
        self.t2seg = QTimer()
        self.t2seg.timeout.connect(self.TimerTwoSec)
        self.t2seg.start(2000)

        # start manager background process
        self.MyThread = WiFiThreadManager()
        self.MyThread.start()


    def TimerTwoSec(self):
        self.two_second_signal.emit()

        
    def UpdateTwoSec (self):
        new_status = self.MyThread.GetStatus()
        self.ui.wifiLabel1.setText(new_status)

        if new_status == 'NO CONN':
            self.ui.wifiButton.setIcon(self.wifi_disa_Icon)
        elif new_status == 'IP':
            self.ui.wifiButton.setIcon(self.wifi_err_Icon)
        elif new_status == 'PING':
            self.ui.wifiButton.setIcon(self.wifi_act_Icon)
        elif new_status == 'TUNNEL':
            self.ui.wifiButton.setIcon(self.wifi_emit_Icon)

        
### end of file ###
