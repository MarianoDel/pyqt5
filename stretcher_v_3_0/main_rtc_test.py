import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor
from serialcomm import SerialComm
from treatment_class import Treatment
from stylesheet_class import ButtonStyles
from time import sleep, time
from datetime import datetime


#Here import the UIs or the classes that got the UIs
from dlg_rtc_cls import RtcDialog



"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### GLOBALS FOR CONFIGURATION #########
## OS where its run
RUNNING_ON_SLACKWARE = 0
RUNNING_ON_RASP = 1
## Date Time as used in
DATE_TIME_USA = 1
DATE_TIME_ARG = 0
## No call the first Dialog - code empty presentation page -
NO_CALL_FIRST_DLG = 0

## This Interface Software version
CURRENT_VERSION = "Stretcher_ver_3_1"

### CUSTOM SIGNALS ####################
#clase de la senial
class Communicate(QObject):
    closeApp = pyqtSignal()

        
####################################
# Different Screens Calls are here #
####################################
    ###############
    # Screens     #
    ###############
    ## RtcScreen
def RtcScreen ():
    a = RtcDialog()
    a.setModal(True)

    date_now = datetime.today()
    a.ui.dayButton.setText(date_now.strftime("%d"))
    a.ui.monthButton.setText(date_now.strftime("%m"))
    a.ui.yearButton.setText(date_now.strftime("%y"))

    a.ui.hourButton.setText(date_now.strftime("%H"))
    a.ui.minuteButton.setText(date_now.strftime("%M"))            

    a.exec_()
    new_day = a.ui.dayButton.text()
    new_month = a.ui.monthButton.text()
    new_year = a.ui.yearButton.text()
    new_hour = a.ui.hourButton.text()
    new_minute = a.ui.minuteButton.text()
    myCmd1 = "sudo date -s {1}/{0}/20{2}".format(new_day, new_month, new_year)
    myCmd2 = "sudo date -s {0}:{1}:00".format(new_hour, new_minute)
    myCmd3 = "sudo hwclock -w"        #guardo info del date en hwclock

    print(myCmd1)
    print(myCmd2)
    print(myCmd3)
    sys.exit()

        

### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
RtcScreen()
sys.exit(app.exec_())


### End of File ###
