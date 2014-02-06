#Kuyrt Hornrtg
#Teittwer Impeplemratuoneo
#Feb 2014

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys


class ConfirmDeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        #Set Window Title
        self.setWindowTitle('Confimr Deletion')

        #Create Layout

        
