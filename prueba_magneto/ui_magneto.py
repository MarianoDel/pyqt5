# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mag_ver_2_0.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 486)
        self.t10 = QtWidgets.QPushButton(Dialog)
        self.t10.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.t10.setObjectName("t10")
        self.t30 = QtWidgets.QPushButton(Dialog)
        self.t30.setGeometry(QtCore.QRect(20, 80, 211, 41))
        self.t30.setObjectName("t30")
        self.t60 = QtWidgets.QPushButton(Dialog)
        self.t60.setGeometry(QtCore.QRect(20, 140, 211, 41))
        self.t60.setObjectName("t60")
        self.c10 = QtWidgets.QPushButton(Dialog)
        self.c10.setGeometry(QtCore.QRect(20, 200, 211, 41))
        self.c10.setObjectName("c10")
        self.c30 = QtWidgets.QPushButton(Dialog)
        self.c30.setGeometry(QtCore.QRect(20, 260, 211, 41))
        self.c30.setObjectName("c30")
        self.c60 = QtWidgets.QPushButton(Dialog)
        self.c60.setGeometry(QtCore.QRect(20, 320, 211, 41))
        self.c60.setObjectName("c60")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 20, 451, 41))
        font = QtGui.QFont()
        font.setFamily("padmaa")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(253, 69, 461, 291))
        self.textEdit.setObjectName("textEdit")
        self.start_treat = QtWidgets.QPushButton(Dialog)
        self.start_treat.setGeometry(QtCore.QRect(20, 380, 211, 41))
        self.start_treat.setObjectName("start_treat")
        self.get_conf = QtWidgets.QPushButton(Dialog)
        self.get_conf.setGeometry(QtCore.QRect(20, 430, 691, 41))
        self.get_conf.setObjectName("get_conf")
        self.stop_treat = QtWidgets.QPushButton(Dialog)
        self.stop_treat.setGeometry(QtCore.QRect(250, 380, 211, 41))
        self.stop_treat.setObjectName("stop_treat")
        self.pause_treat = QtWidgets.QPushButton(Dialog)
        self.pause_treat.setGeometry(QtCore.QRect(480, 380, 231, 41))
        self.pause_treat.setObjectName("pause_treat")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.t10.setText(_translate("Dialog", "TRIANGULAR 10HZ"))
        self.t30.setText(_translate("Dialog", "TRIANGULAR 30HZ"))
        self.t60.setText(_translate("Dialog", "TRIANGULAR 60HZ"))
        self.c10.setText(_translate("Dialog", "CUADRADA 10HZ"))
        self.c30.setText(_translate("Dialog", "CUADRADA 30HZ"))
        self.c60.setText(_translate("Dialog", "CUADRADA 60HZ"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.start_treat.setText(_translate("Dialog", "START TREATMENT"))
        self.get_conf.setText(_translate("Dialog", "Get All Conf"))
        self.stop_treat.setText(_translate("Dialog", "STOP TREATMENT"))
        self.pause_treat.setText(_translate("Dialog", "PAUSE TREATMENT"))

