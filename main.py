from PyQt5 import QtWidgets
from gui.screen.main_menu import UI_MainMenu
from gui.screen.question_screen import UI_QuestionScreen

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_QuestionScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())