# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import gui.screen
import os
from client.controller import execute_action

dirname = os.path.dirname(__file__)
image_folder = os.path.join(dirname, "../images")
loading = 0
maxloading = 5

class UI_LoadingScreen(object):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1280, 960)
        MainWindow.setFixedWidth(1280)
        MainWindow.setFixedHeight(960)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #F0F0F0;")

        # title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 300, 1280, 100))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap(
            os.path.join(image_folder, "./loading.png")))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # progress bar
        self.loading = QtWidgets.QProgressBar(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(190, 400, 901, 61))
        self.loading.setAutoFillBackground(False)
        self.loading.setStyleSheet('''
                                        QProgressBar{
                                            border: solid grey;
                                            border-radius: 10px;
                                            color: black;
                                        }

                                        QProgressBar::chunk {
                                            background-color: #83C5EA;
                                            border-radius: 10px;
                                        }
                                    ''')
        self.loading.setMaximum(maxloading)
        self.loading.setProperty("value", 0)
        self.loading.setTextVisible(False)
        self.loading.setObjectName("loading")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.setLoadingValue(MainWindow))
        self.timer.start(1000)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def setLoadingValue(self, MainWindow):
        global loading
        self.loading.setProperty("value", loading)
        loading += 1
        if loading >= maxloading+1:
            self.timer.stop()
            self.setOk(MainWindow)

    def setOk(self, MainWindow):
        ui = gui.screen.UI_InformationScreen()
        ui.setupUi(MainWindow)
        MainWindow.show()