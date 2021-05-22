from gui_log import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def logscreen(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = MyDialog()
        self.ui.setup(self.window)
        self.window.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Calibration = QtWidgets.QPushButton(self.centralwidget)
        self.Calibration.setGeometry(QtCore.QRect(70, 330, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Calibration.setFont(font)
        self.Calibration.setObjectName("Calibration")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 330, 300, 50))
        self.pushButton.clicked.connect(self.logscreen())
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(50, 10, 671, 121))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("ANTENNA MEASUREMENT SYSTEM")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.menuFile.addAction(self.actionLog)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Calibration.setText(_translate("MainWindow", "Calibration"))
        self.pushButton.setText(_translate("MainWindow", "Measurement"))
        self.Title.setText(_translate("MainWindow", "ANTENNA MEASUREMENT SYSTEM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLog.setText(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
