import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor


"""
        Test for KeyboardDialog

"""

#Here import the UIs or the classes that got the UIs
from wifi_keyboard_cls import KeyboardDialog

####################
# Function Screens #
####################
def KeyboardScreen ():
    a = KeyboardDialog("config this sheet", "config")
    a.setModal(True)
    a.exec_()
    print(a.answer)

    sys.exit(0)


### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
KeyboardScreen()
sys.exit(app.exec_())


### End of File ###
