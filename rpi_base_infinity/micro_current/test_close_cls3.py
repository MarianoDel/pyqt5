import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject

"""
        Test for Main Dialog

"""

#Here import the UIs or classes that got the UIs
from close_cls3 import CloseWindow


    
####################
# Function Screens #
####################
def TestScreen ():

    a = CloseWindow()
    a.show()
    sys.exit(app.exec_())



### End of Dialog ###
############
# Test App #
############
app = QApplication(sys.argv)
TestScreen()



### End of File ###
