from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

from clientui import Ui_MainWindow


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        self.url = url
        self.after_timestamp = 0

        self.sendMessageButton.pressed.connect(self.button_pressed)

        self.load_messages()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def pretty_print(self, message):
        '''
        2020/09/09 10:00:23  Nick
        Text

        '''
        dt = datetime.fromtimestamp(message['timestamp'])
        dt = dt.strftime('%Y/%m/%d %H:%M:%S')
        first_line = dt + '  ' + message['name']
        self.chat_label.append(first_line)
        self.chat_label.append(message['text'])
        self.chat_label.append('')

    def update_messages(self):
        response = None

        try:
            response = requests.get(
                self.url + '/messages',
                params={'after_timestamp': self.after_timestamp}
            )
        except:
            pass

        if response and response.status_code == 200:
            messages = response.json()['messages']
            for message in messages:
                self.pretty_print(message)
                self.after_timestamp = message['timestamp']

            return messages

    def load_messages(self):
        while self.update_messages():
            pass

    def button_pressed(self):
        name = self.inputNamePanel.toPlainText()
        text = self.sendMessagePanel.toPlainText()
        data = {'name': name, 'text': text}

        response = None
        try:
            response = requests.post(
                self.url + '/send',
                json=data
            )
        except:
            pass

        if response and response.status_code == 200:
            self.sendMessagePanel.clear()
        else:
            self.chat_label.append('При отправке произошла ошибка')
            self.chat_label.append('')


app = QtWidgets.QApplication([])
window = Messenger('http://6c0326051e48.ngrok.io')
window.show()
app.exec_()
