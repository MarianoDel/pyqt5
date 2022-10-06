import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime


"""
        Test for RtcDialog

"""

#Here import the UIs or classes that got the UIs
from rtc_cls import RtcDialog

####################
# Function Screens #
####################
def TestScreen ():
    localization = 'usa'
    # localization = 'arg'    
    date_now = datetime.today()
    a = RtcDialog(localization, date_now)
    
    a.setModal(True)
    a.exec_()

    if localization == 'usa':
        new_month = a.ui.dayButton.text()
        new_day = a.ui.monthButton.text()
    elif localization == 'arg':
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
    
    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
