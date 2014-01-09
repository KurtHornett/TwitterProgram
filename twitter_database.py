#Kurt Hornett
#COMP4 - Implemetation
#Twitter CLI - Database management
#Dec 2013

from twitter import *

import re
import urllib.request

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
        link = hm[number-1]['entities']['urls'][0]['url']
        bookmarkTitle,siteName,siteDesc = getBookmarkData(link)
    else:
        link = 'No Link'
        bookmarkTitle,siteName,siteDesc = getBookmarkData(link)
    data = (bookmarkTitle,siteName,siteDesc,link,tweetID[0][0])
    query(sql,data)

def getLatestTweet():
    sql = '''SELECT TweetID FROM Tweet WHERE TweetID = (SELECT MAX(TweetID) FROM Tweet)'''
    maxId = searchQuery(sql)
    return maxId

def getBookmarkData(link):
    bookmarkTitle = input('Please enter a title for the bookmark: ')
    siteName = 'Null'
    siteDesc = 'Null'
    if link != 'No Link':
        try:
            #Create RE for finding title
            regex = re.compile('<title>(.+?)</title>')
            url = urllib.request.urlopen(link) #Gets the data from the url
            html = url.read() #Converts HTTPRequest into text
            html = str(html) #Changes from 'bytes' to str so re will work
            print(regex.search(html).group(1))
            siteName = regex.search(html).group(1)
            siteDesc = input('Please enter a short description of the site: ')
        except:
            print()
            print('No HTML Title Found')
    return bookmarkTitle,siteName,siteDesc

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
            
    
