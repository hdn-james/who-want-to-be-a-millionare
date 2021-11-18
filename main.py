import sys
import json
from PyQt5 import QtWidgets
from gui.screen.main_menu import UI_MainMenu
from server.utils.username import checkUsername
import configuration

configuration.init()

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    configuration.init()
    main()
    
    