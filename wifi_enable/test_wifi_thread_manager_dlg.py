import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor


"""
        Test for WiFiTestDialog

"""

#Here import the UIs or the classes that got the UIs
from wifi_test_thread_cls import WifiTestDialog

####################
# Function Screens #
####################
def WiFiScreen ():
    a = WifiTestDialog()
    a.setModal(True)
    a.exec_()

    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
WiFiScreen()
sys.exit(app.exec_())


### End of File ###
