import re, praw, webbrowser, urllib2, sys
import requests
from urlparse import urlparse
from datetime import datetime
from bs4 import BeautifulSoup


# *******
# GLOBALS
# *******
USER = os.environ['REDDIT_USER']
PASS = os.environ['REDDIT_PASS']

# posting test info
subreddit = os.environ['REDDIT_SUBREDDIT']

# user agent info
user_agent = os.environ['REDDIT_USER_AGENT']

# config your black list here
BLACK_LIST = [
    'gyazo.com',
    'whiteboard.wheresthepart.at',
    'dropbox',
    'ejohn.org',
    'goo.gl']

# supported media types
MEDIA = {
    'jpg',
    'jpeg',
    'mov',
    'png',
    'gif',
    }


# START TESTING CONFIGS
# # reddit API key
# api_key = os.environ['REDDIT_API_KEY']

# # api dev keys
# client_secret = os.environ['REDDIT_CLIENT_SECRET']
# client_id = os.environ['REDDIT_CLIENT_ID']
# redirect_uri = os.environ['REDDIT_REDIRECT_URI']
# END TESTING CONFIGS


# *********
# FUNCTIONS
# *********
def fetch_html(link):
    try:
        response = requests.get(link)
        html_text = response.text

        if type(html_text) == unicode:
            html_text = html_text.encode('ascii', 'ignore')

        return html_text
    except Exception as e:
        print e

    return


# checks if link is in blacklist / returns bool
def inBlackList(link):
    in_list = False
    for item in BLACK_LIST:
        if item in link:
            in_list = True
    return in_list


# Grabs you a token key
def getAuthToken(r):
    url = r.get_authorize_url('uniqueKey', 'identity', True)
    webbrowser.open(url)


# Refreshes AuthToken
def refresh_access(r):
    r.refresh_access_information(access_information['refresh_token'])


# fetches and returns the links title
def getTitle(html):
    html = html.encode('ascii', 'ignore')
    soup = BeautifulSoup(html)

    try:
        title = soup.title.get_text()
        # encoding = sys.stdout.encoding
        # title = title.encode(encoding, 'ignore')
        title = title.encode('ascii', 'ignore')
    except:
        title = 'No title'

    # special case titles
    if 'Gyazo' in title:
        title = 'Gayzo!'

    return title.strip() + ' | '


# Posts the params to /r/wtpa
def redditPOST(USER, PASS, user_agent, subreddit, title, post_url):
    # creates the reddit obj
    r = praw.Reddit(user_agent)

    # logging in
    r.login(USER, PASS)

    # setting oauth params
    # r.set_oauth_app_info(client_id, client_secret, redirect_uri)

    # exchanging codes for access info
    # access_info = r.get_access_information(api_key)

    r.submit(subreddit, title, url=post_url)


# main phenny call
def link_catch(phenny, input):

    # pulls the actual link from the regex groups
    temp = str(input.groups()[1])
    link = temp.split(' ')[0]
    urlGood = True
    title = ''

    if not inBlackList(link):

        try:

            link_extension = urlparse(link).path.split('.')[-1]

            if link_extension not in MEDIA:

                # Fetches the HTML text
                html = fetch_html(link)

                # Pulls the links title from HTML
                title = getTitle(html)

            if title == 'No Title | ' or title == '':
                net_loc = urlparse(link).netloc
                if net_loc.count('.') > 1:
                    title = net_loc.split('.', 1)[1]
                else:
                    title = net_loc

                title += ' | '


        except Exception as e:
            print e, '|', link
            urlGood = False
            pass

        finally:

            if urlGood:

                # takes nick name from input obj
                nick = input.nick

                # gets time and formats to string
                post_time = str(datetime.now())
                post_time = post_time.replace('-', '/')
                post_time = post_time.replace(' ', ' - ')
                post_time = post_time.split('.')[0]

                # concats everything into a single string
                post_title = title + post_time + ' by ' + nick

                # # for testing
                # phenny.say(post_title) # says post string
                # phenny.say(link)      # says actual link

                # # this is the actuall posting. put error handling here
                try:
                    redditPOST(USER, PASS, user_agent, subreddit, post_title, link)
                except:
                    print 'POST FAIL'
                    pass

            else:
                print 'failed: ' + link

    else:
        print 'black: ' + link

link_catch.rule = r'^(.*?)(https?://.+)\b(.*)$'



if __name__ == '__main__':
   print __doc__.strip()

