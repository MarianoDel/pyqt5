# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pru2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyKDE4.kdeui import KLed

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 60, 59, 18))
        self.label.setObjectName("label")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(170, 60, 20, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.kled = KLed(Dialog)
        self.kled.setGeometry(QtCore.QRect(320, 220, 41, 51))
        self.kled.setObjectName("kled")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

from kled import KLed
