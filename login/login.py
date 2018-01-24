# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("#centralwidget { background: rgba(32, 80, 96, 100); }\n"
"\n"
"#topPanel { background-color: qlineargradient(spread:reflect,\n"
"x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100),\n"
"stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"#loginForm\n"
"{\n"
"background: rgba(0, 0, 0, 80);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QLabel { color: white; }\n"
"QLineEdit { border-radius: 3px; }\n"
"\n"
"QPushButton\n"
"{\n"
"color: white;\n"
"background-color: #27a9e3;\n"
"border-width: 0px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover { background-color: #66c011; }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topPanel = QtWidgets.QWidget(self.centralwidget)
        self.topPanel.setObjectName("topPanel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentDateTime = QtWidgets.QLabel(self.topPanel)
        self.currentDateTime.setObjectName("currentDateTime")
        self.horizontalLayout.addWidget(self.currentDateTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shutdownButton = QtWidgets.QPushButton(self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shutdownButton.sizePolicy().hasHeightForWidth())
        self.shutdownButton.setSizePolicy(sizePolicy)
        self.shutdownButton.setMinimumSize(QtCore.QSize(55, 55))
        self.shutdownButton.setText("")
        self.shutdownButton.setObjectName("shutdownButton")
        self.horizontalLayout.addWidget(self.shutdownButton)
        self.restartButton = QtWidgets.QPushButton(self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restartButton.sizePolicy().hasHeightForWidth())
        self.restartButton.setSizePolicy(sizePolicy)
        self.restartButton.setMinimumSize(QtCore.QSize(55, 55))
        self.restartButton.setText("")
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout.addWidget(self.restartButton)
        self.verticalLayout.addWidget(self.topPanel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(150, 150))
        self.logo.setStyleSheet("border: 1px solid;\n"
"")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginForm = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(300, 250))
        self.loginForm.setStyleSheet("\n"
"")
        self.loginForm.setObjectName("loginForm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setContentsMargins(35, 35, 35, 35)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.loginForm)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.loginForm)
        self.username.setObjectName("username")
        self.horizontalLayout_5.addWidget(self.username)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.loginForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.loginForm)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.loginButton = QtWidgets.QPushButton(self.loginForm)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.horizontalLayout_3.addWidget(self.loginForm)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currentDateTime.setText(_translate("MainWindow", "Monday, 25-10-2015 3:14 PM"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))

