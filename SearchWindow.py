# Kurt Hornett
# COMP4 Practical Project
# Implementation
# Interfaces - Main Interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Search')

        #Create items for layout
        self.searchLabel = QLabel('Search Term')
        self.searchLineEdit = QLineEdit()
        self.searchButton = QPushButton('Search')

        #Create main search Interface
        self.layout = QGridLayout()
        self.layout.addWidget(self.searchLabel,0,0)
        self.layout.addWidget(self.searchLineEdit,0,1)
        self.layout.addWidget(self.searchButton,1,1)

        #Create This window's widget
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(self.layout)

        #Set Central Layout
        self.setCentralWidget(self.searchWidget)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    window.raise_()
    app.exec_()
