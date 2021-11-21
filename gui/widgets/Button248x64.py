from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton
import os

url = os.path.dirname("./who-want-to-be-a-millionare/gui/")

class Button248x64(QPushButton):
    mouseHover = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setEnabled(True)
        self.setMouseTracking(True)
        self.setStyleSheet("border: none;")
        self.setAutoFillBackground(False)
        
    def setName(self, name):
        self.setObjectName(name)
        
    def setImage(self, path):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(url, path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(248, 64))

    def enterEvent(self, event):
        self.mouseHover.emit(True)
        self.setIconSize(QtCore.QSize(240, 60))

    def leaveEvent(self, event):
        self.mouseHover.emit(False)
        self.setIconSize(QtCore.QSize(248, 64))