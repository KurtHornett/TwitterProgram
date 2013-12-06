# Kurt Hornett
# COMP4 Program - Database Implementation
# Dec 2013

import sys
import sqlite3

def create_database(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute('select name from sqlite_master where name=?',(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("Table {0} alread exists, recreate? (y/n): ".format(table_name))
            if response == 'y':
                keep_table = False
                print('Table {0} recreated - all previous data shall be lost.'.format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print('Existing table kept')
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

if __name__ == "__main__":
    db_name = 'Bookmark_Database.db'
    SqlUser = """CREATE TABLE User(
                UserID INTEGER
                UserName TEXT
                ScreenName TEXT
                PRIMARY KEY(UserID))"""
    SqlTweet = """CREATE TABLE Tweet(
                TweetID INTEGER
                UserID INTEGER
                TweetText TEXT
                PRIMARY KEY(TweetID)
                FOREIGN KEY(UserID)
                REFERNECES User(UserID))"""
    SqlBookmark = """CREATE TABLE Bookmark(
               BookmarkID INTEGER
               BookmarkTitle TEXT
               SiteName TEXT
               SiteDescription TEXT
               Link TEXT
               TweetID INTEGER
               PRIMARY KEY(BookmarkID)
               FOREIGN KEY(TweetID)
               REFERNCES Tweet(TweetID))"""
    create_database(db_name,'User',SqlUser)
    create_database(db_name,'Tweet',SqlTweet)
    craete_database(db_name,'Bookmark',SqlBookmark)

            
