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
    
    eLOGIN = os.environ['eLOGS_UN']
    ePWD = os.environ['eLOGS_PW']  
    eURL = 'http://ejohn.org/wtpa/wtpa/logs/?q='
    eurl = ''.join((eURL, q))
    
    
    entries = []

    if q == 'none' or q == ' ':
        phenny.say('No Query Selected')
        return
    
    # JMThree Logs
    try:
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (LOGIN, PWD)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        result = urllib2.urlopen(request)

        html = result.readline()
        result.close()

        soup = BeautifulSoup(html)

        # stuffs all entries into a list
        for line in soup.select("tr"):
            entry = line.get_text(' ', strip=True)
            entries.append(entry)

    except urllib2.HTTPError as e:
        if '404' in e:
            phenny.say('Too many searches, please wait a while')
        else:
           e = str(e) + ' | Search must be 4 or more characters'
           phenny.say(e)
           return
        pass
    # END JM3 logs


    # eJohn Logs
    try:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()

        passman.add_password(None, eurl, eLOGIN, ePWD)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        results = urllib2.urlopen(eurl)


        html = results.read().replace('<em>', ' ')

        soup = BeautifulSoup(html)

        div_tag = soup.div
        div = div_tag.get_text().split('#wtpa ')

        for d in div:
            entries.append(d.strip('\n'))

    except Exception as e:
        e_str = ''.join(('ejohn error | ', str(e)))
        phenny.msg('BMO', e_str)
        print e_str
        pass
    
    if not entries:
        phenny.say('Sorry no matches')
    else:
        phenny.say(rand(entries))

search_log.commands = ['logs']
search_log.priority = 'medium'

if __name__ == '__main__': 
   print __doc__.strip()