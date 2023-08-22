# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets


#imported uis
from ui_micro import Ui_MainWindow


class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
            
        
    def control_page_one (self):

        self.page_animation()

    def control_page_two (self):
        self.stackedWidget.setCurrentWidget(self.page_two)
        self.page_animation()

    def control_page_three (self):
        self.stackedWidget.setCurrentWidget(self.page_three)
        self.page_animation()

    def control_page_four (self):
        self.stackedWidget.setCurrentWidget(self.page_four)
        self.page_animation()
        

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


    def ChangePolarity (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_posButton':
            self.ui.ch1_posButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ui.ch1_altButton.setStyleSheet('')
            self.ui.ch1_negButton.setStyleSheet('')

        if sender.objectName() == 'ch1_altButton':
            self.ui.ch1_posButton.setStyleSheet('')
            self.ui.ch1_altButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ui.ch1_negButton.setStyleSheet('')

        if sender.objectName() == 'ch1_negButton':
            self.ui.ch1_posButton.setStyleSheet('')
            self.ui.ch1_altButton.setStyleSheet('')
            self.ui.ch1_negButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            

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

        self.ui.ch1_freqLabel.setText(self.freq_list[self.ch1_freq_index])


    def ChangePower (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_pwrUpButton':
            if self.ch1_pwr_index < 5:
                self.ch1_pwr_index += 1

        if sender.objectName() == 'ch1_pwrDwnButton':
            if self.ch1_pwr_index > 0:
                self.ch1_pwr_index -= 1

        self.ui.ch1_pwrLabel.setText(self.pwr_list[self.ch1_pwr_index])


    def StartCh1 (self):
        pass

    def EnableCh1 (self):
        pass
    
