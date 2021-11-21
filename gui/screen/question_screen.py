# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui.widgets.Button100x100 import Button100x100
from gui.widgets.Button64x64 import Button64x64
from gui.widgets.Answer import Answer
import os
import time

url = os.path.dirname("./who-want-to-be-a-millionare/gui/") 
totalTime = 60

class UI_QuestionScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 960)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 50, 1280, 100))
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap(url + "images/question.png"))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("titleInformation")
        
        #ok button
        self.okBtn = Button100x100(self.centralwidget)
        self.okBtn.setImage("images/OK-btn.png")
        self.okBtn.move(590, 690)
        self.okBtn.setName("okBtn")
        self.okBtn.clicked.connect(self.handleClickOKButton)
        
        #exit button
        self.exitBtn = Button64x64(self.centralwidget)
        self.exitBtn.setImage("images/exit-btn.png")
        self.exitBtn.move(1170, 30)
        self.exitBtn.setName("exitBtn")
        self.exitBtn.clicked.connect(lambda: self.handleClickExitButton(MainWindow))
        
        #pass button
        self.passBtn = Button64x64(self.centralwidget)
        self.passBtn.setImage("images/pass-btn.png")
        self.passBtn.move(1080, 30)
        self.passBtn.setName("passBtn")
        self.passBtn.clicked.connect(self.handleClickPassButton)
        
        #question
        self.question = QtWidgets.QTextBrowser(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(300, 170, 691, 221))
        self.question.setObjectName("question")
        self.question.setStyleSheet(''' border: 1.5px solid #2E7BA6;
                                        color: #1A4F6D;
                                        font-size: 20px;
                                        border-radius: 20px;
                                        padding: 10px;
                                        font-weight: bold; 
                                        background-color: white;''')
        self.question.setText("One more thing, buttons will be generated using for loop; so name value will vary. So I want to attach each name with the button. I have done same thing in Pytk by using for loop and calling the argument base function when clicked.")
        
        #choose A
        self.chooseA = Answer(self.centralwidget)
        self.chooseA.move(90, 480)
        self.chooseA.setText("A. hello")
        self.chooseA.setObjectName("chooseA")
        self.chooseA.clicked.connect(self.handleChooseA)
        
        #chooseB
        self.chooseB = Answer(self.centralwidget)
        self.chooseB.move(90, 590)
        self.chooseB.setText("B. I do not understand why you pass QMouseEvent to the parent constructor, you must pass the parent attribute as shown below")
        self.chooseB.setObjectName("chooseB")
        self.chooseB.clicked.connect(self.handleChooseB)
        
        #choose C
        self.chooseC = Answer(self.centralwidget)
        self.chooseC.move(710, 480)
        self.chooseC.setText("C. hello")
        self.chooseC.setObjectName("chooseC")
        self.chooseC.clicked.connect(self.handleChooseC)
        
        #choose D
        self.chooseD = Answer(self.centralwidget)
        self.chooseD.move(710, 590)
        self.chooseD.setText("D. hello")
        self.chooseD.setObjectName("chooseD")
        self.chooseD.clicked.connect(self.handleChooseD)
        
        #score
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(20, 20, 100, 42))
        self.score.setText("")
        self.score.setPixmap(QtGui.QPixmap(os.path.join(url, "images/score.png")))
        self.score.setScaledContents(True)
        self.score.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score.setObjectName("score")
        
        self.inputScore = QtWidgets.QLineEdit(self.centralwidget)
        self.inputScore.setGeometry(QtCore.QRect(140, 20, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(23)
        self.inputScore.setFont(font)
        self.inputScore.setStyleSheet("background: transparent; color: #FBC02D; border: none;")
        self.inputScore.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputScore.setObjectName("inputScore")
        
        #timer
        self.countdownTimer = QtWidgets.QProgressBar(self.centralwidget)
        self.countdownTimer.setGeometry(QtCore.QRect(20, 80, 221, 23))
        self.countdownTimer.setAutoFillBackground(False)
        self.countdownTimer.setStyleSheet('''
                                                QProgressBar{
                                                    border: solid grey;
                                                    border-radius: 5px;
                                                    color: black;
                                                }

                                                QProgressBar::chunk {
                                                    background-color: #05B8CC;
                                                    border-radius: 5px;
                                                }
                                          ''')
        self.countdownTimer.setMaximum(60)
        self.countdownTimer.setProperty("value", 0)
        self.countdownTimer.setTextVisible(False)
        self.countdownTimer.setObjectName("countdownTimer")
        
        self.setDurationTime()
        
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.timeout.connect(self.runCountdown)
        self.timer.start(1000)
        
        #result
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 250, 1280, 400))
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.result.hide()
        
        #setup
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputScore.setText(_translate("MainWindow", "100"))
        
    #pass button or not
    def isPassLeft(self, isPass):
        if (isPass):
            self.passBtn.show()
        else:
            print("hello")
            self.passBtn.hide()
        
    #main player or not: isMain to check main player or not, isPass to check pass button
    def isMainPlayer(self, isMain, isPass):
        if (isMain):
            self.okBtn.show()
            self.isPassLeft(isPass)
        else: 
            print("hello")
            self.okBtn.hide()
            self.passBtn.hide()
            
    #show result
    def showResult(self, result):
        if result: 
            self.result.setPixmap(QtGui.QPixmap(os.path.join(url, "images/correct.png")))
            self.result.show()
        else:
            self.result.setPixmap(QtGui.QPixmap(os.path.join(url, "images/wrong.png")))
            self.result.show()


    #click button
    def handleClickPassButton(self):
        self.timer.stop()
        print("Pass!")
        
    def handleClickExitButton(self, MainWindow):
        MainWindow.close()
        
    def handleClickOKButton(self):
        self.timer.stop()
        #checkResult --> result = checkResult
        result = True
        self.showResult(result)
    
    #score    
    def setScore(self, score):
        self.inputScore.setText(score)
        
    #time   
    def setDurationTime(self):
        self.time_left_int = totalTime
        
    def runCountdown(self):
        self.time_left_int -= 1
        print(self.time_left_int)
        self.countdownTimer.setValue(totalTime - self.time_left_int)
        if self.time_left_int == 0:
            self.timer.stop()
        
    #answer
    def handleChooseA(self):
        self.chooseA.isChoose(True)
        self.chooseB.isChoose(False)
        self.chooseC.isChoose(False)
        self.chooseD.isChoose(False)
        
    def handleChooseB(self):
        self.chooseA.isChoose(False)
        self.chooseB.isChoose(True)
        self.chooseC.isChoose(False)
        self.chooseD.isChoose(False)
        
    def handleChooseC(self):
        self.chooseA.isChoose(False)
        self.chooseB.isChoose(False)
        self.chooseC.isChoose(True)
        self.chooseD.isChoose(False)
        
    def handleChooseD(self):
        self.chooseA.isChoose(False)
        self.chooseB.isChoose(False)
        self.chooseC.isChoose(False)
        self.chooseD.isChoose(True)
        
    
