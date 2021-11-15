# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.Button64x64 import Button64x64
from widgets.RankingTable import RankingTable

url = "D:/HCMUS/Internetworking/Project/Lab1 - Socket Programming/who-want-to-be-a-millionare/gui/"

class UI_EndgameScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #title
        self.titleInformation = QtWidgets.QLabel(self.centralwidget)
        self.titleInformation.setGeometry(QtCore.QRect(60, 30, 511, 41))
        self.titleInformation.setText("")
        self.titleInformation.setPixmap(QtGui.QPixmap(url + "images/leader-board.png"))
        self.titleInformation.setAlignment(QtCore.Qt.AlignCenter)
        self.titleInformation.setObjectName("titleInformation")
        
        #restart button
        self.restartBtn = Button64x64(self.centralwidget)
        self.restartBtn.setName("restartBtn")
        self.restartBtn.setImage("images/back-btn.png")
        self.restartBtn.move(QtCore.QPoint(210, 340))
        
        #exitBtn
        self.exitBtn = Button64x64(self.centralwidget)
        self.exitBtn.setName("exitBtn")
        self.exitBtn.setImage("images/exit-btn.png")
        self.exitBtn.move(QtCore.QPoint(360, 340))
        self.exitBtn.clicked.connect(self.handleClickExit)
        
        #table
        self.rankingTable = RankingTable(self.centralwidget)
        self.rankingTable.createHeading()
        self.rankingTable.setValue([['1', 'Nhi', '100'], ['2', 'Tan', '50']])
        
        #setup
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    def handleClickExit(self):
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_EndgameScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
