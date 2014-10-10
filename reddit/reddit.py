# This class is used to pass sensative information to the main
# reddit_post.py file.

class RedditCreds:
    
    # user creds and blacklist
    USER = 'your username'
    PASS = 'your password'
    BLACK_LIST = ['blacklistdomain.com']
    
    # reddit api key
    api_key = 'yourapikey'
    
    # # api dev keys
    client_secret ='yourclientsecret'
    client_id = 'yourclientid'
    redirect_uri = 'http://127.0.0.1:65010/authorize_callback'
    
    # posting test info
    subreddit = 'your subreddit to post'

    # user agent info
    user_agent = 'this is a string to explain what your bot does so it doesnt get banned'