from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from time import time
from threading import Timer
from datetime import datetime


# get the UI from here
from first_dialog_ui import Ui_FirstDialog
# get Dialog classes from here
from screen_saver_cls import ScreenSaverDialog

# background setting on ui
# QDialog {
# background-image: url(:/background/resources/Pantalla_00.png);
# }
#################################################
# FirstDialog Class - to get the system running #
#################################################
class FirstDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()

    def __init__(self, localization, screen_saver_timer):
        super(FirstDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_FirstDialog()
        self.ui.setupUi(self)

        # self.program_type = program_type
        self.localization = localization
        self.screen_saver_timeout = screen_saver_timer
        self.ended_label = False
        
        # get the close event
        self.ui.doneButton.clicked.connect(self.accept)

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # to start 1 second timer
        self.t1seg = QTimer()
        self.t1seg.timeout.connect(self.TimerOneSec)
        self.t1seg.start(1000)

        #SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)

        # screen saver timer activation
        self.screensaver_timer = self.screen_saver_timeout

        
    def UpdateDateTime(self, new_date_time):
        date_str = ""
        if self.localization == 'usa':
            date_str = new_date_time.strftime("%m/%d/%Y - %H:%M")
        elif self.localization == 'arg':
            date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")

        self.ui.date_timeLabel.setText(date_str)


        """ QTimer callback emit a signal to not upset the timer interval """
    def TimerOneSec(self):
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)

        if self.ended_label == True:
            self.ended_label = False
            self.ui.doneButton.setText('')
        else:            
            self.ended_label = True
            self.ui.doneButton.setText('Tap to continue')

        # check for screensaver activation
        if self.screensaver_timer > 0:
            self.screensaver_timer -= 1
        else:
            self.ScreenSaverDialogScreen()
            
        


    ## ScreenSaver
    def ScreenSaverDialogScreen (self):
        a = ScreenSaverDialog()
        a.setModal(True)
        a.exec_()

        self.ScreenSaverKick()

    def ScreenSaverKick (self):
        self.screensaver_timer = self.screen_saver_timeout





        
### end of file ###
