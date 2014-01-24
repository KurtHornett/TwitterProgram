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
    def __init__(self,twitter):
        super().__init__()
        #Set Window Titile
        self.setWindowTitle('Show User Tweets')

        self.twitter = twitter

        #Create Tweet Layout
        self.tweetLayout = QGridLayout()
        self.returnButton = QPushButton('Return')
        self.tweetLayout.addWidget(self.returnButton,1,0)

        #Create Menu
        self.usersButton = QPushButton('Users Menu')
        self.usersMenu = QMenu()

        #Add Actions
        self.getUsersNumber()
        self.addActions()
        self.usersMenu.setTitle('Users Menu')

        #Create User Layout
        self.userLayout = QGridLayout()

        #Add Widgets
        self.userLayout.addWidget(self.usersButton,0,0)

        #Create Stacked Layout
        self.userWidget = QWidget()
        self.userWidget.setLayout(self.userLayout)
        self.tweetWidget = QWidget()
        self.tweetWidget.setLayout(self.tweetLayout)
        self.mainLayout = QStackedLayout()
        self.mainLayout.addWidget(self.userWidget)
        self.mainLayout.addWidget(self.tweetWidget)

        #Create central widger
        self.tweetsWidget = QWidget()
        self.tweetsWidget.setLayout(self.mainLayout)

        #Set Centarl Layout
        self.setCentralWidget(self.tweetsWidget)
        

        #Connexion
        self.usersButton.clicked.connect(self.showMenu)
        self.returnButton.clicked.connect(self.showUserMenu)

    def showUserMenu(self):
        self.mainLayout.setCurrentWidget(self.userWidget)

    def showMenu(self):
        self.usersMenu.exec_(QCursor.pos())
        if self.sender().text() != 'User Menu':
            self.printUser()

    def printUser(self):
##        self.usersMenu.exec_(QCursor.pos())
##        print(self.sender().text())
##        if self.sender() in self.actionsList:
##            print('Yes')
        if self.sender().text() != self.usersButton.text():
            self.userChoice = 0
            while self.actionsList[self.userChoice].text() != self.sender().text():
                self.userChoice += 1
            self.displayTweet()

    def displayTweet(self):
        self.timeline = self.twitter.statuses.user_timeline(id=self.userList[self.userChoice][1])
        self.singleTweetLayout = QTextEdit()
        self.singleTweetLayout.setText(self.timeline[0]['text'])
        self.singleTweetLayout.setReadOnly(True)
        self.tweetLayout.addWidget(self.singleTweetLayout,0,0)
        self.mainLayout.setCurrentWidget(self.tweetWidget)

    def getUsersNumber(self):
        self.userList = getUsersFromDatabaseGUI()
        self.userNumber = len(self.userList)

    def addActions(self):
        for count in range(self.userNumber):
            self.usersMenu.addAction('{0}'.format(self.userList[count][0])).triggered.connect(self.printUser)
        self.actionsList = self.usersMenu.actions()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TweetInterface()
    window.show()
    window.raise_()
    app.exec_()
