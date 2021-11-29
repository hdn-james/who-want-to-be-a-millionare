from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox
from gui.widgets.Button35x35 import Button35x35

class DialogFailUsername(QGroupBox):
    def __init__(self, parent = None):
        QGroupBox.__init__(self, parent)
        self.resize(300, 150)
        self.move(480, 300)
        self.setStyleSheet(''' border: 2px solid #FBC02D; 
                               border-radius: 15px; 
                               background-color: white;''')
        self.initUI()

    def initUI(self):
        #message
        self.text = QtWidgets.QTextBrowser(self)
        self.text.setStyleSheet(''' border: none; 
                                    border-radius: 0px;
                                    background-color: transparent; 
                                    padding: 5px;
                                    font-size: 18px;
                                    font-weight: bold;
                                    color: #C58F09;''')
        self.text.resize(300, 100)
        
        #button
        self.btn = Button35x35(self)
        self.btn.setImage("images/back-btn.png")
        self.btn.move(130, 90)
        self.btn.clicked.connect(self.handleBackButton)
        
    def setMessage(self, message):
        self.text.setText(message)
        
    def handleBackButton(self):
        self.hide()