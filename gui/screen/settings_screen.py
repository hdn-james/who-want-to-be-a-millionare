# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui.widgets.Button100x100 import Button100x100
import gui.screen

url = "./who-want-to-be-a-millionare/gui/" 

class UI_SettingsScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 960)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(200, 290, 221, 100))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap(url + "images/volume.png"))
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title.setObjectName("title")
        
        #slider
        self.volume = QtWidgets.QSlider(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(210, 390, 851, 22))
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setObjectName("volume")
        self.volume.setStyleSheet(''' QSlider::groove:horizontal {
                                        border: 1px solid #bbb;
                                        background: white;
                                        height: 10px;
                                        border-radius: 4px;
                                        }

                                        QSlider::sub-page:horizontal {
                                        background: #05B8CC;
                                        border: 1px solid lightgrey;
                                        height: 10px;
                                        border-radius: 5px;
                                        }

                                        QSlider::add-page:horizontal {
                                        background: #fff;
                                        border: 1px solid lightgrey;
                                        height: 10px;
                                        border-radius: 5px;
                                        }

                                        QSlider::handle:horizontal {
                                        background: #2E7BA6;
                                        border: 1px solid 2E7BA6;
                                        width: 13px;
                                        margin-top: -5px;
                                        margin-bottom: -5px;
                                        border-radius: 4px;
                                        }
                                      ''')
        
        #play button
        self.playBtn = Button100x100(self.centralwidget)
        self.playBtn.setName("OKBtn")
        self.playBtn.setImage("images/play-btn.png")
        self.playBtn.move(QtCore.QPoint(590, 450))
        self.playBtn.clicked.connect(lambda: self.handleClickPlayButton(MainWindow))
        
        #setup
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def handleClickPlayButton(self, MainWindow):
        ui = gui.screen.UI_MainMenu()
        ui.setupUi(MainWindow)
        MainWindow.show()

