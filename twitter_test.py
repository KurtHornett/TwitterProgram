# Kurt Hornett
# COMP4 - Implemetation
# Twitter Stream
# Dec 2013

from twitter import *
import os

MY_TWITTER_CREDS = os.path.expanduser('U:\Computing A2\CourseworkProgram\my_app_creds')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("KurtsApp",'Y4zkic6lw0Hu6uB3sNVH4Q', 'YuE239eH7r1wKsGj8KIPTdIXRCipdNaBVHu7al3sF7I',
                        MY_TWITTER_CREDS)
oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, 'Y4zkic6lw0Hu6uB3sNVH4Q', 'YuE239eH7r1wKsGj8KIPTdIXRCipdNaBVHu7al3sF7I'))
    
# Now work with Twitter
tm = twitter.statuses.home_timeline()
print(tm[0]['user']['screen_name'])
print(tm[0]['text'])
    
