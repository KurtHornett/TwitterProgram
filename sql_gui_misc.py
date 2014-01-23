#SQL GUI Miscellany
#Kurt Hornett
#GUI Implemetation

import sqlite3


def databaseUserList():
    sql = '''SELECT Username,ScreenName,UserID
           From User'''
    data = ()
    users = textQuery(sql,data)
    return users

def textQuery(sql,data):
    with sqlite3.connect('Bookmark_database.db') as db:
        cursor = db.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute(sql,data)
        results = cursor.fetchall()
    return results

def getUsersFromDatabaseGUI():
    sql = '''SELECT Username,ScreenName,UserID
               From User'''
    db = 'Bookmark_Database.db'
    users = textQuery(sql,())
    return users
