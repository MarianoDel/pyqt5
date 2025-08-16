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
from ui_menu3 import Ui_MenuWindow


class MenuWindow (QMainWindow):

    #SIGNALS
    # one_second_signal = pyqtSignal()

    def __init__(self, serialport, audio_selected, parent=None):
        super(MenuWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent
        self.audio_selected = audio_selected
        self.datetime_now = datetime.today()

        # volume buttons style
        self.style_vol_act = """color: rgb(255,255,255);
                                background-color: rgb(173, 163, 170);
                                border-radius: 15;
                                border: 2px rgb(173, 163, 170);"""
        self.style_vol_deact = """color: rgb(148,138,146);
                                  border-radius: 15;
                                  border: 2px solid rgb(148, 138, 146);"""

        self.style_conf_deact = """background-color: rgba(81, 70, 75, 150);
                                   color: rgb(255, 255, 255);
                                   border-radius: 25px"""

        self.style_conf_act = """background-color: rgba(148, 138, 146, 150);
                                 color: rgb(255, 255, 255);
                                 border-radius: 25px"""

        # connect buttons
        self.ui.done_Button.clicked.connect(self.close)
        self.ui.config1_Button.clicked.connect(self.AudioConfig)
        self.ui.config2_Button.clicked.connect(self.DateTimeConfig)

        self.ui.audio_full_Button.clicked.connect(self.AudioVolume)
        self.ui.audio_high_Button.clicked.connect(self.AudioVolume)
        self.ui.audio_half_Button.clicked.connect(self.AudioVolume)
        self.ui.audio_low_Button.clicked.connect(self.AudioVolume)
        self.ui.audio_off_Button.clicked.connect(self.AudioVolume)
        self.audio_buttons_list = [self.ui.audio_full_Button, self.ui.audio_high_Button, self.ui.audio_half_Button, self.ui.audio_low_Button, self.ui.audio_off_Button]
        self.audio_buttons_index_list = ['full', 'high', 'half', 'low', 'off']        
        
        self.ui.month_UpButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.day_UpButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.year_UpButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.hour_UpButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.minute_UpButton.clicked.connect(self.DateTimeUpDwn)

        self.ui.month_DwnButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.day_DwnButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.year_DwnButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.hour_DwnButton.clicked.connect(self.DateTimeUpDwn)
        self.ui.minute_DwnButton.clicked.connect(self.DateTimeUpDwn)
        
        self.ui.datetimeButton.clicked.connect(self.DateTimeUpdate)

        # populate audio buttons
        self.AudioVolume_Select (self.audio_selected)
        self.ui.config1_Button.setStyleSheet(self.style_conf_act)
        
        # populate date and time
        self.ui.monthLabel.setText(self.datetime_now.strftime("%m"))
        self.ui.dayLabel.setText(self.datetime_now.strftime("%d"))
        self.ui.yearLabel.setText(self.datetime_now.strftime("%y"))        
        self.ui.hourLabel.setText(self.datetime_now.strftime("%H"))
        self.ui.minuteLabel.setText(self.datetime_now.strftime("%M"))
        self.ui.config2_Button.setStyleSheet(self.style_conf_deact)
        self.DateTimeHide()
        

    def AudioVolume (self):
        sender = self.sender()

        # full, high, half, low, off
        obj_list = sender.objectName().split('_')
        func = obj_list[1]
        self.audio_selected = func
        self.AudioVolume_Select (func)


    def AudioVolume_Select (self, audio_selected):
        for x in range(len(self.audio_buttons_list)):
            if audio_selected == self.audio_buttons_index_list[x]:
                self.audio_buttons_list[x].setStyleSheet(self.style_vol_act)
            else:
                self.audio_buttons_list[x].setStyleSheet(self.style_vol_deact)


    def closeEvent (self, event):
        print("close")
        self.parent.cbMenu(self.audio_selected)


    def AudioConfig (self):
        self.AudioShow()
        self.AudioVolume_Select (self.audio_selected)
        self.ui.config1_Button.setStyleSheet(self.style_conf_act)
        self.ui.config2_Button.setStyleSheet(self.style_conf_deact)        
        self.DateTimeHide()


    def DateTimeConfig (self):
        self.DateTimeShow()
        self.ui.config1_Button.setStyleSheet(self.style_conf_deact)
        self.ui.config2_Button.setStyleSheet(self.style_conf_act)
        self.AudioHide()
        
        
    def AudioShow (self):
        self.ui.audioLabel.show()
        
        for x in range(len(self.audio_buttons_list)):
            self.audio_buttons_list[x].show()


    def AudioHide (self):
        self.ui.audioLabel.hide()
        
        for x in range(len(self.audio_buttons_list)):
            self.audio_buttons_list[x].hide()
            
        
    def DateTimeShow (self):
        self.ui.monthLabel.show()
        self.ui.dayLabel.show()
        self.ui.yearLabel.show()
        self.ui.hourLabel.show()
        self.ui.minuteLabel.show()

        self.ui.month_UpButton.show()
        self.ui.day_UpButton.show()
        self.ui.year_UpButton.show()
        self.ui.hour_UpButton.show()
        self.ui.minute_UpButton.show()

        self.ui.month_DwnButton.show()
        self.ui.day_DwnButton.show()
        self.ui.year_DwnButton.show()
        self.ui.hour_DwnButton.show()
        self.ui.minute_DwnButton.show()
        
        self.ui.datetimeButton.show()

        self.ui.date0Label.show()
        self.ui.date1Label.show()
        self.ui.date2Label.show()
        self.ui.date3Label.show()        

        self.ui.time0Label.show()
        self.ui.time1Label.show()
        self.ui.time2Label.show()


    def DateTimeHide (self):
        self.ui.monthLabel.hide()
        self.ui.dayLabel.hide()
        self.ui.yearLabel.hide()
        self.ui.hourLabel.hide()
        self.ui.minuteLabel.hide()

        self.ui.month_UpButton.hide()
        self.ui.day_UpButton.hide()
        self.ui.year_UpButton.hide()
        self.ui.hour_UpButton.hide()
        self.ui.minute_UpButton.hide()

        self.ui.month_DwnButton.hide()
        self.ui.day_DwnButton.hide()
        self.ui.year_DwnButton.hide()
        self.ui.hour_DwnButton.hide()
        self.ui.minute_DwnButton.hide()
        
        self.ui.datetimeButton.hide()

        self.ui.date0Label.hide()
        self.ui.date1Label.hide()
        self.ui.date2Label.hide()
        self.ui.date3Label.hide()        

        self.ui.time0Label.hide()
        self.ui.time1Label.hide()
        self.ui.time2Label.hide()
        
        
    def DateTimeUpDwn (self):
        sender = self.sender()

        # always ch1
        obj_list = sender.objectName().split('_')
        name = obj_list[0]
        func = obj_list[1]

        if name == 'day':
            up = 31
            dwn = 1
            func_ref = self.ui.dayLabel
            value = int (self.ui.dayLabel.text())

        if name == 'month':
            up = 12
            dwn = 1
            func_ref = self.ui.monthLabel
            value = int (self.ui.monthLabel.text())

        if name == 'year':
            up = 99
            dwn = 0
            func_ref = self.ui.yearLabel
            value = int (self.ui.yearLabel.text())

        if name == 'hour':
            up = 23
            dwn = 0
            func_ref = self.ui.hourLabel
            value = int (self.ui.hourLabel.text())

        if name == 'minute':
            up = 59
            dwn = 0
            func_ref = self.ui.minuteLabel
            value = int (self.ui.minuteLabel.text())
            
        if func == 'UpButton':
            if value < up:
                value += 1

        if func == 'DwnButton':
            if value > dwn:
                value -= 1

        func_ref.setText(f'{value:02d}')


    def DateTimeUpdate (self):
        if self.ui.datetimeButton.text() == 'Done':
            self.close()
            return
            
        self.ui.datetimeButton.setText('Working...')
        
        day = self.ui.dayLabel.text()
        month = self.ui.monthLabel.text()
        year = self.ui.yearLabel.text()
        hour = self.ui.hourLabel.text()
        minute = self.ui.minuteLabel.text()
        
        # myCmd1 = f"sudo date -s {day}/{month}/20{year}"
        myCmd1 = f"sudo date -s {month}/{day}/20{year}"    # us format      
        myCmd2 = f"sudo date -s {hour}:{minute}:00"
        myCmd3 = "sudo hwclock -w"    # save into hwclck
        
        print ("")
        print (f"  distro: {self.parent.distro}")
        print ("")

        # with open ("/home/pi/microc.log", "w") as file:
        #     file.write(f"distro: {self.parent.distro}")

        if self.parent.distro == 'Slackware':
            print(myCmd1)
            print(myCmd2)
            print(myCmd3)
            self.ui.datetimeButton.setText('Done')

        elif self.parent.distro == 'debian' or \
             self.parent.distro == 'Raspbian GNU/Linux':
            self.ui.datetimeButton.setText('Done')
            os.system(myCmd1)
            os.system(myCmd2)            
            os.system(myCmd3)


