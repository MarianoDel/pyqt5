import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor


"""
        Test for ScreenSaverDialog

"""

#Here import the UIs or classes that got the UIs
from screen_saver_cls import ScreenSaverDialog

####################
# Function Screens #
####################
def TestScreen ():
    a = ScreenSaverDialog()
    a.setModal(True)
    a.exec_()

    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
TestScreen()
sys.exit(app.exec_())


### End of File ###
