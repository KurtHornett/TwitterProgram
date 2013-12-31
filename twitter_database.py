#Kurt Hornett
#COMP4 - Implemetation
#Twitter CLI - Database management
#Dec 2013

from twitter import *

from twitter_cli import *

import sqlite3

def databaseMenu():
    print()
    print('Database Management Aspect')
    print()
    print('1. Add User to database')
    print()

def query(sql,data):
    with sqlite3.connect('Bookmark_database-cli-test.db') as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

def searchQuery(sql):
    with sqlite3.connect('Bookmark_database-cli-test.db') as db:
        cursor = db.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()
        return users

def getUser(twitter):
    try:
        search = input('Please enter handle to search for: ')
        userList = twitter.users.lookup(screen_name=search)
        return userList
    except:
        print('An error has occcured')

def getUsersFromDatabase():
    sql = '''SELECT Username,ScreenName
               From User'''
    users = searchQuery(sql)
    return users

def addUserFromSearch(userList):
    sql = '''INSERT INTO User(UserName,ScreenName)
               VALUES(?,?)'''
    data = (userList[0]['name'],userList[0]['screen_name'])
    query(sql,data)

def addUserFromTweet(hm,number):
    sql = '''INSERT INTO User(UserName,ScreenName)
               Values(?,?)'''
    data = (hm[number]['user']['name'],hm[number]['user']['screen_name'])
    query(sql,data)

def addTweet(hm,number):
    sql = '''INSERT INTO Tweet(TweetText) VALUES(?)'''
    data = (hm[number]['text'],)
    query(sql,data)

def addBookmark(hm,number):
    sql = '''INSERT INTO Bookmark(BookmarkTitle,SiteName,SiteDescription,Link,TweetID)
               VALUES(?,?,?,?,?)'''
    data = ('Null Title','Null Site Name','Null Site Description',hm[number]['entities']['urls'][0]['url'],
            1)
    query(sql,data)

if __name__ == '__main__':
    user = getUser(twitter)
    addUserFromSearch(user)
            
    
