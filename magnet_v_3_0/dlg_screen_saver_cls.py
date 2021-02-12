from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QMovie
from time import time
from threading import Timer
from datetime import datetime


#get the UI from here
from ui_screen_saver_dlg import Ui_ScreenSaverDialog


#################################################
# FirstDialog Class - to get the system running #
#################################################
class ScreenSaverDialog(QDialog):

    # signal to update in 10 second
    ten_seconds_signal = pyqtSignal()

    def __init__(self):
        super(ScreenSaverDialog, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_ScreenSaverDialog()
        self.ui.setupUi(self)

        # Setup signals
        self.ui.doneButton.clicked.connect(self.accept)

        self.ui.doneButton.setStyleSheet("background-color: rgba(255, 255, 255, 0); \
                                          border: 0px");

        self.which_movie = 'RK'
        self.movie = QMovie(':/screen_saver/resources/Rk69.gif')
        self.ui.gifLabel.setMovie(self.movie)
        self.movie.start()
        
        # to start 10 seconds timer
        self.t10seg = QTimer()
        self.t10seg.timeout.connect(self.TimerTenSecs)
        self.t10seg.start(10000)

        #SIGNALS
        # connect the timer signal to the Update
        self.ten_seconds_signal.connect(self.UpdateTenSecs)


        """ QTimer callback emit a signal to not upset the timer interval """
    def TimerTenSecs(self):
        self.ten_seconds_signal.emit()


    def UpdateTenSecs (self):
        # do a UI update if its necessary
        if self.which_movie == 'RK':
            self.movie = QMovie(':/screen_saver/resources/UIBJ.gif')
            self.ui.gifLabel.setMovie(self.movie)
            self.movie.start()

            self.which_movie = 'UIBJ'
        elif self.which_movie == 'UIBJ':
            self.movie = QMovie(':/screen_saver/resources/1LFE.gif')
            self.ui.gifLabel.setMovie(self.movie)
            self.movie.start()

            self.which_movie = '1LFE'
        elif self.which_movie == '1LFE':
            self.movie = QMovie(':/screen_saver/resources/Rk69.gif')
            self.ui.gifLabel.setMovie(self.movie)
            self.movie.start()

            self.which_movie = 'RK'


        


        
### end of file ###
