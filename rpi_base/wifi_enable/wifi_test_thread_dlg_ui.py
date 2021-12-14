# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifi_test_thread.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WifiTestDialog(object):
    def setupUi(self, WifiTestDialog):
        WifiTestDialog.setObjectName("WifiTestDialog")
        WifiTestDialog.resize(527, 300)
        self.wifiLabel1 = QtWidgets.QLabel(WifiTestDialog)
        self.wifiLabel1.setGeometry(QtCore.QRect(15, 190, 471, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.wifiLabel1.setFont(font)
        self.wifiLabel1.setStyleSheet("color: rgb(55, 52, 53);")
        self.wifiLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wifiLabel1.setObjectName("wifiLabel1")
        self.wifiButton = QtWidgets.QPushButton(WifiTestDialog)
        self.wifiButton.setGeometry(QtCore.QRect(155, 40, 104, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiButton.sizePolicy().hasHeightForWidth())
        self.wifiButton.setSizePolicy(sizePolicy)
        self.wifiButton.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.wifiButton.setFont(font)
        self.wifiButton.setStyleSheet("background-color: rgb(230, 245, 253);\n"
"border: 0px;\n"
"")
        self.wifiButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/symbols/resources/wifi-symbol_disa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wifiButton.setIcon(icon)
        self.wifiButton.setIconSize(QtCore.QSize(100, 100))
        self.wifiButton.setObjectName("wifiButton")

        self.retranslateUi(WifiTestDialog)
        QtCore.QMetaObject.connectSlotsByName(WifiTestDialog)

    def retranslateUi(self, WifiTestDialog):
        _translate = QtCore.QCoreApplication.translate
        WifiTestDialog.setWindowTitle(_translate("WifiTestDialog", "Dialog"))
        self.wifiLabel1.setText(_translate("WifiTestDialog", "Password:"))

import wifi_res_rc
