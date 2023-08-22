from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer, QEventLoop
import random

#get the UI from here
from security_code_ui import Ui_SecurityDialog
# get Dialog classes from here
from wifi_keyboard_cls import KeyboardDialog


#############################################################
# DisplayModeDialog Class - to set the system power control #
#############################################################
class SecurityDialog(QDialog):
    def __init__(self, ser_instance):
        super(SecurityDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_SecurityDialog()
        self.ui.setupUi(self)

        # get the parent reference and data
        self.ser = ser_instance

        # get the close event
        self.ui.cancelButton.clicked.connect(self.accept)

        # save button
        self.ui.saveButton.clicked.connect(self.SaveNewCode)

        # buttons over line edits
        self.ui.securityButton.clicked.connect(self.SecurityEdition)
        
        self.button_disable = "background-color: rgb(245, 245, 245);\
                               border-radius: 10px;\
                               border:2px solid rgb(159, 162, 164);\
                               color: rgb(159, 162, 164);"        

        self.button_enable = "background-color: rgb(240, 238, 126);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);\
                              color: rgb(55, 52, 53);"        

        self.ui.statusLabel.setText('')

        self.random_number = random.randint(0, 9999)
        self.random_sum = self.SumDigits(self.random_number)
        self.ui.actualLabel.setText(str(self.random_number))
        

    def SumDigits(self, n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

        
    def selectionchange(self):
        self.current_sel = self.ui.comboBox.currentText()
        self.ChangeButtons(self.current_sel)


    def SaveNewCode (self):
        code_str = self.ui.securityEdit.text()
        if  code_str == '':
            self.ui.statusLabel.setText('No new code founded!')
            # delay
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()
            # end delay

        else:
            code_num = int(code_str)
            if code_num == (self.random_sum + 0) or \
               code_num == (self.random_sum + 1) or \
               code_num == (self.random_sum + 2):
                self.ui.statusLabel.setText('new code is valid, processing...')

                if code_num == (self.random_sum + 1):
                    self.ser.Write("tamper enable\r\n")

                if code_num == (self.random_sum + 2):
                    self.ser.Write("tamper disable\r\n")
                    
                # delay
                loop = QEventLoop()
                QTimer.singleShot(1000, loop.quit)
                loop.exec_()
                # end delay

        self.accept()
        
                    
    def SecurityEdition (self):
        sec_str = self.KeyboardScreen("New Security Code:", self.ui.securityEdit.text())
        self.ui.securityEdit.setText(sec_str)



    ####################
    # Function Screens #
    ####################
    def KeyboardScreen (self, conf, last):
        a = KeyboardDialog(conf, last)
        a.setModal(True)
        a.exec_()
        return a.answer

    
### end of file ###
