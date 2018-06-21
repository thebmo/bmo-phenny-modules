import json
import requests
import os
    
# Shortens a link via the google link shortener api
def link_shortener(phenny, input):
    
    # pulls the actual link from the regex groups
    temp = str(input.groups()[1])
    long_link = temp.split(' ')[0]
    if len(long_link) < 70: return

    key = os.environ['YT_DEV_KEY']

    post_url = "https://www.googleapis.com/urlshortener/v1/url?key={}".format(key)
    resource = {'longUrl': long_link}
    headers = {'content-type': 'application/json' }
    
    response = requests.post(post_url,data=json.dumps(resource), headers=headers)
    try:
        short_link = str(response.json()['id'])
        phenny.say(short_link)
    except Exception as e:
        error_msg = "{}: {}".format(e.__class__, e)
        phenny.say("ARF!")

link_shortener.rule = r'^(.*?)(https?://.+)\b(.*)$'



if __name__ == '__main__': 
   print __doc__.strip()
