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
    print('1. Add Tweet to database')
    print()

def query(sql,data):
    with sqlite3.connect('Bookmark_database-cli-test.db') as db:
        cursor = db.cursor()
        cursor.execute(sql,data)
        db.commit()

        
def addUser(hm,number):
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
    databaseMenu()
    choice = getChoice()
    while choice != 0:
        if choice == 1:
            number = int(input('Enter number tweet to add: '))
            data = (hm[number]['user']['user_name'],
                    hm[number]['user']['screen_name'],
                    hm[number]['text'],
                    'Bookmark x',
                    'Site name',
                    'Good Site',
                    hm[number]['entites']['urls'][0]['url'],
                    1
                )
            addToDatabase(data)
            
    
