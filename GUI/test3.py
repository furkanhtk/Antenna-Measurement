import sys
from PyQt5 import QtWidgets
import logging
sys.path.append(r"C:\Users\Furkan\Desktop\ANTENNA MEASUREMENT SYSTEM")
import Master

date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s : %(message)s"
logging.basicConfig(filename='log.log', level=logging.INFO, format=message_format, datefmt=date_strftime_format)

class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class MyDialog(QtWidgets.QDialog, QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        logTextBox = QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)

        self._button = QtWidgets.QPushButton(self)
        self._button.setText('Test Me')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        layout.addWidget(self._button)
        self.setLayout(layout)

        self._button.clicked.connect(self.test)

    def test(self):
        Master.main()


class MyDialog2(QtWidgets.QDialog, QtWidgets.QPlainTextEdit):
    def __init__(self, parent=MyDialog):
        super().__init__(parent)

        logTextBox = QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)

        self._button = QtWidgets.QPushButton(self)
        self._button.setText('Test Me')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        layout.addWidget(self._button)
        self.setLayout(layout)

        self._button.clicked.connect(self.test)

    def test(self):
        Master.main()


app = QtWidgets.QApplication(sys.argv)
dlg = MyDialog()
dlg.show()
dlg.raise_()
sys.exit(app.exec_())