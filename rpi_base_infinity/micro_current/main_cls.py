# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets


#imported uis
from ui_micro import Ui_MainWindow


class MainWindow (QMainWindow):

    #SIGNALS
    one_second_signal = pyqtSignal()

    def __init__(self, serialport, parent=None):
        super(MainWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent
        
        # self.bt_close.clicked.connect(self.close)
        self.ui.bt_menu_close.clicked.connect(self.move_menu)
        self.ui.bt_menu_open.clicked.connect(self.move_menu)

        # ch1 & ch2 acuscope with gain
        self.ui.ch1_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch1_gainDwnButton.clicked.connect(self.GainUpDwn)
        self.ui.ch2_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch2_gainDwnButton.clicked.connect(self.GainUpDwn)
        # self.ch1_gain = 0
        # self.ch2_gain = 0
        self.gain_ch_list = [0,0,0,0]
        self.gain_ui_list = [self.ui.ch1_gainLabel, self.ui.ch2_gainLabel, 0, 0]

        # ch1 ch2 ch3 & ch4 can change polarity
        self.ui.ch1_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_negButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_negButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch3_posButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch3_altButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch3_negButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch4_posButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch4_altButton.clicked.connect(self.ChangePolarity)
        # self.ui.ch4_negButton.clicked.connect(self.ChangePolarity)
        self.pol_pos_ui_list = [self.ui.ch1_posButton, self.ui.ch2_posButton, 0, 0]        
        self.pol_alt_ui_list = [self.ui.ch1_altButton, self.ui.ch2_altButton, 0, 0]
        self.pol_neg_ui_list = [self.ui.ch1_negButton, self.ui.ch2_negButton, 0, 0]                

        # ch1 ch2 ch3 & ch4 timer options
        # self.ch1_timer_index = 0
        # self.ch2_timer_index = 0
        # self.ch3_timer_index = 0
        # self.ch4_timer_index = 0
        self.timer_index_ch_list = [0, 0, 0, 0]        
        self.timer_list = ['6s', '12s', '30s', '1m', '10m', '30m']
        # timer on ch1 ch2 ch3 ch4
        self.ui.ch1_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch1_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerDwnButton.clicked.connect(self.ChangeTimer)
        # self.ui.ch3_timerUpButton.clicked.connect(self.ChangeTimer)
        # self.ui.ch3_timerDwnButton.clicked.connect(self.ChangeTimer)
        # self.ui.ch4_timerUpButton.clicked.connect(self.ChangeTimer)
        # self.ui.ch4_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.timer_ui_list = [self.ui.ch1_timerLabel, self.ui.ch2_timerLabel, 0, 0]

        # frequency options
        # self.ch1_freq_index = 0
        # self.ch2_freq_index = 0
        # self.ch3_freq_index = 0
        # self.ch4_freq_index = 0
        self.freq_index_ch_list = [0, 0, 0, 0]
        self.freq_list = ['0.5Hz', '1.0Hz', '2.0Hz', '4.0Hz', '8.0Hz', '10Hz', '20Hz', '40Hz', '80Hz', '160Hz', '320Hz']
        self.freq_conf_list = ['0.50', '1.00', '2.00', '4.00', '8.00', '10.00', '20.00', '40.00', '80.00', '160.00', '320.00']        
        # ch1 ch2 ch3 ch4 frequency
        self.ui.ch1_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch1_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqDwnButton.clicked.connect(self.ChangeFrequency)
        # self.ui.ch3_freqUpButton.clicked.connect(self.ChangeFrequency)
        # self.ui.ch3_freqDwnButton.clicked.connect(self.ChangeFrequency)
        # self.ui.ch4_freqUpButton.clicked.connect(self.ChangeFrequency)
        # self.ui.ch4_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.freq_ui_list = [self.ui.ch1_freqLabel, self.ui.ch2_freqLabel, 0, 0]

        # ch1 ch2 ch3 ch4 intensity options
        # self.ch1_pwr_index = 0
        # self.ch2_pwr_index = 0
        # self.ch3_pwr_index = 0
        # self.ch4_pwr_index = 0
        self.pwr_index_ch_list = [0, 0, 0, 0]        
        self.pwr_list = ['25uA', '50uA', '100uA', '200uA', '400uA', '600uA']
        # ch1 ch2 ch3 ch4 power
        self.ui.ch1_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch1_pwrDwnButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrDwnButton.clicked.connect(self.ChangePower)
        # self.ui.ch3_pwrUpButton.clicked.connect(self.ChangePower)
        # self.ui.ch3_pwrDwnButton.clicked.connect(self.ChangePower)
        # self.ui.ch4_pwrUpButton.clicked.connect(self.ChangePower)
        # self.ui.ch4_pwrDwnButton.clicked.connect(self.ChangePower)
        self.pwr_ui_list = [self.ui.ch1_pwrLabel, self.ui.ch2_pwrLabel, 0, 0]        

        # ch1 to ch4 others buttons
        self.ui.ch1_startButton.clicked.connect(self.StartChannel)
        self.ui.ch1_stopButton.clicked.connect(self.StopChannel)        
        self.ui.ch1_enableButton.clicked.connect(self.EnableChannel)
        self.ui.ch2_startButton.clicked.connect(self.StartChannel)
        self.ui.ch2_stopButton.clicked.connect(self.StopChannel)        
        self.ui.ch2_enableButton.clicked.connect(self.EnableChannel)
        # self.ui.ch3_startButton.clicked.connect(self.StartCh1)
        # self.ui.ch3_stopButton.clicked.connect(self.StopCh1)        
        # self.ui.ch3_enableButton.clicked.connect(self.EnableCh1)
        # self.ui.ch4_startButton.clicked.connect(self.StartCh1)
        # self.ui.ch4_stopButton.clicked.connect(self.StopCh1)        
        # self.ui.ch4_enableButton.clicked.connect(self.EnableCh1)

        # # self.bt_min.clicked.connect(self.control_minimized)
        # # self.bt_med.clicked.connect(self.control_normal)
        # # self.bt_max.clicked.connect(self.control_maximized)

        # # frame shadows
        # # self.shadow_frame(self.stackedWidget)
        # # self.shadow_frame(self.upperFrame)
        # # self.shadow_frame(self.bt_1)
        # # self.shadow_frame(self.bt_2)
        # # self.shadow_frame(self.bt_3)
        # # self.shadow_frame(self.bt_4)

        # page selection
        self.ui.audioButton.clicked.connect(self.LateralMenu)
        self.ui.configButton.clicked.connect(self.LateralMenu)
        self.ui.logButton.clicked.connect(self.LateralMenu)
        # self.bt_4.clicked.connect(self.LateralMenu)

        ## connect the signals
        # timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)        

        ##
        ## initial setup for channels
        ##
        self.startButton_ui_list = [self.ui.ch1_startButton, self.ui.ch2_startButton, 0 , 0]        
        self.stopButton_ui_list = [self.ui.ch1_stopButton, self.ui.ch2_stopButton, 0 , 0]
        self.remainMins_ui_list = [self.ui.ch1_remainMinsLabel, self.ui.ch2_remainMinsLabel, 0, 0]
        self.remainSecs_ui_list = [self.ui.ch1_remainSecsLabel, self.ui.ch2_remainSecsLabel, 0, 0]
        self.enableButton_ui_list = [self.ui.ch1_enableButton, self.ui.ch2_enableButton, 0, 0]

        self.remaining_minutes_ch_list = [0, 0, 0, 0]
        self.remaining_seconds_ch_list = [0, 0, 0, 0]
        
        for x in range(2):
            self.stopButton_ui_list[x].hide()
            self.remainMins_ui_list[x].hide()
            self.remainSecs_ui_list[x].hide()

        # self.ui.ch1_stopButton.hide()
        # self.ui.ch1_remainMinsLabel.hide()
        # self.ui.ch1_remainSecsLabel.hide()        
        # self.ui.ch2_stopButton.hide()
        # self.ui.ch2_remainMinsLabel.hide()
        # self.ui.ch2_remainSecsLabel.hide()        
        # self.ui.ch3_stopButton.hide()
        # self.ui.ch3_remainMinsLabel.hide()
        # self.ui.ch3_remainSecsLabel.hide()        
        # self.ui.ch4_stopButton.hide()
        # self.ui.ch4_remainMinsLabel.hide()
        # self.ui.ch4_remainSecsLabel.hide()        
        # self.ch1_in_treat = False
        # self.ch2_in_treat = False
        # self.ch3_in_treat = False
        # self.ch4_in_treat = False
        self.in_treat_ch_list = [False, False, False, False]
        self.ui.bt_menu_close.hide()

        
        ## activate the 1 second timer its repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        
    def move_menu (self):
        width = self.ui.lateralMenu.width()
        normal = 0
        if width == 0:
            extender = 450
            self.ui.bt_menu_open.hide()
            self.ui.bt_menu_close.show()
        else:
            extender = normal
            self.ui.bt_menu_open.show()
            self.ui.bt_menu_close.hide()

        # self.animation = QPropertyAnimation(self.lateralMenu, b"maximumWidth")
        self.animation = QPropertyAnimation(self.ui.lateralMenu, b"minimumWidth")        
        self.animation.setStartValue(width)
        self.animation.setEndValue(extender)
        self.animation.setDuration(500)
        # self.animation.setEasingCurve(QEasingCurve.OutInBack)    #InQuad, InOutQuad, InCubic, InOutExpo
        self.animation.start()


    def LateralMenu (self):
        sender = self.sender()
        
        if sender.objectName() == 'audioButton':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_audio)
            
        if sender.objectName() == 'configButton':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_config)

        if sender.objectName() == 'logButton':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_log)
            
        
    def GainUpDwn (self):
        sender = self.sender()

        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'gainUpButton':
            if self.gain_ch_list[ch_index] < 100:
                self.gain_ch_list[ch_index] += 1

        if ch_func == 'gainDwnButton':
            if self.gain_ch_list[ch_index] > 0:
                self.gain_ch_list[ch_index] -= 1
        
        self.gain_ui_list[ch_index].setText(str(self.gain_ch_list[ch_index]))
        self.SendConfig(ch_name, 'set_gain ' + str(self.gain_ch_list[ch_index]))
        
        # if sender.objectName() == 'ch1_gainUpButton':
        #     if self.gain < 100:
        #         self.gain += 1

        # if sender.objectName() == 'ch1_gainDwnButton':
        #     if self.gain > 0:
        #         self.gain -= 1
        
        # self.ui.ch1_gainLabel.setText(str(self.gain))
        # self.SendConfig('ch1', 'set_gain ' + str(self.gain))


    def ChangePolarity (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'posButton':
            self.pol_pos_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.pol_alt_ui_list[ch_index].setStyleSheet('')
            self.pol_neg_ui_list[ch_index].setStyleSheet('')            
            self.SendConfig(ch_name, 'polarity positive')

        if ch_func == 'altButton':
            self.pol_pos_ui_list[ch_index].setStyleSheet('')
            self.pol_alt_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.pol_neg_ui_list[ch_index].setStyleSheet('')            
            self.SendConfig(ch_name, 'polarity alternative')

        if ch_func == 'negButton':
            self.pol_pos_ui_list[ch_index].setStyleSheet('')
            self.pol_alt_ui_list[ch_index].setStyleSheet('')
            self.pol_neg_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.SendConfig(ch_name, 'polarity negative')
        
        # if sender.objectName() == 'ch1_posButton':
        #     self.ui.ch1_posButton.setStyleSheet('background-color: rgb(218, 218, 218);')
        #     self.ui.ch1_altButton.setStyleSheet('')
        #     self.ui.ch1_negButton.setStyleSheet('')
        #     self.SendConfig('ch1', 'polarity positive')

        # if sender.objectName() == 'ch1_altButton':
        #     self.ui.ch1_posButton.setStyleSheet('')
        #     self.ui.ch1_altButton.setStyleSheet('background-color: rgb(218, 218, 218);')
        #     self.ui.ch1_negButton.setStyleSheet('')
        #     self.SendConfig('ch1', 'polarity alternative')

        # if sender.objectName() == 'ch1_negButton':
        #     self.ui.ch1_posButton.setStyleSheet('')
        #     self.ui.ch1_altButton.setStyleSheet('')
        #     self.ui.ch1_negButton.setStyleSheet('background-color: rgb(218, 218, 218);')
        #     self.SendConfig('ch1', 'polarity negative')
            

    def ChangeTimer (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'timerUpButton':
            if self.timer_index_ch_list[ch_index] < 5:
                self.timer_index_ch_list[ch_index] += 1

        if ch_func == 'timerDwnButton':
            if self.timer_index_ch_list[ch_index] > 0:
                self.timer_index_ch_list[ch_index] -= 1

        self.timer_ui_list[ch_index].setText(self.timer_list[self.timer_index_ch_list[ch_index]])
        ## if ch is in treat restart timer
        if self.in_treat_ch_list[ch_index] == True:
            self.StartChannelByIndex(ch_index)
                
        # if sender.objectName() == 'ch1_timerUpButton':
        #     if self.ch1_timer_index < 5:
        #         self.ch1_timer_index += 1

        # if sender.objectName() == 'ch1_timerDwnButton':
        #     if self.ch1_timer_index > 0:
        #         self.ch1_timer_index -= 1

        # self.ui.ch1_timerLabel.setText(self.timer_list[self.ch1_timer_index])
        # if self.ch1_in_treat == True:
        #     self.StartCh1()


    def ChangeFrequency (self):
        sender = self.sender()
        send_encod = False
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'freqUpButton':
            send_encod = True
            if self.freq_index_ch_list[ch_index] < 10:
                self.freq_index_ch_list[ch_index] += 1

        if ch_func == 'freqDwnButton':
            send_encod = True            
            if self.freq_index_ch_list[ch_index] > 0:
                self.freq_index_ch_list[ch_index] -= 1

        self.ChangeFrequencyByIndex(ch_index)
        if send_encod:
            self.SendEncodFreq(ch_name, self.freq_index_ch_list[ch_index])
        

        # if sender.objectName() == 'ch1_freqUpButton':
        #     send_encod = True
        #     if self.ch1_freq_index < 10:
        #         self.ch1_freq_index += 1

        # if sender.objectName() == 'ch1_freqDwnButton':
        #     send_encod = True            
        #     if self.ch1_freq_index > 0:
        #         self.ch1_freq_index -= 1

        # freq_str = self.freq_list[self.ch1_freq_index]
        # self.ui.ch1_freqLabel.setText(freq_str)
        # self.SendConfig('ch1', 'frequency ' + self.freq_conf_list[self.ch1_freq_index])
        # if send_encod:
        #     self.SendEncodFreq('ch1', self.ch1_freq_index)


    def ChangeFrequencyByIndex (self, ch_index):
        freq_str = self.freq_list[self.freq_index_ch_list[ch_index]]                
        self.freq_ui_list[ch_index].setText(freq_str)
        self.SendConfig('ch' + str(ch_index + 1), 'frequency ' + self.freq_conf_list[self.freq_index_ch_list[ch_index]])
        

    def ChangePower (self):
        sender = self.sender()
        send_encod = False
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'pwrUpButton':
            send_encod = True
            if self.pwr_index_ch_list[ch_index] < 5:
                self.pwr_index_ch_list[ch_index] += 1

        if ch_func == 'pwrDwnButton':
            send_encod = True            
            if self.pwr_index_ch_list[ch_index] > 0:
                self.pwr_index_ch_list[ch_index] -= 1

        self.ChangePowerByIndex(ch_index)
        if send_encod:
            self.SendEncodPwr(ch_name, self.pwr_index_ch_list[ch_index])
            
        # if sender.objectName() == 'ch1_pwrUpButton':
        #     send_encod = True            
        #     if self.ch1_pwr_index < 5:
        #         self.ch1_pwr_index += 1

        # if sender.objectName() == 'ch1_pwrDwnButton':
        #     send_encod = True            
        #     if self.ch1_pwr_index > 0:
        #         self.ch1_pwr_index -= 1

        # power_str = self.pwr_list[self.ch1_pwr_index]
        # self.ui.ch1_pwrLabel.setText(power_str)
        # self.SendConfig('ch1', 'intensity ' + power_str)
        # if send_encod:
        #     self.SendEncodPwr('ch1', self.ch1_pwr_index)        

    def ChangePowerByIndex (self, ch_index):
        power_str = self.pwr_list[self.pwr_index_ch_list[ch_index]]
        self.pwr_ui_list[ch_index].setText(power_str)        
        self.SendConfig('ch' + str(ch_index + 1), 'intensity ' + power_str)
        

    def StartChannel (self):
        # sends or resend a start to channel
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if self.in_treat_ch_list[ch_index] == False:
            self.SendConfig(ch_name, 'start')

        self.StartChannelByIndex(ch_index)            

        
        # self.ch1_in_treat == False:
        #     self.SendConfig('ch1', 'start')
            
        # timer = self.ui.ch1_timerLabel.text()
        # if timer[-1] == 's':
        #     self.ch1_remaining_minutes = 0
        #     self.ch1_remaining_seconds = int(timer[:-1])
        # elif timer[-1] == 'm':
        #     self.ch1_remaining_minutes = int(timer[:-1])
        #     self.ch1_remaining_seconds = 0
            
        # self.ui.ch1_remainMinsLabel.setText(str(self.ch1_remaining_minutes) + "'")
        # self.ui.ch1_remainSecsLabel.setText(str(self.ch1_remaining_seconds) + "''")        

        # self.ch1_in_treat = True
        # self.ui.ch1_remainMinsLabel.show()
        # self.ui.ch1_remainSecsLabel.show()
        # self.ui.ch1_stopButton.show()
        # self.ui.ch1_startButton.hide()


    def StartChannelByIndex (self, ch_index):
        timer = self.timer_ui_list[ch_index].text()
        if timer[-1] == 's':
            self.remaining_minutes_ch_list[ch_index] = 0
            self.remaining_seconds_ch_list[ch_index] = int(timer[:-1])
        elif timer[-1] == 'm':
            self.remaining_minutes_ch_list[ch_index] = int(timer[:-1])
            self.remaining_seconds_ch_list[ch_index] = 0

        self.remainMins_ui_list[ch_index].setText(str(self.remaining_minutes_ch_list[ch_index]) + "'")
        self.remainSecs_ui_list[ch_index].setText(str(self.remaining_seconds_ch_list[ch_index]) + "''")        

        self.in_treat_ch_list[ch_index] = True
        self.remainMins_ui_list[ch_index].show()
        self.remainSecs_ui_list[ch_index].show()
        self.stopButton_ui_list[ch_index].show()
        self.startButton_ui_list[ch_index].hide()
        

    def StopChannel (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)
        self.StopChannelByIndex(ch_index)

        # self.SendConfig('ch1', 'stop')
        # self.ch1_in_treat = False
        # self.ui.ch1_remainMinsLabel.hide()
        # self.ui.ch1_remainSecsLabel.hide()
        # self.ui.ch1_stopButton.hide()
        # self.ui.ch1_startButton.show()

        
    def StopChannelByIndex (self, ch_index):
        self.SendConfig('ch' + str(ch_index + 1), 'stop')
        self.in_treat_ch_list[ch_index] = False
        self.remainMins_ui_list[ch_index].hide()
        self.remainSecs_ui_list[ch_index].hide()
        self.stopButton_ui_list[ch_index].hide()
        self.startButton_ui_list[ch_index].show()
        

    def EnableChannel (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if self.enableButton_ui_list[ch_index].text() == 'Enable Channel':
            self.enableButton_ui_list[ch_index].setText('Disable Channel')
            self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(129, 129, 129);\
                                                               border: 2px solid rgb(218, 218, 218);')
            self.SendConfig(ch_name, 'enable')
        else:
            self.enableButton_ui_list[ch_index].setText('Enable Channel')
            self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.SendConfig(ch_name, 'disable')
            

    def SendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command + '\n')

    def SendEncodFreq (self, channel, value):
        if self.s.port_open == True:
            encoder = ''
            if channel == 'ch1':
                encoder = 'encod0'
            elif channel == 'ch2':
                encoder = 'encod2'
            elif channel == 'ch3':
                encoder = 'encod4'
            else: # channel == 'ch4'
                encoder = 'encod6'

            if value <= 9:
                self.s.Write(encoder + ' ' + str(value) + '\n')
            elif value == 10:
                self.s.Write(encoder + ' :\n')
            elif value == 11:
                self.s.Write(encoder + ' ;\n')
                

    def SendEncodPwr (self, channel, value):
        if self.s.port_open == True:
            encoder = ''
            if channel == 'ch1':
                encoder = 'encod1'
            elif channel == 'ch2':
                encoder = 'encod3'
            elif channel == 'ch3':
                encoder = 'encod5'
            else: # channel == 'ch4'
                encoder = 'encod7'
                
            self.s.Write(encoder + ' ' + str(value) + '\n')
            

    def GetChannelIndexFromString (self, channel_str):
            index = 3
            
            if channel_str == 'ch1':
                index = 0
            elif channel_str == 'ch2':
                index = 1
            elif channel_str == 'ch3':
                index = 2
            # else: # channel_str == 'ch4'
            #     index = 3
            return index
        
    ###########################
    # One Second Timer signal #
    ###########################
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        """ one second gone, check if its something to do """
        for x in range(2):
            if self.in_treat_ch_list[x]:
                if (self.remaining_minutes_ch_list[x] > 0 or
                    self.remaining_seconds_ch_list[x] > 0):
                    if self.remaining_seconds_ch_list[x] > 0:
                        self.remaining_seconds_ch_list[x] -= 1
                    else:
                        self.remaining_minutes_ch_list[x] -= 1
                        self.remaining_seconds_ch_list[x] = 59

                    # update ui every second
                    self.remainMins_ui_list[x].setText(str(self.remaining_minutes_ch_list[x]) + "'")
                    self.remainSecs_ui_list[x].setText(str(self.remaining_seconds_ch_list[x]) + "''")

                else:
                    self.StopChannelByIndex(x)

        
        ##################
        # Serial Methods #
        ##################
    def SerialDataCallback (self, rcv):        
        # print ("serial data callback!")
        # print (rcv)
        # self.SerialProcess(rcv)
        if rcv.startswith("enc "):
            rcv_list = rcv.split(' ')
            if rcv_list[1] == '0' or \
               rcv_list[1] == '2' or \
               rcv_list[1] == '4' or \
               rcv_list[1] == '8':
                # frequency encoders
                try:
                    index = int((int(rcv_list[1])) / 2)
                    pos = int(rcv_list[3])
                except:
                    index = 0
                    pos = 0

                if pos > 10:
                    pos = 10

                self.freq_index_ch_list[index] = pos
                self.ChangeFrequencyByIndex(index)

            if rcv_list[1] == '1' or \
               rcv_list[1] == '3' or \
               rcv_list[1] == '5' or \
               rcv_list[1] == '7':
                # power encoders
                try:
                    index = int((int(rcv_list[1]) - 1) / 2)
                    pos = int(rcv_list[3])
                except:
                    index = 0
                    pos = 0

                if pos > 5:
                    pos = 5

                self.pwr_index_ch_list[index] = pos
                self.ChangePowerByIndex(index)
                
        if rcv.startswith("ch1 display "):
            rcv_list = rcv.split(' ')
            try:
                gain = int(rcv_list[2])
            except:
                gain = 0
            print('ch1 display: ' + str(gain))
            self.ui.ch1_displayLabel.setText(str(gain))

        if rcv.startswith("ch2 display "):
            rcv_list = rcv.split(' ')
            try:
                gain = int(rcv_list[2])
            except:
                gain = 0
            print('ch2 display: ' + str(gain))
            self.ui.ch2_displayLabel.setText(str(gain))
            
        if rcv.startswith("ch1 new probe "):
            rcv_list = rcv.split(' ')
            self.ui.ch1_probeLabel.setText(rcv_list[3])

        if rcv.startswith("ch2 new probe "):
            rcv_list = rcv.split(' ')
            self.ui.ch2_probeLabel.setText(rcv_list[3])
            
            
                    
                    
    # def SerialProcess (self, rcv):
    #     show_message = True
    #     if rcv.startswith("antenna none"):
    #         self.antennas_connected.Flush()
    #         self.AntennaUpdate()
        
