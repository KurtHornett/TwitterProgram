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
    with sqlite3.connect('Bookmark_database-cli-test-2.db') as db:
        cursor = db.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute(sql,data)
        db.commit()

def searchQuery(sql,data):
    with sqlite3.connect('Bookmark_database-cli-test-2.db') as db:
        cursor = db.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute(sql,data)
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
    users = searchQuery(sql,())
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
    if checkAdd(data,tweetID):
        query(sql,data)
    else:
        pass

def getLatestTweet():
    sql = '''SELECT TweetID FROM Tweet WHERE TweetID = (SELECT MAX(TweetID) FROM Tweet)'''
    maxId = searchQuery(sql,())
    return maxId

def getBookmarkData(link):
    bookmarkTitle = input('Please enter a title for the bookmark: ')
    siteName = 'Null'
    siteDesc = 'Null'
    if link != 'No Link':
        try:
            #Create RE for finding title
            regex = re.compile('<title>(.*?)</title>')
            url = urllib.request.urlopen(link) #Gets the data from the url
            html = url.read() #Converts HTTPRequest into text
            html = str(html) #Changes from 'bytes' to str so re will work
            siteName = regex.search(html).group(1)
            siteDesc = input('Please enter a short description of the site: ')
        except:
            print()
            print('No HTML Title Found')
            print()
    return bookmarkTitle,siteName,siteDesc

def getBookmarks():
##    sql = '''SELECT TweetText,UserID, TweetID FROM Tweet'''
##    sql2 = '''SELECT Link FROM Bookmark WHERE TweetID = ?'''
##    sql3 = '''SELECT Username FROM User WHERE UserID = ?'''
    sql = '''SELECT Tweet.TweetText,Tweet.UserID,Tweet.TweetID,Bookmark.Link,User.Username,Bookmark.BookmarkID FROM
             Tweet,User,Bookmark WHERE Bookmark.TweetID = Tweet.TweetID AND Tweet.UserID = User.UserID'''
    tweetList = searchQuery(sql,())
    return tweetList

def deleteBookamrk(Dchoice):
    sql = '''DELETE FROM Bookmark WHERE BookmarkID = ?'''
    query(sql,(Dchoice,))
    
def checkAdd(data,tweetID):
    print()
    print('Are you sure you wish to add this bookamrk?')
    print()
    print('Title: {0}'.format(data[0]))
    print('Site Name: {0}'.format(data[1]))
    print('Site Description: {0}'.format(data[2]))
    print('Link: {0}'.format(data[3]))
    username = getIndieUser(tweetID)
    print('User: {0}'.format(username[0][0]))
    print()
    YNadd = getYN()
    print()
    if YNadd == 'Y':
        return True
    else:
        return False

def getIndieUser(tweetID):
    sql = '''SELECT Username FROM User,Tweet WHERE Tweet.TweetID = ? AND Tweet.UserID = User.UserID'''
    username = searchQuery(sql,(tweetID[0][0],))
    return username

def getDataBookmark(choice):
    sql = '''SELECT BookmarkTitle,SiteName,SiteDescription,Link FROM Bookmark
             WHERE BookmarkID = ?'''
    data = (choice,)
    bookmarks = searchQuery(sql,data)
    return bookmarks

def ModifyBookmark(Mchoice,ModChoice,changes):
    if ModChoice == 1:
        sql = '''UPDATE Bookmark
                 SET BookmarkTitle = ?
                 WHERE BookmarkID = ?'''
    elif ModChoice == 2:
        sql = '''UPDATE Bookmark
                 SET SiteName = ?
                 WHERE BookmarkID = ?'''
    elif ModChoice == 3:
        sql = '''UPDATE Bookmark
                 SET SiteDescription = ?
                 WHERE BookmarkID = ?'''
    elif ModChoice == 4:
        sql = '''UPDATE Bookmark
                 SET Link = ?
                 WHERE BookmarkID = ?'''
    data = (changes,Mchoice)
    query(sql,data)

if __name__ == '__main__':
    user = getUser(twitter)
    addUserFromSearch(user)
            
    
