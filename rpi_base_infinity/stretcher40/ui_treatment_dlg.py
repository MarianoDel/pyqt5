# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stretcher_treatment_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TreatmentDialog(object):
    def setupUi(self, TreatmentDialog):
        TreatmentDialog.setObjectName("TreatmentDialog")
        TreatmentDialog.resize(1280, 800)
        TreatmentDialog.setStyleSheet("QDialog {\n"
"background-image: url(:/background/resources/bkg_treat_no_buttons.png);\n"
"}")
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
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
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
        self.stage1PowerLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage1PowerLabel.setGeometry(QtCore.QRect(260, 120, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage1PowerLabel.setFont(font)
        self.stage1PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage1PowerLabel.setObjectName("stage1PowerLabel")
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
        self.stage1MinutesLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage1MinutesLabel.setGeometry(QtCore.QRect(260, 170, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage1MinutesLabel.setFont(font)
        self.stage1MinutesLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.stage1MinutesLabel.setObjectName("stage1MinutesLabel")
        self.stopButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stopButton.setGeometry(QtCore.QRect(70, 630, 120, 120))
        self.stopButton.setMinimumSize(QtCore.QSize(100, 100))
        self.stopButton.setStyleSheet("background-image: url(:/buttons/resources/Stop.png);\n"
"background-color: rgb(237, 50, 55);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.rsmButton = QtWidgets.QPushButton(TreatmentDialog)
        self.rsmButton.setGeometry(QtCore.QRect(250, 630, 120, 120))
        self.rsmButton.setMinimumSize(QtCore.QSize(100, 100))
        self.rsmButton.setStyleSheet("background-image: url(:/buttons/resources/Rsm.png);\n"
"background-color: rgb(0, 168, 89);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
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
        self.doneButton.setStyleSheet("border: 0px;\n"
"color: rgb(55, 52, 53);")
        self.doneButton.setObjectName("doneButton")
        self.layoutWidget_6 = QtWidgets.QWidget(TreatmentDialog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(670, 560, 541, 76))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(22)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ant1Button = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ant1Button.sizePolicy().hasHeightForWidth())
        self.ant1Button.setSizePolicy(sizePolicy)
        self.ant1Button.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ant1Button.setFont(font)
        self.ant1Button.setStyleSheet("border: 0px;\n"
"")
        self.ant1Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/resources/wifi-symbol_disa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ant1Button.setIcon(icon)
        self.ant1Button.setIconSize(QtCore.QSize(100, 100))
        self.ant1Button.setObjectName("ant1Button")
        self.horizontalLayout_5.addWidget(self.ant1Button)
        self.ant2Button = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ant2Button.sizePolicy().hasHeightForWidth())
        self.ant2Button.setSizePolicy(sizePolicy)
        self.ant2Button.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ant2Button.setFont(font)
        self.ant2Button.setStyleSheet("border: 0px;\n"
"")
        self.ant2Button.setText("")
        self.ant2Button.setIcon(icon)
        self.ant2Button.setIconSize(QtCore.QSize(100, 100))
        self.ant2Button.setObjectName("ant2Button")
        self.horizontalLayout_5.addWidget(self.ant2Button)
        self.ant3Button = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ant3Button.sizePolicy().hasHeightForWidth())
        self.ant3Button.setSizePolicy(sizePolicy)
        self.ant3Button.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ant3Button.setFont(font)
        self.ant3Button.setStyleSheet("border: 0px;\n"
"")
        self.ant3Button.setText("")
        self.ant3Button.setIcon(icon)
        self.ant3Button.setIconSize(QtCore.QSize(100, 100))
        self.ant3Button.setObjectName("ant3Button")
        self.horizontalLayout_5.addWidget(self.ant3Button)
        self.tempLabel = QtWidgets.QLabel(TreatmentDialog)
        self.tempLabel.setGeometry(QtCore.QRect(925, 500, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.tempLabel.setFont(font)
        self.tempLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.tempLabel.setObjectName("tempLabel")
        self.stage2MinutesLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage2MinutesLabel.setGeometry(QtCore.QRect(260, 330, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage2MinutesLabel.setFont(font)
        self.stage2MinutesLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.stage2MinutesLabel.setObjectName("stage2MinutesLabel")
        self.stage2PowerLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage2PowerLabel.setGeometry(QtCore.QRect(260, 280, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage2PowerLabel.setFont(font)
        self.stage2PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage2PowerLabel.setObjectName("stage2PowerLabel")
        self.stage3MinutesLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage3MinutesLabel.setGeometry(QtCore.QRect(260, 490, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage3MinutesLabel.setFont(font)
        self.stage3MinutesLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.stage3MinutesLabel.setObjectName("stage3MinutesLabel")
        self.stage3PowerLabel = QtWidgets.QLabel(TreatmentDialog)
        self.stage3PowerLabel.setGeometry(QtCore.QRect(260, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.stage3PowerLabel.setFont(font)
        self.stage3PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage3PowerLabel.setObjectName("stage3PowerLabel")
        self.layoutWidget = QtWidgets.QWidget(TreatmentDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 120, 236, 106))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stage1SignalButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1SignalButton.sizePolicy().hasHeightForWidth())
        self.stage1SignalButton.setSizePolicy(sizePolicy)
        self.stage1SignalButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage1SignalButton.setStyleSheet("background-image: url(:/buttons/resources/triangular_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage1SignalButton.setText("")
        self.stage1SignalButton.setObjectName("stage1SignalButton")
        self.horizontalLayout.addWidget(self.stage1SignalButton)
        self.stage1FreqButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1FreqButton.sizePolicy().hasHeightForWidth())
        self.stage1FreqButton.setSizePolicy(sizePolicy)
        self.stage1FreqButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage1FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/freq1_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage1FreqButton.setText("")
        self.stage1FreqButton.setObjectName("stage1FreqButton")
        self.horizontalLayout.addWidget(self.stage1FreqButton)
        self.layoutWidget_2 = QtWidgets.QWidget(TreatmentDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(5, 280, 236, 106))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stage2SignalButton = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2SignalButton.sizePolicy().hasHeightForWidth())
        self.stage2SignalButton.setSizePolicy(sizePolicy)
        self.stage2SignalButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage2SignalButton.setStyleSheet("background-image: url(:/buttons/resources/square_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage2SignalButton.setText("")
        self.stage2SignalButton.setObjectName("stage2SignalButton")
        self.horizontalLayout_2.addWidget(self.stage2SignalButton)
        self.stage2FreqButton = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2FreqButton.sizePolicy().hasHeightForWidth())
        self.stage2FreqButton.setSizePolicy(sizePolicy)
        self.stage2FreqButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage2FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/freq1_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage2FreqButton.setText("")
        self.stage2FreqButton.setObjectName("stage2FreqButton")
        self.horizontalLayout_2.addWidget(self.stage2FreqButton)
        self.layoutWidget_3 = QtWidgets.QWidget(TreatmentDialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(5, 440, 236, 106))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stage3SignalButton = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3SignalButton.sizePolicy().hasHeightForWidth())
        self.stage3SignalButton.setSizePolicy(sizePolicy)
        self.stage3SignalButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage3SignalButton.setStyleSheet("background-image: url(:/buttons/resources/square_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage3SignalButton.setText("")
        self.stage3SignalButton.setObjectName("stage3SignalButton")
        self.horizontalLayout_3.addWidget(self.stage3SignalButton)
        self.stage3FreqButton = QtWidgets.QPushButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3FreqButton.sizePolicy().hasHeightForWidth())
        self.stage3FreqButton.setSizePolicy(sizePolicy)
        self.stage3FreqButton.setMinimumSize(QtCore.QSize(90, 90))
        self.stage3FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/freq1_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage3FreqButton.setText("")
        self.stage3FreqButton.setObjectName("stage3FreqButton")
        self.horizontalLayout_3.addWidget(self.stage3FreqButton)
        self.stage2BkgButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stage2BkgButton.setGeometry(QtCore.QRect(5, 280, 386, 106))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2BkgButton.sizePolicy().hasHeightForWidth())
        self.stage2BkgButton.setSizePolicy(sizePolicy)
        self.stage2BkgButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.stage2BkgButton.setFont(font)
        self.stage2BkgButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stage2BkgButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(233, 245, 235);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(233, 245, 235);")
        self.stage2BkgButton.setText("")
        self.stage2BkgButton.setObjectName("stage2BkgButton")
        self.stage1BkgButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stage1BkgButton.setGeometry(QtCore.QRect(5, 120, 386, 106))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1BkgButton.sizePolicy().hasHeightForWidth())
        self.stage1BkgButton.setSizePolicy(sizePolicy)
        self.stage1BkgButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.stage1BkgButton.setFont(font)
        self.stage1BkgButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stage1BkgButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(233, 245, 235);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(233, 245, 235);")
        self.stage1BkgButton.setText("")
        self.stage1BkgButton.setObjectName("stage1BkgButton")
        self.stage3BkgButton = QtWidgets.QPushButton(TreatmentDialog)
        self.stage3BkgButton.setGeometry(QtCore.QRect(5, 440, 386, 106))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3BkgButton.sizePolicy().hasHeightForWidth())
        self.stage3BkgButton.setSizePolicy(sizePolicy)
        self.stage3BkgButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.stage3BkgButton.setFont(font)
        self.stage3BkgButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stage3BkgButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(233, 245, 235);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(233, 245, 235);")
        self.stage3BkgButton.setText("")
        self.stage3BkgButton.setObjectName("stage3BkgButton")

        self.retranslateUi(TreatmentDialog)
        QtCore.QMetaObject.connectSlotsByName(TreatmentDialog)

    def retranslateUi(self, TreatmentDialog):
        _translate = QtCore.QCoreApplication.translate
        TreatmentDialog.setWindowTitle(_translate("TreatmentDialog", "Dialog"))
        self.date_timeLabel.setText(_translate("TreatmentDialog", "19/03/2020 - 17:45"))
        self.stage1PowerLabel.setText(_translate("TreatmentDialog", "100%"))
        self.progressLabel.setText(_translate("TreatmentDialog", "Session in Progress"))
        self.remaining_secsLabel.setText(_translate("TreatmentDialog", "59\'\'"))
        self.remaining_minsLabel.setText(_translate("TreatmentDialog", "150\'"))
        self.stage1MinutesLabel.setText(_translate("TreatmentDialog", "120\'"))
        self.doneButton.setText(_translate("TreatmentDialog", "Tap to return to a previous screen"))
        self.tempLabel.setText(_translate("TreatmentDialog", "CH1 Temp: 35.0C"))
        self.stage2MinutesLabel.setText(_translate("TreatmentDialog", "120\'"))
        self.stage2PowerLabel.setText(_translate("TreatmentDialog", "100%"))
        self.stage3MinutesLabel.setText(_translate("TreatmentDialog", "120\'"))
        self.stage3PowerLabel.setText(_translate("TreatmentDialog", "100%"))
import stretcher4_res_rc
