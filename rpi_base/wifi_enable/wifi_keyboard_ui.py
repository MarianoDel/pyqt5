# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifi_keyboard_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyboardDialog(object):
    def setupUi(self, KeyboardDialog):
        KeyboardDialog.setObjectName("KeyboardDialog")
        KeyboardDialog.resize(1280, 800)
        KeyboardDialog.setStyleSheet("")
        self.shiftshortButton = QtWidgets.QPushButton(KeyboardDialog)
        self.shiftshortButton.setGeometry(QtCore.QRect(50, 690, 100, 100))
        self.shiftshortButton.setMinimumSize(QtCore.QSize(100, 100))
        self.shiftshortButton.setStyleSheet("background-image: url(:/symbols/resources/shift.png);\n"
"background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.shiftshortButton.setText("")
        self.shiftshortButton.setObjectName("shiftshortButton")
        self.Button_1 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_1.setGeometry(QtCore.QRect(50, 360, 100, 100))
        self.Button_1.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_1.setObjectName("Button_1")
        self.shiftlongButton = QtWidgets.QPushButton(KeyboardDialog)
        self.shiftlongButton.setGeometry(QtCore.QRect(165, 690, 100, 100))
        self.shiftlongButton.setMinimumSize(QtCore.QSize(100, 100))
        self.shiftlongButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"background-image: url(:/symbols/resources/shift_long.png);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.shiftlongButton.setText("")
        self.shiftlongButton.setObjectName("shiftlongButton")
        self.symbolsButton = QtWidgets.QPushButton(KeyboardDialog)
        self.symbolsButton.setGeometry(QtCore.QRect(290, 690, 200, 100))
        self.symbolsButton.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.symbolsButton.setFont(font)
        self.symbolsButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.symbolsButton.setObjectName("symbolsButton")
        self.spaceButton = QtWidgets.QPushButton(KeyboardDialog)
        self.spaceButton.setGeometry(QtCore.QRect(530, 690, 400, 100))
        self.spaceButton.setMinimumSize(QtCore.QSize(400, 100))
        self.spaceButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);")
        self.spaceButton.setText("")
        self.spaceButton.setObjectName("spaceButton")
        self.cancelButton = QtWidgets.QPushButton(KeyboardDialog)
        self.cancelButton.setGeometry(QtCore.QRect(975, 690, 200, 100))
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
        self.Button_2 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_2.setGeometry(QtCore.QRect(165, 360, 100, 100))
        self.Button_2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_2.setObjectName("Button_2")
        self.Button_4 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_4.setGeometry(QtCore.QRect(395, 360, 100, 100))
        self.Button_4.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_4.setFont(font)
        self.Button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_4.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_4.setObjectName("Button_4")
        self.Button_3 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_3.setGeometry(QtCore.QRect(280, 360, 100, 100))
        self.Button_3.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_3.setObjectName("Button_3")
        self.Button_7 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_7.setGeometry(QtCore.QRect(740, 360, 100, 100))
        self.Button_7.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_7.setFont(font)
        self.Button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_7.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_7.setObjectName("Button_7")
        self.Button_6 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_6.setGeometry(QtCore.QRect(625, 360, 100, 100))
        self.Button_6.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_6.setFont(font)
        self.Button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_6.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_5.setGeometry(QtCore.QRect(510, 360, 100, 100))
        self.Button_5.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_5.setFont(font)
        self.Button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_5.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_5.setObjectName("Button_5")
        self.Button_8 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_8.setGeometry(QtCore.QRect(855, 360, 100, 100))
        self.Button_8.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_8.setFont(font)
        self.Button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_8.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_9.setGeometry(QtCore.QRect(970, 360, 100, 100))
        self.Button_9.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_9.setFont(font)
        self.Button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_9.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_9.setObjectName("Button_9")
        self.Button_10 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_10.setGeometry(QtCore.QRect(1085, 360, 100, 100))
        self.Button_10.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_10.setFont(font)
        self.Button_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_10.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_10.setObjectName("Button_10")
        self.Button_13 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_13.setGeometry(QtCore.QRect(280, 470, 100, 100))
        self.Button_13.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_13.setFont(font)
        self.Button_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_13.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_13.setObjectName("Button_13")
        self.Button_12 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_12.setGeometry(QtCore.QRect(165, 470, 100, 100))
        self.Button_12.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_12.setFont(font)
        self.Button_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_12.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_12.setObjectName("Button_12")
        self.Button_15 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_15.setGeometry(QtCore.QRect(510, 470, 100, 100))
        self.Button_15.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_15.setFont(font)
        self.Button_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_15.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_15.setObjectName("Button_15")
        self.Button_11 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_11.setGeometry(QtCore.QRect(50, 470, 100, 100))
        self.Button_11.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_11.setFont(font)
        self.Button_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_11.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_11.setObjectName("Button_11")
        self.Button_14 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_14.setGeometry(QtCore.QRect(395, 470, 100, 100))
        self.Button_14.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_14.setFont(font)
        self.Button_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_14.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_14.setObjectName("Button_14")
        self.Button_16 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_16.setGeometry(QtCore.QRect(625, 470, 100, 100))
        self.Button_16.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_16.setFont(font)
        self.Button_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_16.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_16.setObjectName("Button_16")
        self.backButton = QtWidgets.QPushButton(KeyboardDialog)
        self.backButton.setGeometry(QtCore.QRect(1085, 470, 100, 100))
        self.backButton.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"background-image: url(:/symbols/resources/backspace.png);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.Button_18 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_18.setGeometry(QtCore.QRect(855, 470, 100, 100))
        self.Button_18.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_18.setFont(font)
        self.Button_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_18.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_18.setObjectName("Button_18")
        self.Button_17 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_17.setGeometry(QtCore.QRect(740, 470, 100, 100))
        self.Button_17.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_17.setFont(font)
        self.Button_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_17.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_17.setObjectName("Button_17")
        self.Button_19 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_19.setGeometry(QtCore.QRect(970, 470, 100, 100))
        self.Button_19.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_19.setFont(font)
        self.Button_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_19.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_19.setObjectName("Button_19")
        self.Button_23 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_23.setGeometry(QtCore.QRect(395, 580, 100, 100))
        self.Button_23.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_23.setFont(font)
        self.Button_23.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_23.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_23.setObjectName("Button_23")
        self.Button_24 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_24.setGeometry(QtCore.QRect(510, 580, 100, 100))
        self.Button_24.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_24.setFont(font)
        self.Button_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_24.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_24.setObjectName("Button_24")
        self.Button_25 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_25.setGeometry(QtCore.QRect(625, 580, 100, 100))
        self.Button_25.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_25.setFont(font)
        self.Button_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_25.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_25.setObjectName("Button_25")
        self.Button_22 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_22.setGeometry(QtCore.QRect(280, 580, 100, 100))
        self.Button_22.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_22.setFont(font)
        self.Button_22.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_22.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_22.setObjectName("Button_22")
        self.Button_20 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_20.setGeometry(QtCore.QRect(50, 580, 100, 100))
        self.Button_20.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_20.setFont(font)
        self.Button_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_20.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_20.setObjectName("Button_20")
        self.Button_21 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_21.setGeometry(QtCore.QRect(165, 580, 100, 100))
        self.Button_21.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_21.setFont(font)
        self.Button_21.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_21.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_21.setObjectName("Button_21")
        self.Button_27 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_27.setGeometry(QtCore.QRect(855, 580, 100, 100))
        self.Button_27.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_27.setFont(font)
        self.Button_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_27.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_27.setObjectName("Button_27")
        self.Button_26 = QtWidgets.QPushButton(KeyboardDialog)
        self.Button_26.setGeometry(QtCore.QRect(740, 580, 100, 100))
        self.Button_26.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Button_26.setFont(font)
        self.Button_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_26.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.Button_26.setObjectName("Button_26")
        self.configEdit = QtWidgets.QLineEdit(KeyboardDialog)
        self.configEdit.setGeometry(QtCore.QRect(120, 255, 996, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.configEdit.setFont(font)
        self.configEdit.setStyleSheet("color: rgb(55, 52, 53);")
        self.configEdit.setObjectName("configEdit")
        self.configLabel = QtWidgets.QLabel(KeyboardDialog)
        self.configLabel.setGeometry(QtCore.QRect(125, 190, 986, 51))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.configLabel.setFont(font)
        self.configLabel.setStyleSheet("color: rgb(55, 52, 53);")
        self.configLabel.setObjectName("configLabel")
        self.enterButton = QtWidgets.QPushButton(KeyboardDialog)
        self.enterButton.setGeometry(QtCore.QRect(975, 580, 200, 100))
        self.enterButton.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setStyleSheet("background-color: rgb(240, 238, 126);\n"
"background-image: url(:/symbols/resources/enter.png);\n"
"border-radius: 10px;\n"
"border:2px solid rgb(55, 52, 53);\n"
"color: rgb(55, 52, 53);")
        self.enterButton.setText("")
        self.enterButton.setObjectName("enterButton")

        self.retranslateUi(KeyboardDialog)
        QtCore.QMetaObject.connectSlotsByName(KeyboardDialog)

    def retranslateUi(self, KeyboardDialog):
        _translate = QtCore.QCoreApplication.translate
        KeyboardDialog.setWindowTitle(_translate("KeyboardDialog", "Dialog"))
        self.Button_1.setText(_translate("KeyboardDialog", "q"))
        self.symbolsButton.setText(_translate("KeyboardDialog", "?123"))
        self.cancelButton.setText(_translate("KeyboardDialog", "Cancel"))
        self.Button_2.setText(_translate("KeyboardDialog", "w"))
        self.Button_4.setText(_translate("KeyboardDialog", "r"))
        self.Button_3.setText(_translate("KeyboardDialog", "e"))
        self.Button_7.setText(_translate("KeyboardDialog", "u"))
        self.Button_6.setText(_translate("KeyboardDialog", "y"))
        self.Button_5.setText(_translate("KeyboardDialog", "t"))
        self.Button_8.setText(_translate("KeyboardDialog", "i"))
        self.Button_9.setText(_translate("KeyboardDialog", "o"))
        self.Button_10.setText(_translate("KeyboardDialog", "p"))
        self.Button_13.setText(_translate("KeyboardDialog", "d"))
        self.Button_12.setText(_translate("KeyboardDialog", "s"))
        self.Button_15.setText(_translate("KeyboardDialog", "g"))
        self.Button_11.setText(_translate("KeyboardDialog", "a"))
        self.Button_14.setText(_translate("KeyboardDialog", "f"))
        self.Button_16.setText(_translate("KeyboardDialog", "h"))
        self.Button_18.setText(_translate("KeyboardDialog", "k"))
        self.Button_17.setText(_translate("KeyboardDialog", "j"))
        self.Button_19.setText(_translate("KeyboardDialog", "l"))
        self.Button_23.setText(_translate("KeyboardDialog", "v"))
        self.Button_24.setText(_translate("KeyboardDialog", "b"))
        self.Button_25.setText(_translate("KeyboardDialog", "n"))
        self.Button_22.setText(_translate("KeyboardDialog", "c"))
        self.Button_20.setText(_translate("KeyboardDialog", "z"))
        self.Button_21.setText(_translate("KeyboardDialog", "x"))
        self.Button_27.setText(_translate("KeyboardDialog", "."))
        self.Button_26.setText(_translate("KeyboardDialog", "m"))
        self.configLabel.setText(_translate("KeyboardDialog", "config"))

import wifi_res_rc
