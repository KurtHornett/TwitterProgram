# Kurt Hornett
# Main Interface
# Implemetation

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from SearchWindow import *
from BookmarkTool import *
from TableView import *
from TweetInterface import *
from DeleteInterface import *

#CLI Modules
from twitter_cli import *
from twitter_database import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Twitter Program')

        #Create Twitter Object
        self.createTwitterObject()

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
        self.tweetAction = self.searchMenu.addAction('Search Users Tweets')
        self.deleteAction = self.managementMenu.addAction('Delete Entries')
        self.modifyAction = self.managementMenu.addAction('Modity Databases')
        self.suggestedAction = self.suggestedMenu.addAction('Display Suggested Users')
        self.trendsAction = self.trendsMenu.addAction('Display Trends')

        #Set Menu Bar
        self.setMenuBar(self.menuBar)

        #Import Layouts
        self.searchInterface = SearchWindow(self.twitter)
        self.tableInterface = TableViewWindow()
        self.tweetSearchInterface = TweetInterface(self.twitter)
        self.deleteInterface = DeleteInterface()

        #Create Layout
        self.layout = QStackedLayout()
        self.layout.addWidget(self.searchInterface.searchWidget)
        self.layout.addWidget(self.tableInterface.tableWidget)
        self.layout.addWidget(self.tweetSearchInterface.tweetsWidget)
        self.layout.addWidget(self.deleteInterface.deleteWidget)

        #Set Main Widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #Add Action Actions
        self.searchAction.triggered.connect(self.newSearch)
        self.tweetAction.triggered.connect(self.tweetSearch)
        self.modifyAction.triggered.connect(self.modifyBookmarks)
        self.deleteAction.triggered.connect(self.deleteBookmarks)
        self.quitAction.triggered.connect(self.quit_)

        #Actions for sub-classes
        self.tableInterface.cancelButton.clicked.connect(self.cancelAction)
        self.deleteInterface.cancelButton.clicked.connect(self.cancelAction)

    def newSearch(self):
        self.layout.setCurrentWidget(self.searchInterface.searchWidget)
        self.setWindowTitle('New Search')
    def tweetSearch(self):
        self.layout.setCurrentWidget(self.tweetSearchInterface.tweetsWidget)
        self.setWindowTitle('Tweet Search Interface')
    def cancelAction(self):
        self.layout.setCurrentWidget(self.searchInterface.searchWidget)
        self.setWindowTitle('New Search')
    def modifyBookmarks(self):
        self.tableInterface.createTableModel()
        self.layout.setCurrentWidget(self.tableInterface.tableWidget)
        self.setWindowTitle('Modify Database')
    def deleteBookmarks(self):
        self.layout.setCurrentWidget(self.deleteInterface.deleteWidget)
        self.setWindowTitle('Deletion Interface')
    def createTwitterObject(self):
        consumer_key = getConsumerKey()
        MY_TWITTER_CREDS = os.path.expanduser('~/.login_credentials')
        if not os.path.exists(MY_TWITTER_CREDS):
            oauth_dance("KurtsApp",'Y4zkic6lw0Hu6uB3sNVH4Q', consumer_key,
                        MY_TWITTER_CREDS)
        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
        #Creation of twitter object with authorized detailes.
        self.twitter = Twitter(auth=OAuth(
            oauth_token, oauth_secret, 'Y4zkic6lw0Hu6uB3sNVH4Q', consumer_key))
    def quit_(self):
        window.close()
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec()
    
        
