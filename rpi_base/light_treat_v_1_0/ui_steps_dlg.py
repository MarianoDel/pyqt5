# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'light_steps_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StepsDialog(object):
    def setupUi(self, StepsDialog):
        StepsDialog.setObjectName("StepsDialog")
        StepsDialog.resize(656, 474)
        self.doneButton = QtWidgets.QPushButton(StepsDialog)
        self.doneButton.setGeometry(QtCore.QRect(20, 220, 611, 191))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.doneButton.setFont(font)
        self.doneButton.setObjectName("doneButton")
        self.label = QtWidgets.QLabel(StepsDialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 591, 126))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(StepsDialog)
        QtCore.QMetaObject.connectSlotsByName(StepsDialog)

    def retranslateUi(self, StepsDialog):
        _translate = QtCore.QCoreApplication.translate
        StepsDialog.setWindowTitle(_translate("StepsDialog", "Dialog"))
        self.doneButton.setText(_translate("StepsDialog", "Tap To Continue!"))
        self.label.setText(_translate("StepsDialog", "Rotate the working\n"
"area and"))

import light1_res_rc
