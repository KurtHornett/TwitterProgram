#SQL GUI Miscellany
#Kurt Hornett
#GUI Implemetation

import sqlite3
from twitter_database import *

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

def addBookmarkGUI(data,db):
    sql = '''INSERT INTO Bookmark(BookmarkTitle,SiteName,SiteDescription,Link,TweetID)
               VALUES(?,?,?,?,?)'''
    query(sql,data,db)

def addTweetGUI(data):
    sql = '''INSERT INTO Tweet(TweetText,UserID) VALUES(?,?)'''
    db = 'Bookmark_Database.db'
    query(sql,data,db)

def getLatestTweetGUI():
    sql = '''SELECT TweetID FROM Tweet WHERE TweetID = (SELECT MAX(TweetID) FROM Tweet)'''
    db = 'Bookmark_Database.db'
    maxId = searchQuery(sql,(),db)
    return maxId

def getBookmarkNumber():
    sql = '''SELECT * FROM Bookmark'''
    db = 'Bookmark_Database.db'
    data = ()
    list_ = textQuery(sql,data)
    num = len(list_)
    return num, list_

def deleteBookmarkGUI(Dchoice):
    sql = '''DELETE FROM Bookmark WHERE BookmarkID = ?'''
    db = 'Bookmark_Database.db'
    query(sql,(Dchoice,),db)

    
        
