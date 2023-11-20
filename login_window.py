
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(626, 376)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)

        self.publicKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.publicKeyLabel.setObjectName("publicKeyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.publicKeyLabel)

        self.keyTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.keyTextEdit.setObjectName("keyTextEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.keyTextEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registerPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerPushButton.setObjectName("registerPushButton")
        self.horizontalLayout.addWidget(self.registerPushButton)
        self.loginPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginPushButton.setObjectName("loginPushButton")
        self.horizontalLayout.addWidget(self.loginPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.registerPushButton.clicked.connect(self.on_register_clicked)


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Komunikator Internetowy"))
        self.usernameLabel.setText(_translate("LoginWindow", "Username"))
        self.passwordLabel.setText(_translate("LoginWindow", "Password"))
        self.publicKeyLabel.setText(_translate("LoginWindow", "Public_key"))
        self.registerPushButton.setText(_translate("LoginWindow", "Zarejestruj"))
        self.loginPushButton.setText(_translate("LoginWindow", "Zaloguj"))

    def on_register_clicked(self):
        print(self.usernameLineEdit.text())
        print(self.passwordLineEdit.text())
        print(self.keyTextEdit.toPlainText())

