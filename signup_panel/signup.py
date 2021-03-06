from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

import requests


class Ui_signup_panel(object):
    def setupUi(self, signup_panel):
        signup_panel.setObjectName("signup_panel")
        signup_panel.setEnabled(True)
        signup_panel.resize(400, 242)
        self.label = QtWidgets.QLabel(signup_panel)
        self.label.setGeometry(QtCore.QRect(100, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.username_label = QtWidgets.QLabel(signup_panel)
        self.username_label.setGeometry(QtCore.QRect(30, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.username_label.setFont(font)
        self.username_label.setTextFormat(QtCore.Qt.MarkdownText)
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setWordWrap(False)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(signup_panel)
        self.password_label.setGeometry(QtCore.QRect(20, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.password_label.setFont(font)
        self.password_label.setTextFormat(QtCore.Qt.MarkdownText)
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setWordWrap(False)
        self.password_label.setObjectName("password_label")
        self.username_line = QtWidgets.QLineEdit(signup_panel)
        self.username_line.setGeometry(QtCore.QRect(180, 80, 181, 41))
        self.username_line.setObjectName("username_line")
        self.pass_line = QtWidgets.QLineEdit(signup_panel)
        self.pass_line.setGeometry(QtCore.QRect(180, 140, 181, 41))
        self.pass_line.setObjectName("pass_line")
        self.signup_button = QtWidgets.QPushButton(signup_panel)
        self.signup_button.setGeometry(QtCore.QRect(160, 200, 88, 34))
        self.signup_button.setObjectName("signup_button")

        self.retranslateUi(signup_panel)
        QtCore.QMetaObject.connectSlotsByName(signup_panel)

    def retranslateUi(self, signup_panel):
        _translate = QtCore.QCoreApplication.translate
        signup_panel.setWindowTitle(_translate("signup_panel", "Dialog"))
        self.label.setText(_translate("signup_panel", "Registration"))
        self.username_label.setText(_translate("signup_panel", "Username:"))
        self.password_label.setText(_translate("signup_panel", "Password:"))
        self.signup_button.setText(_translate("signup_panel", "Sign Up"))


class Dialog(QDialog, Ui_signup_panel):

    def __init__(self, parent=None, url='http://127.0.0.1:5000'):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.url = url

        self.signup_button.clicked.connect(self.insertData)

    @pyqtSlot()
    def insertData(self):
        username = self.username_line.text()
        password = self.pass_line.text()

        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы заполнили не все поля')
            return

        response = requests.post(self.url + '/registration', json={'username': username, 'password': password})
        result = response.json()

        if result['is_exist']:
            msg = QMessageBox.information(self, 'Внимание!', 'Пользователь с таким именем уже зарегистрирован')
        else:
            self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Dialog(url='http://127.0.0.1:5000')
    w.show()
    sys.exit(app.exec_())