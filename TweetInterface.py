#Kurt Hornett
#Show Tweet Tool
#Implemetation - Jan '14

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from twitter_database import *
from sql_gui_misc import *
from BookmarkTool import *

import sys
import re
import urllib.request

class TweetInterface(QMainWindow):
    def __init__(self,twitter):
        super().__init__()
        #Set Window Titile
        self.setWindowTitle('Show User Tweets')

        self.twitter = twitter

        #Create Tweet Layout
        self.tweetLayout = QGridLayout()
        self.helpLabel = QLabel('Please select one of the users tweets.')
        self.returnButton = QPushButton('Return')
        self.tweetLayout.addWidget(self.helpLabel,0,0)
        self.selectTweetButton = QPushButton('Select Tweet')

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
        self.selectTweetButton.clicked.connect(self.showTweetMenu)

    def showUserMenu(self):
        self.mainLayout.setCurrentWidget(self.userWidget)

    def showMenu(self):
        self.usersMenu.exec_(QCursor.pos())
        if self.sender().text() != 'User Menu':
            self.printUser()
            
    def showTweetMenu(self):
        self.tweetSelectMenu.exec_(QCursor.pos())

    def printUser(self):
        if self.sender().text() != self.usersButton.text():
            self.userChoice = 0
            while self.actionsList[self.userChoice].text() != self.sender().text():
                self.userChoice += 1
            self.displayTweet()

    def displayTweet(self):
        self.timeline = self.twitter.statuses.user_timeline(id=self.userList[self.userChoice][1])
        self.tweetLayout.addWidget(self.returnButton,2,0)
        self.tweetTableWidget = QTableWidget(10,2)
        tweetListLabels = ['Username','Tweet Text']
        self.tweetTableWidget.setHorizontalHeaderLabels(tweetListLabels)
        tweetTextList = []
        count = 0
        self.tweetTableWidget.setSortingEnabled(False)
        while count < 10:
            newTableWidget = QTableWidgetItem(self.timeline[count]['text'])
            self.tweetTableWidget.setItem(count,1,newTableWidget)
            userTableWidget = QTableWidgetItem(self.userList[self.userChoice][1])
            self.tweetTableWidget.setItem(count,0,userTableWidget)
            count += 1
        self.tweetSelectMenuFunc()
        self.tweetLayout.addWidget(self.selectTweetButton,2,2)
        self.tweetLayout.addWidget(self.tweetTableWidget,1,0,1,3)
        self.mainLayout.setCurrentWidget(self.tweetWidget)
        

    def tweetSelectMenuFunc(self):
        self.tweetSelectMenu = QMenu()
        for count in range(10):
            self.tweetSelectMenu.addAction('Tweet # {0}'.format(count+1)).triggered.connect(self.selectedTweet)
        self.tweetActionsList = self.tweetSelectMenu.actions()
        
    def getUsersNumber(self):
        self.userList = getUsersFromDatabaseGUI()
        self.userNumber = len(self.userList)

    def addActions(self):
        for count in range(self.userNumber):
            self.usersMenu.addAction('{0}'.format(self.userList[count][0])).triggered.connect(self.printUser)
        self.actionsList = self.usersMenu.actions()

    def selectedTweet(self):
        self.tweetChoice = 0
        while self.tweetActionsList[self.tweetChoice].text() != self.sender().text():
            self.tweetChoice += 1
        self.BookmarkToolWindow = BookmarkWindow(self.timeline,self.tweetChoice,self.userList,self.userChoice)
        if self.timeline[self.tweetChoice]['entities']['urls'] != []:
            self.getLinkInfo(self.timeline[self.tweetChoice]['entities']['urls'][0]['url'])
            bookmarkInfo = [self.timeline[self.tweetChoice]['entities']['urls'][0]['url'],self.siteName]
            self.BookmarkToolWindow.setData(bookmarkInfo)
            self.BookmarkToolWindow.show()
        else:
            bookmarkInfo = ['null','null']
            self.BookmarkToolWindow.setData(bookmarkInfo)
            self.BookmarkToolWindow.show()
            
    def getLinkInfo(self,link):
        regex = re.compile('<title>(.*?)</title>')
        url = urllib.request.urlopen(link) #Gets the data from the url
        html = url.read() #Converts HTTPRequest into text
        html = str(html) #Changes from 'bytes' to str so re will work
        self.siteName = regex.search(html).group(1)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TweetInterface()
    window.show()
    window.raise_()
    app.exec_()
