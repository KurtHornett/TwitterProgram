# Kurt Hornett
# Main Interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from SearchWindow import *
from BookmarkMenu import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Twitter Program')

        #Create Menubar for interface - Add Each Menu
        self.menuBar = QMenuBar()
        self.fileMenu = self.menuBar.addMenu('File')
        self.searchMenu = self.menuBar.addMenu('Search')
        self.managementMenu = self.menuBar.addMenu('Database Management')
        self.suggestedMenu = self.menuBar.addMenu('Suggested Users')
        self.trendsMenu = self.menuBar.addMenu('Display Trends')

        #Add Actions to each Menu
        self.logOutAction = self.fileMenu.addAction('Log Out')
        self.quitAction = self.fileMenu.addAction('Quit')
        self.searchAction = self.searchMenu.addAction('New Search')
        self.addAction = self.managementmenu.addAction('Add Bookmark')
        self.deleteAction = self.managementMenu.addAction('Delete Entries')
        self.modifyAction = self.managementMenu.addAction('Modity Databases')
        self.suggestedAction = self.suggestedMenu.addAction('Display Suggested Users')
        self.trendsAction = self.trendsMenu.addAction('Display Trends')

        #Set Menu Bar
        self.setMenuBar(self.menuBar)

        #Import Layouts
        self.searchInterface = SearchWindow()

        #Create Layout
        self.layout = QStackedLayout()
        self.layout.addWidget(self.searchInterface.searchWidget)

        #Set Main Widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #Add Action Actions
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec()
    
        
