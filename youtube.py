# Video examples for testing. Phennybot's framework
# does not support REGEX grouping, so I've implemented
# some conditional testing. These examples were very useful
#
# embedded video example #1 
# http://www.youtube.com/embed/AA56LgpFbSw?rel=0
#
# embedded video example #2
# http://www.youtube.com/watch?feature=player_embedded&v=n7Z67Wky214
#
# standard video example
# http://www.youtube.com/watch?v=cHN_HR-9-R4
import json
import os
import urllib2
import re


DEV_KEY = os.environ['YT_DEV_KEY']


# strips a string of html entities
def reformat(temp):
    temp = temp.replace('&#39;', '\'')
    temp = temp.replace('&quot;', '\"')
    temp = temp.replace('&amp;', '&')
    return temp


# Returns the JSON data as a dict
def fetch_json_data(DEV_KEY, videoID):

    data_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=snippet,contentDetails'.format(videoID, DEV_KEY)

    response = urllib2.urlopen(data_url)

    # Returns a dict of a list of dicts (items)
    data = json.loads(response.read())

    return data['items'][0]

    
# builds out the duration as a string
# takes duration as PTxxHxxMxxS format, returns as str [x:xx:xx]
def get_duration(duration):
    
    duration = duration.replace('PT', '')
    hours=''
    minutes = seconds = '00'
    
    if 'H' in duration:
        hours = '{}:'.format(duration.split('H')[0])
        duration = duration.split('H')[1]
    if 'M' in duration:
        minutes = duration.split('M')[0].zfill(2)
        duration = duration.split('M')[1]
    if 'S' in duration:
        seconds = duration.replace('S', '').zfill(2)
   
    
    time = ' [{}{}:{}]'.format(hours, minutes, seconds)

    return time
    
# main phenny call
def say_title(phenny, input):

    
    # sets url to trailing part of youtube URL string
    url = input.groups()[2]

    try:
        # catches embed ex. #1
        if re.search('embed/', url):
            url = url.replace('embed/', '')
            videoID = url.replace('?rel=0', '')
        
        # catches embed ex. #2
        elif re.search('player_embed', url):
            videoID = url.replace('watch?feature=player_embedded&v=', '')  
        
        # standard player url, checks for time bookmark &t=3m47s
        else:
            videoID = url.replace('watch?v=', '')
            if re.search('&', videoID):
                vid_temp = ''
                for char in videoID:
                    if char == '&':
                        break
                    else:
                        vid_temp += char
                videoID = vid_temp
        
        # builds the title string to passback to phenny
        
        # calls to the youtube api, returns object with all the metadata
        data  = fetch_json_data(DEV_KEY, videoID)
        
        # sets title to objs title property
        title = reformat(data['snippet']['title'])
        
        # sets duration from the JSON obj (PTxxHxxMxxS)
        duration = data['contentDetails']['duration']

        # adds duration to title string
        title += get_duration(duration)
        
        phenny.say(title)
        
    except Exception as e:
        print e
        print 'bad youtube url: %s' % url
say_title.rule = r'^(.*?)(youtu.?be.*?/)([\w?=/&-]+)\b(.*)$'
# say_title.rule = r'^(.*?)(https?://www.youtube.com/)([\w?=/&-]+)\b(.*)$'



if __name__ == '__main__': 
   print __doc__.strip()