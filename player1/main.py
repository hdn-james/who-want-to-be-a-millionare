import sys
from PyQt5 import QtWidgets
from gui.screen.main_menu import UI_MainMenu
from gui.sound.sound import playBackground
import configuration

configuration.init()

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    playBackground()
    sys.exit(app.exec_())

if __name__ == "__main__":
    configuration.init()
    main()
    
    