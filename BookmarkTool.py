#Kurt Hornett
# COMP4 Practical Project
# Implemetation - Interfaces
# Bookmark Creation interface

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class BookmarkWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set Window Title
        self.setWindowTitle('Bookamrk Creation Tool')

        
