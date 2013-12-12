# Kurt Hornett
# Main Interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from SearchWindow import *
from BookmarkTool import *
from TableView import *

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
        self.addAction = self.managementMenu.addAction('Add Bookmark')
        self.deleteAction = self.managementMenu.addAction('Delete Entries')
        self.modifyAction = self.managementMenu.addAction('Modity Databases')
        self.suggestedAction = self.suggestedMenu.addAction('Display Suggested Users')
        self.trendsAction = self.trendsMenu.addAction('Display Trends')

        #Set Menu Bar
        self.setMenuBar(self.menuBar)

        #Import Layouts
        self.searchInterface = SearchWindow()
        self.bookmarkInterface = BookmarkWindow()
        self.tableInterface = TableViewWindow()

        #Create Layout
        self.layout = QStackedLayout()
        self.layout.addWidget(self.searchInterface.searchWidget)
        self.layout.addWidget(self.bookmarkInterface.bookmarkWidget)
        self.layout.addWidget(self.tableInterface.tableWidget)

        #Set Main Widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #Add Action Actions
        self.searchAction.triggered.connect(self.newSearch)
        self.addAction.triggered.connect(self.addBookmark)
        self.modifyAction.triggered.connect(self.modifyBookmarks)

        #Actions for sub-classes
        self.bookmarkInterface.cancelButton.clicked.connect(self.cancelAction)
        self.tableInterface.cancelButton.clicked.connect(self.cancelAction)

    def newSearch(self):
        self.layout.setCurrentWidget(self.searchInterface.searchWidget)
    def addBookmark(self):
        self.layout.setCurrentWidget(self.bookmarkInterface.bookmarkWidget)
    def cancelAction(self):
        self.layout.setCurrentWidget(self.searchInterface.searchWidget)
    def modifyBookmarks(self):
        self.layout.setCurrentWidget(self.tableInterface.tableWidget)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec()
    
        
