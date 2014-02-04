#Kurt Hornett
# COMP4 Practical Project
# Implemetation - Interfaces
# Bookmark Creation interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class BookmarkWindow(QDialog):
    def __init__(self):
        super().__init__()

        #Set Window Title
        self.setWindowTitle('Bookmark Creation Tool')

        #Create Labels
        self.titleLabel = QLabel('Bookmark Title')
        self.linkLabel = QLabel('Link')
        self.siteNameLabel = QLabel('Site Name')
        self.siteDescLabel = QLabel('Site Description')

        #Create Line Edits
        self.titleLineEdit = QLineEdit()
        self.linkLineEdit = QLineEdit()
        self.linkLineEdit.setReadOnly(True)
        self.siteNameLineEdit = QLineEdit()
        self.siteNameLineEdit.setReadOnly(True)
        self.siteDescLineEdit = QLineEdit()

        #Create Push Button
        self.cancelButton = QPushButton('Cancel')
        self.submitPushButton = QPushButton('Submit')

        #Create Layout
        self.BookmarkLayout = QGridLayout()
        self.BookmarkLayout.addWidget(self.titleLabel,0,0)
        self.BookmarkLayout.addWidget(self.titleLineEdit,0,1,1,3)
        self.BookmarkLayout.addWidget(self.linkLabel,1,0)
        self.BookmarkLayout.addWidget(self.linkLineEdit,1,1)
        self.BookmarkLayout.addWidget(self.siteNameLabel,1,2)
        self.BookmarkLayout.addWidget(self.siteNameLineEdit,1,3)
        self.BookmarkLayout.addWidget(self.siteDescLabel,2,0,)
        self.BookmarkLayout.addWidget(self.siteDescLineEdit,2,1,1,3)
        self.BookmarkLayout.addWidget(self.cancelButton,3,0,1,2)
        self.BookmarkLayout.addWidget(self.submitPushButton,3,2,1,2)

##        #Create Central Widget
        self.bookmarkWidget = QWidget()
        self.bookmarkWidget.setLayout(self.BookmarkLayout)
##        self.setCentralWidget(self.bookmarkWidget)
        self.setLayout(self.BookmarkLayout)
        
        #Set conexions
        self.cancelButton.clicked.connect(self.return_)

    def setData(self,bookmarkInfo):
        self.linkLineEdit.setText(bookmarkInfo[0])
        self.siteNameLineEdit.setText(bookmarkInfo[1])

    def return_(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookmarkWindow()
    window.show()
    window.raise_()
    app.exec_()
        
        

        
