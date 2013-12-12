#Kurt Hornett
#Comp4 Practical Project
#Realtional Table view
#Interfaces - Implemetation

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class TableViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set window title
        self.setWindowTitle('Database Management')

        #Open and connect database
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('Bookmark_Database.db')
        self.db.open()

        #Create Table View & Buttons
        self.tableView = QTableView()
        self.cancelButton = QPushButton('Cancel')
        self.submitButton = QPushButton('Submit')

        #Create Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.tableView,0,0)
        self.layout.addWidget(self.cancelButton,1,0)
        self.layout.addWidget(self.submitButton,1,1)

        #Create Central Widget
        self.tableWidget = QWidget()
        self.tableWidget.setLayout(self.layout)
        self.setCentralWidget(self.tableWidget)

        #Create Table Model
        self.createTableModel()

    def createTableModel(self):
        self.model =QSqlRelationalTableModel()
        self.model.setEditStrategy(QSqlRelationalTableModel.OnManualSubmit)
        self.model.setTable('Bookmark')
        self.tableView.setModel(self.model)
        self.tableView.model().select()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableViewWindow()
    window.show()
    window.raise_()
    app.exec_()
        
        
