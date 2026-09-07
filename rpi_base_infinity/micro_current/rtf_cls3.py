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

#Here import the UIs or classes that got the UIs
from close_cls3 import CloseWindow


class RTFWindow (QMainWindow):

    # SIGNALS
    rtf_one_second_signal = pyqtSignal()

    def __init__(self, serialport, runas='none', parent=None):
        super(RTFWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_RTFWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent
        self.runas = runas

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
        self.rtfmode = self.parent.rtfmode
        self.RTFChangeModeUpdate(self.rtfmode)

        # set initial progress bar config
        self.ui.progressBar.setTextVisible(False)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setFixedHeight(4)
        self.ui.progressBar.setMaximum(self.cycle_time_int - 1)
        self.ui.lcdNumber.display(str(0))
        
        # set initial freq
        self.freq_index = 0

        # set initial tot timer
        self.rtf_remaining_minutes = 20
        self.rtf_remaining_seconds = 0
        self.ui.tot_timerLabel.setText(f'{self.rtf_remaining_minutes}m {self.rtf_remaining_seconds}s')

        # set initial messages
        self.ui.msg1Label.setText('')
        self.ui.msg2Label.setText('')

        # set initial batt values
        self.rtf_mains_mode = self.parent.mains_mode
        self.rtf_mains_state_int = self.parent.mains_state_int
        if self.rtf_mains_mode == 'mains':
            self.ui.battButton.setIcon(self.parent.mains_icon_list[self.rtf_mains_state_int])
        else:    # 'battery'
            self.ui.battButton.setIcon(self.parent.batt_icon_list[self.rtf_mains_state_int])
        batt_str = self.parent.ui.battLabel.text()
        self.ui.battLabel.setText(batt_str)
        
        ## activate the 1 second timer its repetitive
        self.rtf1seg = QTimer()
        self.rtf1seg.timeout.connect(self.RTFTimerOneSec)
        self.rtf1seg.start(1000)
        self.running = True

        ## progress timer for start and first config        
        self.ui.ch2_progressBar.setTextVisible(False)
        self.ui.ch2_progressBar.setValue(0)
        self.ui.ch2_progressBar.setFixedHeight(4)
        self.rtf_progressBar_timer = QTimer()
        self.sine_cnt = 0
        
        if self.runas == 'nervsync':
            self.ui.ch_nameLabel.setText('NervSync')
            self.ui.ch2_progressBar.hide()
            self.RTFSendConfig('square', 'start')
        elif self.runas == 'nervsync_cont':
            self.ui.ch_nameLabel.setText('NervSync')
            self.ui.ch2_progressBar.hide()
            self.RTFChangeModeUpdate('cont')
            self.ui.hit_stop_Button.setEnabled(False)
            self.ui.hit_skip_Button.setEnabled(False)
            self.ui.cont_Button.setEnabled(False)
            self.ui.hit_stop_Button.hide()
            self.ui.hit_skip_Button.hide()
            self.RTFSendConfig('square', 'start')
        elif self.runas == 'cellsync':
            self.ui.ch_nameLabel.setText('CellSync')            
            self.RTFSendConfig('sine', 'start')
            self.ui.hit_stop_Button.setEnabled(False)
            self.ui.hit_skip_Button.setEnabled(False)
            self.ui.cont_Button.setEnabled(False)
            self.ui.hit_stop_Button.hide()
            self.ui.hit_skip_Button.hide()
            self.ui.cont_Button.hide()

            self.ui.ch2_progressBar.setValue(0)
            self.rtf_progressBar_timer.singleShot(200, self.RTFProgressBarSM)
            
        else:
            self.close()

        # to show the battery close window
        self.rtf_battery_low_show = False

        
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
        if self.runas == 'nervsync' or \
           self.runas == 'nervsync_cont':
            self.RTFSendConfig('square frequency', self.parent.freq_conf_list[self.freq_index])
            self.RTFSendEncodFreq('enc 1', self.freq_index)
            self.RTFSendEncodPwr('enc 0', self.pwr_index)        
        else:    # cellsync
            self.RTFSendConfig('sine frequency', self.parent.freq_conf_list[self.freq_index])
            self.RTFSendEncodFreq('enc 3', self.freq_index)
            self.RTFSendEncodPwr('enc 2', self.pwr_index)        


    def RTFSendEncodFreq (self, encoder_str, value):
        if self.s.port_open == True:
            encoder = encoder_str

            if value <= 9:
                self.s.Write(encoder + ' ' + str(value) + '\n')
            elif value == 10:
                self.s.Write(encoder + ' :\n')
            elif value == 11:
                self.s.Write(encoder + ' ;\n')


    def RTFSendEncodPwr (self, encoder_str, value):
        if self.s.port_open == True:
            encoder = encoder_str            
            self.s.Write(encoder + ' ' + str(value) + '\n')

            
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
            # print(f'orig: {orig} remain: {remain} rtf: {self.rtf_remaining_minutes}')
            
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
        if self.runas == 'nervsync' or \
           self.runas == 'nervsync_cont':
            self.RTFSendConfig('square intensity', power_str)
            self.RTFSendEncodPwr('enc 0', self.pwr_index)
        else:    # 'cellsync'
            self.RTFSendConfig('sine intensity', power_str)
            self.RTFSendEncodPwr('enc 2', self.pwr_index)


    def RTFSendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command + '\n')
            print(channel + ' ' + command + '\n')

            
    def RTFStopEmmiting (self):
        self.running = False
        self.ui.msg1Label.setText('Emisions ended!')
        self.ui.msgfreqLabel.setText('')
        self.ui.progressBar.setValue(0)
        
        
    def closeEvent (self, event):
        print("close")
        self.RTFSendConfig('stop', '')
        self.RTFStopEmmiting()
        self.parent.cbRTF(self.rtfmode, self.freq_index, self.pwr_index)


    def RTFUpdateSupplyPower (self, power_str):
        # supply mains 11.2 13.2 08.6 08.3 08.3 08.4 
        # supply battery 00.2 13.2 08.6 08.3 08.3 08.4
        my_mode, my_percent = self.parent.CheckCharge_Mains_Batt_Icon(power_str)

        icon_index = self.parent.CheckBattValues(my_percent)
        self.rtf_mains_state_int = icon_index
        self.rtf_mains_mode = my_mode

        self.ui.battLabel.setText(f'{my_percent}%')
        if self.rtf_mains_mode == 'mains':
            self.ui.battButton.setIcon(self.parent.mains_icon_list[self.rtf_mains_state_int])
        else:
            self.ui.battButton.setIcon(self.parent.batt_icon_list[self.rtf_mains_state_int])

        # show battery_low window
        if my_percent > 22:
            self.battery_low_show = False
        elif my_percent < 17:
            if self.battery_low_show == False:
                self.battery_low_show = True
                self.CloseScreen()
        

    def RTFProgressBarSM (self):
        next_cycle = False
        
        if self.running:
            if self.parent.pol_index_ch_list[1] == 'negative':
                sine_point = -self.parent.sine_pos_table_list[self.sine_cnt]
            elif self.parent.pol_index_ch_list[1] == 'positive':
                sine_point = self.parent.sine_pos_table_list[self.sine_cnt]
            else:    # alternative
                sine_point = self.parent.sine_alt_table_list[self.sine_cnt]

            display, progress = self.parent.ProgressCalcValue(self.parent.pwr_index_ch_list[1], sine_point)
            self.ui.ch2_progressBar.setValue(progress)
            self.ui.lcdNumber.display(str(display))
            next_cycle = True
        else:
            self.ui.ch2_progressBar.setValue(0)
            self.ui.lcdNumber.display('---')

        if self.sine_cnt < 16 - 1:
            self.sine_cnt += 1
        else:
            self.sine_cnt = 0

        if next_cycle:
            self.rtf_progressBar_timer.singleShot(200, self.RTFProgressBarSM)
            
                
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
            self.ui.msg2Label.setText('by time')
            self.RTFSendConfig('stop', '')
            self.RTFStopEmmiting()
            
        
    def RTFSerialDataCallback (self, rcv):        
        # print ("rtf data callback!")
        self.RTFSerialProcessString(rcv)
                

    def RTFSerialProcessString (self, rcv):
        if rcv.startswith("resistance "):
            if self.runas != 'nervsync':
                return
            
            rcv_list = rcv.split(' ')
            try:
                res_int = int(rcv_list[1])
            except:
                res_int = 0

            if res_int < 330:
                display = 100
            # elif res_int > 33000:
            #     display = 0
            else:
                offset = 101 + self.parent.gain_ch1
                f = res_int * (-3.06e-3)
                display = int(f + offset)

            if display > 100:
                display = 100
            elif display < 0:
                display = 0
                
            self.ui.lcdNumber.display(str(display))

            if display > 98:
                if self.rtfmode == 'hit_stop':
                    self.RTFSendConfig('stop', '')
                    self.ui.msg2Label.setText('channel open!')
                    self.RTFStopEmmiting()
                    
                elif self.rtfmode == 'hit_skip':
                    self.ui.msgfreqLabel.setText('sweep cycle')
                    if self.freq_index < len(self.parent.freq_conf_list) - 1:
                        self.freq_index += 1
                    else:
                        self.freq_index = 0

                    self.sweep = 0
                    self.RTFChangeFrequency()
                    

        # supply voltage measurement
        if rcv.startswith("supply "):
            try:
                self.RTFUpdateSupplyPower(rcv)
            except:
                print('error on supply str!')

            return
        # end of supply voltage measurement
                    

####################################
# Different Screens Calls are here #
####################################
        
    ## Screen for Close System Low Batt
    def CloseScreen (self):
        self.a = CloseWindow()
        self.a.show()
        
