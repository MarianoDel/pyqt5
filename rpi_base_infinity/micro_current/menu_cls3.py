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

    def __init__(self, serialport, parent=None):
        super(MenuWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent
        self.datetime_now = datetime.today()

        # connect buttons
        self.ui.conf3Button.clicked.connect(self.close)
        self.ui.audioSlider.valueChanged.connect(self.AudioVolume)
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
        
        # volume setup
        self.volume = self.parent.actual_volume_str
        self.ui.volumeLabel.setText(self.volume + '%')
        vol_int = int((int(self.volume))/10)
        self.ui.audioSlider.setValue(vol_int)

        # populate date and time
        self.ui.monthLabel.setText(self.datetime_now.strftime("%m"))
        self.ui.dayLabel.setText(self.datetime_now.strftime("%d"))
        self.ui.yearLabel.setText(self.datetime_now.strftime("%y"))        
        self.ui.hourLabel.setText(self.datetime_now.strftime("%H"))
        self.ui.minuteLabel.setText(self.datetime_now.strftime("%M"))
        

    def AudioVolume (self):
        current_value = self.ui.audioSlider.value()
        self.ui.volumeLabel.setText(str(current_value * 10) + '%')
        self.volume = str(current_value * 10)


    def closeEvent (self, event):
        print("close")
        self.parent.cbMenu(self.volume)


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


