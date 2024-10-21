from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer, QEventLoop
import get_distro
import os

#get the UI from here
from lan_settings_ui import Ui_LanDialog
# get Dialog classes from here
from wifi_keyboard_cls import KeyboardDialog


#############################################################
# DisplayModeDialog Class - to set the system power control #
#############################################################
class LanDialog(QDialog):
    def __init__(self):
        super(LanDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_LanDialog()
        self.ui.setupUi(self)

        # get the close event
        self.ui.cancelButton.clicked.connect(self.accept)

        # save button
        self.ui.saveButton.clicked.connect(self.SaveNewIp)

        # populate comboBox and connect signals
        self.ui.comboBox.addItem('Fixed IP')
        self.ui.comboBox.addItem('Dynamic IP')
        self.ui.comboBox.setCurrentIndex(1)
        self.current_sel = 'Dynamic IP'

        # self.ui.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.ui.comboBox.activated.connect(self.selectionchange)
        # self.ui.comboBox.highlighted.connect(self.selectionchange)

        # buttons over line edits
        self.ui.ipButton.clicked.connect(self.IpEdition)
        self.ui.gwButton.clicked.connect(self.GwEdition)
        self.ui.dnsButton.clicked.connect(self.DnsEdition)        
        
        self.button_disable = "background-color: rgb(245, 245, 245);\
                               border-radius: 10px;\
                               border:2px solid rgb(159, 162, 164);\
                               color: rgb(159, 162, 164);"        

        self.button_enable = "background-color: rgb(240, 238, 126);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);\
                              color: rgb(55, 52, 53);"        

        self.ChangeButtons(self.current_sel)
        

    def selectionchange(self):
        self.current_sel = self.ui.comboBox.currentText()
        self.ChangeButtons(self.current_sel)


    def SaveNewIp (self):
        self.ui.cancelButton.setStyleSheet(self.button_disable)
        self.ui.saveButton.setStyleSheet(self.button_disable)
        self.ui.saveButton.setText('Saving')
        self.ui.cancelButton.setEnabled(False)
        self.ui.saveButton.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.ipEdit.setEnabled(False)
        self.ui.gwEdit.setEnabled(False)
        self.ui.dnsEdit.setEnabled(False)
        
        # delay
        loop = QEventLoop()
        QTimer.singleShot(200, loop.quit)
        loop.exec_()
        # end delay
        
        distname = get_distro.GetDistroName()
        if distname == 'debian' or \
           distname == 'Raspbian':
            if self.current_sel == 'Fixed IP':
                ip = self.ui.ipEdit.text()
                gw = self.ui.gwEdit.text()
                dns = self.ui.dnsEdit.text()
                os.system('sudo python3 change_lan_settings.py fix ' + ip + ' ' + gw + ' ' + dns)
            elif self.current_sel == 'Dynamic IP':
                os.system('sudo python3 change_lan_settings.py dynamic')
                
        else:
            print('anything on slackware')


        self.ui.saveButton.setText('Saved')
        self.ui.cancelButton.setStyleSheet(self.button_enable)
        self.ui.cancelButton.setText('Done!')
        self.ui.cancelButton.setEnabled(True)

        
    def ChangeButtons (self, selection):
        if selection == 'Dynamic IP':
            self.ui.ipEdit.setEnabled(False)
            self.ui.gwEdit.setEnabled(False)
            self.ui.dnsEdit.setEnabled(False)
        elif selection == 'Fixed IP':
            self.ui.ipEdit.setEnabled(True)
            self.ui.gwEdit.setEnabled(True)
            self.ui.dnsEdit.setEnabled(True)
            
            
    def IpEdition (self):
        ip_str = self.KeyboardScreen("IP/MASK:", self.ui.ipEdit.text())
        self.ui.ipEdit.setText(ip_str)


    def GwEdition (self):
        gw_str = self.KeyboardScreen("GW:", self.ui.gwEdit.text())
        self.ui.gwEdit.setText(gw_str)
        
        
    def DnsEdition (self):
        dns_str = self.KeyboardScreen("DNS:", self.ui.dnsEdit.text())
        self.ui.dnsEdit.setText(dns_str)


    ####################
    # Function Screens #
    ####################
    def KeyboardScreen (self, conf, last):
        a = KeyboardDialog(conf, last)
        a.setModal(True)
        a.exec_()
        return a.answer

    
### end of file ###
