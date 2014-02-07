#Kurt Honrtt
#Twitter Implemenatuib
# Feb 2014

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from sql_gui_misc import *
from twitter_database import *
from ConfirmDeleteDialog import *

import sys

class DeleteInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Deletion Interface')

        #Open and connect database
        self.createConnectedDatabase()

        #Create Objects
        self.helpLabel = QLabel('Bookmarks available to delete: ')
        self.cancelButton = QPushButton('Cancel')
        self.deleteButton = QPushButton('To Delete')
        self.deleteTable = QTableView()

        #Create Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.helpLabel,0,0)
        self.layout.addWidget(self.deleteTable,1,0,1,2)
        self.layout.addWidget(self.cancelButton,2,0)
        self.layout.addWidget(self.deleteButton,2,1)

        #Set Central Widget
        self.deleteWidget = QWidget()
        self.deleteWidget.setLayout(self.layout)
        self.setCentralWidget(self.deleteWidget)

        #Create Tabel Model
        self.createTableModel()
        self.createDeleteAction()

        #connexions
        self.deleteButton.clicked.connect(self.showDeleteMenu)

    def showDeleteMenu(self):
        self.deleteMenu.exec_(QCursor.pos())

    def createTableModel(self):
        self.model = QSqlRelationalTableModel()
        self.model.setEditStrategy(QSqlRelationalTableModel.OnManualSubmit)
        self.model.setTable('Bookmark')
        self.deleteTable.setModel(self.model)
        self.deleteTable.model().select()

    def createConnectedDatabase(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('Bookmark_Database.db')
        self.db.open()

    def createDeleteAction(self):
        self.deleteMenu = QMenu()
        num, self.bookmarkList = getBookmarkNumber()
        for count in range(num):
            self.deleteMenu.addAction('Bookmark # {0}'.format(self.bookmarkList[count][0])).triggered.connect(self.getDeleteOption)
        self.deleteActionList = self.deleteMenu.actions()
    def getDeleteOption(self):
        self.deleteChoice = 0
        count = 0
        while self.deleteActionList[count].text() != self.sender().text():
            count +=1
            self.deleteChoice += 1
        self.confirmDelete()

    def confirmDelete(self):
        try:
            self.confirmDialog = ConfirmDeleteDialog(self.bookmarkList,self.deleteChoice)
            self.confirmDialog.show()
            self.delete()
        except:
            error = QMessageBox()
            error.setText('An Error Occured')
            error.exec_()

    def delete(self):
        deleteBookmarkGUI(self.bookmarkList[self.deleteChoice][0])
        self.createTableModel()
        self.createDeleteAction()
        

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeleteInterface()
    window.show()
    window.raise_()
    app.exec_()
        
        
