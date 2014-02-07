#Kuyrt Hornrtg
#Teittwer Impeplemratuoneo
#Feb 2014

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys


class ConfirmDeleteDialog(QDialog):
    def __init__(self,list_,choice):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Confimr Deletion')

        self.list = list_
        self.choice = choice

        #Create Layout
        self.helpLabel = QLabel('This is going to be deleted')
        self.submitButton = QPushButton('Submit')
        self.titleLabel = QLabel('Title')
        self.titleLineEdit = QLineEdit()
        self.titleLineEdit.setReadOnly(True)
        self.linkLabel = QLabel('Link')
        self.linkLineEdit = QLineEdit()
        self.linkLineEdit.setReadOnly(True)
        self.siteNameLabel = QLabel('Site Name')
        self.siteNameLineEdit = QLineEdit()
        self.siteNameLineEdit.setReadOnly(True)
        self.siteDescLabel = QLabel('Site Description')
        self.siteDescLineEdit = QLineEdit()
        self.siteDescLineEdit.setReadOnly(True)

        self.confirmLayout = QGridLayout()
        self.confirmLayout.addWidget(self.helpLabel,0,0)
        self.confirmLayout.addWidget(self.titleLabel,1,0)
        self.confirmLayout.addWidget(self.titleLineEdit,1,1,1,3)
        self.confirmLayout.addWidget(self.linkLabel,2,0)
        self.confirmLayout.addWidget(self.linkLineEdit,2,1)
        self.confirmLayout.addWidget(self.siteNameLabel,2,2)
        self.confirmLayout.addWidget(self.siteNameLineEdit,2,3)
        self.confirmLayout.addWidget(self.siteDescLabel,3,0)
        self.confirmLayout.addWidget(self.siteDescLineEdit,3,1,1,3)
        self.confirmLayout.addWidget(self.submitButton,4,3)

        self.setLayout(self.confirmLayout)

        self.setData()

        self.submitButton.clicked.connect(self.close)

    def setData(self):
        self.titleLineEdit.setText(self.list[self.choice][1])
        self.linkLineEdit.setText(self.list[self.choice][4])
        self.siteNameLineEdit.setText(self.list[self.choice][2])
        self.siteDescLineEdit.setText(self.list[self.choice][3])
