# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(400, 300)
        self.lcdNumber = QtWidgets.QLCDNumber(ImageDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 90, 111, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.line = QtWidgets.QFrame(ImageDialog)
        self.line.setGeometry(QtCore.QRect(23, 150, 20, 101))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.stackedWidget = QtWidgets.QStackedWidget(ImageDialog)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 200, 120, 80))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Dialog"))

