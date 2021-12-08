from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from time import time
from threading import Timer
import os
import subprocess
import platform


#get the UI from here
from ui_wifi_dlg import Ui_WiFiDialog
from wifi_keyboard_cls import KeyboardDialog


#################################################
# WiFiDialog Class - to get the system running #
#################################################
class WiFiDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()

    def __init__(self):
        super(WiFiDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_WiFiDialog()
        self.ui.setupUi(self)

        # self.t = treatment_instance
        # self.style = style_obj
        # self.ended_label = False

        # get the close event
        self.ui.cancelButton.clicked.connect(self.accept)

        # populate comboBox and connect signals
        self.ui.comboBox.addItem('Scan Networks')
        # self.ui.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.ui.comboBox.activated.connect(self.selectionchange)
        # self.ui.comboBox.highlighted.connect(self.selectionchange)

        # save button
        self.ui.saveButton.clicked.connect(self.SaveNetwork)
        
        # buttons over line edits
        self.ui.ssidButton.clicked.connect(self.SsidEdition)
        self.ui.passButton.clicked.connect(self.PassEdition)

        # to start 1 second timer
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        # SIGNALS
        # connect scan button
        self.ui.scanButton.clicked.connect(self.ScanNetworks)
        
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)

        # first interfase update
        self.GetInterfases()
        self.update_exit = False
        self.update_exit_cnt = 0

        self.button_disable = "background-color: rgb(245, 245, 245);\
                               border-radius: 10px;\
                               border:2px solid rgb(159, 162, 164);\
                               color: rgb(159, 162, 164);"        

        self.button_enable = "background-color: rgb(240, 238, 126);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);\
                              color: rgb(55, 52, 53);"        

        
    def TimerOneSec(self):
        self.one_second_signal.emit()

        
    def UpdateOneSec (self):        
        # do a UI update if its necessary
        recheck = int(self.ui.recheckLabel.text())
        if recheck:
            recheck -= 1
            self.ui.recheckLabel.setText(str(recheck))
        else:
            self.ui.recheckLabel.setText('5')
            self.GetInterfases()

        if self.update_exit:
            if self.update_exit_cnt > 0:
                self.ui.waitLabel.setText('Wait ' + str(self.update_exit_cnt) + ' to save and exit!')
                self.update_exit_cnt -= 1
            else:
                self.ui.saveButton.setText('Exit')
                self.ui.saveButton.setEnabled(True)
                self.ui.saveButton.setStyleSheet(self.button_enable)

    
    def GetInterfases (self):
        output = ""
        try:
            output = subprocess.check_output(['python3','scan_interfase.py'])
        except subprocess.CalledProcessError as err:
            print(err)
            return
 
        output_str = output.decode('utf-8')
        lines = output_str.split('\n')

        for line in lines:
            wired_index = line.find('eth')
            wireless_index = line.find('wlan')
            if wired_index > 0:
                ether_str = 'Net: eth' + line[wired_index + 3]
                self.ui.wiredLabel1.setText(ether_str)

                ip_index = line.find('ip')
                gw_index = line.find('gw')                
                if ip_index > 0 and gw_index > 0:
                    ip_str = 'Ip: ' + line[ip_index + 3:gw_index]
                    self.ui.wiredLabel2.setText(ip_str)
                    gw_str = 'Gw: ' + line[gw_index + 3:]
                    self.ui.wiredLabel3.setText(gw_str)
                    
            if wireless_index > 0:
                ether_str = 'Net: wlan' + line[wireless_index + 4]
                self.ui.wirelessLabel1.setText(ether_str)

                ip_index = line.find('ip')
                gw_index = line.find('gw')                
                if ip_index > 0 and gw_index > 0:
                    ip_str = 'Ip: ' + line[ip_index + 3:gw_index]
                    self.ui.wirelessLabel2.setText(ip_str)
                    gw_str = 'Gw: ' + line[gw_index + 3:]
                    self.ui.wirelessLabel3.setText(gw_str)

                    
    def ScanNetworks (self):
        self.ui.comboBox.clear()
        output = ""
        self.ui.scanButton.setText('Scanning')
        self.ui.scanButton.setStyleSheet(self.button_disable)
        self.ui.scanButton.setEnabled(False)
        try:
            output = subprocess.check_output(['python3','scan_wifi.py'])
        except subprocess.CalledProcessError as err:
            print(err)
            return
 
        output_str = output.decode('utf-8')
        lines = output_str.split('\n')
        self.ui.comboBox.addItems(lines)
        self.ui.scanButton.setText('Scan')
        self.ui.scanButton.setStyleSheet(self.button_enable)
        self.ui.scanButton.setEnabled(True)
        

                    
    def selectionchange(self):
        self.ui.ssidEdit.clear()
        self.ui.passEdit.clear()
        ssid = self.ui.comboBox.currentText()
        print(ssid)
        ssid_index = ssid.find('signal')
        if ssid_index > 0:
            ssid_str = ssid[:ssid_index - 1]
            self.ui.ssidEdit.setText(ssid_str)


    def SsidEdition (self):
        ssid_str = self.KeyboardScreen("SSID:", self.ui.ssidEdit.text())
        self.ui.ssidEdit.setText(ssid_str)

        
    def PassEdition (self):
        pass_str = self.KeyboardScreen("Password:", self.ui.passEdit.text())
        self.ui.passEdit.setText(pass_str)


    def SaveNetwork (self):
        if self.ui.saveButton.text() != 'Exit':
            self.ui.cancelButton.setStyleSheet(self.button_disable)
            self.ui.saveButton.setStyleSheet(self.button_disable)
            self.ui.scanButton.setStyleSheet(self.button_disable)
            self.ui.saveButton.setText('Saving')
            self.ui.cancelButton.setEnabled(False)
            self.ui.saveButton.setEnabled(False)
            self.ui.scanButton.setEnabled(False)
            self.update_exit = True        
            self.update_exit_cnt = 15

            # check root access
            (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)    
            if distname == 'debian':
                os.system('sudo python3 ssid_change_only_one.py ' + self.ui.ssidEdit.text() + ' ' + self.ui.passEdit.text())
                os.system('python3 reconfigure.py 1')
            else:
                pass    #dont do anything in slackware
        else:
            self.accept()
            
        
    ####################
    # Function Screens #
    ####################
    def KeyboardScreen (self, conf, last):
        a = KeyboardDialog(conf, last)
        a.setModal(True)
        a.exec_()
        return a.answer



### End of Dialog ###

        
### end of file ###
