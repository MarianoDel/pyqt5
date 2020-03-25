from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from time import time
from threading import Timer
from datetime import datetime


#get the UI from here
from ui_first_dlg import Ui_FirstDialog


#################################################
# FirstDialog Class - to get the system running #
#################################################
class FirstDialog(QDialog):

    #SIGNALS
    # signal to update in 1 second
    one_second_signal = pyqtSignal()

    def __init__(self):
        super(FirstDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_FirstDialog()
        self.ui.setupUi(self)

        # get the close event
        self.ui.doneButton.clicked.connect(self.accept)

        ### to carry on with date-time
        date_now = datetime.today()
        self.minutes_last = date_now.minute
        self.UpdateDateTime(date_now)

        # to start 1 second timer
        self.next_call = time()
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()

        #SIGNALS
        # connect the timer signal to the Update
        self.one_second_signal.connect(self.UpdateOneSec)

        
    def UpdateDateTime(self, new_date_time):
        date_str = new_date_time.strftime("%d/%m/%Y - %H:%M")
        self.ui.date_timeLabel.setText(date_str)


        """ This runs in other thread is a better idea to use a signal to change the UI """
    def TimerOneSec(self, lapse):
        self.next_call = self.next_call + 1        
        self.t1seg = Timer(self.next_call - time(), self.TimerOneSec, [1]).start()
        self.one_second_signal.emit()


    def UpdateOneSec (self):
        # do a UI update if its necessary
        date_now = datetime.today()
        if date_now.minute != self.minutes_last:
            self.minutes_last = date_now.minute
            self.UpdateDateTime(date_now)            

        
### end of file ###
