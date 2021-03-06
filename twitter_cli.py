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
    print(' 1. Get a Users Time Line')
    print(' 2. Get Home Timeline')
    print(' 3. Print 10 latest Tweets')
    print(' 4. Add User to database')
    print(' 5. Print tweets from User in Database')
    print(' 6. Show Bookmark database')
    print(' 7. Display Single Bookmark')
    print(' 8. Delete bookmark from database')
    print(' 9. Modify bookmark')
    print('10. Display Suggested Users')
    print(' 0. Exit Application')
    print()
    print('Use \'0\' to exit to here anywhere in the program')
    print()

def HomeUserMenu():
    print()
    print('Please select Home Timeline or User Timeline')
    print()
    print('1. Home Timeline')
    print('2. User Timeline')
    print()

def getChoice():
    try:
        choice = int(input('Select number: '))
    except ValueError:
        print('Please enter an integer.')
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
    MY_TWITTER_CREDS = os.path.expanduser('~/.login_credentials')
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
        #Checks to see that the tweets have links; if there are no links then the print statement crashes the
        #programme.
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
        timeline = twitter.statuses.user_timeline(id=input('Please enter screen name: ')) #Gets a users timeline from the API
        return timeline
    except:
        print('An error occured')
              
def displayLinks(hm,count):
    #Prints links as a table
    print('{0:<3} {1:<21}'.format('No.','Link'))
    while count < 10:
        if hm[count]['entities']['urls'] != []:
            print('{0:<3} {1:<21}'.format(count+1,hm[count]['entities']['urls'][0]['url']))
        else:
             print('{0:<3} {1:<21}'.format(count+1,'No Link'))
        count += 1

def displayUsers(users):
    count = 1
    print()
    print('Users in database')
    print()
    #Prints the users in the list
    for user in users:
            print('{0:<3}{1:<21}'.format(count,user[0]))
            count += 1
    print()

def displayUsersTimeline(choice,users,twitter):
    try:
        userTm = twitter.statuses.user_timeline(id=users[choice-1][1])
        count = 0
        displayLatestTweets(userTm,count)
        return userTm
    except:
        print('An error has occured.')


def getYN():
    try:
        YN = input('Commit Action (Y/N): ')
        while YN not in ['y','n','Y','N']:
            YN = input('Input Valid Option: ')
        YN = YN.upper()
        return YN
    except:
        print('An error occured')

def displayBookmarks(List):
    print('{0:<3}{1:<3}{2:<140}{3:<25}{4:<21}'.format(
        'N.','ID','Tweet Text','Link','Username'))
    count = 0
    while count < len(List):
        print('{0:<3}{1:<3}{2:<140}{3:<25}{4:<25}'.format(
            count+1,List[count][5],List[count][0],List[count][3],List[count][4]))
        count += 1

def createIDlist(List):
    IDlist = []
    for count in range(len(List)):
        IDlist.append(List[count][5])
    return IDlist

def DisplaySingleBookmark(List):
    print()
    print('Bookmark Information')
    print()
    print('Title: {0}'.format(List[0][0]))
    print('Site Name: {0}'.format(List[0][1]))
    print('Description: {0}'.format(List[0][2]))
    print('Link: {0}'.format(List[0][3]))
    print()

def displayModifyChoices():
    print()
    print('What to modify?')
    print()
    print('1. Bookmark Title')
    print('2. Site Name')
    print('3. Site Description')
    print('4. Link')
    print()

def getChanges():
    changes = input('Please enter new data: ')
    while changes == '':
        changes = input('Some data must be entered: ')
    return changes

def displaySlugs():
    suggUserSlugs = ['News','Technology','Business']
    count = 0
    print()
    print('Please select the Catergry to get Suggested Users From.')
    print()
    while count < len(suggUserSlugs):
        print('{0}. {1}'.format(count+1,suggUserSlugs[count]))
        count += 1
    print()

def displaySuggestedUsers(suggUsers,twitter):
    count = 0
    print()
    print('Here are the selected users')
    print()
    while count < len(suggUsers):
        print('{0}. {1}'.format(count+1,suggUsers[count]['name']))
        count += 1
    print()
    SuggUserChoice = getChoice()
    if SuggUserChoice != 0:
        FAChoice = chooseFollowAdd()
        if FAChoice != 0:
            FollowAddUser(FAChoice,SuggUserChoice,suggUsers,twitter)

