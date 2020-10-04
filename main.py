from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

from signup_panel.signup import Dialog
from welcome_panel.welcome import MainWindow
from messenger.messenger_client import Messenger

import requests


class Ui_Login_Panel(object):
    def setupUi(self, Login_Panel):
        Login_Panel.setObjectName("Login_Panel")
        Login_Panel.setEnabled(True)
        Login_Panel.resize(400, 300)
        self.label = QtWidgets.QLabel(Login_Panel)
        self.label.setGeometry(QtCore.QRect(110, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.login_label = QtWidgets.QLabel(Login_Panel)
        self.login_label.setGeometry(QtCore.QRect(50, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.login_label.setFont(font)
        self.login_label.setTextFormat(QtCore.Qt.MarkdownText)
        self.login_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.login_label.setWordWrap(False)
        self.login_label.setObjectName("login_label")
        self.login_labe = QtWidgets.QLabel(Login_Panel)
        self.login_labe.setGeometry(QtCore.QRect(10, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.login_labe.setFont(font)
        self.login_labe.setTextFormat(QtCore.Qt.MarkdownText)
        self.login_labe.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.login_labe.setWordWrap(False)
        self.login_labe.setObjectName("login_labe")
        self.login_line = QtWidgets.QLineEdit(Login_Panel)
        self.login_line.setGeometry(QtCore.QRect(180, 80, 181, 41))
        self.login_line.setObjectName("login_line")
        self.pass_line = QtWidgets.QLineEdit(Login_Panel)
        self.pass_line.setGeometry(QtCore.QRect(180, 140, 181, 41))
        self.pass_line.setObjectName("login_line_2")
        self.login_button = QtWidgets.QPushButton(Login_Panel)
        self.login_button.setGeometry(QtCore.QRect(80, 210, 88, 34))
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(Login_Panel)
        self.signup_button.setGeometry(QtCore.QRect(200, 210, 88, 34))
        self.signup_button.setObjectName("signup_button")

        self.retranslateUi(Login_Panel)
        QtCore.QMetaObject.connectSlotsByName(Login_Panel)

    def retranslateUi(self, Login_Panel):
        _translate = QtCore.QCoreApplication.translate
        Login_Panel.setWindowTitle(_translate("Login_Panel", "Dialog"))
        self.label.setText(_translate("Login_Panel", "Messenger"))
        self.login_label.setText(_translate("Login_Panel", "Login:"))
        self.login_labe.setText(_translate("Login_Panel", "Password:"))
        self.login_button.setText(_translate("Login_Panel", "login"))
        self.signup_button.setText(_translate("Login_Panel", "signup"))


class MainLoginPanel(QDialog, Ui_Login_Panel):

    def __init__(self, parent=None, url='http://127.0.0.1:5000'):
        super(MainLoginPanel, self).__init__(parent)
        self.setupUi(self)
        self.url = url

        self.login_button.clicked.connect(self.login_check)
        self.signup_button.clicked.connect(self.signup_check)

    def show_message_box(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self, username):
        self.welcomeWindow = MainWindow(username)
        self.welcomeWindow.show()

    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    def login_check(self):
        username = self.login_line.text()
        password = self.pass_line.text()

        if(not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', "Вы заполнили не все поля")
            return

        response = requests.post(self.url + '/login', json={'username': username, 'password': password})
        result = response.json()

        if result['is_logged']:
            self.welcomeWindowShow(username)
            self.hide()
            self.window = Messenger(self.url, username)
            self.window.show()
        else:
            self.show_message_box('Внимание','Неправильное имя или пароль.')


    def signup_check(self):
        self.signUpShow()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainLoginPanel(url='http://127.0.0.1:5000')
    w.show()
    sys.exit(app.exec_())
