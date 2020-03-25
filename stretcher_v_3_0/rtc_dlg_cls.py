from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from time import time
from threading import Timer
from datetime import datetime


#get the UI from here
from ui_stretcher_rtc import Ui_RtcDialog

## what to do with the info
USE_RTC_STRING_FOR_PRINT = 0
USE_RTC_STRING_FOR_COMMAND = 1

##################################################
# RtcDialog Class - to set the RTC on the system #
##################################################
class RtcDialog(QDialog):
    def __init__(self):
        super(RtcDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_RtcDialog()
        self.ui.setupUi(self)

        # get the close event
        self.ui.doneButton.clicked.connect(self.accept)

        self.ui.UpButton.clicked.connect(self.UpBtn)
        self.ui.DwnButton.clicked.connect(self.DwnBtn)

        self.ui.dayButton.clicked.connect(self.ChangeFocusDay)
        self.ui.monthButton.clicked.connect(self.ChangeFocusMonth)
        self.ui.yearButton.clicked.connect(self.ChangeFocusYear)
        self.ui.hourButton.clicked.connect(self.ChangeFocusHour)
        self.ui.minuteButton.clicked.connect(self.ChangeFocusMinute)
        self.new_focus = "DAY"


    def UpBtn (self, event=None):
        day = int(self.ui.dayButton.text())
        month = int(self.ui.monthButton.text())
        year = int(self.ui.yearButton.text())
        hour = int(self.ui.hourButton.text())
        minute = int(self.ui.minuteButton.text())

        if self.new_focus == "DAY":
            if day < 31:
                day += 1

        if self.new_focus == "MONTH":
            if month < 12:
                month += 1

        if self.new_focus == "YEAR":
            if year < 99:
                year += 1
                
        if self.new_focus == "HOUR":
            if hour < 23:
                hour += 1

        if self.new_focus == "MINUTE":
            if minute < 59:
                minute += 1
                
        self.UpdateNumbers(day, month, year, hour, minute)

        
    def DwnBtn (self, event=None):
        day = int(self.ui.dayButton.text())
        month = int(self.ui.monthButton.text())
        year = int(self.ui.yearButton.text())
        hour = int(self.ui.hourButton.text())
        minute = int(self.ui.minuteButton.text())
        
        if self.new_focus == "DAY":
            if day > 1:
                day -= 1

        if self.new_focus == "MONTH":
            if month > 1:
                month -= 1

        if self.new_focus == "YEAR":
            if year > 0:
                year -= 1
                
        if self.new_focus == "HOUR":
            if hour > 0:
                hour -= 1

        if self.new_focus == "MINUTE":
            if minute > 0:
                minute -= 1

        self.UpdateNumbers(day, month, year, hour, minute)
        

    def ChangeFocusDay (self):
        self.ClearFocus()
        self.new_focus = "DAY"
        self.ui.dayButton.setStyleSheet("background-color: rgb(170, 170, 255);\
                                         border: 0px;")


    def ChangeFocusMonth (self):
        self.ClearFocus()
        self.new_focus = "MONTH"
        self.ui.monthButton.setStyleSheet("background-color: rgb(170, 170, 255);\
                                          border: 0px;")


    def ChangeFocusYear (self):
        self.ClearFocus()
        self.new_focus = "YEAR"
        self.ui.yearButton.setStyleSheet("background-color: rgb(170, 170, 255);\
                                          border: 0px;")


    def ChangeFocusHour (self):
        self.ClearFocus()
        self.new_focus = "HOUR"
        self.ui.hourButton.setStyleSheet("background-color: rgb(170, 170, 255);\
                                          border: 0px;")


    def ChangeFocusMinute (self):
        self.ClearFocus()
        self.new_focus = "MINUTE"
        self.ui.minuteButton.setStyleSheet("background-color: rgb(170, 170, 255);\
                                            border: 0px;")

        
    def ClearFocus (self):
        self.ui.dayButton.setStyleSheet("background-color: rgb(255, 170, 255);\
                                         border: 0px;")
        self.ui.monthButton.setStyleSheet("background-color: rgb(255, 170, 255);\
                                          border: 0px;")
        self.ui.yearButton.setStyleSheet("background-color: rgb(255, 170, 255);\
                                          border: 0px;")
        self.ui.hourButton.setStyleSheet("background-color: rgb(255, 170, 255);\
                                          border: 0px;")
        self.ui.minuteButton.setStyleSheet("background-color: rgb(255, 170, 255);\
                                            border: 0px;")


    def UpdateNumbers (self, d, m, y, h, mm):
        self.ui.dayButton.setText("{0:02d}".format(d))
        self.ui.monthButton.setText("{0:02d}".format(m))
        self.ui.yearButton.setText("{0:02d}".format(y))
        self.ui.hourButton.setText("{0:02d}".format(h))
        self.ui.minuteButton.setText("{0:02d}".format(mm))
        # self.ui.dayButton.setText(f"{d:02d}")
        # self.ui.monthButton.setText(f"{m:02d}")
        # self.ui.yearButton.setText(f"{y:02d}")
        # self.ui.hourButton.setText(f"{h:02d}")
        # self.ui.minuteButton.setText(f"{mm:02d}")
        



    #     ### to carry on with date-time
    #     date_now = datetime.today()
    #     self.minutes_last = date_now.minute
    #     self.UpdateDateTime(date_now)

    #     # to start 1 second timer
    #     self.next_call = time()
    #     self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()


    # def UpdateDateTime(self, new_date_time):
    #     date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
    #     self.ui.date_timeLabel.setText(date_str)

        
    # def TimerOneSec(self, lapse):
    #     self.next_call = self.next_call + 1
    #     self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

    #     # do a UI update if its necessary
    #     date_now = datetime.today()
    #     if date_now.minute != self.minutes_last:
    #         self.minutes_last = date_now.minute
    #         self.UpdateDateTime(date_now)            

        
### end of file ###