def FollowAddUser(FAChoice,SuggUserChoice,SuggUsers,twitter):
    if FAChoice == 1:
        twitter.friendships.create(id=SuggUsers[SuggUserChoice-1]['screen_name'])
        print('User Followed')
    elif FAChoice == 2:
        userList = []
        userList.append(SuggUsers[SuggUserChoice-1])
        users = getUsersFromDatabase()
        check=False
        for users in users:
            if users[1] == SuggUsers[SuggUserChoice-1]['screen_name']:
                check = True
        if check == False:
            addUserFromSearch(userList)
            print('User Added')
        else:
            print('User already exits, not added')
    elif FAChoice == 3:
        twitter.friendships.create(id=SuggUsers[SuggUserChoice-1]['screen_name'])
        userList = []
        userList.append(SuggUsers[SuggUserChoice-1])
        users = getUsersFromDatabase()
        check=False
        for users in users:
            if users[1] == SuggUsers[SuggUserChoice-1]['screen_name']:
                    check = True
            if check == False:
                addUserFromSearch(userList)
            else:
                print('User already exits, not added')
        print('User Added & Followed')
    else:
        print('Nothing Happened')

def displayForSuggUsers(twitter,choice):
    if choice == 1:
        suggUsers = twitter.users.suggestions.news.members()
        displaySuggestedUsers(suggUsers,twitter)
    elif choice == 2:
        suggUsers = twitter.users.suggestions.technology.members()
        displaySuggestedUsers(suggUsers,twitter)
    elif choice == 3:
        suggUsers = twitter.users.suggestion.business.members()
        displaySuggestedUsers(suggUsers,twitter)
    else:
        print('Invalid Choice')

def chooseFollowAdd():
    print()
    print('Would you like to follow or add a user?')
    print()
    print('1. Follow')
    print('2. Add to Database')
    print('3. Both')
    print()
    choice = getChoice()
    return choice

def checkingStuff(twitter):
    suggUsers = twitter.users.suggestions.news.members()
    count = 0
    while count < len(suggUsers):
        print(suggUsers[count]['screen_name'])
        count += 1
    #print(suggUsers)

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
        while choice not in [0,1,2,3,4,5,6,7,8,9,10,99]:
            choice = getChoice()
        if choice == 1:
            userTm = getUserTimeLine()
        elif choice == 2:
            home_timeline = getHomeTimeline(twitter)
            hm = home_timeline
        elif choice == 3:
            HomeUserMenu()
            HoMo = getChoice()
            if HoMo == 1:
                displayLatestTweets(home_timeline,count)
            elif HoMo == 2:
                displayLatestTweets(userTm,count)
        elif choice == 4:
            databaseMenu()
            choice1 = getChoice()
            while choice1 != 0:
                if choice1 == 1:
                    try:
                        user = getUser(twitter)
                        users = getUsersFromDatabase()
                        check=False
                        for users in users:
                            if users[1] == user[0]['screen_name']:
                                check = True
                        if check == False:
                            addUserFromSearch(user)
                        else:
                            print('User already exits, not added')
                    except:
                        print('An error occured')
                    choice1 = 0
                else:
                    choice1 = 0
        elif choice == 5:
            users = getUsersFromDatabase()
            displayUsers(users)
            Uchoice = getChoice()
            while Uchoice != 0:
                userTm = displayUsersTimeline(Uchoice,users,twitter)
                YN = getYN()
                if YN == 'Y':
                    Tnumber = getChoice()
                    addTweet(users,userTm,Tnumber,Uchoice)
                    addBookmark(userTm,Tnumber)
                elif YN == 'N':
                    Uchoice  = 0
        elif choice == 6:
            List = getBookmarks()
            displayBookmarks(List)
        elif choice == 7:
            Bookmarks = getBookmarks()
            displayBookmarks(Bookmarks)
            BookChoice = getChoice()
            while BookChoice > len(Bookmarks):
                print('Please choose integer in list: ')
                BookChoice = getChoice()
            SingleBookmark = getDataBookmark(BookChoice)
            DisplaySingleBookmark(SingleBookmark)
        elif choice == 8:
            List = getBookmarks()
            displayBookmarks(List)
            print()
            print('Please Choose a Bookmark ID to delete, 0 to exit: ')
            print()
            Dchoice = getChoice()
            if Dchoice != 0:
                BList = getDataBookmark(Dchoice)
                DisplaySingleBookmark(BList)
                DlYN = getYN()
                if DlYN == 'Y':
                    deleteBookamrk(Dchoice)
                else:
                    print('Bookmark not deleted')
            else:
                pass
        elif choice == 9:
            Bookmarks = getBookmarks()
            displayBookmarks(Bookmarks)
            Mchoice = getChoice()
            IDlist = createIDlist(Bookmarks)
            while Mchoice not in IDlist:
                Mchoice = getChoice()
            if Mchoice != 0:
                SingleBookmark = getDataBookmark(Mchoice)
                DisplaySingleBookmark(SingleBookmark)
                displayModifyChoices()
                ModChoice = getChoice()
                while ModChoice not in [0,1,2,3,4]:
                    ModChoice = getChoice()
                if ModChoice != 0:
                    changes = getChanges()
                    ModifyBookmark(Mchoice, ModChoice, changes)
        elif choice == 10:
            displaySlugs()
            SuggChoice = getChoice()
            displayForSuggUsers(twitter,SuggChoice) 
        elif choice == 99:
            checkingStuff(twitter)
        else:
            pass
    
    


