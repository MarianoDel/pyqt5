# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_firstDialog(object):
    def setupUi(self, firstDialog):
        firstDialog.setObjectName("firstDialog")
        firstDialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(firstDialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 80, 191, 91))
        self.pushButton.setObjectName("pushButton")
        self.touchLabel = QtWidgets.QLabel(firstDialog)
        self.touchLabel.setGeometry(QtCore.QRect(30, 205, 331, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.touchLabel.setFont(font)
        self.touchLabel.setText("")
        self.touchLabel.setObjectName("touchLabel")

        self.retranslateUi(firstDialog)
        QtCore.QMetaObject.connectSlotsByName(firstDialog)

    def retranslateUi(self, firstDialog):
        _translate = QtCore.QCoreApplication.translate
        firstDialog.setWindowTitle(_translate("firstDialog", "Dialog"))
        self.pushButton.setText(_translate("firstDialog", "Open New Window"))

