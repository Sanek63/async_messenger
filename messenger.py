from PyQt5 import QtWidgets

from clientui import Ui_MainWindow


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec_()