# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modal.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_modalDialog(object):
    def setupUi(self, modalDialog):
        modalDialog.setObjectName("modalDialog")
        modalDialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(modalDialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 160, 281, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(modalDialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 70, 131, 51))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(modalDialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.parentLabel = QtWidgets.QLabel(modalDialog)
        self.parentLabel.setGeometry(QtCore.QRect(40, 220, 221, 16))
        self.parentLabel.setObjectName("parentLabel")

        self.retranslateUi(modalDialog)
        QtCore.QMetaObject.connectSlotsByName(modalDialog)

    def retranslateUi(self, modalDialog):
        _translate = QtCore.QCoreApplication.translate
        modalDialog.setWindowTitle(_translate("modalDialog", "Dialog"))
        self.pushButton.setText(_translate("modalDialog", "Listo!"))
        self.checkBox.setText(_translate("modalDialog", "CheckBox"))
        self.label.setText(_translate("modalDialog", "Nueva ventana Modal"))
        self.parentLabel.setText(_translate("modalDialog", "TextLabel"))

