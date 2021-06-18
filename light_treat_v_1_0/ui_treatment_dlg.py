# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'light_treatment_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TreatmentDialog(object):
    def setupUi(self, TreatmentDialog):
        TreatmentDialog.setObjectName("TreatmentDialog")
        TreatmentDialog.resize(1280, 800)
        TreatmentDialog.setStyleSheet("QDialog {\n"
"background-image: url(:/background/resources/background_magnet_03.png);\n"
"}")
        self.stepsButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stepsButton.setGeometry(QtCore.QRect(100, 290, 100, 100))
        self.stepsButton.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stepsButton.setFont(font)
        self.stepsButton.setStyleSheet("background-image: url(:/frequencies/resources/62_64Hz.png);\n"
"background-color: rgb(196, 161, 203);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.stepsButton.setText("")
        self.stepsButton.setObjectName("stepsButton")
        self.signalLargeButton = QtWidgets.QPushButton(TreatmentDialog)
        self.signalLargeButton.setGeometry(QtCore.QRect(100, 120, 232, 100))
        self.signalLargeButton.setMinimumSize(QtCore.QSize(100, 100))
        self.signalLargeButton.setStyleSheet("background-image: url(:/buttons/resources/Sinus.png);\n"
"background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.signalLargeButton.setText("")
        self.signalLargeButton.setObjectName("signalLargeButton")
        self.textEdit = QtWidgets.QTextEdit(TreatmentDialog)
        self.textEdit.setGeometry(QtCore.QRect(450, 650, 796, 111))
        self.textEdit.setStyleSheet("border:2px outset;\n"
"background-color: rgb(246, 255, 254);\n"
"border-radius: 16px;\n"
"color: rgb(0, 0, 127);\n"
"border-color: rgb(55, 52, 53);")
        self.textEdit.setObjectName("textEdit")
        self.stop_rsmButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stop_rsmButton.setGeometry(QtCore.QRect(70, 630, 300, 120))
        self.stop_rsmButton.setMinimumSize(QtCore.QSize(100, 100))
        self.stop_rsmButton.setStyleSheet("background-image: url(:/buttons/resources/Stop-Pause.png);\n"
"background-color: rgb(237, 50, 55);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.stop_rsmButton.setText("")
        self.stop_rsmButton.setObjectName("stop_rsmButton")
        self.date_timeLabel = QtWidgets.QLabel(TreatmentDialog)
        self.date_timeLabel.setGeometry(QtCore.QRect(910, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.date_timeLabel.setFont(font)
        self.date_timeLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.date_timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.date_timeLabel.setObjectName("date_timeLabel")
        self.powerRedLabel = QtWidgets.QLabel(TreatmentDialog)
        self.powerRedLabel.setGeometry(QtCore.QRect(90, 425, 296, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.powerRedLabel.setFont(font)
        self.powerRedLabel.setStyleSheet("color: rgb(122, 181, 191);")
        self.powerRedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.powerRedLabel.setObjectName("powerRedLabel")
        self.progressLabel = QtWidgets.QLabel(TreatmentDialog)
        self.progressLabel.setGeometry(QtCore.QRect(448, 109, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.progressLabel.setFont(font)
        self.progressLabel.setStyleSheet("color: rgb(0, 163, 86);")
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setObjectName("progressLabel")
        self.remaining_secsLabel = QtWidgets.QLabel(TreatmentDialog)
        self.remaining_secsLabel.setGeometry(QtCore.QRect(950, 280, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(65)
        font.setBold(True)
        font.setWeight(75)
        self.remaining_secsLabel.setFont(font)
        self.remaining_secsLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.remaining_secsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.remaining_secsLabel.setObjectName("remaining_secsLabel")
        self.remaining_minsLabel = QtWidgets.QLabel(TreatmentDialog)
        self.remaining_minsLabel.setGeometry(QtCore.QRect(448, 200, 481, 231))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(150)
        font.setBold(True)
        font.setWeight(75)
        self.remaining_minsLabel.setFont(font)
        self.remaining_minsLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.remaining_minsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.remaining_minsLabel.setObjectName("remaining_minsLabel")
        self.minutesLabel = QtWidgets.QLabel(TreatmentDialog)
        self.minutesLabel.setGeometry(QtCore.QRect(90, 560, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.minutesLabel.setFont(font)
        self.minutesLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.minutesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.minutesLabel.setObjectName("minutesLabel")
        self.stopButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stopButton.setGeometry(QtCore.QRect(70, 630, 120, 120))
        self.stopButton.setMinimumSize(QtCore.QSize(100, 100))
        self.stopButton.setStyleSheet("background-image: url(:/buttons/resources/Stop.png);\n"
"background-color: rgb(237, 50, 55);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.rsmButton = QtWidgets.QPushButton(TreatmentDialog)
        self.rsmButton.setGeometry(QtCore.QRect(250, 630, 120, 120))
        self.rsmButton.setMinimumSize(QtCore.QSize(100, 100))
        self.rsmButton.setStyleSheet("background-image: url(:/buttons/resources/Rsm.png);\n"
"background-color: rgb(0, 168, 89);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.rsmButton.setText("")
        self.rsmButton.setObjectName("rsmButton")
        self.doneButton = QtWidgets.QPushButton(TreatmentDialog)
        self.doneButton.setGeometry(QtCore.QRect(450, 500, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.doneButton.setFont(font)
        self.doneButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.doneButton.setStyleSheet("background-color: rgb(230, 245, 253);\n"
"border: 0px;\n"
"color: rgb(55, 52, 53);")
        self.doneButton.setObjectName("doneButton")
        self.powerIRedLabel = QtWidgets.QLabel(TreatmentDialog)
        self.powerIRedLabel.setGeometry(QtCore.QRect(90, 485, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.powerIRedLabel.setFont(font)
        self.powerIRedLabel.setStyleSheet("color: rgb(176, 152, 128);")
        self.powerIRedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.powerIRedLabel.setObjectName("powerIRedLabel")
        self.signalShortButton = QtWidgets.QPushButton(TreatmentDialog)
        self.signalShortButton.setGeometry(QtCore.QRect(100, 120, 100, 100))
        self.signalShortButton.setMinimumSize(QtCore.QSize(100, 100))
        self.signalShortButton.setStyleSheet("background-image: url(:/buttons/resources/Sinus.png);\n"
"background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.signalShortButton.setText("")
        self.signalShortButton.setObjectName("signalShortButton")

        self.retranslateUi(TreatmentDialog)
        QtCore.QMetaObject.connectSlotsByName(TreatmentDialog)

    def retranslateUi(self, TreatmentDialog):
        _translate = QtCore.QCoreApplication.translate
        TreatmentDialog.setWindowTitle(_translate("TreatmentDialog", "Dialog"))
        self.date_timeLabel.setText(_translate("TreatmentDialog", "19/03/2020 - 17:45"))
        self.powerRedLabel.setText(_translate("TreatmentDialog", "100%"))
        self.progressLabel.setText(_translate("TreatmentDialog", "Session in Progress"))
        self.remaining_secsLabel.setText(_translate("TreatmentDialog", "59\'\'"))
        self.remaining_minsLabel.setText(_translate("TreatmentDialog", "115\'"))
        self.minutesLabel.setText(_translate("TreatmentDialog", "120\'"))
        self.doneButton.setText(_translate("TreatmentDialog", "Tap to return to a previous screen"))
        self.powerIRedLabel.setText(_translate("TreatmentDialog", "100%"))

import light1_res_rc
