# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magnet_memory_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MemoryDialog(object):
    def setupUi(self, MemoryDialog):
        MemoryDialog.setObjectName("MemoryDialog")
        MemoryDialog.resize(430, 275)
        self.memButton = QtWidgets.QPushButton(MemoryDialog)
        self.memButton.setGeometry(QtCore.QRect(20, 40, 100, 100))
        self.memButton.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.memButton.setFont(font)
        self.memButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.memButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(255, 244, 230);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.memButton.setObjectName("memButton")
        self.saveButton = QtWidgets.QPushButton(MemoryDialog)
        self.saveButton.setGeometry(QtCore.QRect(180, 20, 211, 50))
        self.saveButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(157, 211, 175);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.saveButton.setObjectName("saveButton")
        self.emptyButton = QtWidgets.QPushButton(MemoryDialog)
        self.emptyButton.setGeometry(QtCore.QRect(180, 110, 211, 50))
        self.emptyButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.emptyButton.setFont(font)
        self.emptyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.emptyButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(157, 211, 175);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.emptyButton.setObjectName("emptyButton")
        self.backButton = QtWidgets.QPushButton(MemoryDialog)
        self.backButton.setGeometry(QtCore.QRect(180, 200, 211, 50))
        self.backButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(243, 74, 125);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.backButton.setObjectName("backButton")

        self.retranslateUi(MemoryDialog)
        QtCore.QMetaObject.connectSlotsByName(MemoryDialog)

    def retranslateUi(self, MemoryDialog):
        _translate = QtCore.QCoreApplication.translate
        MemoryDialog.setWindowTitle(_translate("MemoryDialog", "Dialog"))
        self.memButton.setText(_translate("MemoryDialog", "I"))
        self.saveButton.setText(_translate("MemoryDialog", "Save Params"))
        self.emptyButton.setText(_translate("MemoryDialog", "Empty Mem"))
        self.backButton.setText(_translate("MemoryDialog", "Back!"))

import magnet3_res_rc
