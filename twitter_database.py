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
        results = cursor.fetchall()
        return results

def getUser(twitter):
    try:
        search = input('Please enter handle to search for: ')
        userList = twitter.users.lookup(screen_name=search)
        return userList
    except:
        print('An error has occcured')

def getUsersFromDatabase():
    sql = '''SELECT Username,ScreenName,UserID
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

def addTweet(Users,UserTm,Tnumber,Uchoice):
    sql = '''INSERT INTO Tweet(TweetText,UserID) VALUES(?,?)'''
    data = (UserTm[Tnumber-1]['text'],Users[Uchoice-1][2])
    query(sql,data)

def addBookmark(hm,number):
    sql = '''INSERT INTO Bookmark(BookmarkTitle,SiteName,SiteDescription,Link,TweetID)
               VALUES(?,?,?,?,?)'''
    tweetID = getLatestTweet()
    if hm[number-1]['entities']['urls'] != []:
        link = hm[number-1]['entities']['urls'][0]['expanded_url']
    else:
        link = 'No Link'
    data = ('Null','Null','Null',link,tweetID[0][0])
    query(sql,data)

def getLatestTweet():
    sql = '''SELECT TweetID FROM Tweet WHERE TweetID = (SELECT MAX(TweetID) FROM Tweet)'''
    maxId = searchQuery(sql)
    return maxId

def getBookmarkData():
    bookmarkTitle = input('Please enter a title for the bookmark: ')
    
    return bookmarkTitle

def getBookmarks():
##    sql = '''SELECT TweetText,UserID, TweetID FROM Tweet'''
##    sql2 = '''SELECT Link FROM Bookmark WHERE TweetID = ?'''
##    sql3 = '''SELECT Username FROM User WHERE UserID = ?'''
    sql = '''SELECT Tweet.TweetText,Tweet.UserID,Tweet.TweetID,Bookmark.Link,User.Username FROM
             Tweet,User,Bookmark WHERE Bookmark.TweetID = Tweet.TweetID AND Tweet.UserID = User.UserID'''
    tweetList = searchQuery(sql)
    return tweetList

if __name__ == '__main__':
    user = getUser(twitter)
    addUserFromSearch(user)
            
    
