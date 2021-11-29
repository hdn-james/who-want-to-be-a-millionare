from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel

class Answer(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.resize(481, 61)
        self.setWordWrap(True)
        self.setStyleSheet(''' border: 1px solid gray;
                               border-radius: 30px; 
                               background-color: white; 
                               font-weight: bold;
                               color: #5B5B5B;
                               padding: 8px; 
                               font-size: 14px; ''')
        
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        
    def isChoose(self, bool):
        if (bool): 
            self.setStyleSheet(''' border: 3px solid #E05350;
                                    border-radius: 30px; 
                                    background-color: white;
                                    font-weight: bold;
                                    color: #E05350;
                                    padding: 8px; 
                                    font-size: 14px; ''')
        else:
            self.setStyleSheet(''' border: 1px solid gray;
                                    border-radius: 30px; 
                                    background-color: white; 
                                    font-weight: bold; 
                                    color: #5B5B5B;
                                    padding: 8px; 
                                    font-size: 14px;  ''')