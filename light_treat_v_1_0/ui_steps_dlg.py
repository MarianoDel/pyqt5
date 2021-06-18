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
        self.doneButton.setGeometry(QtCore.QRect(175, 150, 311, 191))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.doneButton.setFont(font)
        self.doneButton.setObjectName("doneButton")
        self.buzzButton = QtWidgets.QPushButton(StepsDialog)
        self.buzzButton.setGeometry(QtCore.QRect(50, 65, 156, 56))
        self.buzzButton.setObjectName("buzzButton")

        self.retranslateUi(StepsDialog)
        QtCore.QMetaObject.connectSlotsByName(StepsDialog)

    def retranslateUi(self, StepsDialog):
        _translate = QtCore.QCoreApplication.translate
        StepsDialog.setWindowTitle(_translate("StepsDialog", "Dialog"))
        self.doneButton.setText(_translate("StepsDialog", "Done!"))
        self.buzzButton.setText(_translate("StepsDialog", "Buzzer"))

import light1_res_rc
