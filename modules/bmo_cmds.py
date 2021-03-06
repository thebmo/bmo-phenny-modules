import random
import time


# # juju always remembers
# def member(phenny, input):
#     phenny.say('I MEMBER!')
# member.rule = r'^(.*?)(\b(?i)(re)?member\b)(.*)$'

# juju says wow some times
def wow(phenny, input):
    random.seed(time.time())
    rand = random.randint(0, 500)
    print rand
    
    if (rand > 450) and (rand % 2 == 0):
    	wow = 'wow... | https://youtu.be/KlLMlJ2tDkg'
    	phenny.say(wow)
wow.rule = r'^(.*?)(\b(?i)wow\b)(.*)$'

# responds to oh jeez
def oh_jeez(phenny, input):
    jeez = 'Ooooh JEEZ! | https://youtu.be/gGrNAB45CtY'
    phenny.say(jeez)
oh_jeez.rule = r'^(.*?)(\b(?i)o*h\s?je*z\b)(.*)$'

# responds to dedicated with the deditated wam video
def dedicated_ram(phenny, input):
    wam = 'DEDITATED WAM FOR UR SERBER? | https://youtu.be/LP0HYIkHs2Q'
    phenny.say(wam)
dedicated_ram.rule = r'^(.*?)(\b[dD][eE][dD][iI][cC][aA][tT][eE][dD]\b)(.*)$'


# Dennis, the cat?
def dennis(phenny, input):
    # if not input.admin: return

    phenny.say('The Cat?')
dennis.rule = r'^(.*?)(\b[dD][eE][nN][nN][iI][sS]\b)(.*)$'


# SO >> VIOLATION
# Yells at lauren when she starts a line with
# any varyation of "so"
def sov(phenny, input):

    if input.nick == 'lauren':
        punc = { ',', ':', ';', '\'', '!', '?', '.' }
        words = input.groups()[1].lower()

        first_word = words.split(' ')[0]

        for p in punc:
            first_word = first_word.replace(p, '')

        if first_word == 'so':
            phenny.say("VIOLATION!")

sov.rule = r'^(.*?)(^(?i)so.*)(.*)$'
sov.priority = 'medium'


# Responds with You're right
def urite(phenny, input):
    rite = ''.join((input.nick, ':', ' urite!'))
    phenny.say(rite)
urite.rule = r'^(.*?)(\b(?i)amirite\b)(.*)$'


# Chooses a random item from the input
# Pipe Seperated
def choose_one(phenny, input):
    choices = input.groups()[1]
    if choices.count(' or ') == 1:
        choices = choices.split(' or ')
    else:
        choices = choices.split('|')

    if len(choices) > 1:
        phenny.say(random.choice(choices))
choose_one.commands = ['choose']

# Links: Too many cooks video if regex catches a similar phrase
def too_many_cooks(phenny, input):
    TOO = input.groups()[1].upper()
    MANY = 'https://youtu.be/QrGrOK8oZG8'
    COOKS = ' | '.join((TOO, MANY))
    phenny.say(COOKS)
too_many_cooks.rule = r'^(.*?)(\b(?i)too.many.+ks\b)(.*)$'


# links WTPA whiteboard
def wtpa(phenny, input):
    params = str(input.groups()[1]).lower()

    if 'help' in params:
        link = 'commands: drama, reddit'
    elif 'drama' in params:
        link = 'http://whiteboard.wherestheparty.at/wiki/Drama'

    elif 'reddit' in params:
        link = 'http://www.reddit.com/r/wtpa'

    else:
        link = 'http://whiteboard.wherestheparty.at/ use HELP for more options'

    phenny.say(link)
wtpa.commands = ['wtpa']
wtpa.priority = 'medium'


# DAGON BE PRAISED
def dagon(phenny, input):
    if not input.admin: return

    phenny.say('DAGON BE PRAISED!!')
dagon.rule = r'^(.*?)(\b[dD][aA][gG][oO][nN]\b)(.*)$'


# # VIOLATION
# def violation(phenny, input):
    # # if not input.admin: return
    # if 'http' in str(input) or len(str(input).split(' ')) > 2:
        # phenny.say("VIOLATION!")
    # else:
        # phenny.say(input)
# violation.rule = r'^(.*?)([vV][iI][oO][lL][aA][tT][iI][oO][nN])(.*)$'


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


# # auto correct drama to diarrhea
def diarrama(phenny, input):
    # g = input.nick + ": " + input.groups()[1]
    # phenny.say(g)
    phenny.say('%s: *diarrhea' % input.nick)
diarrama.rule = r'^(.*?)(\b(?i)drama\b)(.*)$'


# tests for group(1) text
def group_test(phenny, input):
    # g = input.groups()[1]
    # g = g.split(' ')
    # phenny.say(g[1])

    phenny.say(input.groups()[1])
group_test.commands = ['gpt']


# the help request
def help(phenny, input):
    # help list
    available_cmds = '.wtpa .request .request_list' # .text .getnum'

    # more = 'for more info try: .help <command>'
    more = 'Available Commands:'

    params = input.groups()[1]

    # if params == None:
    phenny.msg(input.nick, more)
    phenny.msg(input.nick, available_cmds)
help.commands = ['help']
help.priority = 'medium'


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


if __name__ == '__main__':
    print __doc__.strip()
