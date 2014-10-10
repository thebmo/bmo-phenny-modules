# This class is used to pass sensative information to the main
# reddit_post.py file.

class RedditCreds:
    
    # user creds and blacklist
    USER = 'JujuTheDog'
    PASS = 'qazwert$0369'
    BLACK_LIST = ['gyazo.com', 'whiteboard.wheresthepart.at', 'dropbox', 'ejohn.org']
    
    # reddit api key
    api_key = 'N4pMshxY3jRTfmBuFHJGBvsp67o'
    
    # # api dev keys
    client_secret ='onjVXgYW3oan2gos_PwtHtxegEo'
    client_id = 'T3UOEWO5sM4JMw'
    redirect_uri = 'http://127.0.0.1:65010/authorize_callback'
    
    # posting test info
    subreddit = 'wtpa'

    # user agent info
    user_agent = 'This bot uses praw to upload links to reddit from WTPA'