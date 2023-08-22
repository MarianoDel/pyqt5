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

    def __init__(self, serialport):
        super(MainWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        
        # self.bt_close.clicked.connect(self.close)
        self.ui.bt_menu_close.clicked.connect(self.move_menu)
        self.ui.bt_menu_open.clicked.connect(self.move_menu)

        self.ui.ch1_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ui.ch1_gainDwnButton.clicked.connect(self.GainUpDwn)
        self.gain = 50

        # polarity on ch1
        self.ui.ch1_posButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_altButton.clicked.connect(self.ChangePolarity)
        self.ui.ch1_negButton.clicked.connect(self.ChangePolarity)

        # timer options
        self.ch1_timer_index = 0
        self.timer_list = ['6s', '12s', '30s', '1m', '10m', '30m']
        # timer on ch1
        self.ui.ch1_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ui.ch1_timerDwnButton.clicked.connect(self.ChangeTimer)

        # frequency options
        self.ch1_freq_index = 0
        self.freq_list = ['0.5Hz', '1.0Hz', '2.0Hz', '4.0Hz', '8.0Hz', '10Hz', '20Hz', '40Hz', '80Hz', '160Hz', '320Hz']
        # frequency on ch1
        self.ui.ch1_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ui.ch1_freqDwnButton.clicked.connect(self.ChangeFrequency)

        # intensity options
        self.ch1_pwr_index = 0
        self.pwr_list = ['25uA', '50uA', '100uA', '200uA', '400uA', '600uA']
        # power on ch1
        self.ui.ch1_pwrUpButton.clicked.connect(self.ChangePower)
        self.ui.ch1_pwrDwnButton.clicked.connect(self.ChangePower)

        # others on ch1
        self.ui.ch1_startButton.clicked.connect(self.StartCh1)
        self.ui.ch1_stopButton.clicked.connect(self.StopCh1)        
        self.ui.ch1_enableButton.clicked.connect(self.EnableCh1)

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
        
        ## initial setup
        self.ui.ch1_stopButton.hide()
        self.ui.ch1_remainMinsLabel.hide()
        self.ui.ch1_remainSecsLabel.hide()        
        self.ui.bt_menu_close.hide()
        self.ch1_in_treat = False        
        
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
        
        if sender.objectName() == 'ch1_gainUpButton':
            if self.gain < 100:
                self.gain += 1

        if sender.objectName() == 'ch1_gainDwnButton':
            if self.gain > 0:
                self.gain -= 1

        self.ui.ch1_gainLabel.setText(str(self.gain))
        self.ui.ch1_displayLabel.setText(str(self.gain))
        self.SendConfig('ch1', 'gain ' + str(self.gain))


    def ChangePolarity (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_posButton':
            self.ui.ch1_posButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ui.ch1_altButton.setStyleSheet('')
            self.ui.ch1_negButton.setStyleSheet('')
            self.SendConfig('ch1', 'polarity positive')

        if sender.objectName() == 'ch1_altButton':
            self.ui.ch1_posButton.setStyleSheet('')
            self.ui.ch1_altButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ui.ch1_negButton.setStyleSheet('')
            self.SendConfig('ch1', 'polarity alternative')

        if sender.objectName() == 'ch1_negButton':
            self.ui.ch1_posButton.setStyleSheet('')
            self.ui.ch1_altButton.setStyleSheet('')
            self.ui.ch1_negButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.SendConfig('ch1', 'polarity negative')
            

    def ChangeTimer (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_timerUpButton':
            if self.ch1_timer_index < 5:
                self.ch1_timer_index += 1

        if sender.objectName() == 'ch1_timerDwnButton':
            if self.ch1_timer_index > 0:
                self.ch1_timer_index -= 1

        self.ui.ch1_timerLabel.setText(self.timer_list[self.ch1_timer_index])


    def ChangeFrequency (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_freqUpButton':
            if self.ch1_freq_index < 10:
                self.ch1_freq_index += 1

        if sender.objectName() == 'ch1_freqDwnButton':
            if self.ch1_freq_index > 0:
                self.ch1_freq_index -= 1

        freq_str = self.freq_list[self.ch1_freq_index]
        self.ui.ch1_freqLabel.setText(freq_str)
        self.SendConfig('ch1', 'freq ' + freq_str)


    def ChangePower (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_pwrUpButton':
            if self.ch1_pwr_index < 5:
                self.ch1_pwr_index += 1

        if sender.objectName() == 'ch1_pwrDwnButton':
            if self.ch1_pwr_index > 0:
                self.ch1_pwr_index -= 1

        power_str = self.pwr_list[self.ch1_pwr_index]
        self.ui.ch1_pwrLabel.setText(power_str)
        self.SendConfig('ch1', 'power ' + power_str)


    def StartCh1 (self):
        self.SendConfig('ch1', 'start')
        timer = self.ui.ch1_timerLabel.text()
        if timer[-1] == 's':
            self.ch1_remaining_minutes = 0
            self.ch1_remaining_seconds = int(timer[:-1])
        elif timer[-1] == 'm':
            self.ch1_remaining_minutes = int(timer[:-1])
            self.ch1_remaining_seconds = 0
            
        self.ui.ch1_remainMinsLabel.setText(str(self.ch1_remaining_minutes) + "'")
        self.ui.ch1_remainSecsLabel.setText(str(self.ch1_remaining_seconds) + "''")        

        self.ch1_in_treat = True
        self.ui.ch1_remainMinsLabel.show()
        self.ui.ch1_remainSecsLabel.show()
        self.ui.ch1_stopButton.show()
        self.ui.ch1_startButton.hide()


    def StopCh1 (self):
        self.SendConfig('ch1', 'stop')
        self.ch1_in_treat = False
        self.ui.ch1_remainMinsLabel.hide()
        self.ui.ch1_remainSecsLabel.hide()
        self.ui.ch1_stopButton.hide()
        self.ui.ch1_startButton.show()



    def EnableCh1 (self):
        self.SendConfig('ch1', 'enable channel')
    

    def SendConfig (self, channel, command):
        if self.s.port_open == True:
            self.s.Write(channel + ' ' + command)

 
    ###########################
    # One Second Timer signal #
    ###########################
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        """ one second gone, check if its something to do """
        if self.ch1_in_treat:
            if (self.ch1_remaining_minutes > 0 or
                self.ch1_remaining_seconds > 0):
                if self.ch1_remaining_seconds > 0:
                    self.ch1_remaining_seconds -= 1
                else:
                    self.ch1_remaining_minutes -= 1
                    self.ch1_remaining_seconds = 59

                #todos los segundos actualizo ui
                self.ui.ch1_remainMinsLabel.setText(str(self.ch1_remaining_minutes) + "'")
                self.ui.ch1_remainSecsLabel.setText(str(self.ch1_remaining_seconds) + "''")

            else:
                self.StopCh1()

        # date_now = datetime.today()
        # if date_now.minute != self.minutes_last:
        #     # print(date_now)
        #     self.minutes_last = date_now.minute
        #     self.UpdateDateTime(date_now)

           
