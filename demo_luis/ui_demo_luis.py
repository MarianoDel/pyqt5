# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_luis.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Oxygen Mono")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(60, 220, 51, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_2.setGeometry(QtCore.QRect(170, 220, 51, 160))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_3.setGeometry(QtCore.QRect(270, 220, 51, 160))
        self.verticalSlider_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 81, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/Inicio_listo_800_600.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 81, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 81, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 130, 81, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 130, 101, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 90, 261, 16))
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(410, 270, 241, 101))
        self.dateEdit.setObjectName("dateEdit")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 450, 301, 81))
        self.lcdNumber.setProperty("intValue", 22)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Date: 24-05-2019 Hour: 21:36"))
        self.label_6.setText(_translate("Dialog", "30:00"))
        self.label_7.setText(_translate("Dialog", "Remaining time:"))

import new_res_rc
