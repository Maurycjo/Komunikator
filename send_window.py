# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\send_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.receiverLabel = QtWidgets.QLabel(self.centralwidget)
        self.receiverLabel.setObjectName("receiverLabel")
        self.horizontalLayout.addWidget(self.receiverLabel)
        self.receiverLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.horizontalLayout.addWidget(self.receiverLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.messageTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.gridLayout_2.addWidget(self.messageTextEdit, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sendPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendPushButton.setObjectName("sendPushButton")
        self.horizontalLayout_2.addWidget(self.sendPushButton)
        self.exportPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportPushButton.setObjectName("exportPushButton")
        self.horizontalLayout_2.addWidget(self.exportPushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wyslij wiadomość"))
        self.receiverLabel.setText(_translate("MainWindow", "Odbiorca"))
        self.sendPushButton.setText(_translate("MainWindow", "Wyślij"))
        self.exportPushButton.setText(_translate("MainWindow", "Eksportuj historie wiadmości do pliku"))
