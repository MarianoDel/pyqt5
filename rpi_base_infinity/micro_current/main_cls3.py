# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtCore, QtWidgets
from datetime import datetime
import os
# import threading

#imported uis
from ui_micro3 import Ui_MainWindow

#Here import the UIs or classes that got the UIs
from menu_cls3 import MenuWindow
from rtf_cls3 import RTFWindow


class MainWindow (QMainWindow):

    #SIGNALS
    one_second_signal = pyqtSignal()

    def __init__(self, config_class, serialport, parent=None):
        super(MainWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.config_class = config_class
        self.distro = self.config_class.GetCurrentSystem()
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

        # save batt str
        self.batt_str_list = ['00.0', '00.0', '00.0', '00.0']
        self.style_label_perc = """color: rgb(255, 255, 255);
                                   font: 12 24pt "TT Norms ExtraLight";"""
        self.style_label_volts = """color: rgb(255, 255, 255);
                                    font: 12 14pt "TT Norms ExtraLight";"""
        self.ui.battLabel.setStyleSheet(self.style_label_perc)
        

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
            
        self.probe_cn_ui_list = [self.ui.ch1_probeCnButton, self.ui.ch2_probeCnButton]
        self.probe_ncn_ui_list = [self.ui.ch1_probeNCnButton, self.ui.ch2_probeNCnButton]
        for x in range(2):
            self.probe_cn_ui_list[x].setStyleSheet(self.style_pol_deact)
            self.probe_ncn_ui_list[x].setStyleSheet(self.style_pol_act)
        
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

        ## Hamburger Menu Button
        self.ui.hambButton.clicked.connect(self.MenuScreen)
        self.audio_selected = self.config_class.audio_selected

        ## RTF Roll Through Function Button
        self.ui.rtf_startButton.clicked.connect(self.RTFScreen)
        
        ## connect the signals
        # timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)
        self.parent.rcv_signal.connect(self.SerialDataCallback)
        self.serialcb = self.parent.rcv_signal

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

        self.progress_config = 'init'
        
        self.in_treat_ch_list = [False, False]
        self.in_treat_show_sine = False    # todavia la uso?????

        # all channels none probe
        self.probeLabel_ui_list = [self.ui.ch1_probeLabel, self.ui.ch2_probeLabel]
        for x in range(2):
            self.probeLabel_ui_list[x].setText('Probe')

        # mains and battery buttons
        self.ui.battButton.clicked.connect(self.ShowVoltages)
        
        # batteries full at start
        self.mains_mode = 'mains'
        self.mains_state_int = 0
        self.batt_revert = False
        self.revert_cnt = 0
        
        ## setup mains & battery icons
        self.mains_icon_list = [QIcon(':/icons/resources/batt_charge_0.png'),\
                                QIcon(':/icons/resources/batt_charge_25.png'),\
                                QIcon(':/icons/resources/batt_charge_50.png'),\
                                QIcon(':/icons/resources/batt_charge_75.png'),\
                                QIcon(':/icons/resources/batt_charge_100.png')]
        self.batt_icon_list = [QIcon(':/icons/resources/batt_0.png'),\
                               QIcon(':/icons/resources/batt_25.png'),\
                               QIcon(':/icons/resources/batt_50.png'),\
                               QIcon(':/icons/resources/batt_75.png'),\
                               QIcon(':/icons/resources/batt_100.png')]
        self.plates_icon_list = [QIcon(':/icons/resources/conector.png'),\
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

        self.ui.ch2_progressBar.setTextVisible(False)
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
        self.platesButton_ui_list = [self.ui.pch4upButton, self.ui.pch4dwnButton, self.ui.pch3upButton, self.ui.pch3dwnButton, self.ui.pch2upButton, self.ui.pch2dwnButton, self.ui.pch1upButton, self.ui.pch1dwnButton]
        self.last_probe = 0
        self.ui.intpButton.setIcon(self.plates_icon_list[0])

        ## to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)
        
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
        self.SendConfig('audio volume', self.audio_selected)

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

        self.remainMins_ui_list[ch_index].setText(str(self.remaining_minutes_ch_list[ch_index]) + "m")
        self.remainSecs_ui_list[ch_index].setText(str(self.remaining_seconds_ch_list[ch_index]) + "s")        

        
    def StartChannelByIndex (self, ch_index):
        self.StartChannelUpdateTimer(ch_index)
        
        self.in_treat_ch_list[ch_index] = True
        self.remainMins_ui_list[ch_index].show()
        self.remainSecs_ui_list[ch_index].show()
        # self.stopButton_ui_list[ch_index].show()
        self.startButton_ui_list[ch_index].setText("STOP")
        # always stops ch0 meas
        self.displayLabel_ui_list[0].display('---')

        if ch_index == 1:
            self.ui.ch2_progressBar.setValue(0)
            # self.ui.ch1_displayLabel.setText('0')
            self.progressBar_timer.singleShot(200, self.ProgressBarSM)
            # print("   starting sine SM")
        
        
    def StopChannelByIndex (self, ch_index):
        self.SendConfig('stop', '')        

        self.in_treat_ch_list[ch_index] = False
        self.remainMins_ui_list[ch_index].hide()
        self.remainSecs_ui_list[ch_index].hide()
        # self.stopButton_ui_list[ch_index].hide()
        self.startButton_ui_list[ch_index].setText("START")
        # self.displayTextLabel_ui_list[ch_index].setText('')
        

    def SendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command + '\n')
            print(channel + ' ' + command + '\n')

            
    def SendEncodFreq (self, channel_str, value):
        if self.s.port_open == True:
            encoder = ''
            if channel_str == 'ch1':
                encoder = 'enc 0'
            else:    # ch2
                encoder = 'enc 2'

            if value <= 9:
                self.s.Write(encoder + ' ' + str(value) + '\n')
            elif value == 10:
                self.s.Write(encoder + ' :\n')
            elif value == 11:
                self.s.Write(encoder + ' ;\n')
                

    def SendEncodPwr (self, channel_str, value):
        if self.s.port_open == True:
            encoder = ''
            if channel_str == 'ch1':
                encoder = 'enc 1'
            else:    # ch2
                encoder = 'enc 3'
                
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
        if self.batt_revert:
            return

        self.batt_revert = True
        self.revert_cnt = 2

        batt_str = f'{self.batt_str_list[0]}V {self.batt_str_list[1]}V\n{self.batt_str_list[2]}V {self.batt_str_list[3]}V'
        self.ui.battLabel.setStyleSheet(self.style_label_volts)
        self.ui.battLabel.setText(batt_str)
            

    def RevertVoltages (self):
        if self.revert_cnt > 0:
            self.revert_cnt -= 1
            return
            
        if self.batt_revert:
            self.batt_revert = False

            total_charge = 0
            for x in range(4):
                try:
                    total_charge += self.BatteryCharge(float(self.batt_str_list[x]))
                except:
                    pass

            total_perc = total_charge * 100 / (4 * 9000)
            total_perc_int = int(total_perc)
            self.ui.battLabel.setStyleSheet(self.style_label_perc)
            self.ui.battLabel.setText(f'{total_perc_int}%')
            
            
    def UpdateSupplyPower (self, power_str):
        # supply mains 11.2 13.2 08.6 08.3 08.3 08.4 
        # supply battery 00.2 13.2 08.6 08.3 08.3 08.4 
        icon_change = False
        
        power_str_list = power_str.split(' ')
        if power_str_list[1] == 'mains':
            if self.mains_mode != 'mains':
                self.mains_mode = 'mains'
                icon_change = True
                
        elif power_str_list [1] == 'battery':
            if self.mains_mode != 'battery':
                self.mains_mode = 'battery'
                icon_change = True                

        # update mains & battery voltages
        for x in range (4):
            self.batt_str_list[x] = power_str_list[x+4] 

        print(f'a:{self.batt_str_list[0]} b:{self.batt_str_list[1]} c: {self.batt_str_list[2]} d: {self.batt_str_list[3]}')

        if self.batt_revert:
            return

        total_charge = 0
        for x in range(4):
            total_charge += self.BatteryCharge(float(self.batt_str_list[x]))

        total_perc = total_charge * 100 / (4 * 9000)
        total_perc_int = int(total_perc)
        print(f'charge batt: {total_charge} percent: {total_perc_int}')
        self.ui.battLabel.setText(f'{total_perc_int}%')

        icon_index = self.CheckBattValues(total_perc_int)
        if icon_change:
            self.mains_state_int = icon_index
            if self.mains_mode == 'mains':
                self.ui.battButton.setIcon(self.mains_icon_list[self.mains_state_int])
            else:
                self.ui.battButton.setIcon(self.batt_icon_list[self.mains_state_int])
            
        if self.mains_state_int != icon_index:
            self.mains_state_int = icon_index
            if self.mains_mode == 'mains':
                self.ui.battButton.setIcon(self.mains_icon_list[self.mains_state_int])
            else:
                self.ui.battButton.setIcon(self.batt_icon_list[self.mains_state_int])

            
    def CheckBattValues (self, total_perc_int):
        state = 0
        if total_perc_int > 95:
            state = 4
        elif total_perc_int > 75:
            state = 3
        elif total_perc_int > 50:
            state = 2
        elif total_perc_int > 25:
            state = 1

        return state


    def BatteryCharge (self, batt_volt):
        if batt_volt >= 8.4:
            batt_volt = 8.4

        if batt_volt < 6.4:
            batt_volt = 6.4

        batt_volt = batt_volt - 6.4    # between 2 and 0
        batt_mca = batt_volt * 4500    # 9000 mca is the max charga
        return batt_mca
        

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
            self.platesButton_ui_list[x].setIcon(self.plates_icon_list[0])
            
        for x in range (4):
            dmask = 3 << (2*x)
            lw = 2 * x
            up = 2 * x + 1
            if x != 3:
                # check all conns but not the probe
                if (plates_int & dmask) == dmask:
                    # two plates connected
                    if self.pol_index_ch_list[0] == 'positive':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[3])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[2])
                    elif self.pol_index_ch_list[0] == 'negative':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[2])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[3])
                    else:
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[1])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[1])

                elif plates_int & dmask:
                    # one plate conn
                    pos_int = (plates_int & dmask) >> (2*x)                    
                    if pos_int & 0x01:
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[1])
                    else:
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[1])

            elif self.last_probe:
                # conn of probe kit with probe present
                if (plates_int & 0x40):
                    if self.pol_index_ch_list[0] == 'positive':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[3])
                    elif self.pol_index_ch_list[0] == 'negative':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[2])
                    else:
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[1])
                
            else:
                # conn of probe kit no probe
                if (plates_int & dmask) == dmask:
                    # two plates connected
                    if self.pol_index_ch_list[0] == 'positive':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[3])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[2])
                    elif self.pol_index_ch_list[0] == 'negative':
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[2])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[3])
                    else:
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[1])
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[1])

                elif plates_int & dmask:
                    # one plate conn
                    pos_int = (plates_int & dmask) >> (2*x)                    
                    if pos_int & 0x01:
                        self.platesButton_ui_list[lw].setIcon(self.plates_icon_list[1])
                    else:
                        self.platesButton_ui_list[up].setIcon(self.plates_icon_list[1])
                
                
    def SetProbePolarity (self, probe_int):
        # clean probe
        self.ui.intpButton.setIcon(self.plates_icon_list[0])

        if probe_int:
            # probe connected
            if self.last_plates & 0x40:
                if self.pol_index_ch_list[0] == 'positive':
                    self.ui.intpButton.setIcon(self.plates_icon_list[2])
                elif self.pol_index_ch_list[0] == 'negative':
                    self.ui.intpButton.setIcon(self.plates_icon_list[3])
                else:
                    self.ui.intpButton.setIcon(self.plates_icon_list[1])
            else:
                self.ui.intpButton.setIcon(self.plates_icon_list[1])

            
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
        if self.in_treat_ch_list[1] == True:
            if self.pol_index_ch_list[1] == 'negative':
                sine_point = -self.sine_pos_table_list[self.sine_cnt]
            elif self.pol_index_ch_list[1] == 'positive':
                sine_point = self.sine_pos_table_list[self.sine_cnt]
            else:    # alternative
                sine_point = self.sine_alt_table_list[self.sine_cnt]

            display, progress = self.ProgressCalcValue(self.pwr_index_ch_list[1], sine_point)
            self.ui.ch2_progressBar.setValue(progress)
            self.ui.ch2_lcdNumber.display(str(display))
            # self.ui.ch2_displayLabel.display(str(display))            
            next_cycle = True
        else:
            self.ui.ch2_progressBar.setValue(0)
            self.ui.ch2_lcdNumber.display('---')
            self.in_treat_show_sine = False

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
        disp_value = prog_value
        if prog_value < 0:
            prog_value = -prog_value
            
        if prog_value > 100:
            prog_value = 100

        if disp_value > 100:
            disp_value = 100

        if disp_value < -99:
            disp_value = -99
            
        # disp_value = sine_point * c
        # disp_value = int(disp_value)
        # if disp_value > 1000:
        #     disp_value = 1000
            
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
                    self.remainMins_ui_list[x].setText(str(self.remaining_minutes_ch_list[x]) + "m")
                    self.remainSecs_ui_list[x].setText(str(self.remaining_seconds_ch_list[x]) + "s")

                else:
                    self.StopChannelByIndex(x)

        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)


    def UpdateDateTime(self, new_date_time):
        date_str = ""
        date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        self.ui.datetimeLabel.setText(date_str)
        
        
    ##################
    # Serial Methods #
    ##################
    def SerialDataCallback (self, rcv):        
        # print ("serial data callback!")
        # print (rcv)
        # self.SerialProcess(rcv)
        if rcv.startswith('\n'):
            return

        # encoders by position
        if rcv.startswith("encp "):
            # print("   in rx encoders!")
            rcv_list = rcv.split(' ')            
            try:
                index = int(rcv_list[1])
            except:
                index = 8

            # print(f"   enc index: {index}")
            if index > 7:
                return

            if index == 0 or index == 2:
                # frequency encoders
                try:
                    pos = ord(rcv_list[2]) - ord('0')
                except:
                    pos = 11

                # print(f"   enc pos: {pos}")                    
                if pos > 11:
                    return

                if index == 0:
                    ch_index = 0
                else:
                    ch_index = 1
                    
                self.freq_index_ch_list[ch_index] = pos
                self.ChangeFrequencyByIndex(ch_index)
                                        
            elif index == 1 or index == 3:
                # power encoders                
                try:
                    pos = ord(rcv_list[2]) - ord('0')
                except:
                    pos = 6

                if pos > 5:
                    return

                if index == 1:
                    ch_index = 0
                else:
                    ch_index = 1

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

            if self.probeLabel_ui_list[0].text() == 'NervSync' and \
               self.in_treat_ch_list[0] == False:
                # self.displayLabel_ui_list[0].setText(str(gain))
                self.ui.ch1_lcdNumber.display(str(gain))                
                
            elif self.probeLabel_ui_list[1].text() == 'CellSync':
                # self.displayLabel_ui_list[1].setText(str(gain))
                pass
            else:
                pass

            return
        # end of display values

        # probe messages
        if ch_str.startswith("new probe NervSync"):
            self.probeLabel_ui_list[0].setText("NervSync") 
            self.probe_cn_ui_list[0].setStyleSheet(self.style_pol_act)
            self.probe_ncn_ui_list[0].setStyleSheet(self.style_pol_deact)

            self.probeLabel_ui_list[1].setText("Probe")
            self.probe_cn_ui_list[1].setStyleSheet(self.style_pol_deact)
            self.probe_ncn_ui_list[1].setStyleSheet(self.style_pol_act)
            return
        if ch_str.startswith("new probe CellSync"):
            self.probeLabel_ui_list[0].setText("Probe")            
            self.probe_cn_ui_list[0].setStyleSheet(self.style_pol_deact)
            self.probe_ncn_ui_list[0].setStyleSheet(self.style_pol_act)

            self.probeLabel_ui_list[1].setText("CellSync")
            self.probe_cn_ui_list[1].setStyleSheet(self.style_pol_act)
            self.probe_ncn_ui_list[1].setStyleSheet(self.style_pol_deact)
            self.ui.ch1_lcdNumber.display('---')
            return
        # end of probe messages

        # probe others
        if ch_str.startswith("none probe"):
            self.probeLabel_ui_list[0].setText('Probe')
            self.probe_cn_ui_list[0].setStyleSheet(self.style_pol_deact)
            self.probe_ncn_ui_list[0].setStyleSheet(self.style_pol_act)
            self.probeLabel_ui_list[1].setText('Probe')
            self.probe_cn_ui_list[1].setStyleSheet(self.style_pol_deact)
            self.probe_ncn_ui_list[1].setStyleSheet(self.style_pol_act)
            self.ui.ch1_lcdNumber.display('---')
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
                        self.probe_cn_ui_list[0].setStyleSheet(self.style_pol_act)
                        self.probe_ncn_ui_list[0].setStyleSheet(self.style_pol_deact)

                        self.probeLabel_ui_list[1].setText("Probe")
                        self.probe_cn_ui_list[1].setStyleSheet(self.style_pol_deact)
                        self.probe_ncn_ui_list[1].setStyleSheet(self.style_pol_act)
                        
                    if self.in_treat_ch_list[0] == False and \
                       self.in_treat_ch_list[1] == False:
                        self.SendConfig('square', 'start')
                        self.StartChannelByIndex(0)
                        
                if rcv_list[2] == 'sine':
                    if self.probeLabel_ui_list[1].text() != 'CellSync':
                        self.probeLabel_ui_list[0].setText("Probe")
                        self.probe_cn_ui_list[0].setStyleSheet(self.style_pol_deact)
                        self.probe_ncn_ui_list[0].setStyleSheet(self.style_pol_act)

                        self.probeLabel_ui_list[1].setText("CellSync")
                        self.probe_cn_ui_list[1].setStyleSheet(self.style_pol_act)
                        self.probe_ncn_ui_list[1].setStyleSheet(self.style_pol_deact)

                    if self.in_treat_ch_list[0] == False and \
                       self.in_treat_ch_list[1] == False:
                        self.SendConfig('sine', 'start')
                        self.StartChannelByIndex(1)
                        
            else:
                # just for backward compatibility on probe start
                if self.probeLabel_ui_list[0].text() == 'NervSync' and \
                   self.in_treat_ch_list[0] == False and \
                   self.in_treat_ch_list[1] == False:                    
                    self.SendConfig('square', 'start')
                    self.StartChannelByIndex(0)
                
                elif self.probeLabel_ui_list[1].text() == 'CellSync' and \
                     self.in_treat_ch_list[0] == False and \
                     self.in_treat_ch_list[1] == False:
                    self.SendConfig('sine', 'start')
                    self.StartChannelByIndex(1)

                else:
                    pass
                            
            return
        # end of probe others 2

        # for show sine progress
        if ch_str.startswith("starting sinusoidal"):
            self.in_treat_show_sine = True
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


