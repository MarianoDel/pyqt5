# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 395)
        self.enviar1 = QtWidgets.QPushButton(Dialog)
        self.enviar1.setGeometry(QtCore.QRect(60, 30, 211, 34))
        self.enviar1.setObjectName("enviar1")
        self.enviar2 = QtWidgets.QPushButton(Dialog)
        self.enviar2.setGeometry(QtCore.QRect(60, 100, 211, 34))
        self.enviar2.setObjectName("enviar2")
        self.enviar3 = QtWidgets.QPushButton(Dialog)
        self.enviar3.setGeometry(QtCore.QRect(60, 170, 211, 34))
        self.enviar3.setObjectName("enviar3")
        self.recibido = QtWidgets.QLabel(Dialog)
        self.recibido.setGeometry(QtCore.QRect(60, 240, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans [GOOG]")
        font.setPointSize(14)
        self.recibido.setFont(font)
        self.recibido.setObjectName("recibido")
        self.diag = QtWidgets.QLabel(Dialog)
        self.diag.setGeometry(QtCore.QRect(60, 330, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans [GOOG]")
        font.setPointSize(14)
        self.diag.setFont(font)
        self.diag.setText("")
        self.diag.setObjectName("diag")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(390, 130, 88, 81))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enviar1.setText(_translate("Dialog", "Presione para enviar"))
        self.enviar2.setText(_translate("Dialog", "Presione para enviar"))
        self.enviar3.setText(_translate("Dialog", "Presione para enviar"))
        self.recibido.setText(_translate("Dialog", "Nada en Rx"))
        self.closeButton.setText(_translate("Dialog", "Close"))

