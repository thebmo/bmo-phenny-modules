import os
import cPickle as pickle

# grab the CWD of the bot and adjust to the module level
CWD = os.getcwd()
CWD += '\modules'
NAMES_FILE = os.path.join(CWD, 'names.p')


# Returns the names from the pickle file
def load_names():
    n = open(NAMES_FILE, 'rb') 
    names = pickle.load(n)
    n.close()
    return names


# Saves the users to the pickle file
def store(user, names, newnick):
    try:
        names[user]['nick'] = newnick
        n = open(NAMES_FILE, 'wb')
        pickle.dump(names, n)
        n.close()

    except Exception as e:
        print user, 'not in dict |', e
        pass


# Creates a reverse dict and returns a name key string
def retrieve_name(oldnick, names):
    rnames = {}
    for k, v in names.items():
        rnames[v['nick']] = k
    
    try:
        name = rnames[oldnick]
        return name

    except Exception as e:
        print 'nick tracker | nick not found:', e
    

# Catches a name change and updates the master list
# Runs on automatic nick changes
def nick_updater(phenny, input):
    
    names = load_names()
    
    temp = input.group().split(' ')
    oldnick = input.nick
    newnick = temp[-1]
    
    user = retrieve_name(oldnick, names)
    
    store(user, names, newnick)
    print user, '|', oldnick, '->', newnick    
nick_update.event = 'NICK'
nick_update.rule = r'.*'
nick_update.priority = 'high'


# Prints all names
def print_names(phenny, input):
    
    names = load_names()
    
    for name in names:
        p_name = ' | '.join((
            name, 
            names[name]['nick'], 
            names[name]['num'], 
            names[name]['email']
            ))
        phenny.msg(input.nick, p_name)
print_names.commands = ['directory']


# Nick/Name fetcher
# Accepts a user nick and returns their info only
def fetch_name(phenny, input):
    names = load_names()
    nick = input.groups()[1]
    nick = nick.split(' ')[0]
    
    user = retrieve_name(nick, names)
    try:
        name_info = ' | '.join((user, names[user]['nick'],  names[user]['num'], names[user]['email']))
        phenny.say(name_info)
    except Exception as e:
        phenny.say('Nick not found.')
        pass
fetch_name.commands = ['name']

# def add_name(phenny, input):
# def update_name(phenny, input):


if __name__ == '__main__': 
   print __doc__.strip()
