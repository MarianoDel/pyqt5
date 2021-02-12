# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magnet_screen_saver_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScreenSaverDialog(object):
    def setupUi(self, ScreenSaverDialog):
        ScreenSaverDialog.setObjectName("ScreenSaverDialog")
        ScreenSaverDialog.resize(1280, 800)
        ScreenSaverDialog.setStyleSheet("")
        self.gifLabel = QtWidgets.QLabel(ScreenSaverDialog)
        self.gifLabel.setGeometry(QtCore.QRect(0, -1, 1280, 800))
        self.gifLabel.setStyleSheet("background-image: url(:/screen_saver/resources/Rk69.gif);")
        self.gifLabel.setText("")
        self.gifLabel.setPixmap(QtGui.QPixmap(":/screen_saver/Rk69.gif"))
        self.gifLabel.setObjectName("gifLabel")
        self.doneButton = QtWidgets.QPushButton(ScreenSaverDialog)
        self.doneButton.setGeometry(QtCore.QRect(100, 81, 1091, 631))
        self.doneButton.setText("")
        self.doneButton.setObjectName("doneButton")

        self.retranslateUi(ScreenSaverDialog)
        QtCore.QMetaObject.connectSlotsByName(ScreenSaverDialog)

    def retranslateUi(self, ScreenSaverDialog):
        _translate = QtCore.QCoreApplication.translate
        ScreenSaverDialog.setWindowTitle(_translate("ScreenSaverDialog", "Dialog"))

import magnet3_res_rc
