from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer, QEventLoop
import platform
import os

#get the UI from here
from display_mode_ui import Ui_DisplayModeDialog


#############################################################
# DisplayModeDialog Class - to set the system power control #
#############################################################
class DisplayModeDialog(QDialog):
    def __init__(self, treatment_instance):
        super(DisplayModeDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_DisplayModeDialog()
        self.ui.setupUi(self)

        # get the close event
        self.ui.cancelButton.clicked.connect(self.RebootOrCancel)

        # save button
        self.ui.saveButton.clicked.connect(self.SaveNewMode)

        # populate comboBox and connect signals
        self.ui.comboBox.addItem('Magnet ver 4.0')
        self.ui.comboBox.addItem('Magnet ver 4.1')
        self.ui.comboBox.addItem('Stretcher ver 4.0')
        self.ui.comboBox.addItem('Light Treatment')
        self.current_sel = ''

        # self.ui.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.ui.comboBox.activated.connect(self.selectionchange)
        # self.ui.comboBox.highlighted.connect(self.selectionchange)

        self.button_disable = "background-color: rgb(245, 245, 245);\
                               border-radius: 10px;\
                               border:2px solid rgb(159, 162, 164);\
                               color: rgb(159, 162, 164);"        

        self.button_enable = "background-color: rgb(240, 238, 126);\
                              border-radius: 10px;\
                              border:2px solid rgb(55, 52, 53);\
                              color: rgb(55, 52, 53);"        
        
        

    def selectionchange(self):
        self.current_sel = self.ui.comboBox.currentText()
        self.ui.currentLabel.setText('Change to: ' + self.current_sel)


    def SaveNewMode (self):
        self.ui.cancelButton.setStyleSheet(self.button_disable)
        self.ui.saveButton.setStyleSheet(self.button_disable)
        self.ui.saveButton.setText('Saving')
        self.ui.cancelButton.setEnabled(False)
        self.ui.saveButton.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        # delay
        loop = QEventLoop()
        QTimer.singleShot(200, loop.quit)
        loop.exec_()
        # end delay
        
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)    
        if distname == 'debian':
            if self.current_sel == 'Magnet ver 4.0':
                os.system('python3 change_display_operation_mode.py magnet40')
            elif self.current_sel == 'Magnet ver 4.1':
                os.system('python3 change_display_operation_mode.py magnet41')
            elif self.current_sel == 'Stretcher ver 4.0':
                os.system('python3 change_display_operation_mode.py stretcher40')
            elif self.current_sel == 'Light Treatment':
                os.system('python3 change_display_operation_mode.py light_treat')
                
        else:
            print('slackware: not executing change_display_operation_mode.py')


        self.ui.saveButton.setText('Saved')
        self.ui.cancelButton.setStyleSheet(self.button_enable)
        self.ui.cancelButton.setText('Done!')
        self.ui.cancelButton.setEnabled(True)

    def RebootOrCancel (self):
        sender = self.sender()

        if sender.text() == 'Done!':
            (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)    
            if distname == 'debian':
                os.system('sudo reboot')
                
            else:
                print('slackware: not rebooting')
                self.accept()

        else:
            self.accept()


        
### end of file ###
