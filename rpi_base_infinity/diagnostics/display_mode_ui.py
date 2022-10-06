# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_mode.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DisplayModeDialog(object):
    def setupUi(self, DisplayModeDialog):
        DisplayModeDialog.setObjectName("DisplayModeDialog")
        DisplayModeDialog.resize(718, 500)
        self.label = QtWidgets.QLabel(DisplayModeDialog)
        self.label.setGeometry(QtCore.QRect(110, 10, 496, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(DisplayModeDialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 651, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(55, 52, 53);")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.cancelButton = QtWidgets.QPushButton(DisplayModeDialog)
        self.cancelButton.setGeometry(QtCore.QRect(30, 305, 200, 100))
        self.cancelButton.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.cancelButton.setObjectName("cancelButton")
        self.saveButton = QtWidgets.QPushButton(DisplayModeDialog)
        self.saveButton.setGeometry(QtCore.QRect(380, 305, 300, 100))
        self.saveButton.setMinimumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.saveButton.setObjectName("saveButton")
        self.currentLabel = QtWidgets.QLabel(DisplayModeDialog)
        self.currentLabel.setGeometry(QtCore.QRect(30, 60, 681, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.currentLabel.setFont(font)
        self.currentLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.currentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentLabel.setObjectName("currentLabel")

        self.retranslateUi(DisplayModeDialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DisplayModeDialog)

    def retranslateUi(self, DisplayModeDialog):
        _translate = QtCore.QCoreApplication.translate
        DisplayModeDialog.setWindowTitle(_translate("DisplayModeDialog", "Dialog"))
        self.label.setText(_translate("DisplayModeDialog", "Change Display Operation Mode!!!"))
        self.cancelButton.setText(_translate("DisplayModeDialog", "Cancel"))
        self.saveButton.setText(_translate("DisplayModeDialog", "Save && Exit"))
        self.currentLabel.setText(_translate("DisplayModeDialog", "Current mode: Stretcher ver 3.2"))

import diagnostics_res_rc
