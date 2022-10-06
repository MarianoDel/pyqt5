# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stretcher_treatment_dlg.ui'
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
"background-image: url(:/background/resources/background_stretcher_infinity_02.png);\n"
"}")
        self.freqButton = QtWidgets.QPushButton(TreatmentDialog)
        self.freqButton.setGeometry(QtCore.QRect(100, 290, 100, 100))
        self.freqButton.setMinimumSize(QtCore.QSize(100, 100))
        self.freqButton.setStyleSheet("background-image: url(:/frequencies/resources/62_64Hz.png);\n"
"background-color: rgb(196, 161, 203);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.freqButton.setText("")
        self.freqButton.setObjectName("freqButton")
        self.signalButton = QtWidgets.QPushButton(TreatmentDialog)
        self.signalButton.setGeometry(QtCore.QRect(100, 120, 100, 100))
        self.signalButton.setMinimumSize(QtCore.QSize(100, 100))
        self.signalButton.setStyleSheet("background-image: url(:/buttons/resources/Sinus.png);\n"
"background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.signalButton.setText("")
        self.signalButton.setObjectName("signalButton")
        self.textEdit = QtWidgets.QTextEdit(TreatmentDialog)
        self.textEdit.setGeometry(QtCore.QRect(450, 620, 791, 151))
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
        self.powerLabel = QtWidgets.QLabel(TreatmentDialog)
        self.powerLabel.setGeometry(QtCore.QRect(90, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.powerLabel.setFont(font)
        self.powerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.powerLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.powerLabel.setObjectName("powerLabel")
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
        self.minutesLabel.setGeometry(QtCore.QRect(90, 520, 151, 51))
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
        self.doneButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"color: rgb(55, 52, 53);")
        self.doneButton.setObjectName("doneButton")

        self.retranslateUi(TreatmentDialog)
        QtCore.QMetaObject.connectSlotsByName(TreatmentDialog)

    def retranslateUi(self, TreatmentDialog):
        _translate = QtCore.QCoreApplication.translate
        TreatmentDialog.setWindowTitle(_translate("TreatmentDialog", "Dialog"))
        self.date_timeLabel.setText(_translate("TreatmentDialog", "19/03/2020 - 17:45"))
        self.powerLabel.setText(_translate("TreatmentDialog", "100%"))
        self.progressLabel.setText(_translate("TreatmentDialog", "Session in Progress"))
        self.remaining_secsLabel.setText(_translate("TreatmentDialog", "59\'\'"))
        self.remaining_minsLabel.setText(_translate("TreatmentDialog", "115\'"))
        self.minutesLabel.setText(_translate("TreatmentDialog", "120\'"))
        self.doneButton.setText(_translate("TreatmentDialog", "Tap to return to a previous screen"))

import stretcher3_res_rc
