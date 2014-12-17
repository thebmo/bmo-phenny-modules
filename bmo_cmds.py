import random


# DAGON BE PRAISED
def dagon(phenny, input):
    if not input.admin: return
    
    phenny.say('DAGON BE PRAISED!!')

dagon.rule = r'^(.*?)(\b[dD][aA][gG][oO][nN]\b)(.*)$'

# joins a channel
def chan_join(phenny, input):
    
    #admins only!
    if not input.admin: return
    channel = input.groups()[1]
    phenny.write(['JOIN'], channel)
chan_join.commands = ['join']
chan_join.priority = 'medium'


# leaves a channel
def leave_chan(phenny,  input):
    if not input.admin: return
    channel = input.groups()[1]
    phenny.write(['PART'], channel)
leave_chan.commands = ['leave']
leave_chan.priority = 'medium'

# drama to diarrhea
def diarrama(phenny, input):
    # g = input.nick + ": " + input.groups()[1]
    # phenny.say(g)
    phenny.say('%s: *diarrhea' % input.nick)
diarrama.rule = r'^(.*?)(\b[dD][rR][aA][mM][aA]\b)(.*)$'
    
def group_test(phenny, input):
    phenny.say(input.groups()[1])
group_test.commands = ['gpt']


# maybe some day
# # corrects fredbot
# def fredbot_fewest(phenny, input):
    # phenny.say('Fredbot: *least')
# fredbot_fewest.rule = r'^(.*?)(\bfewest\b)(.*)$'

# def fredbot_fewer(phenny, input):
    # # g = input.nick + ": " + input.groups()[1]
    # # phenny.say(g)
    # phenny.say('Fredbot: *less')
# fredbot_fewer.rule = r'^(.*?)(\bfewer\b)(.*)$'

# help list
available_cmds = '.request .request_list .text .getnum'
more = 'for more info try: .help <command>'

# the help request
def help(phenny, input):
    params = input.groups()[1]
    
    if params == None:
        phenny.msg(input.nick, available_cmds)
        phenny.msg(input.nick, more)
help.commands = ['help']
help.priority = 'medium'

    
if __name__ == '__main__': 
   print __doc__.strip()