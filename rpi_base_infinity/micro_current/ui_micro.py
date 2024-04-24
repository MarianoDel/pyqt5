# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'micro.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.statusFrame = QtWidgets.QFrame(self.frame)
        self.statusFrame.setMinimumSize(QtCore.QSize(0, 100))
        self.statusFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusFrame.setObjectName("statusFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.statusFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(1669, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_menu_open = QtWidgets.QPushButton(self.statusFrame)
        self.bt_menu_open.setMinimumSize(QtCore.QSize(100, 0))
        self.bt_menu_open.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.bt_menu_open.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/go-previous-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_open.setIcon(icon)
        self.bt_menu_open.setIconSize(QtCore.QSize(50, 50))
        self.bt_menu_open.setObjectName("bt_menu_open")
        self.horizontalLayout_2.addWidget(self.bt_menu_open)
        self.bt_menu_close = QtWidgets.QPushButton(self.statusFrame)
        self.bt_menu_close.setMinimumSize(QtCore.QSize(100, 0))
        self.bt_menu_close.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.bt_menu_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/go-next-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu_close.setIcon(icon1)
        self.bt_menu_close.setIconSize(QtCore.QSize(50, 50))
        self.bt_menu_close.setObjectName("bt_menu_close")
        self.horizontalLayout_2.addWidget(self.bt_menu_close)
        self.verticalLayout_2.addWidget(self.statusFrame)
        self.channelsFrame = QtWidgets.QFrame(self.frame)
        self.channelsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.channelsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.channelsFrame.setObjectName("channelsFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.channelsFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.channelsFrame)
        self.frame_2.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setGeometry(QtCore.QRect(1080, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.ch1_pwrLabel = QtWidgets.QLabel(self.groupBox_4)
        self.ch1_pwrLabel.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_pwrLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_pwrLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_pwrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_pwrLabel.setObjectName("ch1_pwrLabel")
        self.ch1_pwrDwnButton = QtWidgets.QPushButton(self.groupBox_4)
        self.ch1_pwrDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch1_pwrDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_pwrDwnButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_pwrDwnButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/go-down-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ch1_pwrDwnButton.setIcon(icon2)
        self.ch1_pwrDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_pwrDwnButton.setObjectName("ch1_pwrDwnButton")
        self.ch1_pwrUpButton = QtWidgets.QPushButton(self.groupBox_4)
        self.ch1_pwrUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch1_pwrUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_pwrUpButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_pwrUpButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/go-up-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ch1_pwrUpButton.setIcon(icon3)
        self.ch1_pwrUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_pwrUpButton.setObjectName("ch1_pwrUpButton")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_5.setGeometry(QtCore.QRect(865, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.ch1_freqLabel = QtWidgets.QLabel(self.groupBox_5)
        self.ch1_freqLabel.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_freqLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_freqLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_freqLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_freqLabel.setObjectName("ch1_freqLabel")
        self.ch1_freqDwnButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ch1_freqDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch1_freqDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_freqDwnButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_freqDwnButton.setText("")
        self.ch1_freqDwnButton.setIcon(icon2)
        self.ch1_freqDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_freqDwnButton.setObjectName("ch1_freqDwnButton")
        self.ch1_freqUpButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ch1_freqUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch1_freqUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_freqUpButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_freqUpButton.setText("")
        self.ch1_freqUpButton.setIcon(icon3)
        self.ch1_freqUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_freqUpButton.setObjectName("ch1_freqUpButton")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_6.setGeometry(QtCore.QRect(650, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.ch1_timerLabel = QtWidgets.QLabel(self.groupBox_6)
        self.ch1_timerLabel.setGeometry(QtCore.QRect(19, 27, 156, 81))
        self.ch1_timerLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_timerLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_timerLabel.setObjectName("ch1_timerLabel")
        self.ch1_timerDwnButton = QtWidgets.QPushButton(self.groupBox_6)
        self.ch1_timerDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch1_timerDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_timerDwnButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_timerDwnButton.setText("")
        self.ch1_timerDwnButton.setIcon(icon2)
        self.ch1_timerDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_timerDwnButton.setObjectName("ch1_timerDwnButton")
        self.ch1_timerUpButton = QtWidgets.QPushButton(self.groupBox_6)
        self.ch1_timerUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch1_timerUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_timerUpButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_timerUpButton.setText("")
        self.ch1_timerUpButton.setIcon(icon3)
        self.ch1_timerUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_timerUpButton.setObjectName("ch1_timerUpButton")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_7.setGeometry(QtCore.QRect(435, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.ch1_posButton = QtWidgets.QPushButton(self.groupBox_7)
        self.ch1_posButton.setGeometry(QtCore.QRect(20, 45, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton.setFont(font)
        self.ch1_posButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch1_posButton.setObjectName("ch1_posButton")
        self.ch1_altButton = QtWidgets.QPushButton(self.groupBox_7)
        self.ch1_altButton.setGeometry(QtCore.QRect(20, 95, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_altButton.setFont(font)
        self.ch1_altButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_altButton.setObjectName("ch1_altButton")
        self.ch1_negButton = QtWidgets.QPushButton(self.groupBox_7)
        self.ch1_negButton.setGeometry(QtCore.QRect(20, 145, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_negButton.setFont(font)
        self.ch1_negButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_negButton.setObjectName("ch1_negButton")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 25, 391, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_8.setObjectName("groupBox_8")
        self.ch1_displayLabel = QtWidgets.QLabel(self.groupBox_8)
        self.ch1_displayLabel.setGeometry(QtCore.QRect(5, 25, 181, 161))
        self.ch1_displayLabel.setStyleSheet("background-color: rgb(157, 205, 255);\n"
"font: 75 65pt \"Liberation Sans\";")
        self.ch1_displayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_displayLabel.setObjectName("ch1_displayLabel")
        self.ch1_gainLabel = QtWidgets.QLabel(self.groupBox_8)
        self.ch1_gainLabel.setGeometry(QtCore.QRect(225, 35, 130, 81))
        self.ch1_gainLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel.setObjectName("ch1_gainLabel")
        self.ch1_gainDwnButton = QtWidgets.QPushButton(self.groupBox_8)
        self.ch1_gainDwnButton.setGeometry(QtCore.QRect(205, 125, 81, 60))
        self.ch1_gainDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_gainDwnButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_gainDwnButton.setText("")
        self.ch1_gainDwnButton.setIcon(icon2)
        self.ch1_gainDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_gainDwnButton.setObjectName("ch1_gainDwnButton")
        self.ch1_gainUpButton = QtWidgets.QPushButton(self.groupBox_8)
        self.ch1_gainUpButton.setGeometry(QtCore.QRect(295, 125, 81, 60))
        self.ch1_gainUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch1_gainUpButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_gainUpButton.setText("")
        self.ch1_gainUpButton.setIcon(icon3)
        self.ch1_gainUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch1_gainUpButton.setObjectName("ch1_gainUpButton")
        self.ch1_displayTextLabel = QtWidgets.QLabel(self.groupBox_8)
        self.ch1_displayTextLabel.setGeometry(QtCore.QRect(15, 25, 161, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_displayTextLabel.setFont(font)
        self.ch1_displayTextLabel.setStyleSheet("background-color: rgb(157, 205, 255);\n"
"color: rgb(85, 170, 255);")
        self.ch1_displayTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_displayTextLabel.setObjectName("ch1_displayTextLabel")
        self.ch1_startButton = QtWidgets.QPushButton(self.frame_2)
        self.ch1_startButton.setGeometry(QtCore.QRect(1300, 50, 101, 156))
        self.ch1_startButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_startButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/pan-start-symbolic-rtl.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ch1_startButton.setIcon(icon4)
        self.ch1_startButton.setIconSize(QtCore.QSize(32, 32))
        self.ch1_startButton.setObjectName("ch1_startButton")
        self.ch1_enableButton = QtWidgets.QPushButton(self.frame_2)
        self.ch1_enableButton.setGeometry(QtCore.QRect(1435, 140, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_enableButton.setFont(font)
        self.ch1_enableButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_enableButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_enableButton.setObjectName("ch1_enableButton")
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_9.setGeometry(QtCore.QRect(1620, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.ch1_probeLabel = QtWidgets.QLabel(self.groupBox_9)
        self.ch1_probeLabel.setGeometry(QtCore.QRect(18, 45, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_probeLabel.setFont(font)
        self.ch1_probeLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch1_probeLabel.setObjectName("ch1_probeLabel")
        self.ch1_stopButton = QtWidgets.QPushButton(self.frame_2)
        self.ch1_stopButton.setGeometry(QtCore.QRect(1300, 130, 101, 76))
        self.ch1_stopButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgb(129, 129, 129);\n"
"/*border: 2px solid red;*/\n"
"border: 2px solid rgb(218, 218, 218);\n"
"}\n"
"")
        self.ch1_stopButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/media-playback-stop-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ch1_stopButton.setIcon(icon5)
        self.ch1_stopButton.setIconSize(QtCore.QSize(32, 32))
        self.ch1_stopButton.setObjectName("ch1_stopButton")
        self.ch1_remainMinsLabel = QtWidgets.QLabel(self.frame_2)
        self.ch1_remainMinsLabel.setGeometry(QtCore.QRect(1285, 50, 81, 76))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_remainMinsLabel.setFont(font)
        self.ch1_remainMinsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ch1_remainMinsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ch1_remainMinsLabel.setObjectName("ch1_remainMinsLabel")
        self.ch1_remainSecsLabel = QtWidgets.QLabel(self.frame_2)
        self.ch1_remainSecsLabel.setGeometry(QtCore.QRect(1370, 55, 96, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_remainSecsLabel.setFont(font)
        self.ch1_remainSecsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ch1_remainSecsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ch1_remainSecsLabel.setObjectName("ch1_remainSecsLabel")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.channelsFrame)
        self.frame_3.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox_10 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_10.setGeometry(QtCore.QRect(435, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_10.setObjectName("groupBox_10")
        self.ch2_posButton = QtWidgets.QPushButton(self.groupBox_10)
        self.ch2_posButton.setGeometry(QtCore.QRect(20, 45, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_posButton.setFont(font)
        self.ch2_posButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch2_posButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_posButton.setObjectName("ch2_posButton")
        self.ch2_altButton = QtWidgets.QPushButton(self.groupBox_10)
        self.ch2_altButton.setGeometry(QtCore.QRect(20, 95, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_altButton.setFont(font)
        self.ch2_altButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch2_altButton.setObjectName("ch2_altButton")
        self.ch2_negButton = QtWidgets.QPushButton(self.groupBox_10)
        self.ch2_negButton.setGeometry(QtCore.QRect(20, 145, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_negButton.setFont(font)
        self.ch2_negButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch2_negButton.setObjectName("ch2_negButton")
        self.groupBox_11 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_11.setGeometry(QtCore.QRect(1080, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.ch2_pwrLabel = QtWidgets.QLabel(self.groupBox_11)
        self.ch2_pwrLabel.setGeometry(QtCore.QRect(14, 27, 166, 81))
        self.ch2_pwrLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch2_pwrLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch2_pwrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_pwrLabel.setObjectName("ch2_pwrLabel")
        self.ch2_pwrDwnButton = QtWidgets.QPushButton(self.groupBox_11)
        self.ch2_pwrDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch2_pwrDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_pwrDwnButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_pwrDwnButton.setText("")
        self.ch2_pwrDwnButton.setIcon(icon2)
        self.ch2_pwrDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_pwrDwnButton.setObjectName("ch2_pwrDwnButton")
        self.ch2_pwrUpButton = QtWidgets.QPushButton(self.groupBox_11)
        self.ch2_pwrUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch2_pwrUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_pwrUpButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_pwrUpButton.setText("")
        self.ch2_pwrUpButton.setIcon(icon3)
        self.ch2_pwrUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_pwrUpButton.setObjectName("ch2_pwrUpButton")
        self.groupBox_12 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 20, 391, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_12.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_12.setObjectName("groupBox_12")
        self.ch2_displayLabel = QtWidgets.QLabel(self.groupBox_12)
        self.ch2_displayLabel.setGeometry(QtCore.QRect(5, 25, 181, 161))
        self.ch2_displayLabel.setStyleSheet("background-color: rgb(157, 205, 255);\n"
"font: 75 65pt \"Liberation Sans\";")
        self.ch2_displayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_displayLabel.setObjectName("ch2_displayLabel")
        self.ch2_gainLabel = QtWidgets.QLabel(self.groupBox_12)
        self.ch2_gainLabel.setGeometry(QtCore.QRect(225, 35, 130, 81))
        self.ch2_gainLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch2_gainLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch2_gainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_gainLabel.setObjectName("ch2_gainLabel")
        self.ch2_gainDwnButton = QtWidgets.QPushButton(self.groupBox_12)
        self.ch2_gainDwnButton.setGeometry(QtCore.QRect(205, 125, 81, 60))
        self.ch2_gainDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_gainDwnButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_gainDwnButton.setText("")
        self.ch2_gainDwnButton.setIcon(icon2)
        self.ch2_gainDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_gainDwnButton.setObjectName("ch2_gainDwnButton")
        self.ch2_gainUpButton = QtWidgets.QPushButton(self.groupBox_12)
        self.ch2_gainUpButton.setGeometry(QtCore.QRect(295, 125, 81, 60))
        self.ch2_gainUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_gainUpButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_gainUpButton.setText("")
        self.ch2_gainUpButton.setIcon(icon3)
        self.ch2_gainUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_gainUpButton.setObjectName("ch2_gainUpButton")
        self.groupBox_13 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_13.setGeometry(QtCore.QRect(865, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_13.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_13.setObjectName("groupBox_13")
        self.ch2_freqLabel = QtWidgets.QLabel(self.groupBox_13)
        self.ch2_freqLabel.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch2_freqLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch2_freqLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch2_freqLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_freqLabel.setObjectName("ch2_freqLabel")
        self.ch2_freqDwnButton = QtWidgets.QPushButton(self.groupBox_13)
        self.ch2_freqDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch2_freqDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_freqDwnButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_freqDwnButton.setText("")
        self.ch2_freqDwnButton.setIcon(icon2)
        self.ch2_freqDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_freqDwnButton.setObjectName("ch2_freqDwnButton")
        self.ch2_freqUpButton = QtWidgets.QPushButton(self.groupBox_13)
        self.ch2_freqUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch2_freqUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_freqUpButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_freqUpButton.setText("")
        self.ch2_freqUpButton.setIcon(icon3)
        self.ch2_freqUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_freqUpButton.setObjectName("ch2_freqUpButton")
        self.ch2_enableButton = QtWidgets.QPushButton(self.frame_3)
        self.ch2_enableButton.setGeometry(QtCore.QRect(1435, 135, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_enableButton.setFont(font)
        self.ch2_enableButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch2_enableButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_enableButton.setObjectName("ch2_enableButton")
        self.ch2_startButton = QtWidgets.QPushButton(self.frame_3)
        self.ch2_startButton.setGeometry(QtCore.QRect(1300, 45, 101, 156))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_startButton.setFont(font)
        self.ch2_startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ch2_startButton.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"")
        self.ch2_startButton.setText("")
        self.ch2_startButton.setIcon(icon4)
        self.ch2_startButton.setIconSize(QtCore.QSize(32, 32))
        self.ch2_startButton.setObjectName("ch2_startButton")
        self.groupBox_14 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_14.setGeometry(QtCore.QRect(650, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_14.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_14.setObjectName("groupBox_14")
        self.ch2_timerLabel = QtWidgets.QLabel(self.groupBox_14)
        self.ch2_timerLabel.setGeometry(QtCore.QRect(19, 27, 156, 81))
        self.ch2_timerLabel.setMinimumSize(QtCore.QSize(130, 80))
        self.ch2_timerLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch2_timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_timerLabel.setObjectName("ch2_timerLabel")
        self.ch2_timerDwnButton = QtWidgets.QPushButton(self.groupBox_14)
        self.ch2_timerDwnButton.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.ch2_timerDwnButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_timerDwnButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_timerDwnButton.setText("")
        self.ch2_timerDwnButton.setIcon(icon2)
        self.ch2_timerDwnButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_timerDwnButton.setObjectName("ch2_timerDwnButton")
        self.ch2_timerUpButton = QtWidgets.QPushButton(self.groupBox_14)
        self.ch2_timerUpButton.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.ch2_timerUpButton.setMinimumSize(QtCore.QSize(60, 60))
        self.ch2_timerUpButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_timerUpButton.setText("")
        self.ch2_timerUpButton.setIcon(icon3)
        self.ch2_timerUpButton.setIconSize(QtCore.QSize(50, 50))
        self.ch2_timerUpButton.setObjectName("ch2_timerUpButton")
        self.groupBox_15 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_15.setGeometry(QtCore.QRect(1620, 15, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_15.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_15.setObjectName("groupBox_15")
        self.ch2_probeLabel = QtWidgets.QLabel(self.groupBox_15)
        self.ch2_probeLabel.setGeometry(QtCore.QRect(18, 45, 151, 131))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_probeLabel.setFont(font)
        self.ch2_probeLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch2_probeLabel.setObjectName("ch2_probeLabel")
        self.ch2_linkButton = QtWidgets.QPushButton(self.frame_3)
        self.ch2_linkButton.setGeometry(QtCore.QRect(1435, 55, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_linkButton.setFont(font)
        self.ch2_linkButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch2_linkButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch2_linkButton.setObjectName("ch2_linkButton")
        self.frame_2.raise_()
        self.frame_2.raise_()
        self.groupBox_10.raise_()
        self.groupBox_11.raise_()
        self.groupBox_12.raise_()
        self.groupBox_13.raise_()
        self.ch2_enableButton.raise_()
        self.ch2_startButton.raise_()
        self.groupBox_14.raise_()
        self.groupBox_15.raise_()
        self.ch2_linkButton.raise_()
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.channelsFrame)
        self.frame_4.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.groupBox_16 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_16.setGeometry(QtCore.QRect(15, 25, 196, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_16.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_16.setObjectName("groupBox_16")
        self.ch1_displayLabel_3 = QtWidgets.QLabel(self.groupBox_16)
        self.ch1_displayLabel_3.setGeometry(QtCore.QRect(5, 25, 181, 161))
        self.ch1_displayLabel_3.setStyleSheet("background-color: rgb(157, 205, 255);\n"
"font: 75 65pt \"Liberation Sans\";")
        self.ch1_displayLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_displayLabel_3.setObjectName("ch1_displayLabel_3")
        self.groupBox_17 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_17.setGeometry(QtCore.QRect(235, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_17.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_16.setGeometry(QtCore.QRect(20, 45, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_16.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_29.setGeometry(QtCore.QRect(20, 95, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_30.setGeometry(QtCore.QRect(20, 145, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_31.setGeometry(QtCore.QRect(1230, 140, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_31.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_31.setObjectName("pushButton_31")
        self.groupBox_18 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_18.setGeometry(QtCore.QRect(660, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_18.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.ch1_gainLabel_13 = QtWidgets.QLabel(self.groupBox_18)
        self.ch1_gainLabel_13.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_gainLabel_13.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_13.setObjectName("ch1_gainLabel_13")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_32.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_32.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_32.setText("")
        self.pushButton_32.setIcon(icon2)
        self.pushButton_32.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_33.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_33.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_33.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_33.setText("")
        self.pushButton_33.setIcon(icon3)
        self.pushButton_33.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_33.setObjectName("pushButton_33")
        self.groupBox_19 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_19.setGeometry(QtCore.QRect(445, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_19.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_19.setObjectName("groupBox_19")
        self.ch1_gainLabel_14 = QtWidgets.QLabel(self.groupBox_19)
        self.ch1_gainLabel_14.setGeometry(QtCore.QRect(19, 27, 156, 81))
        self.ch1_gainLabel_14.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_14.setObjectName("ch1_gainLabel_14")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_19)
        self.pushButton_34.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_34.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_34.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_34.setText("")
        self.pushButton_34.setIcon(icon2)
        self.pushButton_34.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_19)
        self.pushButton_35.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_35.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_35.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_35.setText("")
        self.pushButton_35.setIcon(icon3)
        self.pushButton_35.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_36.setGeometry(QtCore.QRect(1095, 50, 101, 156))
        self.pushButton_36.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_36.setText("")
        self.pushButton_36.setIcon(icon4)
        self.pushButton_36.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_36.setObjectName("pushButton_36")
        self.groupBox_20 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_20.setGeometry(QtCore.QRect(875, 25, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_20.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_20.setObjectName("groupBox_20")
        self.ch1_gainLabel_15 = QtWidgets.QLabel(self.groupBox_20)
        self.ch1_gainLabel_15.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_gainLabel_15.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_15.setObjectName("ch1_gainLabel_15")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_37.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_37.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_37.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_37.setText("")
        self.pushButton_37.setIcon(icon2)
        self.pushButton_37.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_38.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_38.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_38.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_38.setText("")
        self.pushButton_38.setIcon(icon3)
        self.pushButton_38.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_38.setObjectName("pushButton_38")
        self.groupBox_21 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_21.setGeometry(QtCore.QRect(1620, 115, 191, 96))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_21.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_21.setObjectName("groupBox_21")
        self.label_3 = QtWidgets.QLabel(self.groupBox_21)
        self.label_3.setGeometry(QtCore.QRect(20, 35, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar_2.setGeometry(QtCore.QRect(1235, 60, 571, 36))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"    border: 2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"    text-align: right;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"}")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.frame_3.raise_()
        self.frame_3.raise_()
        self.frame_3.raise_()
        self.groupBox_16.raise_()
        self.groupBox_17.raise_()
        self.pushButton_31.raise_()
        self.groupBox_18.raise_()
        self.groupBox_19.raise_()
        self.pushButton_36.raise_()
        self.groupBox_20.raise_()
        self.groupBox_21.raise_()
        self.progressBar_2.raise_()
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.channelsFrame)
        self.frame_5.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.groupBox_22 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_22.setGeometry(QtCore.QRect(235, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_22.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_22.setObjectName("groupBox_22")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_39.setGeometry(QtCore.QRect(20, 45, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_39.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_40.setGeometry(QtCore.QRect(20, 95, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_41.setGeometry(QtCore.QRect(20, 145, 146, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_41.setObjectName("pushButton_41")
        self.groupBox_23 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_23.setGeometry(QtCore.QRect(660, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_23.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_23.setObjectName("groupBox_23")
        self.ch1_gainLabel_16 = QtWidgets.QLabel(self.groupBox_23)
        self.ch1_gainLabel_16.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_gainLabel_16.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_16.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_16.setObjectName("ch1_gainLabel_16")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_23)
        self.pushButton_42.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_42.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_42.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_42.setText("")
        self.pushButton_42.setIcon(icon2)
        self.pushButton_42.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_23)
        self.pushButton_43.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_43.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_43.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_43.setText("")
        self.pushButton_43.setIcon(icon3)
        self.pushButton_43.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_44.setGeometry(QtCore.QRect(1230, 135, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_44.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_44.setObjectName("pushButton_44")
        self.groupBox_24 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_24.setGeometry(QtCore.QRect(445, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_24.setFont(font)
        self.groupBox_24.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_24.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_24.setObjectName("groupBox_24")
        self.ch1_gainLabel_17 = QtWidgets.QLabel(self.groupBox_24)
        self.ch1_gainLabel_17.setGeometry(QtCore.QRect(19, 27, 156, 81))
        self.ch1_gainLabel_17.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_17.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_17.setObjectName("ch1_gainLabel_17")
        self.pushButton_45 = QtWidgets.QPushButton(self.groupBox_24)
        self.pushButton_45.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_45.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_45.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_45.setText("")
        self.pushButton_45.setIcon(icon2)
        self.pushButton_45.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_24)
        self.pushButton_46.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_46.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_46.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_46.setText("")
        self.pushButton_46.setIcon(icon3)
        self.pushButton_46.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_46.setObjectName("pushButton_46")
        self.groupBox_25 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_25.setGeometry(QtCore.QRect(1620, 110, 191, 96))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_25.setFont(font)
        self.groupBox_25.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_25.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_25.setObjectName("groupBox_25")
        self.label_4 = QtWidgets.QLabel(self.groupBox_25)
        self.label_4.setGeometry(QtCore.QRect(20, 35, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox_26 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_26.setGeometry(QtCore.QRect(875, 20, 191, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_26.setFont(font)
        self.groupBox_26.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_26.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_26.setObjectName("groupBox_26")
        self.ch1_gainLabel_18 = QtWidgets.QLabel(self.groupBox_26)
        self.ch1_gainLabel_18.setGeometry(QtCore.QRect(14, 27, 161, 81))
        self.ch1_gainLabel_18.setMinimumSize(QtCore.QSize(130, 80))
        self.ch1_gainLabel_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Liberation Sans\";")
        self.ch1_gainLabel_18.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_gainLabel_18.setObjectName("ch1_gainLabel_18")
        self.pushButton_47 = QtWidgets.QPushButton(self.groupBox_26)
        self.pushButton_47.setGeometry(QtCore.QRect(10, 124, 81, 60))
        self.pushButton_47.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_47.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_47.setText("")
        self.pushButton_47.setIcon(icon2)
        self.pushButton_47.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox_26)
        self.pushButton_48.setGeometry(QtCore.QRect(100, 125, 81, 60))
        self.pushButton_48.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton_48.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_48.setText("")
        self.pushButton_48.setIcon(icon3)
        self.pushButton_48.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_48.setObjectName("pushButton_48")
        self.groupBox_27 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_27.setGeometry(QtCore.QRect(15, 20, 196, 196))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_27.setFont(font)
        self.groupBox_27.setStyleSheet("QGroupBox{\n"
"border: 2px solid red;\n"
"margin-top: 12px;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"/*subcontrol-origin: top right;*/\n"
"subcontrol-position: top center;\n"
"padding: 0 3px 0 3px;\n"
"top: -8px;\n"
"}")
        self.groupBox_27.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_27.setObjectName("groupBox_27")
        self.ch1_displayLabel_4 = QtWidgets.QLabel(self.groupBox_27)
        self.ch1_displayLabel_4.setGeometry(QtCore.QRect(5, 25, 181, 161))
        self.ch1_displayLabel_4.setStyleSheet("background-color: rgb(157, 205, 255);\n"
"font: 75 65pt \"Liberation Sans\";")
        self.ch1_displayLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_displayLabel_4.setObjectName("ch1_displayLabel_4")
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_49.setGeometry(QtCore.QRect(1095, 45, 101, 156))
        self.pushButton_49.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_49.setText("")
        self.pushButton_49.setIcon(icon4)
        self.pushButton_49.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_50.setGeometry(QtCore.QRect(1415, 135, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_50.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_50.setObjectName("pushButton_50")
        self.progressBar = QtWidgets.QProgressBar(self.frame_5)
        self.progressBar.setGeometry(QtCore.QRect(1235, 55, 571, 36))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"    text-align: right;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.lateralMenu = QtWidgets.QFrame(self.channelsFrame)
        self.lateralMenu.setMinimumSize(QtCore.QSize(0, 0))
        self.lateralMenu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.lateralMenu.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.lateralMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lateralMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lateralMenu.setObjectName("lateralMenu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.lateralMenu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.lateralMenu)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.audioButton = QtWidgets.QPushButton(self.frame_7)
        self.audioButton.setMinimumSize(QtCore.QSize(0, 50))
        self.audioButton.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.audioButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/audio-speakers-symbolic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audioButton.setIcon(icon6)
        self.audioButton.setIconSize(QtCore.QSize(32, 32))
        self.audioButton.setObjectName("audioButton")
        self.verticalLayout_7.addWidget(self.audioButton)
        self.logButton = QtWidgets.QPushButton(self.frame_7)
        self.logButton.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.logButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/resources/view-paged-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logButton.setIcon(icon7)
        self.logButton.setIconSize(QtCore.QSize(50, 50))
        self.logButton.setObjectName("logButton")
        self.verticalLayout_7.addWidget(self.logButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.configButton = QtWidgets.QPushButton(self.frame_7)
        self.configButton.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.configButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/resources/system-run-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configButton.setIcon(icon8)
        self.configButton.setIconSize(QtCore.QSize(50, 50))
        self.configButton.setObjectName("configButton")
        self.verticalLayout_6.addWidget(self.configButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.pushButton_6.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/resources/insert-link-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.lateralMenu)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_audio = QtWidgets.QWidget()
        self.page_audio.setObjectName("page_audio")
        self.ch1_posButton_2 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_2.setGeometry(QtCore.QRect(15, 50, 86, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_2.setFont(font)
        self.ch1_posButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch1_posButton_2.setObjectName("ch1_posButton_2")
        self.label = QtWidgets.QLabel(self.page_audio)
        self.label.setGeometry(QtCore.QRect(20, 10, 266, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ch1_posButton_3 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_3.setGeometry(QtCore.QRect(120, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_3.setFont(font)
        self.ch1_posButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_3.setStyleSheet("")
        self.ch1_posButton_3.setObjectName("ch1_posButton_3")
        self.ch1_posButton_4 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_4.setGeometry(QtCore.QRect(225, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_4.setFont(font)
        self.ch1_posButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_4.setStyleSheet("")
        self.ch1_posButton_4.setObjectName("ch1_posButton_4")
        self.ch1_posButton_5 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_5.setGeometry(QtCore.QRect(325, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_5.setFont(font)
        self.ch1_posButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_5.setStyleSheet("")
        self.ch1_posButton_5.setObjectName("ch1_posButton_5")
        self.label_2 = QtWidgets.QLabel(self.page_audio)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 246, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.page_audio)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 160, 291, 36))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QtWidgets.QLabel(self.page_audio)
        self.label_5.setGeometry(QtCore.QRect(340, 165, 56, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_audio)
        self.label_6.setGeometry(QtCore.QRect(20, 215, 266, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ch1_posButton_6 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_6.setGeometry(QtCore.QRect(20, 260, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_6.setFont(font)
        self.ch1_posButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_6.setStyleSheet("")
        self.ch1_posButton_6.setObjectName("ch1_posButton_6")
        self.ch1_posButton_7 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_7.setGeometry(QtCore.QRect(20, 315, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_7.setFont(font)
        self.ch1_posButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_7.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.ch1_posButton_7.setObjectName("ch1_posButton_7")
        self.ch1_posButton_8 = QtWidgets.QPushButton(self.page_audio)
        self.ch1_posButton_8.setGeometry(QtCore.QRect(20, 370, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_posButton_8.setFont(font)
        self.ch1_posButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch1_posButton_8.setStyleSheet("")
        self.ch1_posButton_8.setObjectName("ch1_posButton_8")
        self.stackedWidget.addWidget(self.page_audio)
        self.page_log = QtWidgets.QWidget()
        self.page_log.setObjectName("page_log")
        self.textEdit = QtWidgets.QTextEdit(self.page_log)
        self.textEdit.setGeometry(QtCore.QRect(5, 45, 401, 651))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.page_log)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 286, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_log)
        self.page_config = QtWidgets.QWidget()
        self.page_config.setObjectName("page_config")
        self.label_8 = QtWidgets.QLabel(self.page_config)
        self.label_8.setGeometry(QtCore.QRect(10, 5, 356, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_51 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_51.setGeometry(QtCore.QRect(10, 70, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_51.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_52.setGeometry(QtCore.QRect(10, 145, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_52.setStyleSheet("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_53.setGeometry(QtCore.QRect(10, 310, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_53.setStyleSheet("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_54.setGeometry(QtCore.QRect(10, 235, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_54.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_55.setGeometry(QtCore.QRect(10, 475, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_55.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_56.setGeometry(QtCore.QRect(10, 400, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_56.setStyleSheet("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_57.setGeometry(QtCore.QRect(10, 640, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_57.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.page_config)
        self.pushButton_58.setGeometry(QtCore.QRect(10, 565, 396, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_58.setStyleSheet("\n"
"")
        self.pushButton_58.setObjectName("pushButton_58")
        self.stackedWidget.addWidget(self.page_config)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.lateralMenu)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.channelsFrame)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Intensity"))
        self.ch1_pwrLabel.setText(_translate("MainWindow", "100uA"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Frequency"))
        self.ch1_freqLabel.setText(_translate("MainWindow", "100Hz"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Timer"))
        self.ch1_timerLabel.setText(_translate("MainWindow", "100s"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Polarity"))
        self.ch1_posButton.setText(_translate("MainWindow", "Positive"))
        self.ch1_altButton.setText(_translate("MainWindow", "Alternative"))
        self.ch1_negButton.setText(_translate("MainWindow", "Negative"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Gain Spectrum"))
        self.ch1_displayLabel.setText(_translate("MainWindow", "100"))
        self.ch1_gainLabel.setText(_translate("MainWindow", "100"))
        self.ch1_displayTextLabel.setText(_translate("MainWindow", "Offline Gain"))
        self.ch1_enableButton.setText(_translate("MainWindow", "Enable Channel"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Probe"))
        self.ch1_probeLabel.setText(_translate("MainWindow", "Normal Probe"))
        self.ch1_remainMinsLabel.setText(_translate("MainWindow", "22\'"))
        self.ch1_remainSecsLabel.setText(_translate("MainWindow", "22\'\'"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Polarity"))
        self.ch2_posButton.setText(_translate("MainWindow", "Positive"))
        self.ch2_altButton.setText(_translate("MainWindow", "Alternative"))
        self.ch2_negButton.setText(_translate("MainWindow", "Negative"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Intensity"))
        self.ch2_pwrLabel.setText(_translate("MainWindow", "100uA"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Gain Spectrum"))
        self.ch2_displayLabel.setText(_translate("MainWindow", "100"))
        self.ch2_gainLabel.setText(_translate("MainWindow", "100"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Frequency"))
        self.ch2_freqLabel.setText(_translate("MainWindow", "100Hz"))
        self.ch2_enableButton.setText(_translate("MainWindow", "Enable Channel"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Timer"))
        self.ch2_timerLabel.setText(_translate("MainWindow", "100s"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Probe"))
        self.ch2_probeLabel.setText(_translate("MainWindow", "Normal Probe"))
        self.ch2_linkButton.setText(_translate("MainWindow", "Link To Ch1"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Gain"))
        self.ch1_displayLabel_3.setText(_translate("MainWindow", "100"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Polarity"))
        self.pushButton_16.setText(_translate("MainWindow", "Positive"))
        self.pushButton_29.setText(_translate("MainWindow", "Alternative"))
        self.pushButton_30.setText(_translate("MainWindow", "Negative"))
        self.pushButton_31.setText(_translate("MainWindow", "Enable Channel"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Frequency"))
        self.ch1_gainLabel_13.setText(_translate("MainWindow", "100Hz"))
        self.groupBox_19.setTitle(_translate("MainWindow", "Timer"))
        self.ch1_gainLabel_14.setText(_translate("MainWindow", "100s"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Intensity"))
        self.ch1_gainLabel_15.setText(_translate("MainWindow", "100uA"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Probe"))
        self.label_3.setText(_translate("MainWindow", "Normal Probe"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p%"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Polarity"))
        self.pushButton_39.setText(_translate("MainWindow", "Positive"))
        self.pushButton_40.setText(_translate("MainWindow", "Alternative"))
        self.pushButton_41.setText(_translate("MainWindow", "Negative"))
        self.groupBox_23.setTitle(_translate("MainWindow", "Frequency"))
        self.ch1_gainLabel_16.setText(_translate("MainWindow", "100Hz"))
        self.pushButton_44.setText(_translate("MainWindow", "Enable Channel"))
        self.groupBox_24.setTitle(_translate("MainWindow", "Timer"))
        self.ch1_gainLabel_17.setText(_translate("MainWindow", "100s"))
        self.groupBox_25.setTitle(_translate("MainWindow", "Probe"))
        self.label_4.setText(_translate("MainWindow", "Normal Probe"))
        self.groupBox_26.setTitle(_translate("MainWindow", "Intensity"))
        self.ch1_gainLabel_18.setText(_translate("MainWindow", "100uA"))
        self.groupBox_27.setTitle(_translate("MainWindow", "Gain"))
        self.ch1_displayLabel_4.setText(_translate("MainWindow", "100"))
        self.pushButton_50.setText(_translate("MainWindow", "Link To Ch3"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.ch1_posButton_2.setText(_translate("MainWindow", "CH1"))
        self.label.setText(_translate("MainWindow", "Audio Output for channel:"))
        self.ch1_posButton_3.setText(_translate("MainWindow", "CH2"))
        self.ch1_posButton_4.setText(_translate("MainWindow", "CH3"))
        self.ch1_posButton_5.setText(_translate("MainWindow", "CH4"))
        self.label_2.setText(_translate("MainWindow", "Audio Volume:"))
        self.label_5.setText(_translate("MainWindow", "100%"))
        self.label_6.setText(_translate("MainWindow", "Audio options:"))
        self.ch1_posButton_6.setText(_translate("MainWindow", "Full audio"))
        self.ch1_posButton_7.setText(_translate("MainWindow", "Start Stop audio"))
        self.ch1_posButton_8.setText(_translate("MainWindow", "No audio"))
        self.label_7.setText(_translate("MainWindow", "System Log:"))
        self.label_8.setText(_translate("MainWindow", "Device Configurations:"))
        self.pushButton_51.setText(_translate("MainWindow", "CH1 Acuscope"))
        self.pushButton_52.setText(_translate("MainWindow", "CH1 Myopulse"))
        self.pushButton_53.setText(_translate("MainWindow", "CH2 Myopulse"))
        self.pushButton_54.setText(_translate("MainWindow", "CH2 Acuscope"))
        self.pushButton_55.setText(_translate("MainWindow", "CH3 Myopulse"))
        self.pushButton_56.setText(_translate("MainWindow", "CH3 Acuscope"))
        self.pushButton_57.setText(_translate("MainWindow", "CH4 Myopulse"))
        self.pushButton_58.setText(_translate("MainWindow", "CH4 Acuscope"))

import microc_res_rc
