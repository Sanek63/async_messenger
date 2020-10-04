from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.chat_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.chat_label.setEnabled(True)
        self.chat_label.setGeometry(QtCore.QRect(10, 60, 461, 351))
        self.chat_label.setObjectName("chat_label")
        self.sendMessagePanel = QtWidgets.QTextEdit(self.centralwidget)
        self.sendMessagePanel.setGeometry(QtCore.QRect(10, 420, 371, 41))
        self.sendMessagePanel.setObjectName("sendMessagePanel")
        self.sendMessageButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendMessageButton.setGeometry(QtCore.QRect(397, 420, 71, 41))
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.inputNamePanel = QtWidgets.QLabel(self.centralwidget)
        self.inputNamePanel.setGeometry(QtCore.QRect(370, 20, 104, 31))
        self.inputNamePanel.setObjectName("inputNamePanel")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(310, 20, 58, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Messenger"))
        self.main_label.setText(_translate("MainWindow", "Messenger"))
        self.sendMessagePanel.setPlaceholderText(_translate("MainWindow", "Введите сообщение..."))
        self.sendMessageButton.setText(_translate("MainWindow", ">"))
        self.name_label.setText(_translate("MainWindow", "name:"))
