# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'security_code.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecurityDialog(object):
    def setupUi(self, SecurityDialog):
        SecurityDialog.setObjectName("SecurityDialog")
        SecurityDialog.resize(646, 489)
        SecurityDialog.setStyleSheet("")
        self.securityEdit = QtWidgets.QLineEdit(SecurityDialog)
        self.securityEdit.setGeometry(QtCore.QRect(25, 200, 591, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.securityEdit.setFont(font)
        self.securityEdit.setStyleSheet("color: rgb(55, 52, 53);")
        self.securityEdit.setObjectName("securityEdit")
        self.cancelButton = QtWidgets.QPushButton(SecurityDialog)
        self.cancelButton.setGeometry(QtCore.QRect(25, 355, 200, 100))
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
        self.saveButton = QtWidgets.QPushButton(SecurityDialog)
        self.saveButton.setGeometry(QtCore.QRect(315, 355, 300, 100))
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
        self.lanLabel1 = QtWidgets.QLabel(SecurityDialog)
        self.lanLabel1.setGeometry(QtCore.QRect(25, 10, 396, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lanLabel1.setFont(font)
        self.lanLabel1.setStyleSheet("color: rgb(55, 52, 53);")
        self.lanLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lanLabel1.setObjectName("lanLabel1")
        self.lanLabel2 = QtWidgets.QLabel(SecurityDialog)
        self.lanLabel2.setGeometry(QtCore.QRect(25, 130, 301, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lanLabel2.setFont(font)
        self.lanLabel2.setStyleSheet("color: rgb(55, 52, 53);")
        self.lanLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lanLabel2.setObjectName("lanLabel2")
        self.securityButton = QtWidgets.QPushButton(SecurityDialog)
        self.securityButton.setGeometry(QtCore.QRect(25, 200, 591, 76))
        self.securityButton.setStyleSheet("background-color: rgba(196, 255, 157, 0);\n"
"border: 0px\n"
"")
        self.securityButton.setText("")
        self.securityButton.setObjectName("securityButton")
        self.actualLabel = QtWidgets.QLabel(SecurityDialog)
        self.actualLabel.setGeometry(QtCore.QRect(445, 10, 131, 56))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.actualLabel.setFont(font)
        self.actualLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.actualLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.actualLabel.setObjectName("actualLabel")
        self.statusLabel = QtWidgets.QLabel(SecurityDialog)
        self.statusLabel.setGeometry(QtCore.QRect(25, 295, 586, 36))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.statusLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(SecurityDialog)
        QtCore.QMetaObject.connectSlotsByName(SecurityDialog)

    def retranslateUi(self, SecurityDialog):
        _translate = QtCore.QCoreApplication.translate
        SecurityDialog.setWindowTitle(_translate("SecurityDialog", "Dialog"))
        self.cancelButton.setText(_translate("SecurityDialog", "Cancel"))
        self.saveButton.setText(_translate("SecurityDialog", "Save && Exit"))
        self.lanLabel1.setText(_translate("SecurityDialog", "Actual Security Code:"))
        self.lanLabel2.setText(_translate("SecurityDialog", "Enter new Code:"))
        self.actualLabel.setText(_translate("SecurityDialog", "9999"))
        self.statusLabel.setText(_translate("SecurityDialog", "No new code detected!"))

import diagnostics_res_rc
