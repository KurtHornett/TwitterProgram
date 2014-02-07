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

class SuggestedInteface(QMainWindow):
    def __init__(self):
        super().__init__()
        #set Window Title
        self.setWindowTile('Suggested Users')

        #Set up Inerface
        self.slugButton = QPushButton('Select Topic')
         
