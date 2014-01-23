#Kurt Hornett
#Show Tweet Tool
#Implemetation - Jan '14

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from twitter_database import *
from sql_gui_misc import *

import sys

class TweetInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        #Set Window Titile
        self.setWindowTitle('Show User Tweets')

        #Create Tweet Layout
        self.tweetLayout = QVBoxLayout()

        #Add 
        

        #Create Menu
        self.usersButton = QPushButton('Users Menu')
        self.usersMenu = QMenu()

        #Add Actions
        self.getUsersNumber()
        self.addActions()
        self.usersMenu.setTitle('Users Menu')

        #Create Layout
        self.layout = QGridLayout()

        #Add Widgets
        self.layout.addWidget(self.usersButton,0,0)

        #Create central widger
        self.tweetWidget = QWidget()
        self.tweetWidget.setLayout(self.layout)

        #Set Centarl Layout
        self.setCentralWidget(self.tweetWidget)

        #Connexion
        self.usersButton.clicked.connect(self.showMenu)

    def showMenu(self):
        self.usersMenu.exec_(QCursor.pos())
        print(self.sender().text())
        if self.sender() in self.actionsList:
            print('Yes')

    def printUser(self):
        pass

    def getUsersNumber(self):
        self.userList = getUsersFromDatabaseGUI()
        self.userNumber = len(self.userList)

    def addActions(self):
        for count in range(self.userNumber):
            self.usersMenu.addAction('{0}'.format(self.userList[count][0])).triggered.connect(self.showMenu)
        self.actionsList = self.usersMenu.actions()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TweetInterface()
    window.show()
    window.raise_()
    app.exec_()
