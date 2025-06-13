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
from ui_micro3 import Ui_MainWindow


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

        # ch1 acuscope with gain
        self.ui.ch1_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch1_gainDwnButton.clicked.connect(self.GainUpDwn)

        # ch1 gain
        self.gain_ch1 = 0
        self.ui.ch1_gainLabel.setText(str(self.gain_ch1))        

        # ch1 ch2 can change polarity
        self.ui.ch1_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_negButton.clicked.connect(self.ChangePolarity)

        self.ui.ch2_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch2_negButton.clicked.connect(self.ChangePolarity)

        # polarity buttons and style
        self.style_pol_act = """color: rgb(255,255,255);
                                background-color: rgb(173, 163, 170);
                                border-radius: 15;
                                border: 2px rgb(173, 163, 170);"""
        self.style_pol_deact = """color: rgb(148,138,146);
                                  border-radius: 15;
                                  border: 2px solid rgb(148, 138, 146);"""
        self.pol_pos_ui_list = [self.ui.ch1_posButton, self.ui.ch2_posButton]        
        self.pol_alt_ui_list = [self.ui.ch1_altButton, self.ui.ch2_altButton]
        self.pol_neg_ui_list = [self.ui.ch1_negButton, self.ui.ch2_negButton]
        self.pol_index_ch_list = ['', '']
        for x in range(2):
            self.pol_index_ch_list[x] = 'positive'
            
        # ch1 ch2 timer options
        self.timer_index_ch_list = [0, 0]        
        self.timer_list = ['6s', '12s', '30s', '1m', '10m', '30m']
        # timer on ch1 ch2
        self.ui.ch1_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch1_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch2_timerDwnButton.clicked.connect(self.ChangeTimer)
        self.timer_ui_list = [self.ui.ch1_timerLabel, self.ui.ch2_timerLabel]
        for x in range(2):
            self.timer_ui_list[x].setText(self.timer_list[self.timer_index_ch_list[x]])
            
        # frequency options
        self.freq_index_ch_list = [0, 0]
        self.freq_list = ['0.5Hz', '1.0Hz', '2.0Hz', '4.0Hz', '8.0Hz', '10Hz', '20Hz', '40Hz', '80Hz', '160Hz', '320Hz']
        self.freq_conf_list = ['0.50', '1.00', '2.00', '4.00', '8.00', '10.00', '20.00', '40.00', '80.00', '160.00', '320.00']        
        # ch1 ch2 frequency
        self.ui.ch1_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch1_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch2_freqDwnButton.clicked.connect(self.ChangeFrequency)
        self.freq_ui_list = [self.ui.ch1_freqLabel, self.ui.ch2_freqLabel]
        for x in range(2):
            freq_str = self.freq_list[self.freq_index_ch_list[x]]                
            self.freq_ui_list[x].setText(freq_str)

        # ch1 ch2 intensity options
        self.pwr_index_ch_list = [0, 0]        
        self.pwr_list = ['25uA', '50uA', '100uA', '200uA', '400uA', '600uA']
        # ch1 ch2 power
        self.ui.ch1_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch1_pwrDwnButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch2_pwrDwnButton.clicked.connect(self.ChangePower)
        self.pwr_ui_list = [self.ui.ch1_pwrLabel, self.ui.ch2_pwrLabel]
        for x in range(2):
            power_str = self.pwr_list[self.pwr_index_ch_list[x]]
            self.pwr_ui_list[x].setText(power_str)

        # ch1 and ch2 others buttons
        self.ui.ch1_startButton.clicked.connect(self.StartChannel)
        # self.ui.ch1_stopButton.clicked.connect(self.StopChannel)        

        # self.ui.ch1_enableButton.clicked.connect(self.EnableChannel)
        self.ui.ch2_startButton.clicked.connect(self.StartChannel)
        # self.ui.ch2_stopButton.clicked.connect(self.StopChannel)
        # self.ui.ch2_enableButton.clicked.connect(self.EnableChannel)

        # # self.bt_min.clicked.connect(self.control_minimized)
        # # self.bt_med.clicked.connect(self.control_normal)
        # # self.bt_max.clicked.connect(self.control_maximized)

        ## connect the signals
        # timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)        

        ##
        ## initial setup for channels
        ##
        self.startButton_ui_list = [self.ui.ch1_startButton, self.ui.ch2_startButton]
        # self.stopButton_ui_list = [self.ui.ch1_stopButton, self.ui.ch2_stopButton]
        self.remainMins_ui_list = [self.ui.ch1_remainMinsLabel, self.ui.ch2_remainMinsLabel]
        self.remainSecs_ui_list = [self.ui.ch1_remainSecsLabel, self.ui.ch2_remainSecsLabel]

        self.remaining_minutes_ch_list = [0, 0]
        self.remaining_seconds_ch_list = [0, 0]
        
        for x in range(2):
            # self.stopButton_ui_list[x].hide()
            self.remainMins_ui_list[x].hide()
            self.remainSecs_ui_list[x].hide()

        # disable all channels on startup
        # self.SendConfig('ch1', 'disable')
        # self.SendConfig('ch2', 'disable')
        # self.SendConfig('ch2', 'disable')
        # self.SendConfig('ch4', 'disable')
        # self.SendConfig('ch1', 'enable')
        # self.SendConfig('ch2', 'enable')
        # self.SendConfig('ch2', 'enable')
        # self.SendConfig('ch4', 'enable')
        self.progress_config = 'init'
        
        self.in_treat_ch_list = [False, False]
        self.in_treat_show_sine = False

        # all channels none probe
        self.probeLabel_ui_list = [self.ui.ch1_probeLabel, self.ui.ch2_probeLabel]
        for x in range(2):
            self.probeLabel_ui_list[x].setText('Probe')

        # mains and battery buttons
        self.ui.battButton.clicked.connect(self.ShowVoltages)
        # batteries full at start
        self.mains_state = 'mains'
        self.battery_a_state = '4'    
        self.battery_b_state = '4'
        self.battery_c_state = '4'    
        self.battery_d_state = '4'
        self.mains_voltage_str = '--'
        self.battery_a_voltage_str = '--'
        self.battery_b_voltage_str = '--'
        self.battery_c_voltage_str = '--'
        self.battery_d_voltage_str = '--'
        self.batt_revert = False
        self.revert_cnt = 0
        
        ## setup mains & battery icons
        self.mains_icon_connect = QIcon(':/icons/resources/mains_1.png')
        self.mains_icon_disconnect = QIcon(':/icons/resources/mains_2.png')
        self.batticon_list = [QIcon(':/icons/resources/batt_0_4.png'),\
                              QIcon(':/icons/resources/batt_1_4.png'),\
                              QIcon(':/icons/resources/batt_2_4.png'),\
                              QIcon(':/icons/resources/batt_3_4.png'),\
                              QIcon(':/icons/resources/batt_4_4.png')]
        self.platesicon_list = [QIcon(':/icons/resources/conector.png'),\
                                QIcon(':/icons/resources/conector_alt.png'),\
                                QIcon(':/icons/resources/conector_pos.png'),\
                                QIcon(':/icons/resources/conector_neg.png')]
        
    
        ## activate the 1 second timer its repetitive
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        self.displayLabel_ui_list = [self.ui.ch1_lcdNumber, self.ui.ch2_lcdNumber]
        for x in range(2):
            self.displayLabel_ui_list[x].display('---')

        # self.displayTextLabel_ui_list = [self.ui.ch1_displayTextLabel, self.ch2_dummy, self.ui.ch2_displayTextLabel, self.ch4_dummy]
        # for x in range(4):
        #     self.displayTextLabel_ui_list[x].setText('')

        self.ui.ch2_progressBar.setValue(0)
        self.ui.ch2_progressBar.setFixedHeight(4)
        
        ## progress timer for start and first config
        self.progress_timer = QTimer()
        self.progressBar_timer = QTimer()
        self.sine_cnt = 0
        self.sine_pos_table_list = [0.57, 1.06, 1.39, 1.5, 1.39, 1.06, 0.57, 0, 0.38, 0.71, 0.92, 1, 0.92, 0.71, 0.38, 0]
        self.sine_alt_table_list = [0.57, 1.06, 1.39, 1.5, 1.39, 1.06, 0.57, 0, -0.57, -1.06, -1.39, -1.5, -1.39, -1.06, -0.57, 0]

        ## plates & probe labels
        self.last_plates = 0
        self.platesButton_ui_list = [self.ui.pch4upButton, self.ui.pch4dwnButton, self.ui.pch2upButton, self.ui.pch2dwnButton, self.ui.pch2upButton, self.ui.pch2dwnButton, self.ui.pch1upButton, self.ui.pch1dwnButton]
        self.last_probe = 0
        self.ui.intpButton.setIcon(self.platesicon_list[0])

        ## Roll Through Function
        self.ui.rtf_startButton.clicked.connect(self.StartRoll)
        # self.ui.rtf_stopButton.clicked.connect(self.StopRoll)        
        self.rtf_endhook = False
        self.rtf_endhook_state = ''


        # tell the system we are up
        self.SendSystemUP()
        os.system("sleep 0.2")
        self.SendSystemUP()
        os.system("sleep 0.1")

        # tell mainboard the default config
        self.ChangeFrequencyFunc (0, 6)    #square 20Hz
        self.ChangeFrequencyFunc (1, 6)    #sine 20Hz    
        self.ChangePowerFunc(0, 2)    #square 100uA
        self.ChangePowerFunc(1, 2)    #sine 100uA
        self.ChangePolarityFunc(0, 'posButton')

        
        # Treatment_SetFrequency_Str (MODE_SQUARE, "20.00");
        # Treatment_SetIntensity_Str (MODE_SQUARE, "100");
        # Treatment_SetFrequency_Str (MODE_SINE, "20.00");
        # Treatment_SetIntensity_Str (MODE_SINE, "100");
        # Treatment_SetPolarity_Str ("alt");

        # get connectors update
        self.SendConfig('conn', 'get')
        
            
        
    def GainUpDwn (self):
        sender = self.sender()

        # always ch1
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]

        if ch_func == 'gainUpButton':
            if self.gain_ch1 < 100:
                self.gain_ch1 += 1

        if ch_func == 'gainDwnButton':
            if self.gain_ch1 > 0:
                self.gain_ch1 -= 1

        self.ui.ch1_gainLabel.setText(str(self.gain_ch1))
        self.SendConfig(ch_name, 'set_gain ' + str(self.gain_ch1))
        

    # change both polarities
    def ChangePolarity (self):
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        ## change this, do two channels at once
        for ch_index in [0 ,1]:
            if ch_func == 'posButton':
                self.pol_index_ch_list[ch_index] = 'positive'
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_deact)            
                # self.SendConfig('polarity', 'positive')            

            if ch_func == 'altButton':
                self.pol_index_ch_list[ch_index] = 'alternative'            
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_deact)            
                # self.SendConfig('polarity', 'alternative')

            if ch_func == 'negButton':
                self.pol_index_ch_list[ch_index] = 'negative'            
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                # self.SendConfig('polarity', 'negative')

        # send conf only one time
        if ch_func == 'posButton':
            self.SendConfig('polarity', 'positive')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)

        if ch_func == 'altButton':
            self.SendConfig('polarity', 'alternative')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)            

        if ch_func == 'negButton':
            self.SendConfig('polarity', 'negative')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)            


    def ChangePolarityFunc (self, ch_index, ch_func_str):
        ch_func = ch_func_str

        ## change this, do two channels at once
        for ch_index in [0 ,1]:
            if ch_func == 'posButton':
                self.pol_index_ch_list[ch_index] = 'positive'
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                # self.SendConfig('polarity', 'positive')            

            if ch_func == 'altButton':
                self.pol_index_ch_list[ch_index] = 'alternative'            
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                # self.SendConfig('polarity', 'alternative')

            if ch_func == 'negButton':
                self.pol_index_ch_list[ch_index] = 'negative'            
                self.pol_pos_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_alt_ui_list[ch_index].setStyleSheet(self.style_pol_deact)
                self.pol_neg_ui_list[ch_index].setStyleSheet(self.style_pol_act)
                # self.SendConfig('polarity', 'negative')

        # send conf only one time
        if ch_func == 'posButton':
            self.SendConfig('polarity', 'positive')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)

        if ch_func == 'altButton':
            self.SendConfig('polarity', 'alternative')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)            

        if ch_func == 'negButton':
            self.SendConfig('polarity', 'negative')
            self.SetPlatesPolarity(self.last_plates)
            self.SetProbePolarity(self.last_probe)            


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


    def ChangeFrequencyFunc (self, ch_index, freq_list_index):
        self.freq_index_ch_list[ch_index] = freq_list_index
        self.ChangeFrequencyByIndex(ch_index)
        self.SendEncodFreq(f"ch{ch_index+1}", self.freq_index_ch_list[ch_index])
            

    def ChangeFrequencyByIndex (self, ch_index):
        freq_str = self.freq_list[self.freq_index_ch_list[ch_index]]                
        self.freq_ui_list[ch_index].setText(freq_str)
        # self.SendConfig('ch' + str(ch_index + 1), 'frequency ' + self.freq_conf_list[self.freq_index_ch_list[ch_index]])
        if ch_index == 0:
            self.SendConfig('square frequency', self.freq_conf_list[self.freq_index_ch_list[ch_index]])
        else:
            self.SendConfig('sine frequency', self.freq_conf_list[self.freq_index_ch_list[ch_index]])

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
            

    def ChangePowerFunc (self, ch_index, pwr_list_index):
        self.pwr_index_ch_list[ch_index] = pwr_list_index
        self.ChangePowerByIndex(ch_index)
        self.SendEncodPwr(f"ch{ch_index+1}", self.pwr_index_ch_list[ch_index])

            
    def ChangePowerByIndex (self, ch_index):
        power_str = self.pwr_list[self.pwr_index_ch_list[ch_index]]
        self.pwr_ui_list[ch_index].setText(power_str)        
        # self.SendConfig('ch' + str(ch_index + 1), 'intensity ' + power_str)
        if ch_index == 0:
            self.SendConfig('square intensity', power_str)
        else:
            self.SendConfig('sine intensity', power_str)
        

    def StartChannel (self):
        # sends or resend a start to channel
        sender = self.sender()
        
        obj_list = sender.objectName().split('_')
        ch_name = obj_list[0]
        ch_func = obj_list[1]
        ch_index = self.GetChannelIndexFromString(ch_name)

        # check for stops
        if self.startButton_ui_list[ch_index].text() == "STOP":
            self.StopChannelByIndex(ch_index)
            return

        # check only one channel start
        for x in range(2):
            if self.in_treat_ch_list[x] != False:
                return

        # start the channel
        if self.in_treat_ch_list[ch_index] == False:            
            if ch_index == 0:
                self.SendConfig('square', 'start')
            else:
                self.SendConfig('sine', 'start')
                
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
        # self.stopButton_ui_list[ch_index].show()
        self.startButton_ui_list[ch_index].setText("STOP")

        if ch_index == 0:
            # clean display
            # self.displayLabel_ui_list[ch_index].setText('--')
            self.displayLabel_ui_list[ch_index].display('--')            

        if ch_index == 1:
            self.ui.ch1_progressBar.setValue(0)
            self.ui.ch1_displayLabel.setText('0')
            self.progressBar_timer.singleShot(200, self.ProgressBarSM)
            # print("   starting sine SM")
        

    # def StopChannel (self):
    #     sender = self.sender()
        
    #     obj_list = sender.objectName().split('_')
    #     ch_name = obj_list[0]
    #     ch_func = obj_list[1]
    #     ch_index = self.GetChannelIndexFromString(ch_name)
    #     self.StopChannelByIndex(ch_index)

        
    def StopChannelByIndex (self, ch_index):
        self.SendConfig('stop', '')        

        self.in_treat_ch_list[ch_index] = False
        self.remainMins_ui_list[ch_index].hide()
        self.remainSecs_ui_list[ch_index].hide()
        # self.stopButton_ui_list[ch_index].hide()
        self.startButton_ui_list[ch_index].setText("START")
        # self.displayTextLabel_ui_list[ch_index].setText('')

        if self.rtf_endhook == True:
            self.Roll_SM()


    def StartRoll (self):
        for ch_index in range (2):
            if self.in_treat_ch_list[ch_index] != False:
                self.ui.rtf_line1Label.setText("Some channel is running")
                return

        if self.ui.ch1_probeLabel.text() != "NervSync":
            self.ui.rtf_line1Label.setText("NervSync Probe NC")
            return

        self.ChangeFrequencyFunc (0, 0)
        self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[0]}")
        self.SendConfig('square', 'start')
        self.StartChannelByIndex(0)
        self.rtf_endhook_state = 'freq1'
        self.rtf_endhook = True
        self.ui.rtf_startButton.hide()
        self.ui.rtf_stopButton.show()        


    def Roll_SM (self):
        time_for_meas = 3000
        if self.rtf_endhook_state == 'freq1':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[0]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

        elif self.rtf_endhook_state == 'freq1_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 1)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[1]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq2'
            
        elif self.rtf_endhook_state == 'freq2':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[1]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

        elif self.rtf_endhook_state == 'freq2_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 1)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[1]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq3'

        elif self.rtf_endhook_state == 'freq3':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[1]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

        elif self.rtf_endhook_state == 'freq3_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 3)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[3]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq4'
            
        elif self.rtf_endhook_state == 'freq4':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[3]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

        elif self.rtf_endhook_state == 'freq4_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 4)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[4]}")            
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq5'
            
        elif self.rtf_endhook_state == 'freq5':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[4]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

        elif self.rtf_endhook_state == 'freq5_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 5)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[5]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq6'
            
        elif self.rtf_endhook_state == 'freq6':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[5]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

            
        elif self.rtf_endhook_state == 'freq6_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 6)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[6]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq7'
            
        elif self.rtf_endhook_state == 'freq7':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[6]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'

            
        elif self.rtf_endhook_state == 'freq7_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 7)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[7]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq8'
            
        elif self.rtf_endhook_state == 'freq8':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[7]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'


        elif self.rtf_endhook_state == 'freq8_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 8)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[8]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq9'
            
        elif self.rtf_endhook_state == 'freq9':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[8]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'


        elif self.rtf_endhook_state == 'freq9_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 9)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[9]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq10'
            
        elif self.rtf_endhook_state == 'freq10':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[9]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'


        elif self.rtf_endhook_state == 'freq10_meas':
            # get value

            # change freq
            self.ChangeFrequencyFunc (0, 10)
            self.ui.rtf_line1Label.setText(f"Running on {self.freq_list[10]}")
            self.SendConfig('square', 'start')
            self.StartChannelByIndex(0)
            self.rtf_endhook_state = 'freq11'
            
        elif self.rtf_endhook_state == 'freq11':
            self.ui.rtf_line1Label.setText(f"Measure {self.freq_list[10]}")
            self.progressBar_timer.singleShot(time_for_meas, self.Roll_SM)
            self.rtf_endhook_state = f'{self.rtf_endhook_state}_meas'
            

        elif self.rtf_endhook_state == 'freq11_meas':
            # get value

            # stop roll
            self.rtf_endhook = False            
            self.ui.rtf_line1Label.setText("Roll Stops")            
            self.ui.rtf_startButton.show()
            self.ui.rtf_stopButton.hide()        

            

    def StopRoll (self):
        if self.rtf_endhook == True:
            self.StopChannelByIndex(0)
            # self.ChangeFrequencyFunc (0, self.rtf_freq_last_index)
            self.rtf_endhook = False
            self.ui.rtf_startButton.show()
            self.ui.rtf_stopButton.hide()        

            
        
    # def EnableChannel (self):
    #     sender = self.sender()
        
    #     obj_list = sender.objectName().split('_')
    #     ch_name = obj_list[0]
    #     ch_func = obj_list[1]
    #     ch_index = self.GetChannelIndexFromString(ch_name)

    #     if self.enableButton_ui_list[ch_index].text() == 'Enable Channel':
    #         # check if SendConfig is ready to sent
    #         if self.progress_config != 'init':
    #             return

    #         self.enableButton_ui_list[ch_index].setText('Disable Channel')
    #         self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(129, 129, 129);\
    #                                                            border: 2px solid rgb(218, 218, 218);')
    #         self.SendConfig(ch_name, 'enable')
    #         self.SendConfigByIndex (ch_index)
    #     else:
    #         self.enableButton_ui_list[ch_index].setText('Enable Channel')
    #         self.enableButton_ui_list[ch_index].setStyleSheet('background-color: rgb(218, 218, 218);')
    #         self.probeLabel_ui_list[ch_index].setText('None')

    #         if self.in_treat_ch_list[ch_index] == True:
    #             self.StopChannelByIndex(ch_index)
                
    #         if ch_index < 3:
    #             self.displayLabel_ui_list[ch_index].setText('--')
    #         self.SendConfig(ch_name, 'disable')
            

    def SendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command + '\n')
            print(channel + ' ' + command + '\n')

            
    def SendEncodFreq (self, channel, value):
        if self.s.port_open == True:
            encoder = ''
            if channel == 'ch1':
                encoder = 'encod0'
            elif channel == 'ch2':
                encoder = 'encod2'
            elif channel == 'ch2':
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
            elif channel == 'ch2':
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

        if sender.objectName() == 'battcButton':
            self.ui.battcButton.setIcon(QIcon())
            self.ui.battcButton.setText(self.battery_c_voltage_str)
            self.battc_revert = True
            self.revert_cnt = 2            

        if sender.objectName() == 'battdButton':
            self.ui.battdButton.setIcon(QIcon())
            self.ui.battdButton.setText(self.battery_d_voltage_str)
            self.battd_revert = True
            self.revert_cnt = 2            
            

    def RevertVoltages (self):
        if self.revert_cnt > 0:
            self.revert_cnt -= 1
            return
            
        if self.batt_revert:
            self.ui.battButton.setText('')
            self.batta_revert = False
            self.ui.battButton.setIcon(self.batticon_list[int(self.battery_a_state)])
            
            
    def UpdateSupplyPower (self, power_str):
        # supply mains 11.2 13.2 08.6 08.3 08.3 08.4 
        # supply battery 6.2V 8.4V 8.4V 4 4
        update_volts = False
        update_values = False
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
        batta_str = power_str_list[7]
        battb_str = power_str_list[6]
        battc_str = power_str_list[5]
        battd_str = power_str_list[4]
        print(f'a:{batta_str} b:{battb_str} c: {battc_str} d: {battd_str}')
        try:
            batta = float(batta_str)
            battb = float(battb_str)
            battc = float(battc_str)
            battd = float(battd_str)
            update_values = True
        except:
            print('error in values')
            pass
            
        if update_volts and update_values:
            self.mains_voltage_str = power_str_list [2]
            self.battery_a_voltage_str = power_str_list [7]
            self.battery_b_voltage_str = power_str_list [6]
            self.battery_c_voltage_str = power_str_list [5]
            self.battery_d_voltage_str = power_str_list [4]

            self.battery_a_state = self.CheckBattValues(batta)
            self.battery_b_state = self.CheckBattValues(battb)
            self.battery_c_state = self.CheckBattValues(battc)
            self.battery_d_state = self.CheckBattValues(battd)
            
            self.ui.battaButton.setIcon(self.batticon_list[int(self.battery_a_state)])                
            self.ui.battbButton.setIcon(self.batticon_list[int(self.battery_b_state)])
            self.ui.battcButton.setIcon(self.batticon_list[int(self.battery_c_state)])                
            self.ui.battdButton.setIcon(self.batticon_list[int(self.battery_d_state)])

            
    def CheckBattValues (self, volt_float):
        state = '0'
        if volt_float > 8.0:
            state = '4'
        elif volt_float > 7.5:
            state = '3'
        elif volt_float > 7.0:
            state = '2'
        elif volt_float > 6.5:
            state = '1'

        return state
        

    def UpdatePlatesConnectors (self, conn_plates_str, conn_probe_str):
        # uncomment if get state every 6 secs
        plates = int(conn_plates_str, 16)
        probe = int(conn_probe_str, 16)        
        if self.last_plates == plates and \
           self.last_probe == probe:
            return

        # update plates & probe
        self.last_plates = plates
        self.last_probe = probe

        # check pairs colors
        self.SetPlatesPolarity(plates)
        self.SetProbePolarity(probe)

        
    def SetPlatesPolarity (self, plates_int):
        # clean all
        for x in range (8):
            self.platesButton_ui_list[x].setIcon(self.platesicon_list[0])
            
        for x in range (4):
            dmask = 3 << (2*x)
            lw = 2 * x
            up = 2 * x + 1
            if (plates_int & dmask) == dmask:
                # two plates connected
                if self.pol_index_ch_list[0] == 'positive':
                    self.platesButton_ui_list[lw].setIcon(self.platesicon_list[2])
                    self.platesButton_ui_list[up].setIcon(self.platesicon_list[3])
                elif self.pol_index_ch_list[0] == 'negative':
                    self.platesButton_ui_list[lw].setIcon(self.platesicon_list[3])
                    self.platesButton_ui_list[up].setIcon(self.platesicon_list[2])
                else:
                    self.platesButton_ui_list[lw].setIcon(self.platesicon_list[1])
                    self.platesButton_ui_list[up].setIcon(self.platesicon_list[1])
            elif plates_int & dmask:
                print(f"plates: {plates_int} probe: {self.last_probe}")
                
                if (plates_int & 0x40) and self.last_probe:
                    if self.pol_index_ch_list[0] == 'positive':
                        self.platesButton_ui_list[up].setIcon(self.platesicon_list[3])
                    elif self.pol_index_ch_list[0] == 'negative':
                        self.platesButton_ui_list[up].setIcon(self.platesicon_list[2])
                    else:
                        self.platesButton_ui_list[up].setIcon(self.platesicon_list[1])
                else:
                    # one plate connected and not probe
                    pos_int = (plates_int & dmask) >> (2*x)
                    
                    print(f"plates: {plates_int} pos_int: {pos_int}")
                    if pos_int & 0x01:
                        self.platesButton_ui_list[up].setIcon(self.platesicon_list[1])
                    else:
                        self.platesButton_ui_list[lw].setIcon(self.platesicon_list[1])
                
                
    def SetProbePolarity (self, probe_int):
        # clean probe
        self.ui.intpButton.setIcon(self.platesicon_list[0])

        if probe_int:
            # probe connected
            if self.last_plates & 0x40:
                if self.pol_index_ch_list[0] == 'positive':
                    self.ui.intpButton.setIcon(self.platesicon_list[2])
                elif self.pol_index_ch_list[0] == 'negative':
                    self.ui.intpButton.setIcon(self.platesicon_list[3])
                else:
                    self.ui.intpButton.setIcon(self.platesicon_list[1])
            else:
                self.ui.intpButton.setIcon(self.platesicon_list[1])

            
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
            # self.progress_config = 'mode'
            self.progress_config = 'init'
        #     self.progress_timer.singleShot(50, self.SendConfigChannelSM)
        # elif self.progress_config == 'mode':
        #     if self.prog_ch_index == 0 or self.prog_ch_index == 1:
        #         self.SendConfig(self.prog_ch_name, 'mode square')
        #     else:
        #         self.SendConfig(self.prog_ch_name, 'mode sine')
        #     self.progress_config = 'init'

            
    def ProgressBarSM (self):
        next_cycle = False

        # print(f" in SM {self.in_treat_ch_list[2]} show {self.in_treat_show_sine_list[2]}")
        if self.in_treat_ch_list[1] == True and \
           self.in_treat_show_sine_list[1] == True:
            if self.pol_index_ch_list[1] == 'negative':
                sine_point = -self.sine_pos_table_list[self.sine_cnt]
            elif self.pol_index_ch_list[1] == 'positive':
                sine_point = self.sine_pos_table_list[self.sine_cnt]
            else:    # alternative
                sine_point = self.sine_alt_table_list[self.sine_cnt]

            display, progress = self.ProgressCalcValue(self.pwr_index_ch_list[1], sine_point)
            self.ui.ch2_progressBar.setValue(progress)
            self.ui.ch2_displayLabel.setText(str(display))
            next_cycle = True
        else:
            self.ui.ch2_progressBar.setValue(0)
            self.ui.ch2_displayLabel.setText('--')
            self.in_treat_show_sine_list[1] = False

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
        # "conn 0x%02x 0x%02x\r\n"        
        if rcv.startswith("conn "):
            rcv_list = rcv.split(' ')
            self.UpdatePlatesConnectors(rcv_list[1], rcv_list[2])
            return
        # if rcv.startswith("ch"):

        #     ch_index = rcv_list[0][-1]
        #     try:
        #         ch_index = int (ch_index)
        #     except:
        #         ch_index = 5
                
        #     if ch_index < 5:
        #         ch_index = ch_index - 1
        #     else:
        #         return

        #     rcv_str = rcv[4:]
        #     # print("receiv: " + rcv_str + " in index: " + str(ch_index))
        #     self.ParseChannelsComms(ch_index, rcv_str)
        self.ParseChannelsComms(rcv)
            

    def ParseChannelsComms (self, ch_str):
        # display values
        if ch_str.startswith("display "):
            rcv_list = ch_str.split(' ')
            try:
                gain = int(rcv_list[1])
            except:
                gain = 0
            # print('ch1 display: ' + str(gain))

            if self.probeLabel_ui_list[0].text() == 'NervSync':
                self.displayLabel_ui_list[0].setText(str(gain))
                
            elif self.probeLabel_ui_list[1].text() == 'CellSync':
                self.displayLabel_ui_list[1].setText(str(gain))

            else:
                pass

            return
        # end of display values

        # probe messages
        if ch_str.startswith("new probe NervSync"):
            self.probeLabel_ui_list[0].setText("NervSync")
            self.probeLabel_ui_list[1].setText("None")
            return
        if ch_str.startswith("new probe CellSync"):
            self.probeLabel_ui_list[0].setText("None")            
            self.probeLabel_ui_list[1].setText("CellSync")
            return
        # end of probe messages

        # probe others
        if ch_str.startswith("none probe"):
            self.probeLabel_ui_list[0].setText('None')
            self.probeLabel_ui_list[1].setText('None')            
            # if self.enableButton_ui_list[ch_index].text() == 'Disable Channel' and \
            #    self.in_treat_ch_list[ch_index] == True:
            #     self.StopChannelByIndex(ch_index)
            return
        # end of probe others

        # probe others 2
        if ch_str.startswith("probe start"):
            rcv_list = ch_str.split(' ')
            if len(rcv_list) == 3:
                if rcv_list[2] == 'square':
                    if self.probeLabel_ui_list[0].text() != 'NervSync':
                        self.probeLabel_ui_list[0].setText("NervSync")
                        self.probeLabel_ui_list[1].setText("None")
                    if self.in_treat_ch_list[0] == False:
                        self.SendConfig('square', 'start')
                        self.StartChannelByIndex(0)
                        
                if rcv_list[2] == 'sine':
                    if self.probeLabel_ui_list[1].text() != 'CellSync':
                        self.probeLabel_ui_list[0].setText("None")
                        self.probeLabel_ui_list[1].setText("CellSync")
                    if self.in_treat_ch_list[1] == False:
                        self.SendConfig('sine', 'start')
                        self.StartChannelByIndex(1)
                        
            else:
                if self.probeLabel_ui_list[0].text() == 'NervSync' and \
                   self.in_treat_ch_list[0] == False:
                    self.SendConfig('square', 'start')
                    self.StartChannelByIndex(0)
                
                elif self.probeLabel_ui_list[1].text() == 'CellSync' and \
                     self.in_treat_ch_list[1] == False:
                    self.SendConfig('sine', 'start')
                    self.StartChannelByIndex(1)

                else:
                    pass
                            
            return
        # end of probe others 2

        # for show sine progress
        if ch_str.startswith("starting sinusoidal"):
            self.in_treat_show_sine_list[1] = True
            # print(f" in serial {self.in_treat_show_sine_list[2]}")
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

            if self.probeLabel_ui_list[0].text() == 'NervSync' and \
                 self.in_treat_ch_list[0] == True:
                # self.displayTextLabel_ui_list[0].setText('Res. ' + str(res_int) + res_mult)
                pass

            if self.probeLabel_ui_list[1].text() == 'CellSync' and \
                 self.in_treat_ch_list[1] == True:
                # self.displayTextLabel_ui_list[1].setText('Res. ' + str(res_int) + res_mult)
                pass

            # end of resistance meas online
