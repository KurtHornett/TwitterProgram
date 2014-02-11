#Kurt Hornett
#COMP4 Implementation
#Suggested Users Interface
#February 2014

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from sql_gui_misc import *
from twitter_database import *

import sys

class SuggestedInterface(QMainWindow):
    def __init__(self,twitter):
        super().__init__()
        #set Window Title
        self.setWindowTitle('Suggested Users')
        self.twitter = twitter

        #Set up Inerface
        self.helpLabel = QLabel('Suggested Users selection Interface. Select A Topic before User')
        self.slugButton = QPushButton('Select Topic')
        self.userHelpLabel = QLabel('Select a topic for Users')
        self.cancelButton = QPushButton('Cancel')
        self.selectUserButton = QPushButton('Select User')
        self.userTableWidget = QTableWidget()

        #Create Layout et cetera
        self.layout = QGridLayout()
        self.layout.addWidget(self.helpLabel,0,0)
        #self.layout.addWidget(self.userHelpLabel,1,0)
        self.layout.addWidget(self.slugButton,1,0)
        self.layout.addWidget(self.userTableWidget,1,1)
        self.layout.addWidget(self.cancelButton,3,0)
        self.layout.addWidget(self.selectUserButton,3,1)

        #Pre-lim mthds
        self.slugMenu()

        #Create Widget set Widget
        self.suggUserWidget = QWidget()
        self.suggUserWidget.setLayout(self.layout)
        self.setCentralWidget(self.suggUserWidget)

        #Connexions
        self.slugButton.clicked.connect(self.showSlugMenu)

    def slugMenu(self):
        self.slugMenu = QMenu()
        self.newsAction = self.slugMenu.addAction('News Users').triggered.connect(self.getSuggUsers)
        self.techAction = self.slugMenu.addAction('Technology Users').triggered.connect(self.getSuggUsers)
        self.bussAction = self.slugMenu.addAction('Business Users').triggered.connect(self.getSuggUsers)

    def showSlugMenu(self):
        self.slugMenu.exec_(QCursor.pos())

    def getSuggUsers(self):
        print(self.sender().text())
        if self.sender().text() == 'News Users':
            self.suggUsers = self.twitter.users.suggestions.news.members()
        elif self.sender().text() == 'Technology Users':
            self.suggUsers = self.twitter.users.suggestions.technology.members()
        elif self.sender().text() == 'Business Users':
            self.suggUsers = self.twitter.users.suggestions.business.members()
        print(self.suggUsers)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SuggestedInterface()
    window.show()
    window.raise_()
    app.exec_()
        
        
         
