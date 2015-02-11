import os
import vimeo
import pprint


def vimeo_title(phenny, input):
    access_token = os.environ['VIMEO_TOKEN']
    client_secret = os.environ['VIMEO_SECRET']
    api_key =  os.environ['VIMEO_API']

    VID = input.groups()[2]
    
    v = vimeo.VimeoClient(
        token=access_token,
        key=api_key,
        secret=client_secret)


    # assert about_me.status_code == 200  # Make sure we got back a successful response.
    # print about_me.json()   # Load the body's JSON data.

    video = v.get('/videos/108018156')
        
    # p = pprint.PrettyPrinter()
    # p.pprint(video.json())

    duration = get_duration(video.json()['duration'])
    title = video.json()['name']
    full_title = "%s -%s" % (title, duration)
    phenny.say(full_title)

vimeo_title.rule = r'^(.*?)(vimeo.com?/)([\w?=/&-]+)\b(.*)$'


# builds out the duration as a string
# takes duration as int, returns as str [x:xx:xx]
# taken from youtube
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

    
if __name__ == '__main__':
   print __doc__.strip()
   