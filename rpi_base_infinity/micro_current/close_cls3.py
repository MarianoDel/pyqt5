# use python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QTimer
from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtCore, QtWidgets


#imported uis
from ui_close3 import Ui_CloseWindow


class CloseWindow (QMainWindow):

    #SIGNALS
    # one_second_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(CloseWindow, self).__init__()

        # Setup the user interface from Designer.
        self.ui = Ui_CloseWindow()
        self.ui.setupUi(self)

        # get parent info
        self.parent = parent

        # move the window
        self.move(510, 240)

        # connect buttons
        self.ui.doneButton.clicked.connect(self.close)

        # get the close timer running
        self.close5seg = QTimer()
        self.close5seg.timeout.connect(self.close)
        self.close5seg.start(5000)

        # change style of text
        # self.style_txt_msg = """color: rgb(255, 255, 255);
        #                         font: 12 36pt "TT Norms ExtraLight";
        #                         font-feature-settings: "dlig" 0;"""
        # self.ui.mainLabel.setStyleSheet(self.style_txt_msg)
        
