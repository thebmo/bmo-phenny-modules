import gdata.youtube
import gdata.youtube.service
import re
from modules.youtube.You_Tube_Creds import yCREDS


# Video examples for testing. Phennybot's framework
# does not support REGEX grouping, so I've implimented
# some conditional testing. These examples were very useful

# embedded video example #1 
# http://www.youtube.com/embed/AA56LgpFbSw?rel=0

# embedded video example #2
# http://www.youtube.com/watch?feature=player_embedded&v=n7Z67Wky214

# standard video example
# http://www.youtube.com/watch?v=cHN_HR-9-R4

# instanciates an instance of your youtubecredentials
creds = yCREDS

# strips a string of html entities
def reformat(temp):
    temp = temp.replace('&#39;', '\'')
    temp = temp.replace('&quot;', '\"')
    temp = temp.replace('&amp;', '&')
    return temp

# builds out the duration as a string
# takes duration as int, returns as str [x:xx:xx]
def get_duration(duration):
    
    # sets Hour, minute, remainder seconds
    # based off duration input in seconds
    d_hours = 0
    d_mins = duration/60
    if d_mins > 60:
        d_hours = d_mins/60
        d_mins = d_mins%60
    d_secs = duration%60
   
   # for formating seconds
    s_lead = 1
    if d_secs < 10:
        s_lead = 2
    
   # for formating minutes
    m_lead = 1
    if d_mins < 10:
        m_lead = 2
    
    # duration as a string
    d_time = ''
    
    # checks for hour time and adds to d_time if true
    if d_hours > 0:
        d_time+= str(d_hours) + ':'
    
    # builds the rest of duration as string
    d_time += str(d_mins).zfill(m_lead) + ":" + str(d_secs).zfill(s_lead)
    
    return ' [' + d_time +']'
    
# main phenny call
def say_title(phenny, input):
    
    # opens the youtube service
    yt_service = gdata.youtube.service.YouTubeService()
	
    # authorize - you need to sign up for your own access key, or be rate-limited
    yt_service.developer_key = creds.DEV_KEY
    yt_service.client_id = creds.CLIENT_ID
    
    # for testing regex groups from input
    # print input.groups()[1]
    # print input.groups()[2]
    
    # sets url to trailing part of youtube URL string
    url = input.groups()[2]
    
    try:
        # catches embed ex. #1
        if re.search('embed/', url):
            url = url.replace('embed/', '')
            VideoID = url.replace('?rel=0', '')
        
        # catches embed ex. #2
        elif re.search('player_embed', url):
            VideoID = url.replace('watch?feature=player_embedded&v=', '')  
        
        # standard player url, checks for time bookmark &t=3m47s
        else:
            VideoID = url.replace('watch?v=', '')
            if re.search('&', VideoID):
                vid_temp = ''
                for char in VideoID:
                    if char == '&':
                        break
                    else:
                        vid_temp += char
                VideoID = vid_temp
        
        # builds the title string to passback to phenny
        
        # calls to the youtube api, returns object with all the metadata
        entry  = yt_service.GetYouTubeVideoEntry(video_id=VideoID)
        
        # sets title to objs title property
        title = reformat(entry.media.title.text)
        
        # sets duration as int from objs duration property
        duration = int(entry.media.duration.seconds)

        # adds duration to title string
        title += get_duration(duration)
        
        phenny.say(title)
        
    except gdata.service.RequestError as e:
        print 'RequestError: %s' % e
        print 'bad youtube url: %s' % url
say_title.rule = r'^(.*?)(https?://www.youtube.com/)([\w?=/&-]+)\b(.*)$'



if __name__ == '__main__': 
   print __doc__.strip()