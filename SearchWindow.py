# Kurt Hornett
# COMP4 Practical Project
# Implementation
# Interfaces - Main Interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from MainWindow import *
from TableView import *
from sql_gui_misc import *

import sys

class SearchWindow(QMainWindow):
    def __init__(self,twitter):
        super().__init__()
        #Set Window Title
        self.twitter = twitter
        self.setWindowTitle('Search')

        #Create items for layout
        self.searchLabel = QLabel('Search Term')
        self.searchLineEdit = QLineEdit()
        self.searchButton = QPushButton('Search')
        self.usersLabel = QLabel('Users in Database')

        #Create main search Interface
        self.tableView = QTableView()
        connectDatabase = TableViewWindow()
        self.layout = QGridLayout()
        self.layout.addWidget(self.searchLabel,0,0)
        self.layout.addWidget(self.searchLineEdit,0,1)
        self.layout.addWidget(self.searchButton,1,1)

        #Open and Connect Database
        connectDatabase.createConnectedDatabase()
        #Add Users Widget
        self.createTableModel()
        self.layout.addWidget(self.usersLabel,2,0)
        self.layout.addWidget(self.tableView,3,0,1,2)
        
        #Create This window's widget
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(self.layout)

        #Set Central Layout
        self.setCentralWidget(self.searchWidget)

        #Set Up object Links
        self.searchButton.clicked.connect(self.searchUser)
        
    def createTableModel(self):
        #Creates a Table Model to show the Usrs in Database without ability to edit.
        self.model =QSqlTableModel()
        self.model.setTable('User')
        self.tableView.setModel(self.model)
        self.tableView.model().select()

    def searchUser(self):
        #Allows for searching for a user from Twitter and then ading to Database
        print(self.twitter)
        if self.searchLineEdit.text() != '':
            search = self.searchLineEdit.text()
            self.userList = self.twitter.users.lookup(screen_name=search)
            users = databaseUserList()
            check = False
            for users in users:
                if users[1] == userList[0]['screen_name']:
                    check = True
            if check == False:
                print(self.userList)
            else:
                error = QMessageBox()
                error.setText('User already in database, did not add.')
                error.exec_()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    window.raise_()
    app.exec_()
