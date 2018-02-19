# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lipo2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 600)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"\n"
"")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(40, 120, 91, 251))
        self.verticalSlider.setStyleSheet("QSlider::groove:vertical {\n"
"background: red;\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"border: 1px solid #bbb;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: green;\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"border: 1px solid #777;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: white;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"background: pink;\n"
"}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider.setObjectName("verticalSlider")
        self.dial_2 = QtWidgets.QDial(Dialog)
        self.dial_2.setGeometry(QtCore.QRect(540, 110, 241, 251))
        self.dial_2.setObjectName("dial_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(600, 200, 131, 81))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 400, 811, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(9, 9, 811, 81))
        self.frame.setStyleSheet("QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0539216 rgba(128, 128, 128, 255), stop:0.637255 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:checked, QPushButton:pressed {\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"\n"
"QToolButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton:checked, QPushButton:pressed {\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(390, 20, 411, 34))
        self.closeButton.setCheckable(True)
        self.closeButton.setObjectName("closeButton")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 81, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/continua.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)
        self.toolButton.setAutoExclusive(True)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(120, 10, 91, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pulsada.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setAutoExclusive(True)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(220, 10, 91, 61))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setAutoExclusive(True)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.Powerlabel = QtWidgets.QLabel(Dialog)
        self.Powerlabel.setGeometry(QtCore.QRect(190, 200, 119, 73))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Powerlabel.sizePolicy().hasHeightForWidth())
        self.Powerlabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.Powerlabel.setFont(font)
        self.Powerlabel.setObjectName("Powerlabel")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(271, 131, 101, 204))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pLevel1000 = QtWidgets.QLabel(self.widget)
        self.pLevel1000.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel1000.setText("")
        self.pLevel1000.setPixmap(QtGui.QPixmap(":/images/power_meter7.png"))
        self.pLevel1000.setObjectName("pLevel1000")
        self.verticalLayout_2.addWidget(self.pLevel1000)
        self.pLevel825 = QtWidgets.QLabel(self.widget)
        self.pLevel825.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel825.setText("")
        self.pLevel825.setPixmap(QtGui.QPixmap(":/images/power_meter6.png"))
        self.pLevel825.setObjectName("pLevel825")
        self.verticalLayout_2.addWidget(self.pLevel825)
        self.pLevel750 = QtWidgets.QLabel(self.widget)
        self.pLevel750.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel750.setText("")
        self.pLevel750.setPixmap(QtGui.QPixmap(":/images/power_meter5.png"))
        self.pLevel750.setObjectName("pLevel750")
        self.verticalLayout_2.addWidget(self.pLevel750)
        self.pLevel625 = QtWidgets.QLabel(self.widget)
        self.pLevel625.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel625.setText("")
        self.pLevel625.setPixmap(QtGui.QPixmap(":/images/power_meter4.png"))
        self.pLevel625.setScaledContents(False)
        self.pLevel625.setObjectName("pLevel625")
        self.verticalLayout_2.addWidget(self.pLevel625)
        self.pLevel500 = QtWidgets.QLabel(self.widget)
        self.pLevel500.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel500.setText("")
        self.pLevel500.setPixmap(QtGui.QPixmap(":/images/power_meter3b.png"))
        self.pLevel500.setObjectName("pLevel500")
        self.verticalLayout_2.addWidget(self.pLevel500)
        self.pLevel325 = QtWidgets.QLabel(self.widget)
        self.pLevel325.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel325.setText("")
        self.pLevel325.setPixmap(QtGui.QPixmap(":/images/power_meter3.png"))
        self.pLevel325.setObjectName("pLevel325")
        self.verticalLayout_2.addWidget(self.pLevel325)
        self.pLevel250 = QtWidgets.QLabel(self.widget)
        self.pLevel250.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel250.setText("")
        self.pLevel250.setPixmap(QtGui.QPixmap(":/images/power_meter0.png"))
        self.pLevel250.setScaledContents(False)
        self.pLevel250.setObjectName("pLevel250")
        self.verticalLayout_2.addWidget(self.pLevel250)
        self.pLevel125 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pLevel125.sizePolicy().hasHeightForWidth())
        self.pLevel125.setSizePolicy(sizePolicy)
        self.pLevel125.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pLevel125.setText("")
        self.pLevel125.setPixmap(QtGui.QPixmap(":/images/power_meter0.png"))
        self.pLevel125.setScaledContents(False)
        self.pLevel125.setObjectName("pLevel125")
        self.verticalLayout_2.addWidget(self.pLevel125)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_6.setText(_translate("Dialog", "PushButton"))
        self.pushButton_5.setText(_translate("Dialog", "PushButton"))
        self.pushButton_12.setText(_translate("Dialog", "PushButton"))
        self.pushButton_14.setText(_translate("Dialog", "PushButton"))
        self.pushButton_13.setText(_translate("Dialog", "PushButton"))
        self.pushButton_11.setText(_translate("Dialog", "PushButton"))
        self.pushButton_10.setText(_translate("Dialog", "PushButton"))
        self.pushButton_9.setText(_translate("Dialog", "PushButton"))
        self.pushButton_8.setText(_translate("Dialog", "PushButton"))
        self.pushButton_7.setText(_translate("Dialog", "PushButton"))
        self.closeButton.setText(_translate("Dialog", "CLOSE"))
        self.toolButton.setText(_translate("Dialog", "Continua"))
        self.toolButton_2.setText(_translate("Dialog", "Pulsada"))
        self.toolButton_3.setText(_translate("Dialog", "Modulada"))
        self.Powerlabel.setText(_translate("Dialog", "0%"))

import res_lipo2_rc
