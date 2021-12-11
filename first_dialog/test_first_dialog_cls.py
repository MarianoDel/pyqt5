import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor


"""
        Test for FirstDialog

"""

#Here import the UIs or classes that got the UIs
from first_dialog_cls import FirstDialog

####################
# Function Screens #
####################
def TestScreen ():
    # a = FirstDialog('magnet', 'usa', 30)
    # a = FirstDialog('magnet', 'arg', 30)
    a = FirstDialog('stretcher', 'usa', 30)
    # a = FirstDialog('stretcher', 'arg', 30)
    
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
