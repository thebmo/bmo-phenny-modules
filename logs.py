import base64
import os
import urllib2
from bs4 import BeautifulSoup
from random import choice as rand


def search_log(phenny, input):
    q = str(input.groups()[1]).lower().replace(' ', '%20')
    LOGIN = os.environ['LOGS_UN']
    PWD = os.environ['LOGS_PW']

    URL = 'http://wtpa.jmthree.com/buttlog/?query='
    url = ''.join((URL, q))

    try:
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (LOGIN, PWD)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)

        html = result.readline()
        result.close()

        # # for testing, reads from a file instead of pings the site
        # butters = 'C:\\Users\\bmo\\Desktop\\phenny\\modules\\butters.html'
        # with open(butters, 'r') as B:
            # html = B.read()

        soup = BeautifulSoup(html)

        entries = []
        # stuffs all entries into a list
        for line in soup.select("tr"):
            entry = line.get_text(' ', strip=True)
            entries.append(entry)
        if q == 'none' or q == ' ':
            phenny.say('No Query Selected')
        else:
            if not entries:
                phenny.say('Sorry no matches')
            else:
                phenny.say(rand(entries))
    except urllib2.HTTPError as e:
        if '404' in e:
            phenny.say('Too many searches, please wait a while')
        else:
            print 'logs.py', e

search_log.commands = ['logs']
search_log.priority = 'medium'

if __name__ == '__main__': 
   print __doc__.strip()