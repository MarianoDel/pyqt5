# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magnet_stages_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StagesDialog(object):
    def setupUi(self, StagesDialog):
        StagesDialog.setObjectName("StagesDialog")
        StagesDialog.resize(1280, 800)
        StagesDialog.setStyleSheet("QDialog {\n"
"    background-image: url(:/background/resources/bkg_stage_no_buttons.png);\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(725, 115, 521, 102))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.freq1Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq1Button.sizePolicy().hasHeightForWidth())
        self.freq1Button.setSizePolicy(sizePolicy)
        self.freq1Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq1Button.setStyleSheet("background-image: url(:/frequencies/resources/0_98Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq1Button.setText("")
        self.freq1Button.setObjectName("freq1Button")
        self.horizontalLayout_2.addWidget(self.freq1Button)
        self.freq2Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq2Button.sizePolicy().hasHeightForWidth())
        self.freq2Button.setSizePolicy(sizePolicy)
        self.freq2Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq2Button.setStyleSheet("background-image: url(:/frequencies/resources/1_96Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq2Button.setText("")
        self.freq2Button.setObjectName("freq2Button")
        self.horizontalLayout_2.addWidget(self.freq2Button)
        self.freq3Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq3Button.sizePolicy().hasHeightForWidth())
        self.freq3Button.setSizePolicy(sizePolicy)
        self.freq3Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq3Button.setStyleSheet("background-image: url(:/frequencies/resources/3_92Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq3Button.setText("")
        self.freq3Button.setObjectName("freq3Button")
        self.horizontalLayout_2.addWidget(self.freq3Button)
        self.freq4Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq4Button.sizePolicy().hasHeightForWidth())
        self.freq4Button.setSizePolicy(sizePolicy)
        self.freq4Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq4Button.setStyleSheet("background-image: url(:/frequencies/resources/7_83Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq4Button.setText("")
        self.freq4Button.setObjectName("freq4Button")
        self.horizontalLayout_2.addWidget(self.freq4Button)
        self.freq5Button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq5Button.sizePolicy().hasHeightForWidth())
        self.freq5Button.setSizePolicy(sizePolicy)
        self.freq5Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq5Button.setStyleSheet("background-image: url(:/frequencies/resources/11_79Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq5Button.setText("")
        self.freq5Button.setObjectName("freq5Button")
        self.horizontalLayout_2.addWidget(self.freq5Button)
        self.layoutWidget_2 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(725, 220, 521, 102))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.freq1Button_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq1Button_2.sizePolicy().hasHeightForWidth())
        self.freq1Button_2.setSizePolicy(sizePolicy)
        self.freq1Button_2.setMinimumSize(QtCore.QSize(90, 90))
        self.freq1Button_2.setStyleSheet("background-image: url(:/frequencies/resources/16_67Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq1Button_2.setText("")
        self.freq1Button_2.setObjectName("freq1Button_2")
        self.horizontalLayout_3.addWidget(self.freq1Button_2)
        self.freq1Button_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq1Button_3.sizePolicy().hasHeightForWidth())
        self.freq1Button_3.setSizePolicy(sizePolicy)
        self.freq1Button_3.setMinimumSize(QtCore.QSize(90, 90))
        self.freq1Button_3.setStyleSheet("background-image: url(:/frequencies/resources/23_58Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq1Button_3.setText("")
        self.freq1Button_3.setObjectName("freq1Button_3")
        self.horizontalLayout_3.addWidget(self.freq1Button_3)
        self.freq1Button_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq1Button_4.sizePolicy().hasHeightForWidth())
        self.freq1Button_4.setSizePolicy(sizePolicy)
        self.freq1Button_4.setMinimumSize(QtCore.QSize(90, 90))
        self.freq1Button_4.setStyleSheet("background-image: url(:/frequencies/resources/30_80Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq1Button_4.setText("")
        self.freq1Button_4.setObjectName("freq1Button_4")
        self.horizontalLayout_3.addWidget(self.freq1Button_4)
        self.freq1Button_5 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq1Button_5.sizePolicy().hasHeightForWidth())
        self.freq1Button_5.setSizePolicy(sizePolicy)
        self.freq1Button_5.setMinimumSize(QtCore.QSize(90, 90))
        self.freq1Button_5.setStyleSheet("background-image: url(:/frequencies/resources/62_64Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq1Button_5.setText("")
        self.freq1Button_5.setObjectName("freq1Button_5")
        self.horizontalLayout_3.addWidget(self.freq1Button_5)
        self.freq6Button = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq6Button.sizePolicy().hasHeightForWidth())
        self.freq6Button.setSizePolicy(sizePolicy)
        self.freq6Button.setMinimumSize(QtCore.QSize(90, 90))
        self.freq6Button.setStyleSheet("background-image: url(:/frequencies/resources/86_22Hz_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.freq6Button.setText("")
        self.freq6Button.setObjectName("freq6Button")
        self.horizontalLayout_3.addWidget(self.freq6Button)
        self.layoutWidget1 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(880, 361, 341, 106))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.triangularButton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triangularButton.sizePolicy().hasHeightForWidth())
        self.triangularButton.setSizePolicy(sizePolicy)
        self.triangularButton.setMinimumSize(QtCore.QSize(90, 90))
        self.triangularButton.setStyleSheet("background-image: url(:/buttons/resources/triangular_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.triangularButton.setText("")
        self.triangularButton.setObjectName("triangularButton")
        self.horizontalLayout.addWidget(self.triangularButton)
        self.squareButton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.squareButton.sizePolicy().hasHeightForWidth())
        self.squareButton.setSizePolicy(sizePolicy)
        self.squareButton.setMinimumSize(QtCore.QSize(90, 90))
        self.squareButton.setStyleSheet("background-image: url(:/buttons/resources/square_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.squareButton.setText("")
        self.squareButton.setObjectName("squareButton")
        self.horizontalLayout.addWidget(self.squareButton)
        self.sinusoidalButton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidalButton.sizePolicy().hasHeightForWidth())
        self.sinusoidalButton.setSizePolicy(sizePolicy)
        self.sinusoidalButton.setMinimumSize(QtCore.QSize(90, 90))
        self.sinusoidalButton.setStyleSheet("background-image: url(:/buttons/resources/sinus_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(230, 231, 232);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.sinusoidalButton.setText("")
        self.sinusoidalButton.setObjectName("sinusoidalButton")
        self.horizontalLayout.addWidget(self.sinusoidalButton)
        self.layoutWidget2 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(750, 490, 471, 291))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clearButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(232, 175, 181);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(233, 245, 235);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.acceptButton = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())
        self.acceptButton.setSizePolicy(sizePolicy)
        self.acceptButton.setMinimumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.acceptButton.setFont(font)
        self.acceptButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.acceptButton.setStyleSheet("color: rgb(55, 52, 53);\n"
"background-color: rgb(191, 211, 199);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.acceptButton.setObjectName("acceptButton")
        self.verticalLayout.addWidget(self.acceptButton)
        self.minutesLabel = QtWidgets.QLabel(StagesDialog)
        self.minutesLabel.setGeometry(QtCore.QRect(490, 675, 166, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.minutesLabel.setFont(font)
        self.minutesLabel.setStyleSheet("color: rgb(62, 64, 149);")
        self.minutesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minutesLabel.setObjectName("minutesLabel")
        self.powerLabel = QtWidgets.QLabel(StagesDialog)
        self.powerLabel.setGeometry(QtCore.QRect(455, 520, 206, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.powerLabel.setFont(font)
        self.powerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.powerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.powerLabel.setObjectName("powerLabel")
        self.date_timeLabel = QtWidgets.QLabel(StagesDialog)
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
        self.diagButton = QtWidgets.QPushButton(StagesDialog)
        self.diagButton.setGeometry(QtCore.QRect(45, 30, 186, 41))
        self.diagButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px")
        self.diagButton.setText("")
        self.diagButton.setObjectName("diagButton")
        self.layoutWidget_6 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(230, 505, 216, 110))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.powerDwnButton = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerDwnButton.sizePolicy().hasHeightForWidth())
        self.powerDwnButton.setSizePolicy(sizePolicy)
        self.powerDwnButton.setMinimumSize(QtCore.QSize(90, 90))
        self.powerDwnButton.setStyleSheet("background-image: url(:/buttons/resources/abajo_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(232, 175, 181);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.powerDwnButton.setText("")
        self.powerDwnButton.setObjectName("powerDwnButton")
        self.horizontalLayout_5.addWidget(self.powerDwnButton)
        self.powerUpButton = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerUpButton.sizePolicy().hasHeightForWidth())
        self.powerUpButton.setSizePolicy(sizePolicy)
        self.powerUpButton.setMinimumSize(QtCore.QSize(90, 90))
        self.powerUpButton.setStyleSheet("background-image: url(:/buttons/resources/arriba_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(214, 137, 155);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.powerUpButton.setText("")
        self.powerUpButton.setObjectName("powerUpButton")
        self.horizontalLayout_5.addWidget(self.powerUpButton)
        self.layoutWidget_7 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget_7.setGeometry(QtCore.QRect(230, 655, 216, 111))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.timeDwnButton = QtWidgets.QPushButton(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeDwnButton.sizePolicy().hasHeightForWidth())
        self.timeDwnButton.setSizePolicy(sizePolicy)
        self.timeDwnButton.setMinimumSize(QtCore.QSize(90, 90))
        self.timeDwnButton.setStyleSheet("background-image: url(:/buttons/resources/abajo_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(195, 211, 247);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.timeDwnButton.setText("")
        self.timeDwnButton.setObjectName("timeDwnButton")
        self.horizontalLayout_6.addWidget(self.timeDwnButton)
        self.timeUpButton = QtWidgets.QPushButton(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeUpButton.sizePolicy().hasHeightForWidth())
        self.timeUpButton.setSizePolicy(sizePolicy)
        self.timeUpButton.setMinimumSize(QtCore.QSize(90, 90))
        self.timeUpButton.setStyleSheet("background-image: url(:/buttons/resources/arriba_90_90.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(134, 152, 188);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.timeUpButton.setText("")
        self.timeUpButton.setObjectName("timeUpButton")
        self.horizontalLayout_6.addWidget(self.timeUpButton)
        self.totalMinutesLabel = QtWidgets.QLabel(StagesDialog)
        self.totalMinutesLabel.setGeometry(QtCore.QRect(340, 95, 166, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.totalMinutesLabel.setFont(font)
        self.totalMinutesLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.totalMinutesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalMinutesLabel.setObjectName("totalMinutesLabel")
        self.stage1Button = QtWidgets.QPushButton(StagesDialog)
        self.stage1Button.setGeometry(QtCore.QRect(25, 205, 200, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1Button.sizePolicy().hasHeightForWidth())
        self.stage1Button.setSizePolicy(sizePolicy)
        self.stage1Button.setMinimumSize(QtCore.QSize(90, 90))
        self.stage1Button.setMaximumSize(QtCore.QSize(200, 270))
        self.stage1Button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.stage1Button.setText("")
        self.stage1Button.setObjectName("stage1Button")
        self.stage2Button = QtWidgets.QPushButton(StagesDialog)
        self.stage2Button.setGeometry(QtCore.QRect(250, 205, 200, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2Button.sizePolicy().hasHeightForWidth())
        self.stage2Button.setSizePolicy(sizePolicy)
        self.stage2Button.setMinimumSize(QtCore.QSize(90, 90))
        self.stage2Button.setMaximumSize(QtCore.QSize(200, 270))
        self.stage2Button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.stage2Button.setText("")
        self.stage2Button.setObjectName("stage2Button")
        self.stage3Button = QtWidgets.QPushButton(StagesDialog)
        self.stage3Button.setGeometry(QtCore.QRect(480, 205, 200, 270))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3Button.sizePolicy().hasHeightForWidth())
        self.stage3Button.setSizePolicy(sizePolicy)
        self.stage3Button.setMinimumSize(QtCore.QSize(90, 90))
        self.stage3Button.setMaximumSize(QtCore.QSize(200, 270))
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.stage3Button.setFont(font)
        self.stage3Button.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.stage3Button.setText("")
        self.stage3Button.setObjectName("stage3Button")
        self.stage1MinutesLabel = QtWidgets.QLabel(StagesDialog)
        self.stage1MinutesLabel.setGeometry(QtCore.QRect(40, 260, 166, 66))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage1MinutesLabel.setFont(font)
        self.stage1MinutesLabel.setStyleSheet("color: rgb(62, 64, 149);")
        self.stage1MinutesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage1MinutesLabel.setObjectName("stage1MinutesLabel")
        self.stage2MinutesLabel = QtWidgets.QLabel(StagesDialog)
        self.stage2MinutesLabel.setGeometry(QtCore.QRect(265, 260, 166, 66))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage2MinutesLabel.setFont(font)
        self.stage2MinutesLabel.setStyleSheet("color: rgb(62, 64, 149);")
        self.stage2MinutesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage2MinutesLabel.setObjectName("stage2MinutesLabel")
        self.stage1PowerLabel = QtWidgets.QLabel(StagesDialog)
        self.stage1PowerLabel.setGeometry(QtCore.QRect(25, 305, 206, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage1PowerLabel.setFont(font)
        self.stage1PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage1PowerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage1PowerLabel.setObjectName("stage1PowerLabel")
        self.stage2PowerLabel = QtWidgets.QLabel(StagesDialog)
        self.stage2PowerLabel.setGeometry(QtCore.QRect(250, 305, 206, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage2PowerLabel.setFont(font)
        self.stage2PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage2PowerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage2PowerLabel.setObjectName("stage2PowerLabel")
        self.stage3PowerLabel = QtWidgets.QLabel(StagesDialog)
        self.stage3PowerLabel.setGeometry(QtCore.QRect(480, 305, 206, 81))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage3PowerLabel.setFont(font)
        self.stage3PowerLabel.setStyleSheet("color: rgb(237, 50, 55);")
        self.stage3PowerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage3PowerLabel.setObjectName("stage3PowerLabel")
        self.stage3MinutesLabel = QtWidgets.QLabel(StagesDialog)
        self.stage3MinutesLabel.setGeometry(QtCore.QRect(495, 260, 166, 66))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.stage3MinutesLabel.setFont(font)
        self.stage3MinutesLabel.setStyleSheet("color: rgb(62, 64, 149);")
        self.stage3MinutesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stage3MinutesLabel.setObjectName("stage3MinutesLabel")
        self.layoutWidget_9 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget_9.setGeometry(QtCore.QRect(255, 380, 191, 91))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stage2SignalButton = QtWidgets.QPushButton(self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2SignalButton.sizePolicy().hasHeightForWidth())
        self.stage2SignalButton.setSizePolicy(sizePolicy)
        self.stage2SignalButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage2SignalButton.setStyleSheet("background-image: url(:/buttons/resources/square_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage2SignalButton.setText("")
        self.stage2SignalButton.setObjectName("stage2SignalButton")
        self.horizontalLayout_8.addWidget(self.stage2SignalButton)
        self.stage2FreqButton = QtWidgets.QPushButton(self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage2FreqButton.sizePolicy().hasHeightForWidth())
        self.stage2FreqButton.setSizePolicy(sizePolicy)
        self.stage2FreqButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage2FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/62_64Hz_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(220, 188, 203);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage2FreqButton.setText("")
        self.stage2FreqButton.setObjectName("stage2FreqButton")
        self.horizontalLayout_8.addWidget(self.stage2FreqButton)
        self.layoutWidget_10 = QtWidgets.QWidget(StagesDialog)
        self.layoutWidget_10.setGeometry(QtCore.QRect(485, 380, 191, 91))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.stage3SignalButton = QtWidgets.QPushButton(self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3SignalButton.sizePolicy().hasHeightForWidth())
        self.stage3SignalButton.setSizePolicy(sizePolicy)
        self.stage3SignalButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage3SignalButton.setStyleSheet("background-image: url(:/buttons/resources/sinus_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage3SignalButton.setText("")
        self.stage3SignalButton.setObjectName("stage3SignalButton")
        self.horizontalLayout_9.addWidget(self.stage3SignalButton)
        self.stage3FreqButton = QtWidgets.QPushButton(self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage3FreqButton.sizePolicy().hasHeightForWidth())
        self.stage3FreqButton.setSizePolicy(sizePolicy)
        self.stage3FreqButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage3FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/86_22Hz_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(220, 188, 203);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage3FreqButton.setText("")
        self.stage3FreqButton.setObjectName("stage3FreqButton")
        self.horizontalLayout_9.addWidget(self.stage3FreqButton)
        self.stage1Label = QtWidgets.QLabel(StagesDialog)
        self.stage1Label.setGeometry(QtCore.QRect(25, 205, 201, 271))
        self.stage1Label.setStyleSheet("background-image: url(:/stage_buttons/resources/stage1_enable.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(254, 254, 254);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage1Label.setText("")
        self.stage1Label.setObjectName("stage1Label")
        self.stage2Label = QtWidgets.QLabel(StagesDialog)
        self.stage2Label.setGeometry(QtCore.QRect(250, 205, 201, 271))
        self.stage2Label.setStyleSheet("background-image: url(:/stage_buttons/resources/stage2_enable.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(254, 254, 254);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage2Label.setText("")
        self.stage2Label.setObjectName("stage2Label")
        self.stage3Label = QtWidgets.QLabel(StagesDialog)
        self.stage3Label.setGeometry(QtCore.QRect(480, 205, 201, 271))
        self.stage3Label.setStyleSheet("background-image: url(:/stage_buttons/resources/stage3_enable.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(254, 254, 254);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage3Label.setText("")
        self.stage3Label.setObjectName("stage3Label")
        self.stage1SignalButton = QtWidgets.QPushButton(StagesDialog)
        self.stage1SignalButton.setGeometry(QtCore.QRect(45, 385, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1SignalButton.sizePolicy().hasHeightForWidth())
        self.stage1SignalButton.setSizePolicy(sizePolicy)
        self.stage1SignalButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage1SignalButton.setStyleSheet("background-image: url(:/buttons/resources/triangular_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(237, 211, 152);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage1SignalButton.setText("")
        self.stage1SignalButton.setObjectName("stage1SignalButton")
        self.stage1FreqButton = QtWidgets.QPushButton(StagesDialog)
        self.stage1FreqButton.setGeometry(QtCore.QRect(135, 385, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stage1FreqButton.sizePolicy().hasHeightForWidth())
        self.stage1FreqButton.setSizePolicy(sizePolicy)
        self.stage1FreqButton.setMinimumSize(QtCore.QSize(75, 75))
        self.stage1FreqButton.setStyleSheet("background-image: url(:/frequencies/resources/0_98Hz_75_75.png);\n"
"background-repeat:no-repeat;\n"
"background-position: center center;\n"
"background-color: rgb(220, 188, 203);\n"
"border-radius: 20px;\n"
"border:3px solid rgb(55, 52, 53);")
        self.stage1FreqButton.setText("")
        self.stage1FreqButton.setObjectName("stage1FreqButton")

        self.retranslateUi(StagesDialog)
        QtCore.QMetaObject.connectSlotsByName(StagesDialog)

    def retranslateUi(self, StagesDialog):
        _translate = QtCore.QCoreApplication.translate
        StagesDialog.setWindowTitle(_translate("StagesDialog", "Dialog"))
        self.clearButton.setText(_translate("StagesDialog", "Clear"))
        self.backButton.setText(_translate("StagesDialog", "Back"))
        self.acceptButton.setText(_translate("StagesDialog", "Accept"))
        self.minutesLabel.setText(_translate("StagesDialog", "120\'"))
        self.powerLabel.setText(_translate("StagesDialog", "100%"))
        self.date_timeLabel.setText(_translate("StagesDialog", "19/03/2020 - 17:45"))
        self.totalMinutesLabel.setText(_translate("StagesDialog", "105"))
        self.stage1MinutesLabel.setText(_translate("StagesDialog", "45\'"))
        self.stage2MinutesLabel.setText(_translate("StagesDialog", "60\'"))
        self.stage1PowerLabel.setText(_translate("StagesDialog", "85%"))
        self.stage2PowerLabel.setText(_translate("StagesDialog", "100%"))
        self.stage3PowerLabel.setText(_translate("StagesDialog", "100%"))
        self.stage3MinutesLabel.setText(_translate("StagesDialog", "60\'"))

import magnet4_res_rc
