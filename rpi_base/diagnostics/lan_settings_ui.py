# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lan_settings.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LanDialog(object):
    def setupUi(self, LanDialog):
        LanDialog.setObjectName("LanDialog")
        LanDialog.resize(644, 714)
        LanDialog.setStyleSheet("")
        self.ipEdit = QtWidgets.QLineEdit(LanDialog)
        self.ipEdit.setGeometry(QtCore.QRect(25, 200, 591, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit.setFont(font)
        self.ipEdit.setStyleSheet("color: rgb(55, 52, 53);")
        self.ipEdit.setObjectName("ipEdit")
        self.gwEdit = QtWidgets.QLineEdit(LanDialog)
        self.gwEdit.setGeometry(QtCore.QRect(25, 340, 591, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.gwEdit.setFont(font)
        self.gwEdit.setStyleSheet("color: rgb(55, 52, 53);")
        self.gwEdit.setObjectName("gwEdit")
        self.comboBox = QtWidgets.QComboBox(LanDialog)
        self.comboBox.setGeometry(QtCore.QRect(25, 30, 591, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(55, 52, 53);")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.cancelButton = QtWidgets.QPushButton(LanDialog)
        self.cancelButton.setGeometry(QtCore.QRect(25, 585, 200, 100))
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
        self.saveButton = QtWidgets.QPushButton(LanDialog)
        self.saveButton.setGeometry(QtCore.QRect(315, 585, 300, 100))
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
        self.lanLabel1 = QtWidgets.QLabel(LanDialog)
        self.lanLabel1.setGeometry(QtCore.QRect(25, 140, 236, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lanLabel1.setFont(font)
        self.lanLabel1.setStyleSheet("color: rgb(55, 52, 53);")
        self.lanLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lanLabel1.setObjectName("lanLabel1")
        self.lanLabel2 = QtWidgets.QLabel(LanDialog)
        self.lanLabel2.setGeometry(QtCore.QRect(25, 280, 201, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lanLabel2.setFont(font)
        self.lanLabel2.setStyleSheet("color: rgb(55, 52, 53);")
        self.lanLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lanLabel2.setObjectName("lanLabel2")
        self.dnsEdit = QtWidgets.QLineEdit(LanDialog)
        self.dnsEdit.setGeometry(QtCore.QRect(25, 480, 591, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.dnsEdit.setFont(font)
        self.dnsEdit.setStyleSheet("color: rgb(55, 52, 53);")
        self.dnsEdit.setObjectName("dnsEdit")
        self.lanLabel3 = QtWidgets.QLabel(LanDialog)
        self.lanLabel3.setGeometry(QtCore.QRect(25, 420, 201, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lanLabel3.setFont(font)
        self.lanLabel3.setStyleSheet("color: rgb(55, 52, 53);")
        self.lanLabel3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lanLabel3.setObjectName("lanLabel3")
        self.gwButton = QtWidgets.QPushButton(LanDialog)
        self.gwButton.setGeometry(QtCore.QRect(25, 340, 591, 76))
        self.gwButton.setStyleSheet("background-color: rgba(196, 255, 157, 0);\n"
"border: 0px\n"
"")
        self.gwButton.setText("")
        self.gwButton.setObjectName("gwButton")
        self.dnsButton = QtWidgets.QPushButton(LanDialog)
        self.dnsButton.setGeometry(QtCore.QRect(25, 480, 591, 76))
        self.dnsButton.setStyleSheet("background-color: rgba(196, 255, 157, 0);\n"
"border: 0px\n"
"")
        self.dnsButton.setText("")
        self.dnsButton.setObjectName("dnsButton")
        self.ipButton = QtWidgets.QPushButton(LanDialog)
        self.ipButton.setGeometry(QtCore.QRect(25, 200, 591, 76))
        self.ipButton.setStyleSheet("background-color: rgba(196, 255, 157, 0);\n"
"border: 0px\n"
"")
        self.ipButton.setText("")
        self.ipButton.setObjectName("ipButton")

        self.retranslateUi(LanDialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(LanDialog)

    def retranslateUi(self, LanDialog):
        _translate = QtCore.QCoreApplication.translate
        LanDialog.setWindowTitle(_translate("LanDialog", "Dialog"))
        self.cancelButton.setText(_translate("LanDialog", "Cancel"))
        self.saveButton.setText(_translate("LanDialog", "Save && Exit"))
        self.lanLabel1.setText(_translate("LanDialog", "IP/Mask Bits:"))
        self.lanLabel2.setText(_translate("LanDialog", "Gateway:"))
        self.lanLabel3.setText(_translate("LanDialog", "DNS:"))

import diagnostics_res_rc
