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
        #self.layout.addWidget(self.selectUserButton,3,1)

        #Pre-lim mthds
        self.slugMenu()

        #Create Widget set Widget
        self.suggUserWidget = QWidget()
        self.suggUserWidget.setLayout(self.layout)
        self.setCentralWidget(self.suggUserWidget)

        #Connexions
        self.slugButton.clicked.connect(self.showSlugMenu)
        self.selectUserButton.clicked.connect(self.showUserMenu)

    def slugMenu(self):
        self.slugMenu = QMenu()
        self.newsAction = self.slugMenu.addAction('News Users').triggered.connect(self.getSuggUsers)
        self.techAction = self.slugMenu.addAction('Technology Users').triggered.connect(self.getSuggUsers)
        self.bussAction = self.slugMenu.addAction('Business Users').triggered.connect(self.getSuggUsers)

    def showSlugMenu(self):
        self.slugMenu.exec_(QCursor.pos())

    def showUserMenu(self):
        self.userMenu.exec_(QCursor.pos())

    def getSuggUsers(self):
        if self.sender().text() == 'News Users':
            self.suggUsers = self.twitter.users.suggestions.news.members()
        elif self.sender().text() == 'Technology Users':
            self.suggUsers = self.twitter.users.suggestions.technology.members()
        elif self.sender().text() == 'Business Users':
            self.suggUsers = self.twitter.users.suggestions.business.members()
        self.createTable()

    def createTable(self):
        self.userTableWidget.setColumnCount(2)
        self.userTableWidget.setRowCount(len(self.suggUsers))
        columnNames = ['Screen Name','User Name']
        self.userTableWidget.setHorizontalHeaderLabels(columnNames)
        count = 0
        while count < len(self.suggUsers):
            screenTableWidgetItem = QTableWidgetItem(self.suggUsers[count]['name'])
            userTableWidgetItem = QTableWidgetItem(self.suggUsers[count]['screen_name'])
            self.userTableWidget.setItem(count,0,screenTableWidgetItem)
            self.userTableWidget.setItem(count,1,userTableWidgetItem)
            count += 1
        self.createSubmitButton()

    def createSubmitButton(self):
        self.userMenu = QMenu()
        count = 0
        for users in self.suggUsers:
            self.userMenu.addAction('User {0}'.format(count+1)).triggered.connect(self.addUser)
            count += 1
        self.userActionList = self.userMenu.actions()
        self.addButton()


    def addButton(self):
        self.layout.addWidget(self.selectUserButton,3,1)

    def addUser(self):
        self.userChoice = 0
        while self.userActionList[self.userChoice].text() != self.sender().text():
            self.userChoice += 1
        try:
            data = (self.suggUsers[self.userChoice]['name'],self.suggUsers[self.userChoice]['screen_name'])
            addSuggestedUser(data)
        except:
            error = QMessageBox()
            error.setText('An Error Occured')
            error.setWindowTitle('Error Message')
            error.exec_()
        self.confirmMessage()
            

    def confirmMessage(self):
        confirm = QMessageBox()
        confirm.setText('\'{0}\' added to database'.format(self.suggUsers[self.userChoice]['name']))
        confirm.setWindowTitle('User Added to database')
        confirm.exec_()
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SuggestedInterface()
    window.show()
    window.raise_()
    app.exec_()
        
        
         
