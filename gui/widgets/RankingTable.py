from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class RankingTable(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.setGeometry(QtCore.QRect(130, 90, 381, 221))
        self.setStyleSheet(''' 
                           QTableWidget {
                               border: none;
                               background-color: transparent;
                           }
                           
                           QHeaderView::section {
                               background-color: #2E7BA6;
                               color: white;
                               font-weight: bold;
                               border-radius: 14px;
                               margin: 2px;
                            }
                            
                            QTableWidget::item {
                               background-color: #83C5EA;
                               color: white;
                               text-align: center;
                               font-weight: bold;
                               border-radius: 14px;
                               margin: 2px;
                            }
                           
                            QScrollBar:vertical {
                                border: 2px solid #2E7BA6;
                                background: #83C5EA;
                                width: 15px;
                                margin: 0px;
                                border-radius: 15px;
                            }
                            
                            QScrollBar::handle:vertical {
                                background: #2E7BA6;
                                min-height: 20px;
                            }
                                                        
                            QScrollBar::add-line:vertical {
                                height: 0px;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                            }
                            ''')
        self.setAutoScroll(True)
        self.setShowGrid(False)
        self.setColumnCount(3)
        self.setObjectName("rankingTable")
        self.horizontalHeader().setVisible(True)
        self.verticalHeader().setVisible(False)
        
        #resize column
        column = self.horizontalHeader()       
        column.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.setColumnWidth(0, 50)
        self.setColumnWidth(2, 80)
        
    def createHeading(self):
        header = ['Rank', 'Username', 'Score']
        self.setHorizontalHeaderLabels(header)
        
    def setValue(self, results):
        #results: list[rank, username, score]
        for row, result in enumerate(results):
            self.insertRow(row)
            for col, item in enumerate(result):
                newItem = QTableWidgetItem(item)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.setItem(row, col, newItem)