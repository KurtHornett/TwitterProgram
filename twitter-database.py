#Kurt Hornett
#COMP4 - Implemetation
#Twitter CLI - Database management
#Dec 2013

from twitter import *

from twitter-cli import *

import sqlite3

def databaseMenu():
    print()
    print('Database Management Aspect')
    print()
    print('1. Add Tweet to database')
    print()

def addToDatabase(hm,count):
    with sqlite3.connect('Bookmark_database-cli-test.db') as db:
        cursor = db.cursor()
        sql = ''' '''
        cursor.execute(sql,data)
        db.commit()

if __name__ == '__main__':
    databaseMenu()
    choice = getChoice()
    while choice != 0:
        if choice == 1:
            
    
