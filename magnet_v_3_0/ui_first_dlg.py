# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magnet_first_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstDialog(object):
    def setupUi(self, FirstDialog):
        FirstDialog.setObjectName("FirstDialog")
        FirstDialog.resize(1280, 800)
        FirstDialog.setStyleSheet("QDialog {\n"
"background-image: url(:/background/resources/background_magnet_01.png);\n"
"}")
        self.doneButton = QtWidgets.QPushButton(FirstDialog)
        self.doneButton.setGeometry(QtCore.QRect(330, 510, 621, 121))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.doneButton.setFont(font)
        self.doneButton.setStyleSheet("background-color: rgb(230, 245, 253);\n"
"border: 0px;\n"
"color: rgb(55, 52, 53);")
        self.doneButton.setObjectName("doneButton")
        self.date_timeLabel = QtWidgets.QLabel(FirstDialog)
        self.date_timeLabel.setGeometry(QtCore.QRect(910, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.date_timeLabel.setFont(font)
        self.date_timeLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.date_timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.date_timeLabel.setObjectName("date_timeLabel")

        self.retranslateUi(FirstDialog)
        QtCore.QMetaObject.connectSlotsByName(FirstDialog)

    def retranslateUi(self, FirstDialog):
        _translate = QtCore.QCoreApplication.translate
        FirstDialog.setWindowTitle(_translate("FirstDialog", "Dialog"))
        self.doneButton.setText(_translate("FirstDialog", "Tap to continue"))
        self.date_timeLabel.setText(_translate("FirstDialog", "19/03/2020 - 17:45"))

import magnet3_res_rc
