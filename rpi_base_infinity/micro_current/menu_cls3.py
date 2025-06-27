# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtCore, QtWidgets
import os
# import threading

#imported uis
from ui_menu3 import Ui_MenuWindow


class MenuWindow (QMainWindow):

    #SIGNALS
    # one_second_signal = pyqtSignal()

    def __init__(self, serialport, parent=None):
        super(MenuWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        # get parent info
        self.s = serialport
        self.parent = parent

        # connect buttons
        self.ui.conf3Button.clicked.connect(self.close)
        self.ui.audioSlider.valueChanged.connect(self.AudioVolume)
        
        self.volume = self.ui.volumeLabel.text()
        

    def AudioVolume (self):
        current_value = self.ui.audioSlider.value()
        self.ui.volumeLabel.setText(str(current_value) + '%')
        self.volume = self.ui.volumeLabel.text()


    def closeEvent (self, event):
        print("close")
        self.parent.cbMenu(self.volume)
