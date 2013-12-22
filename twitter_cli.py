#Kurt Hornett
#COMP4 - Implemetation
#Twitter Implemetation work - MarkII
#Dec 2013

#External Modules
from twitter import *
from sqlite3 import *

#User Made Maodules
from twitter_database import *

#System Modules
import os
import pickle

#Creation of a CLI Inteface for interacting with twitter.
#Limiting to viewing 10 latest tweets from timeline for testing purposes.

def mainMenu():
    #Typical main menu 
    print()
    print('Twitter Management Program')
    print()
    print('1. Get a Users Time Line')
    print('2. Get Home Timeline')
    print('3. Print 10 latest Tweets')
    print('4. Add Tweet to database')
    print('0. Exit Application')
    print()

def HomeUserMenu():
    print()
    print('Please select Home Timeline or User Timeline')
    print()
    print('1. Home Timeline')
    print('2. User Timeline')
    print()

def getChoice():
    choice = int(input('Select number: '))
    return choice

def getConsumerKey():
    #Get Consumer key from hidden file - API advises it's kept secret
    with open('.consumer_key.txt','rb') as key:
        consumer_key = pickle.load(key)
    return consumer_key

def authApp(consumer_key):
    #All necessary proceedures for authorising app and therefore loggin into twitter, doesn't allow log out.
    #Uses PIN authorization  - could change to UserPass later in app stages and implemetation
    #MY_TWITTER_CREDS = os.path.expanduser('~/.login_credentials')
    if not os.path.exists(MY_TWITTER_CREDS):
        oauth_dance("KurtsApp",'Y4zkic6lw0Hu6uB3sNVH4Q', consumer_key,
                        MY_TWITTER_CREDS)


def createTwitterObject():
    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    #Creation of twitter object with authorized detailes.
    twitter = Twitter(auth=OAuth(
        oauth_token, oauth_secret, 'Y4zkic6lw0Hu6uB3sNVH4Q', consumer_key))
    return twitter

def getHomeTimeline(twitter):
    #Creates home_timeline object with all available tweets from the home timeline. 
    home_timeline = twitter.statuses.home_timeline()
    return home_timeline

def displayLatestTweets(hm,count):
    #Print information of 10 latest tweets as a table
    print('{0:<3}{1:<15}{2:<140}{3:<21}'.format('No.','Screen Name','Tweet Text','Links'))
    while count < 10:
        if hm[count]['entities']['urls'] != []:
            print('{0:<3}{1:<15}{2:<140}{3:<21}'.format(count+1,hm[count]['user']['screen_name'],
                                                            hm[count]['text'],
                                                            hm[count]['entities']['urls'][0]['url']))
        else:
            print('{0:<3}{1:<15}{2:<140}{3:<21}'.format(count+1,hm[count]['user']['screen_name'],
                                                            hm[count]['text'],
                                                            'No Link'))
            
        count += 1

def getUserTimeLine():
    try:
        timeline = twitter.statuses.user_timeline(id=input('Please enter screen name: '))
        return timeline
    except:
        print('An error occured')
              
def displayLinks(hm,count):
    print('{0:<3} {1:<21}'.format('No.','Link'))
    while count < 10:
        if hm[count]['entities']['urls'] != []:
            print('{0:<3} {1:<21}'.format(count+1,hm[count]['entities']['urls'][0]['url']))
        else:
             print('{0:<3} {1:<21}'.format(count+1,'No Link'))
        count += 1
def checkingStuff(hm,count):
    while count <= 10:
        print(hm[count]['entities']['urls'])
        count += 1

if __name__ == "__main__":
    #Consumer key required regardless
    consumer_key = getConsumerKey()
    MY_TWITTER_CREDS = os.path.expanduser('~/.login_credentials')
    authApp(consumer_key)
    twitter = createTwitterObject()
    choice = 1
    count = 0
    #Typical while loop for managing program.
    #0 being catch-out for exiting program.
    while choice != 0:
        mainMenu()
        choice = getChoice()
        if choice == 1:
            userTm = getUserTimeLine()
        if choice == 2:
            home_timeline = getHomeTimeline(twitter)
            hm = home_timeline
        if choice == 3:
            HomeUserMenu()
            HoMo = getChoice()
            if HoMo == 1:
                displayLatestTweets(home_timeline,count)
            else:
                displayLatestTweets(userTm,count)
        if choice == 4:
            databaseMenu()
            choice = getChoice()
            while choice != 0:
                if choice == 1:
                    number = int(input('Enter number tweet to add: '))
                    addUser(hm,number)
                    addTweet(hm,number)
                    addBookmark(hm,number)
        if choice == 9:
            displayLinks(home_timeline,count)
        
        
    