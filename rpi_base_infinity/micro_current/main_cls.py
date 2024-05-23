# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtCore, QtWidgets
import os
import threading

#imported uis
from ui_micro import Ui_MainWindow


def thread_function (distro, direction):
    if distro == 'Slackware ':
        if direction == 'up':
            os.system("play up.wav")
        else:
            os.system("play down.wav")
            
    elif distro == 'debian':
        if direction == 'up':
            os.system("omxplayer up_long3.wav")
        else:
            os.system("omxplayer down_long3.wav")
            

class MainWindow (QMainWindow):

    #SIGNALS
    one_second_signal = pyqtSignal()

    def __init__(self, distro, serialport, parent=None):
        super(MainWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.distro = distro
        self.parent = parent

        # threading routines
        # if self.distro == 'Slackware ':
        #     self.thread_start = threading.Thread(target=thread_function, args=('Slackware ','up',))
        #     self.thread_stop = threading.Thread(target=thread_function, args=('Slackware ','down',))
        # elif self.distro == 'debian':
        #     self.thread_start = threading.Thread(target=thread_function, args=('debian','up',))
        #     self.thread_stop = threading.Thread(target=thread_function, args=('debian','down',))
        # else:
        #     print("distro error, no threads instanciated!")

        # self.bt_close.clicked.connect(self.close)
        self.ui.bt_menu_close.clicked.connect(self.move_menu)
        self.ui.bt_menu_open.clicked.connect(self.move_menu)

        # ch1 & ch2 acuscope with gain
        self.ui.ch1_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch1_gainDwnButton.clicked.connect(self.GainUpDwn)
        self.ui.ch2_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch2_gainDwnButton.clicked.connect(self.GainUpDwn)
        self.gain_ch_list = [0,0,0,0]
        self.gain_ui_list = [self.ui.ch1_gainLabel, self.ui.ch2_gainLabel, 0, 0]
        for x in range(2):
            self.gain_ui_list[x].setText(str(self.gain_ch_list[x]))

        # ch1 ch2 ch3 & ch4 can change polarity
        self.ui.ch1_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_negButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_negButton.clicked.connect(self.ChangePolarity)
        self.ui.ch3_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch3_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch3_negButton.clicked.connect(self.ChangePolarity)
        self.ui.ch4_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch4_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch4_negButton.clicked.connect(self.ChangePolarity)
        self.pol_pos_ui_list = [self.ui.ch1_posButton, self.ui.ch2_posButton, self.ui.ch3_posButton, self.ui.ch4_posButton]        
        self.pol_alt_ui_list = [self.ui.ch1_altButton, self.ui.ch2_altButton, self.ui.ch3_altButton, self.ui.ch4_altButton]
        self.pol_neg_ui_list = [self.ui.ch1_negButton, self.ui.ch2_negButton, self.ui.ch3_negButton, self.ui.ch4_negButton]
        self.pol_index_ch_list = ['', '', '', '']
        for x in range(4):
            self.pol_index_ch_list[x] = 'positive'
            
        # ch1 ch2 ch3 & ch4 timer options
        self.timer_index_ch_list = [0, 0, 0, 0]        
        self.timer_list = ['6s', '12s', '30s', '1m', '10m', '30m']
        # timer on ch1 ch2 ch3 ch4
        self.ui.ch1_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch1_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.ui.ch3_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch3_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.ui.ch4_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch4_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.timer_ui_list = [self.ui.ch1_timerLabel, self.ui.ch2_timerLabel, self.ui.ch3_timerLabel, self.ui.ch4_timerLabel]
        for x in range(4):
            self.timer_ui_list[x].setText(self.timer_list[self.timer_index_ch_list[x]])
            
        # frequency options
        self.freq_index_ch_list = [0, 0, 0, 0]
        self.freq_list = ['0.5Hz', '1.0Hz', '2.0Hz', '4.0Hz', '8.0Hz', '10Hz', '20Hz', '40Hz', '80Hz', '160Hz', '320Hz']
        self.freq_conf_list = ['0.50', '1.00', '2.00', '4.00', '8.00', '10.00', '20.00', '40.00', '80.00', '160.00', '320.00']        
        # ch1 ch2 ch3 ch4 frequency
        self.ui.ch1_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch1_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch3_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch3_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch4_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch4_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.freq_ui_list = [self.ui.ch1_freqLabel, self.ui.ch2_freqLabel, self.ui.ch3_freqLabel, self.ui.ch4_freqLabel]
        for x in range(4):
            freq_str = self.freq_list[self.freq_index_ch_list[x]]                
            self.freq_ui_list[x].setText(freq_str)

        # ch1 ch2 ch3 ch4 intensity options
        self.pwr_index_ch_list = [0, 0, 0, 0]        
        self.pwr_list = ['25uA', '50uA', '100uA', '200uA', '400uA', '600uA']
        # ch1 ch2 ch3 ch4 power
        self.ui.ch1_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch1_pwrDwnButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrDwnButton.clicked.connect(self.ChangePower)
        self.ui.ch3_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch3_pwrDwnButton.clicked.connect(self.ChangePower)
        self.ui.ch4_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch4_pwrDwnButton.clicked.connect(self.ChangePower)
        self.pwr_ui_list = [self.ui.ch1_pwrLabel, self.ui.ch2_pwrLabel, self.ui.ch3_pwrLabel, self.ui.ch4_pwrLabel]
        for x in range(4):
            power_str = self.pwr_list[self.pwr_index_ch_list[x]]
            self.pwr_ui_list[x].setText(power_str)

        # ch1 to ch4 others buttons
        self.ui.ch1_startButton.clicked.connect(self.StartChannel)
        self.ui.ch1_stopButton.clicked.connect(self.StopChannel)        
        self.ui.ch1_enableButton.clicked.connect(self.EnableChannel)
        self.ui.ch2_startButton.clicked.connect(self.StartChannel)
        self.ui.ch2_stopButton.clicked.connect(self.StopChannel)        
        self.ui.ch2_enableButton.clicked.connect(self.EnableChannel)
        self.ui.ch3_startButton.clicked.connect(self.StartChannel)
        self.ui.ch3_stopButton.clicked.connect(self.StopChannel)
        self.ui.ch3_enableButton.clicked.connect(self.EnableChannel)
        self.ui.ch4_startButton.clicked.connect(self.StartChannel)
        self.ui.ch4_stopButton.clicked.connect(self.StopChannel)        
        self.ui.ch4_enableButton.clicked.connect(self.EnableChannel)

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
        self.startButton_ui_list = [self.ui.ch1_startButton, self.ui.ch2_startButton, self.ui.ch3_startButton, self.ui.ch4_startButton]
        self.stopButton_ui_list = [self.ui.ch1_stopButton, self.ui.ch2_stopButton, self.ui.ch3_stopButton, self.ui.ch4_stopButton]
        self.remainMins_ui_list = [self.ui.ch1_remainMinsLabel, self.ui.ch2_remainMinsLabel, self.ui.ch3_remainMinsLabel, self.ui.ch4_remainMinsLabel]
        self.remainSecs_ui_list = [self.ui.ch1_remainSecsLabel, self.ui.ch2_remainSecsLabel, self.ui.ch3_remainSecsLabel, self.ui.ch4_remainSecsLabel]
        self.enableButton_ui_list = [self.ui.ch1_enableButton, self.ui.ch2_enableButton, self.ui.ch3_enableButton, self.ui.ch4_enableButton]

        self.remaining_minutes_ch_list = [0, 0, 0, 0]
        self.remaining_seconds_ch_list = [0, 0, 0, 0]
        
        for x in range(4):
            self.stopButton_ui_list[x].hide()
            self.remainMins_ui_list[x].hide()
            self.remainSecs_ui_list[x].hide()

        # disable all channels on startup
        self.SendConfig('ch1', 'disable')
        self.SendConfig('ch2', 'disable')
        self.SendConfig('ch3', 'disable')
        self.SendConfig('ch4', 'disable')
        self.progress_config = 'init'
        
        self.in_treat_ch_list = [False, False, False, False]
        self.in_treat_show_sine_list = [False, False, False, False]
        self.ui.bt_menu_close.hide()

        # all channels none probe
        self.probeLabel_ui_list = [self.ui.ch1_probeLabel, self.ui.ch2_probeLabel, self.ui.ch3_probeLabel, self.ui.ch4_probeLabel]
        for x in range(4):
            self.probeLabel_ui_list[x].setText('None')

        # mains and battery buttons
        self.ui.mainsButton.clicked.connect(self.ShowVoltages)
        self.ui.battaButton.clicked.connect(self.ShowVoltages)
        self.ui.battbButton.clicked.connect(self.ShowVoltages)
        # batteries full at start
        self.mains_state = 'mains'
        self.battery_a_state = '4'    
        self.battery_b_state = '4'
        self.mains_voltage_str = '--'
        self.battery_a_voltage_str = '--'
        self.battery_b_voltage_str = '--'
        self.mains_revert = False
        self.batta_revert = False
        self.battb_revert = False
        self.revert_cnt = 0
        
        ## setup mains & battery icons
        self.mains_icon_connect = QIcon(':/icons/resources/mains_1.png')
        self.mains_icon_disconnect = QIcon(':/icons/resources/mains_2.png')
        self.batticon_list = [QIcon(':/icons/resources/batt_0_4.png'),\
                              QIcon(':/icons/resources/batt_1_4.png'),\
                              QIcon(':/icons/resources/batt_2_4.png'),\
                              QIcon(':/icons/resources/batt_3_4.png'),\
                              QIcon(':/icons/resources/batt_4_4.png')]
        
    
        ## activate the 1 second timer its repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        self.displayLabel_ui_list = [self.ui.ch1_displayLabel, self.ui.ch2_displayLabel, self.ui.ch3_displayLabel, self.ui.ch4_displayLabel]
        for x in range(4):
            self.displayLabel_ui_list[x].setText('--')

        self.displayTextLabel_ui_list = [self.ui.ch1_displayTextLabel, self.ui.ch2_displayTextLabel, self.ui.ch3_displayTextLabel, self.ui.ch4_displayTextLabel]
        for x in range(4):
            self.displayTextLabel_ui_list[x].setText('')

        self.ui.ch3_progressBar.setValue(0)
        self.ui.ch4_progressBar.setValue(0)
        ## progress timer for start and first config
        self.progress_timer = QTimer()
        self.progressBar_timer = QTimer()
        self.sine_cnt = 0
        self.sine_pos_table_list = [0.57, 1.06, 1.39, 1.5, 1.39, 1.06, 0.57, 0, 0.38, 0.71, 0.92, 1, 0.92, 0.71, 0.38, 0]
        self.sine_alt_table_list = [0.57, 1.06, 1.39, 1.5, 1.39, 1.06, 0.57, 0, -0.57, -1.06, -1.39, -1.5, -1.39, -1.06, -0.57, 0]

        # tell the system we are up
        self.SendSystemUP()
        os.system("sleep 0.2")
        self.SendSystemUP()
        
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
        

    def ChangePolarity (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if ch_func == 'posButton':
            self.pol_index_ch_list[ch_index] = 'positive'
            self.pol_pos_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.pol_alt_ui_list[ch_index].setStyleSheet('')
            self.pol_neg_ui_list[ch_index].setStyleSheet('')            
            self.SendConfig(ch_name, 'polarity positive')

        if ch_func == 'altButton':
            self.pol_index_ch_list[ch_index] = 'alternative'            
            self.pol_pos_ui_list[ch_index].setStyleSheet('')
            self.pol_alt_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.pol_neg_ui_list[ch_index].setStyleSheet('')            
            self.SendConfig(ch_name, 'polarity alternative')

        if ch_func == 'negButton':
            self.pol_index_ch_list[ch_index] = 'negative'            
            self.pol_pos_ui_list[ch_index].setStyleSheet('')
            self.pol_alt_ui_list[ch_index].setStyleSheet('')
            self.pol_neg_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.SendConfig(ch_name, 'polarity negative')
                    

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
            # self.StartChannelByIndex(ch_index)
            self.StartChannelUpdateTimer(ch_index)            
                

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

        # check enable channel or None in probe
        if self.enableButton_ui_list[ch_index].text() == 'Enable Channel' or \
           self.probeLabel_ui_list[ch_index].text() == 'None':
            return


        if self.in_treat_ch_list[ch_index] == False:
            if self.distro == 'Slackware ':
                # os.system("play up.wav")
                self.thread_start = threading.Thread(target=thread_function, args=('Slackware ','up',))
                self.thread_start.start()
            elif self.distro == 'debian':
                # os.system("omxplayer up_long3.wav")
                self.thread_start = threading.Thread(target=thread_function, args=('debian','up',))
                self.thread_start.start()                
                
            self.SendConfig(ch_name, 'start')

        self.StartChannelByIndex(ch_index)            


    def StartChannelUpdateTimer (self, ch_index):
        timer = self.timer_ui_list[ch_index].text()
        if timer[-1] == 's':
            self.remaining_minutes_ch_list[ch_index] = 0
            self.remaining_seconds_ch_list[ch_index] = int(timer[:-1])
        elif timer[-1] == 'm':
            self.remaining_minutes_ch_list[ch_index] = int(timer[:-1])
            self.remaining_seconds_ch_list[ch_index] = 0

        self.remainMins_ui_list[ch_index].setText(str(self.remaining_minutes_ch_list[ch_index]) + "'")
        self.remainSecs_ui_list[ch_index].setText(str(self.remaining_seconds_ch_list[ch_index]) + "''")        

        
    def StartChannelByIndex (self, ch_index):
        self.StartChannelUpdateTimer(ch_index)
        
        self.in_treat_ch_list[ch_index] = True
        self.remainMins_ui_list[ch_index].show()
        self.remainSecs_ui_list[ch_index].show()
        self.stopButton_ui_list[ch_index].show()
        self.startButton_ui_list[ch_index].hide()

        if ch_index == 0 or \
           ch_index == 1:
            # clean display
            self.displayLabel_ui_list[ch_index].setText('--')

        if ch_index == 2:
            self.ui.ch3_progressBar.setValue(0)
            self.ui.ch3_displayLabel.setText('0')
            if self.in_treat_ch_list[3] != True:
                self.progressBar_timer.singleShot(200, self.ProgressBarSM)
        elif ch_index == 3:
            self.ui.ch4_progressBar.setValue(0)
            self.ui.ch4_displayLabel.setText('0')
            if self.in_treat_ch_list[2] != True:
                self.progressBar_timer.singleShot(200, self.ProgressBarSM)
        

    def StopChannel (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)
        self.StopChannelByIndex(ch_index)

        
    def StopChannelByIndex (self, ch_index):
        self.SendConfig('ch' + str(ch_index + 1), 'stop')
        if self.distro == 'Slackware ':
            # os.system("play up.wav")
            self.thread_stop = threading.Thread(target=thread_function, args=('Slackware ','down',))
            self.thread_stop.start()
        elif self.distro == 'debian':
            # os.system("omxplayer up_long3.wav")
            self.thread_stop = threading.Thread(target=thread_function, args=('debian','down',))
            self.thread_stop.start()                
        
        self.in_treat_ch_list[ch_index] = False
        self.remainMins_ui_list[ch_index].hide()
        self.remainSecs_ui_list[ch_index].hide()
        self.stopButton_ui_list[ch_index].hide()
        self.startButton_ui_list[ch_index].show()
        self.displayTextLabel_ui_list[ch_index].setText('')
        

    def EnableChannel (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        if self.enableButton_ui_list[ch_index].text() == 'Enable Channel':
            # check if SendConfig is ready to sent
            if self.progress_config != 'init':
                return

            self.enableButton_ui_list[ch_index].setText('Disable Channel')
            self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(129, 129, 129);\
                                                               border: 2px solid rgb(218, 218, 218);')
            self.SendConfig(ch_name, 'enable')
            self.SendConfigByIndex (ch_index)
        else:
            self.enableButton_ui_list[ch_index].setText('Enable Channel')
            self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
            self.probeLabel_ui_list[ch_index].setText('None')

            if self.in_treat_ch_list[ch_index] == True:
                self.StopChannelByIndex(ch_index)
                
            if ch_index < 3:
                self.displayLabel_ui_list[ch_index].setText('--')
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


    def SendSystemUP (self):
        if self.s.port_open == True:
            self.s.Write('rpi is up\n')
            

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


    def ShowVoltages (self):
        sender = self.sender()
        
        if sender.objectName() == 'mainsButton':
            self.ui.mainsButton.setIcon(QIcon())
            self.ui.mainsButton.setText(self.mains_voltage_str)
            self.mains_revert = True
            self.revert_cnt = 2
            
        if sender.objectName() == 'battaButton':
            self.ui.battaButton.setIcon(QIcon())
            self.ui.battaButton.setText(self.battery_a_voltage_str)
            self.batta_revert = True            
            self.revert_cnt = 2            

        if sender.objectName() == 'battbButton':
            self.ui.battbButton.setIcon(QIcon())
            self.ui.battbButton.setText(self.battery_b_voltage_str)
            self.battb_revert = True
            self.revert_cnt = 2            
            

    def RevertVoltages (self):
        if self.revert_cnt > 0:
            self.revert_cnt -= 1
            return
            
        if self.mains_revert:
            self.ui.mainsButton.setText('')
            self.mains_revert = False
            if self.mains_state == 'mains':
                self.ui.mainsButton.setIcon(self.mains_icon_connect)
            else:
                self.ui.mainsButton.setIcon(self.mains_icon_disconnect)

        if self.batta_revert:
            self.ui.battaButton.setText('')
            self.batta_revert = False
            self.ui.battaButton.setIcon(self.batticon_list[int(self.battery_a_state)])

        if self.battb_revert:
            self.ui.battbButton.setText('')
            self.battb_revert = False
            self.ui.battbButton.setIcon(self.batticon_list[int(self.battery_b_state)])
                
            
    def UpdateSupplyPower (self, power_str):
        # supply mains 13.2V 8.4V 8.4V 4 4
        # supply battery 6.2V 8.4V 8.4V 4 4
        update_volts = False
        power_str_list = power_str.split(' ')
        if power_str_list[1] == 'mains':
            if self.mains_state != 'mains':
                self.mains_state = 'mains'
                self.ui.mainsButton.setIcon(self.mains_icon_connect)
            update_volts = True
        elif power_str_list [1] == 'battery':
            if self.mains_state != 'battery':
                self.mains_state = 'battery'
                self.ui.mainsButton.setIcon(self.mains_icon_disconnect)
            update_volts = True

        # update mains & battery voltages
        batta_str = power_str_list[5]
        battb_str = power_str_list[6]
        if update_volts and \
           batta_str[0] >= '0' and batta_str[0] < '5' and \
           battb_str[0] >= '0' and battb_str[0] < '5':
            self.mains_voltage_str = power_str_list [2]
            self.battery_a_voltage_str = power_str_list [3]
            self.battery_b_voltage_str = power_str_list [4]
            if self.battery_a_state != power_str_list[5]:
                self.battery_a_state = power_str_list[5]
                self.ui.battaButton.setIcon(self.batticon_list[int(self.battery_a_state)])

            if self.battery_b_state != power_str_list[6]:
                self.battery_b_state = power_str_list[6]
                self.ui.battbButton.setIcon(self.batticon_list[int(self.battery_b_state)])                

            
    ############################
    # Progress Timed Functions #
    ############################
    def SendConfigByIndex (self, ch_index):
        self.prog_ch_index = ch_index
        self.prog_ch_name = 'ch' + str(ch_index + 1)
        self.SendConfigChannelSM ()
        
        
    def SendConfigChannelSM (self):
        if self.progress_config == 'init':
            self.progress_config = 'gain'
            self.progress_timer.singleShot(2000, self.SendConfigChannelSM)
        elif self.progress_config == 'gain':
            self.SendConfig(self.prog_ch_name, 'set_gain ' + str(self.gain_ch_list[self.prog_ch_index]))
            self.progress_config = 'polarity'
            self.progress_timer.singleShot(50, self.SendConfigChannelSM)
        elif self.progress_config == 'polarity':
            self.SendConfig(self.prog_ch_name, 'polarity ' + self.pol_index_ch_list[self.prog_ch_index])
            self.progress_config = 'frequency'
            self.progress_timer.singleShot(50, self.SendConfigChannelSM)
        elif self.progress_config == 'frequency':
            self.SendConfig(self.prog_ch_name, 'frequency ' + self.freq_conf_list[self.freq_index_ch_list[self.prog_ch_index]])
            self.SendEncodFreq(self.prog_ch_name, self.freq_index_ch_list[self.prog_ch_index])
            self.progress_config = 'intensity'
            self.progress_timer.singleShot(50, self.SendConfigChannelSM)
        elif self.progress_config == 'intensity':
            power_str = self.pwr_list[self.pwr_index_ch_list[self.prog_ch_index]]
            self.SendConfig(self.prog_ch_name, 'intensity ' + power_str)
            self.SendEncodPwr(self.prog_ch_name, self.pwr_index_ch_list[self.prog_ch_index])
            self.progress_config = 'mode'
            self.progress_timer.singleShot(50, self.SendConfigChannelSM)
        elif self.progress_config == 'mode':
            if self.prog_ch_index == 0 or self.prog_ch_index == 1:
                self.SendConfig(self.prog_ch_name, 'mode square')
            else:
                self.SendConfig(self.prog_ch_name, 'mode sine')
            self.progress_config = 'init'

            
    def ProgressBarSM (self):
        next_cycle = False
        
        if self.in_treat_ch_list[2] == True and \
           self.in_treat_show_sine_list[2] == True:
            if self.pol_index_ch_list[2] == 'negative':
                sine_point = -self.sine_pos_table_list[self.sine_cnt]
            elif self.pol_index_ch_list[2] == 'positive':
                sine_point = self.sine_pos_table_list[self.sine_cnt]
            else:    # alternative
                sine_point = self.sine_alt_table_list[self.sine_cnt]

            display, progress = self.ProgressCalcValue(self.pwr_index_ch_list[2], sine_point)
            self.ui.ch3_progressBar.setValue(progress)
            self.ui.ch3_displayLabel.setText(str(display))
            next_cycle = True
        else:
            self.ui.ch3_progressBar.setValue(0)
            self.ui.ch3_displayLabel.setText('--')
            self.in_treat_show_sine_list[2] = False

        if self.in_treat_ch_list[3] == True and \
           self.in_treat_show_sine_list[3] == True:
            if self.pol_index_ch_list[3] == 'negative':
                sine_point = -self.sine_pos_table_list[self.sine_cnt]
            elif self.pol_index_ch_list[3] == 'positive':
                sine_point = self.sine_pos_table_list[self.sine_cnt]
            else:    # alternative
                sine_point = self.sine_alt_table_list[self.sine_cnt]

            display, progress = self.ProgressCalcValue(self.pwr_index_ch_list[3], sine_point)
            self.ui.ch4_progressBar.setValue(progress)
            self.ui.ch4_displayLabel.setText(str(display))            
            next_cycle = True
        else:
            self.ui.ch4_progressBar.setValue(0)
            self.ui.ch4_displayLabel.setText('--')
            self.in_treat_show_sine_list[3] = False

        if self.sine_cnt < 16 - 1:
            self.sine_cnt += 1
        else:
            self.sine_cnt = 0
            
        if next_cycle:
            self.progressBar_timer.singleShot(200, self.ProgressBarSM)

            
    def ProgressCalcValue (self, curr_index, sine_point):
        if curr_index == 0:    #25uA
            c = 25
            pp = 16
        elif curr_index == 1:    #50uA
            c = 50
            pp = 24
        elif curr_index == 2:    #100uA
            c = 100
            pp = 56
        elif curr_index == 3:    #200uA
            c = 200
            pp = 66
        elif curr_index == 4:    #400uA
            c = 400
            pp = 80
        else:                    #600uA
            c = 600
            pp = 100

        prog_value = sine_point * pp
        prog_value = int(prog_value)
        if prog_value < 0:
            prog_value = -prog_value
            
        if prog_value > 100:
            prog_value = 100

        disp_value = sine_point * c
        disp_value = int(disp_value)
        if disp_value > 1000:
            disp_value = 1000
            
        return disp_value, prog_value
            
    ###########################
    # One Second Timer signal #
    ###########################
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        """ one second gone, check if its something to do """
        self.RevertVoltages()
        
        for x in range(4):
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
        if rcv.startswith('\n'):
            return

        # encoders by deltas        
        if rcv.startswith("enc +") or \
           rcv.startswith("enc -"):
            rcv_list = rcv.split(' ')
            try:
                index = int(rcv_list[2])
            except:
                index = 8

            if index > 7:
                return

            if rcv_list [1] == '+':
                direction_up = True
            else:
                direction_up = False
                
            if index % 2 == 0:
                # frequency encoders
                if index == 0:
                    ch_index = 0
                elif index == 2:
                    ch_index = 1
                elif index == 4:
                    ch_index = 2
                else:
                    ch_index = 3

                if direction_up:
                    if self.freq_index_ch_list[ch_index] < 10:
                        self.freq_index_ch_list[ch_index] += 1
                        self.ChangeFrequencyByIndex(ch_index)
                        self.SendEncodFreq('ch' + str(ch_index + 1), self.freq_index_ch_list[ch_index])
                else:
                    if self.freq_index_ch_list[ch_index] > 0:
                        self.freq_index_ch_list[ch_index] -= 1
                        self.ChangeFrequencyByIndex(ch_index)
                        self.SendEncodFreq('ch' + str(ch_index + 1), self.freq_index_ch_list[ch_index])
                        
            else:
                # power encoders                
                if index == 1:
                    ch_index = 0
                elif index == 3:
                    ch_index = 1
                elif index == 5:
                    ch_index = 2
                else:
                    ch_index = 3

                if direction_up:
                    if self.pwr_index_ch_list[ch_index] < 5:
                        self.pwr_index_ch_list[ch_index] += 1
                        self.ChangePowerByIndex(ch_index)
                        self.SendEncodPwr('ch' + str(ch_index + 1), self.pwr_index_ch_list[ch_index])
                else:
                    if self.pwr_index_ch_list[ch_index] > 0:
                        self.pwr_index_ch_list[ch_index] -= 1
                        self.ChangePowerByIndex(ch_index)
                        self.SendEncodPwr('ch' + str(ch_index + 1), self.pwr_index_ch_list[ch_index])

            return
        # end of encoders by deltas
        
        # encoders by position
        if rcv.startswith("encp "):
            rcv_list = rcv.split(' ')            
            try:
                index = int(rcv_list[1])
            except:
                index = 8

            if index > 7:
                return
        
            if index % 2 == 0:
                # frequency encoders
                if index == 0:
                    ch_index = 0
                elif index == 2:
                    ch_index = 1
                elif index == 4:
                    ch_index = 2
                else:
                    ch_index = 3

                try:
                    pos = int(rcv_list[2])
                except:
                    pos = 11

                if pos > 10:
                    return

                self.freq_index_ch_list[ch_index] = pos
                self.ChangeFrequencyByIndex(ch_index)
                                        
            else:
                # power encoders                
                if index == 1:
                    ch_index = 0
                elif index == 3:
                    ch_index = 1
                elif index == 5:
                    ch_index = 2
                else:
                    ch_index = 3

                try:
                    pos = int(rcv_list[2])
                except:
                    pos = 6

                if pos > 5:
                    return

                self.pwr_index_ch_list[ch_index] = pos
                self.ChangePowerByIndex(ch_index)
                
            return
        # end of encoders by position

        # supply voltage measurement
        if rcv.startswith("supply "):
            try:
                self.UpdateSupplyPower(rcv)
            except:
                print('error on supply str!')

            return
        # end of supply voltage measurement
                
        # channels comms
        if rcv.startswith("ch"):
            rcv_list = rcv.split(' ')
            ch_index = rcv_list[0][-1]
            try:
                ch_index = int (ch_index)
            except:
                ch_index = 5
                
            if ch_index < 5:
                ch_index = ch_index - 1
            else:
                return

            rcv_str = rcv[4:]
            # print("receiv: " + rcv_str + " in index: " + str(ch_index))
            self.ParseChannelsComms(ch_index, rcv_str)
            

    def ParseChannelsComms (self, ch_index, ch_str):
        # display values
        if ch_str.startswith("display "):
            rcv_list = ch_str.split(' ')
            try:
                gain = int(rcv_list[1])
            except:
                gain = 0
            # print('ch1 display: ' + str(gain))

            # check ch disable else show meas
            if self.enableButton_ui_list[ch_index].text() == 'Disable Channel':
                # not show ch1 or ch2 if in treat
                if ch_index == 0 or \
                   ch_index == 1:
                    if self.in_treat_ch_list[ch_index] == True:
                        return

                self.displayLabel_ui_list[ch_index].setText(str(gain))

            return
        # end of display values

        # probe messages
        if ch_str.startswith("new probe "):
            rcv_list = ch_str.split(' ')
            self.probeLabel_ui_list[ch_index].setText(rcv_list[2])
            return
        # end of probe messages

        # probe others
        if ch_str.startswith("none probe"):
            self.probeLabel_ui_list[ch_index].setText('None')
            if self.enableButton_ui_list[ch_index].text() == 'Disable Channel' and \
               self.in_treat_ch_list[ch_index] == True:
                self.StopChannelByIndex(ch_index)
            return
        # end of probe others

        # probe others 2
        if ch_str.startswith("probe start"):
            # check if channel is enable
            if self.enableButton_ui_list[ch_index].text() == 'Enable Channel':
                return

            if self.in_treat_ch_list[ch_index] == False:
                if self.distro == 'Slackware ':
                    # os.system("play up.wav")
                    self.thread_start = threading.Thread(target=thread_function, args=('Slackware ','up',))
                    self.thread_start.start()
                elif self.distro == 'debian':
                    # os.system("omxplayer up_long3.wav")
                    self.thread_start = threading.Thread(target=thread_function, args=('debian','up',))
                    self.thread_start.start()                
                
                self.SendConfig('ch' + str(ch_index + 1), 'start')

            self.StartChannelByIndex(ch_index)
            return
        # end of probe others 2

        # for show sine progress
        if ch_str.startswith("starting"):
            self.in_treat_show_sine_list[ch_index] = True
            return
        # end of for show sine progress

        # resistance meas online
        if ch_str.startswith("resistance "):
            rcv_list = ch_str.split(' ')
            try:
                res_int = int(rcv_list[1])
            except:
                res_int = 0

            res_mult = ''                
            if res_int > 1000:
                res_int = res_int / 1000
                res_int = int(res_int)
                res_mult = 'k'
                
            if self.in_treat_ch_list[ch_index] == True:
                self.displayTextLabel_ui_list[ch_index].setText('Res. ' + str(res_int) + res_mult)
        # end of resistance meas online
