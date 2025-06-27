# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtCore, QtWidgets
import os
# import threading

#imported uis
from ui_rtf3 import Ui_RTFWindow


class RTFWindow (QMainWindow):

    # SIGNALS
    rtf_one_second_signal = pyqtSignal()

    def __init__(self, serialport, parent=None):
        super(RTFWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_RTFWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent

        # mode buttons and style
        self.style_act = """color: rgb(255,255,255);
                            background-color: rgb(173, 163, 170);
                            border-radius: 25;
                            border: 2px rgb(173, 163, 170);"""
        self.style_deact = """color: rgb(148,138,146);
                              border-radius: 25;
                              border: 2px solid rgb(148, 138, 146);"""
        
        # connect buttons
        self.ui.doneButton.clicked.connect(self.close)
        self.ui.hit_stop_Button.clicked.connect(self.RTFChangeMode)
        self.ui.hit_skip_Button.clicked.connect(self.RTFChangeMode)
        self.ui.cont_Button.clicked.connect(self.RTFChangeMode)
        self.ui.pwrUpButton.clicked.connect(self.RTFChangePower)
        self.ui.pwrDwnButton.clicked.connect(self.RTFChangePower)
        self.ui.timerUpButton.clicked.connect(self.RTFChangeCycleTime)
        self.ui.timerDwnButton.clicked.connect(self.RTFChangeCycleTime)        
        self.ui.tot_timerUpButton.clicked.connect(self.RTFChangeTimer)
        self.ui.tot_timerDwnButton.clicked.connect(self.RTFChangeTimer)        

        # cycle time list and initial time
        self.cycle_timer_list = [6, 12, 30, 60]
        self.cycle_timer_index = 0
        self.cycle_time_int = 6
        self.ui.timerLabel.setText('6s')
        self.sweep = 6
        self.changing_timer = 0
        
        # timer signal to the Update
        self.rtf_one_second_signal.connect(self.RTFOneSecUpdate)
        self.parent.serialcb.connect(self.RTFSerialDataCallback)
        
        ## upload parent values
        # set initial power
        self.pwr_index = self.parent.pwr_index_ch_list[0]
        power_str = self.parent.pwr_list[self.pwr_index]
        self.ui.pwrLabel.setText(power_str)
        self.RTFChangePowerUpdate()

        # set initial mode
        self.rtfmode = 'hit_stop'
        self.RTFChangeModeUpdate(self.rtfmode)

        # set initial progress bar config
        self.ui.progressBar.setTextVisible(False)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setFixedHeight(4)
        self.ui.progressBar.setMaximum(self.cycle_time_int - 1)
        
        # set initial freq
        self.freq_index = 0

        # set initial tot timer
        self.rtf_remaining_minutes = 20
        self.rtf_remaining_seconds = 0
        self.ui.tot_timerLabel.setText(f'{self.rtf_remaining_minutes}m {self.rtf_remaining_seconds}s')
        
        ## activate the 1 second timer its repetitive
        self.rtf1seg = QTimer()
        self.rtf1seg.timeout.connect(self.RTFTimerOneSec)
        self.rtf1seg.start(1000)
        self.running = True

        self.RTFSendConfig('square', 'start')

        
    def RTFChangeMode (self):
        sender = self.sender()
        obj_name = sender.objectName()
        
        if obj_name == 'hit_stop_Button':
            self.RTFChangeModeUpdate('hit_stop')

        if obj_name == 'hit_skip_Button':
            self.RTFChangeModeUpdate('hit_skip')            

        if obj_name == 'cont_Button':
            self.RTFChangeModeUpdate('cont')

                
    def RTFChangeModeUpdate (self, mode_str):
        if mode_str == 'hit_stop':
            self.rtfmode = 'hit_stop'
            self.ui.hit_stop_Button.setStyleSheet(self.style_act)
            self.ui.hit_skip_Button.setStyleSheet(self.style_deact)
            self.ui.cont_Button.setStyleSheet(self.style_deact)            

        if mode_str == 'hit_skip':
            self.rtfmode = 'hit_skip'            
            self.ui.hit_stop_Button.setStyleSheet(self.style_deact)
            self.ui.hit_skip_Button.setStyleSheet(self.style_act)
            self.ui.cont_Button.setStyleSheet(self.style_deact)            

        if mode_str == 'cont':
            self.rtfmode = 'cont'
            self.ui.hit_stop_Button.setStyleSheet(self.style_deact)
            self.ui.hit_skip_Button.setStyleSheet(self.style_deact)
            self.ui.cont_Button.setStyleSheet(self.style_act)            
                

    def RTFChangeFrequency (self):
        freq_str = self.parent.freq_list[self.freq_index]
        self.ui.freqLabel.setText(freq_str)
        # self.SendConfig('ch' + str(ch_index + 1), 'frequency ' + self.freq_conf_list[self.freq_index_ch_list[ch_index]])
        self.RTFSendConfig('square frequency', self.parent.freq_conf_list[self.freq_index])

        
    def RTFChangeCycleTime (self):
        sender = self.sender()
        obj_name = sender.objectName()

        if obj_name == 'timerUpButton':
            if self.cycle_timer_index < len(self.cycle_timer_list) - 1:
                self.cycle_timer_index += 1

        if obj_name == 'timerDwnButton':
            if self.cycle_timer_index > 0:
                self.cycle_timer_index -= 1

        self.cycle_time_int = self.cycle_timer_list[self.cycle_timer_index]
        self.ui.timerLabel.setText(f'{self.cycle_time_int}s')
        self.ui.progressBar.setMaximum(self.cycle_time_int - 1)
        ## if ch is in treat restart timer
        # if self.in_treat_ch_list[ch_index] == True:
            # self.StartChannelByIndex(ch_index)
            # self.StartChannelUpdateTimer(ch_index)            


    def RTFChangeTimer (self):
        sender = self.sender()
        obj_name = sender.objectName()

        self.changing_timer = 3
        self.rtf_remaining_seconds = 0

        orig = self.rtf_remaining_minutes

        if self.rtf_remaining_minutes > 10:
            remain = self.rtf_remaining_minutes % 5
            self.rtf_remaining_minutes -= remain
            print(f'orig: {orig} remain: {remain} rtf: {self.rtf_remaining_minutes}')
            
        if obj_name == 'tot_timerUpButton':
            if self.rtf_remaining_minutes > 50:
                self.rtf_remaining_minutes = 60
            elif self.rtf_remaining_minutes >= 10:
                self.rtf_remaining_minutes += 5
            else:
                self.rtf_remaining_minutes += 1
                
        if obj_name == 'tot_timerDwnButton':
            if self.rtf_remaining_minutes > 10:
                self.rtf_remaining_minutes -= 5
            elif self.rtf_remaining_minutes > 1:
                self.rtf_remaining_minutes -= 1

        self.ui.tot_timerLabel.setText(f'{self.rtf_remaining_minutes}m {self.rtf_remaining_seconds}s')
        

    def RTFChangePower (self):
        sender = self.sender()
        obj_name = sender.objectName()

        if obj_name == 'pwrUpButton':
            if self.pwr_index < 5:
                self.pwr_index += 1

        if obj_name == 'pwrDwnButton':
            if self.pwr_index > 0:
                self.pwr_index -= 1

        self.RTFChangePowerUpdate()
    

    def RTFChangePowerUpdate (self):
        power_str = self.parent.pwr_list[self.pwr_index]
        self.ui.pwrLabel.setText(power_str)        
        self.RTFSendConfig('square intensity', power_str)


    def RTFSendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command + '\n')
            print(channel + ' ' + command + '\n')

            
    def RTFStopEmmiting (self):
        self.running = False
        self.ui.msg1Label.setText('Emisions ended!')
        self.ui.msgfreqLabel.setText('')
        
        
    def closeEvent (self, event):
        print("close")
        self.RTFSendConfig('stop', '')
        self.RTFStopEmmiting()
        # self.parent.cbMenu(self.volume)
        self.parent.cbRTF()        


    ###########################
    # One Second Timer signal #
    ###########################
    def RTFTimerOneSec(self):
        self.rtf_one_second_signal.emit()


    def RTFOneSecUpdate (self):
        if self.running == False:
            return

        if self.changing_timer:
            self.changing_timer -= 1
            return
        
        if self.sweep < self.cycle_time_int - 1:
            self.sweep += 1
        else:
            self.sweep = 0

        self.ui.progressBar.setValue(self.sweep)            
        if self.sweep == 0:
            self.ui.msgfreqLabel.setText('cycle sweep')
            if self.freq_index < len(self.parent.freq_conf_list) - 1:
                self.freq_index += 1
            else:
                self.freq_index = 0
            self.RTFChangeFrequency()
        else:
            self.ui.msgfreqLabel.setText('')

        if (self.rtf_remaining_minutes > 0 or
            self.rtf_remaining_seconds > 0):
            if self.rtf_remaining_seconds > 0:
                self.rtf_remaining_seconds -= 1
            else:
                self.rtf_remaining_minutes -= 1
                self.rtf_remaining_seconds = 59

            # update ui every second
            self.ui.tot_timerLabel.setText(f'{self.rtf_remaining_minutes}m {self.rtf_remaining_seconds}s')
        else:
            # self.StopChannelByIndex(x)
            pass
            
        
    def RTFSerialDataCallback (self, rcv):        
        # print ("rtf data callback!")
        self.RTFSerialProcessString(rcv)
                

    def RTFSerialProcessString (self, rcv):
        if rcv.startswith("resistance "):
            rcv_list = rcv.split(' ')
            try:
                res_int = int(rcv_list[1])
            except:
                res_int = 0

            if res_int < 330:
                display = 100
            elif res_int > 33000:
                display = 0
            else:
                f = res_int * (-3.06e-3)
                display = int(f + 101)

            if display > 100:
                display = 100
            elif display < 0:
                display = 0
                
            self.ui.lcdNumber.display(str(display))

            if display > 98:
                if self.rtfmode == 'hit_stop':
                    self.RTFSendConfig('stop', '')
                    self.RTFStopEmmiting()
                    
                elif self.rtfmode == 'hit_skip':
                    self.ui.msgfreqLabel.setText('sweep cycle')
                    if self.freq_index < len(self.parent.freq_conf_list) - 1:
                        self.freq_index += 1
                    else:
                        self.freq_index = 0

                    self.sweep = 0
                    self.RTFChangeFrequency()
                    
