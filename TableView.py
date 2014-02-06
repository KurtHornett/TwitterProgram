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
        self.createConnectedDatabase()

        #Create Table View & Buttons
        self.tableView = QTableView()
        self.label = QLabel('Edit Bookmarks and click \'Submit\'')
        self.cancelButton = QPushButton('Cancel')
        self.submitButton = QPushButton('Submit')

        #Create Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.label,0,0)
        self.layout.addWidget(self.tableView,1,0,1,2)
        self.layout.addWidget(self.cancelButton,2,0)
        self.layout.addWidget(self.submitButton,2,1)

        #Create Central Widget
        self.tableWidget = QWidget()
        self.tableWidget.setLayout(self.layout)
        self.setCentralWidget(self.tableWidget)

        #Create Table Model
        self.createTableModel()

        #Connexions
        self.submitButton.clicked.connect(self.updateModify)

    def createTableModel(self):
        self.model = QSqlRelationalTableModel()
        self.model.setEditStrategy(QSqlRelationalTableModel.OnManualSubmit)
        self.model.setTable('Bookmark')
        self.tableView.setModel(self.model)
        self.tableView.model().select()

    def createConnectedDatabase(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('Bookmark_Database.db')
        self.db.open()

    def updateModify(self):
        try:
            self.model.submitAll()
            doneMessage = QMessageBox()
            doneMessage.setWindowTitle('Confimation Message')
            doneMessage.setText('Database modified')
            doneMessage.exec_()
        except:
            error = QErrorMessage()
            error.showMessage('An Eror Occured')
            error.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableViewWindow()
    window.show()
    window.raise_()
    app.exec_()
        
        
