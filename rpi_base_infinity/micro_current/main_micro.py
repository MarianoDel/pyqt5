# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from treatment_class import Treatment
import platform
from serialcomm import SerialComm


### GLOBALS FOR CONFIGURATION #########
CURRENT_VERSION = 'Micro Current ver 1.0'



class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('micro.ui', self)

        # self.bt_close.clicked.connect(self.close)
        self.bt_menu_close.clicked.connect(self.move_menu)
        self.bt_menu_open.clicked.connect(self.move_menu)

        self.ch1_gainUpButton.clicked.connect(self.GainUpDwn)
        self.ch1_gainDwnButton.clicked.connect(self.GainUpDwn)
        self.gain = 50

        # polarity on ch1
        self.ch1_posButton.clicked.connect(self.ChangePolarity)
        self.ch1_altButton.clicked.connect(self.ChangePolarity)
        self.ch1_negButton.clicked.connect(self.ChangePolarity)

        # timer options
        self.ch1_timer_index = 0
        self.timer_list = ['6s', '12s', '30s', '1m', '10m', '30m']
        # timer on ch1
        self.ch1_timerUpButton.clicked.connect(self.ChangeTimer)
        self.ch1_timerDwnButton.clicked.connect(self.ChangeTimer)

        # frequency options
        self.ch1_freq_index = 0
        self.freq_list = ['0.5Hz', '1.0Hz', '2.0Hz', '4.0Hz', '8.0Hz', '10Hz', '20Hz', '40Hz', '80Hz', '160Hz', '320Hz']
        # frequency on ch1
        self.ch1_freqUpButton.clicked.connect(self.ChangeFrequency)
        self.ch1_freqDwnButton.clicked.connect(self.ChangeFrequency)

        # intensity options
        self.ch1_pwr_index = 0
        self.pwr_list = ['25uA', '50uA', '100uA', '200uA', '400uA', '600uA']
        # power on ch1
        self.ch1_pwrUpButton.clicked.connect(self.ChangePower)
        self.ch1_pwrDwnButton.clicked.connect(self.ChangePower)

        # others on ch1
        self.ch1_startButton.clicked.connect(self.StartCh1)
        self.ch1_enableButton.clicked.connect(self.EnableCh1)
        
        # self.bt_min.clicked.connect(self.control_minimized)
        # self.bt_med.clicked.connect(self.control_normal)
        # self.bt_max.clicked.connect(self.control_maximized)

        # frame shadows
        # self.shadow_frame(self.stackedWidget)
        # self.shadow_frame(self.upperFrame)
        # self.shadow_frame(self.bt_1)
        # self.shadow_frame(self.bt_2)
        # self.shadow_frame(self.bt_3)
        # self.shadow_frame(self.bt_4)

        # page selection
        # self.bt_1.clicked.connect(self.control_page_one)
        # self.bt_2.clicked.connect(self.control_page_two)
        # self.bt_3.clicked.connect(self.control_page_three)
        # self.bt_4.clicked.connect(self.control_page_four)

        ## Distro Information
        self.t = Treatment()
        self.distro = self.GetDistroName(True)
        # print ('distro: ' + self.distro + ' distro len: ' + str(len(self.distro)))
        print (self.distro)        
        
        self.t.SetCurrentVersion(CURRENT_VERSION)
        self.t.SetCurrentSystem(self.distro)
        
        ## PARA SLACKWARE
        if self.t.GetCurrentSystem() == 'Slackware ':
            # self.s = SerialComm(self.MyObjCallback, '/dev/ttyACM0')
            self.s = SerialComm(self.MyObjCallback, '/dev/ttyUSB0')
        ## PARA RASPBERRY
        elif self.t.GetCurrentSystem() == 'debian':
            self.s = SerialComm(self.MyObjCallback, '/dev/serial0')
        
        

    def move_menu (self):
        width = self.lateralMenu.width()
        normal = 0
        if width == 0:
            extender = 450
            self.bt_menu_open.hide()
            self.bt_menu_close.show()
        else:
            extender = normal
            self.bt_menu_open.show()
            self.bt_menu_close.hide()

        # self.animation = QPropertyAnimation(self.lateralMenu, b"maximumWidth")
        self.animation = QPropertyAnimation(self.lateralMenu, b"minimumWidth")        
        self.animation.setStartValue(width)
        self.animation.setEndValue(extender)
        self.animation.setDuration(500)
        # self.animation.setEasingCurve(QEasingCurve.OutInBack)    #InQuad, InOutQuad, InCubic, InOutExpo
        self.animation.start()

        
    def shadow_frame (self, frame):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(8)
        shadow.setYOffset(8)
        shadow.setColor(QColor(20, 200, 255, 255))
        frame.setGraphicsEffect(shadow)


    def control_minimized (self):
        self.showMinimized()


    def control_normal (self):
        self.showNormal()
        self.bt_med.hide()
        self.bt_max.show()


    def control_maximized (self):
        self.showMaximized()
        self.bt_med.show()
        self.bt_max.hide()


    def control_page_one (self):
        self.stackedWidget.setCurrentWidget(self.page_one)
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
        

    def page_animation (self):
        width = self.stackedWidget.width()
        x1 = self.framePages.rect().right()
        normal = 100
        if width == 100:
            extender = x1
        else:
            extender = normal

        self.animation2 = QPropertyAnimation(self.stackedWidget, b'maximumWidth')
        self.animation2.setStartValue(width)
        self.animation2.setEndValue(extender)
        self.animation2.setDuration(500)
        self.animation2.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation2.start()

        
    def GainUpDwn (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_gainUpButton':
            if self.gain < 100:
                self.gain += 1

        if sender.objectName() == 'ch1_gainDwnButton':
            if self.gain > 0:
                self.gain -= 1

        self.ch1_gainLabel.setText(str(self.gain))
        self.ch1_displayLabel.setText(str(self.gain))


    def ChangePolarity (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_posButton':
            self.ch1_posButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ch1_altButton.setStyleSheet('')
            self.ch1_negButton.setStyleSheet('')

        if sender.objectName() == 'ch1_altButton':
            self.ch1_posButton.setStyleSheet('')
            self.ch1_altButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            self.ch1_negButton.setStyleSheet('')

        if sender.objectName() == 'ch1_negButton':
            self.ch1_posButton.setStyleSheet('')
            self.ch1_altButton.setStyleSheet('')
            self.ch1_negButton.setStyleSheet('background-color: rgb(218, 218, 218);')
            

    def ChangeTimer (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_timerUpButton':
            if self.ch1_timer_index < 5:
                self.ch1_timer_index += 1

        if sender.objectName() == 'ch1_timerDwnButton':
            if self.ch1_timer_index > 0:
                self.ch1_timer_index -= 1

        self.ch1_timerLabel.setText(self.timer_list[self.ch1_timer_index])


    def ChangeFrequency (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_freqUpButton':
            if self.ch1_freq_index < 10:
                self.ch1_freq_index += 1

        if sender.objectName() == 'ch1_freqDwnButton':
            if self.ch1_freq_index > 0:
                self.ch1_freq_index -= 1

        self.ch1_freqLabel.setText(self.freq_list[self.ch1_freq_index])


    def ChangePower (self):
        sender = self.sender()
        
        if sender.objectName() == 'ch1_pwrUpButton':
            if self.ch1_pwr_index < 5:
                self.ch1_pwr_index += 1

        if sender.objectName() == 'ch1_pwrDwnButton':
            if self.ch1_pwr_index > 0:
                self.ch1_pwr_index -= 1

        self.ch1_pwrLabel.setText(self.pwr_list[self.ch1_pwr_index])


    def StartCh1 (self):
        pass

    def EnableCh1 (self):
        pass

    def GetDistroName (self, show=False):
        (distname, version, nid) = platform.linux_distribution(full_distribution_name=1)
        if show:
            os_text = "--" + distname + version + "-- "
            print("os: " + os_text)

        return distname

    def MyObjCallback (self, dataread):
        d = dataread.rstrip()
        self.rcv_signal.emit(d)
    
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())

    