####################################
# Different Screens Calls are here #
####################################

    ## Screen for Hamburger Menu
    def MenuScreen (self):
        # self.screensaver_window = False
        self.a = MenuWindow(self.s, self.audio_selected, parent=self)
        # self.a = MenuWindow(self.s)
        self.a.show()
        # self.hide()

    def cbMenu (self, volume):
        print(f"menu done: {volume}")
        if volume != self.audio_selected:
            self.config_class.audio_selected = volume
            self.config_class.SaveConfigFile()
            
        self.audio_selected = volume
        self.SendConfig('audio volume', self.audio_selected)
        self.UpdateDateTime(datetime.today())


    ## Screen for RTF
    def RTFScreen (self):
        for ch_index in range (2):
            if self.in_treat_ch_list[ch_index] != False:
                print("some channel is running!")
                # self.ui.rtf_line1Label.setText("Some channel is running")
                return

        # if self.ui.ch1_probeLabel.text() != "NervSync":
        #     print("NervSync Probe NC")
        #     # self.ui.rtf_line1Label.setText("NervSync Probe NC")            
        #     return
        
        # self.screensaver_window = False
        self.a = RTFWindow(self.s, parent=self)
        self.a.show()


    def cbRTF (self):
        print("rtf done, updating configs to main window")
        self.ChangeFrequencyByIndex (0)    #square send actual config
        self.ChangeFrequencyByIndex (1)    #sine send actual config
        os.system("sleep 0.05")
        self.ChangePowerByIndex(0)    #square send actual config
        self.ChangePowerByIndex(1)    #sine send actual config

