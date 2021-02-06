import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor
from time import sleep, time
# from datetime import datetime


#Here import the UIs or the classes that got the UIs
from dlg_screen_saver_cls import ScreenSaverDialog



"""
    Pruebas con seniales y eventos custom
    http://zetcode.com/gui/pyqt5/eventssignals/
"""

### GLOBALS FOR CONFIGURATION #########

### CUSTOM SIGNALS ####################

        
####################################
# Different Screens Calls are here #
####################################
    ###############
    # Screens     #
    ###############
def ScreenSaverScreen ():
    a = ScreenSaverDialog()
    a.setModal(True)
    a.exec_()

    sys.exit()

        

### End of Dialog ###

############
# Main App #
############
app = QApplication(sys.argv)
ScreenSaverScreen()
sys.exit(app.exec_())


### End of File ###
