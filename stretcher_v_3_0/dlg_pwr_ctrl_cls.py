from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject


#get the UI from here
from ui_pwr_ctrl_dlg import Ui_PowerControlDialog


##############################################################
# PowerControlDialog Class - to set the system power control #
##############################################################
class PowerControlDialog(QDialog):
    def __init__(self):
        super(PowerControlDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_PowerControlDialog()
        self.ui.setupUi(self)

        # get the close event and connect the other buttons
        self.ui.doneButton.clicked.connect(self.accept)
        self.ui.triangUpButton.clicked.connect(self.triangUpBtn)
        self.ui.triangDwnButton.clicked.connect(self.triangDwnBtn)
        self.ui.squareUpButton.clicked.connect(self.squareUpBtn)
        self.ui.squareDwnButton.clicked.connect(self.squareDwnBtn)
        self.ui.sinusUpButton.clicked.connect(self.sinusUpBtn)
        self.ui.sinusDwnButton.clicked.connect(self.sinusDwnBtn)

        ## this ones must be getted from config.txt file or passed as object arguments
        self.trianglimit = 100
        self.squarelimit = 100
        self.sinuslimit = 100
        self.peak = 3.6
        self.resistance065 = 42
        self.resistance080 = 21
        self.tempcoef065 = 2.2
        self.tempcoef080 = 1.8
        self.tempamb = 25
        

        ## first run
        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateTriang()
        self.UpdateSquare()
        self.UpdateSinus()
        

    def triangUpBtn (self):
        if self.trianglimit < 100:
            self.trianglimit += 1

        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.UpdateTriang()

    def triangDwnBtn (self):
        if self.trianglimit > 10:
            self.trianglimit -= 1

        self.ui.triangLimitLabel.setText(str(self.trianglimit) + "%")
        self.UpdateTriang()

    def squareUpBtn (self):
        if self.squarelimit < 100:
            self.squarelimit += 1

        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.UpdateSquare()

    def squareDwnBtn (self):
        if self.squarelimit > 10:
            self.squarelimit -= 1

        self.ui.squareLimitLabel.setText(str(self.squarelimit) + "%")
        self.UpdateSquare()

    def sinusUpBtn (self):
        if self.sinuslimit < 100:
            self.sinuslimit += 1

        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateSinus()

    def sinusDwnBtn (self):
        if self.sinuslimit > 10:
            self.sinuslimit -= 1

        self.ui.sinusLimitLabel.setText(str(self.sinuslimit) + "%")
        self.UpdateSinus()        


    def UpdateTriang (self):
        i = 0.01 * self.peak * self.trianglimit
        i = i * 0.4083
        self.ui.triangCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080        
        self.ui.triangPwr065Label.setText("{0:.1f}".format(p065))
        self.ui.triangPwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.triangTemp065Label.setText(str(int(t065)))
        self.ui.triangTemp080Label.setText(str(int(t080)))
        

    def UpdateSquare (self):
        i = 0.01 * self.peak * self.squarelimit
        i = i * 0.7071
        self.ui.squareCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080        
        self.ui.squarePwr065Label.setText("{0:.1f}".format(p065))
        self.ui.squarePwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.squareTemp065Label.setText(str(int(t065)))
        self.ui.squareTemp080Label.setText(str(int(t080)))
        

    def UpdateSinus (self):
        i = 0.01 * self.peak * self.sinuslimit
        i = i * 0.5
        self.ui.sinusCurrLabel.setText("{0:.3f}".format(i))

        p065 = i * i * self.resistance065
        p080 = i * i * self.resistance080
        self.ui.sinusPwr065Label.setText("{0:.1f}".format(p065))
        self.ui.sinusPwr080Label.setText("{0:.1f}".format(p080))

        t065 = p065 * self.tempcoef065 + self.tempamb 
        t080 = p080 * self.tempcoef080 + self.tempamb
        self.ui.sinusTemp065Label.setText(str(int(t065)))
        self.ui.sinusTemp080Label.setText(str(int(t080)))
        
        
        
    # def DwnBtn (self, event=None):
    #     day = int(self.ui.dayButton.text())
    #     month = int(self.ui.monthButton.text())
    #     year = int(self.ui.yearButton.text())
    #     hour = int(self.ui.hourButton.text())
    #     minute = int(self.ui.minuteButton.text())
        
    #     if self.new_focus == "DAY":
    #         if day > 1:
    #             day -= 1

    #     if self.new_focus == "MONTH":
    #         if month > 1:
    #             month -= 1

    #     if self.new_focus == "YEAR":
    #         if year > 0:
    #             year -= 1
                
    #     if self.new_focus == "HOUR":
    #         if hour > 0:
    #             hour -= 1

    #     if self.new_focus == "MINUTE":
    #         if minute > 0:
    #             minute -= 1

    #     self.UpdateNumbers(day, month, year, hour, minute)
        

    # def ChangeFocusDay (self):
    #     self.ClearFocus()
    #     self.new_focus = "DAY"
    #     self.ui.dayButton.setStyleSheet("background-color: rgb(170, 170, 255);\
    #                                      border: 0px;")


    # def ChangeFocusMonth (self):
    #     self.ClearFocus()
    #     self.new_focus = "MONTH"
    #     self.ui.monthButton.setStyleSheet("background-color: rgb(170, 170, 255);\
    #                                       border: 0px;")


    # def ChangeFocusYear (self):
    #     self.ClearFocus()
    #     self.new_focus = "YEAR"
    #     self.ui.yearButton.setStyleSheet("background-color: rgb(170, 170, 255);\
    #                                       border: 0px;")


    # def ChangeFocusHour (self):
    #     self.ClearFocus()
    #     self.new_focus = "HOUR"
    #     self.ui.hourButton.setStyleSheet("background-color: rgb(170, 170, 255);\
    #                                       border: 0px;")


    # def ChangeFocusMinute (self):
    #     self.ClearFocus()
    #     self.new_focus = "MINUTE"
    #     self.ui.minuteButton.setStyleSheet("background-color: rgb(170, 170, 255);\
    #                                         border: 0px;")

        
    # def ClearFocus (self):
    #     self.ui.dayButton.setStyleSheet("background-color: rgb(255, 170, 255);\
    #                                      border: 0px;")
    #     self.ui.monthButton.setStyleSheet("background-color: rgb(255, 170, 255);\
    #                                       border: 0px;")
    #     self.ui.yearButton.setStyleSheet("background-color: rgb(255, 170, 255);\
    #                                       border: 0px;")
    #     self.ui.hourButton.setStyleSheet("background-color: rgb(255, 170, 255);\
    #                                       border: 0px;")
    #     self.ui.minuteButton.setStyleSheet("background-color: rgb(255, 170, 255);\
    #                                         border: 0px;")


    # def UpdateNumbers (self, d, m, y, h, mm):
    #     self.ui.dayButton.setText("{0:02d}".format(d))
    #     self.ui.monthButton.setText("{0:02d}".format(m))
    #     self.ui.yearButton.setText("{0:02d}".format(y))
    #     self.ui.hourButton.setText("{0:02d}".format(h))
    #     self.ui.minuteButton.setText("{0:02d}".format(mm))
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
