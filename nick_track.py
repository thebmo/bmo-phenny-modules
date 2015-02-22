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
def store(names, nick='', user='' ):
    
    # If user is specified updates user nick
    if user:
        try:
            names[user]['nick'] = nick

        except Exception as e:
            print user, 'not in dict |', e
            pass
    
    # Saves the dict to pickle file
    n = open(NAMES_FILE, 'wb')
    pickle.dump(names, n)
    n.close()
        


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
    
    store(names, newnick, user)
    print user, '|', oldnick, '->', newnick    
nick_updater.event = 'NICK'
nick_updater.rule = r'.*'
nick_updater.priority = 'high'


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
        phenny.msg(input.nick, name_info)
    except Exception as e:
        phenny.msg(input.nick, 'Nick not found.')
        pass
fetch_name.commands = ['name']


# Add an entry to the pickle file
# name nick num email
def add_name(phenny, input):
    
    if not input.admin: return
    try:
        params = input.groups()[1].split(' ')
    except:
        print 'No Params| name nick num email'
        return

    if not params or len(params) < 4:
        phenny.msg(input.nick, 'bad params| name nick num email')
        return
    
    names = load_names()
    names[params[0]] = { 'nick': params[1], 'num': params[2], 'email': params[3] }
    store(names)
    p_confirm = 'Added %s' % names[params[0]]
    phenny.msg(input.nick, p_confirm)
add_name.commands = ['add_name']
    

# Deletes the user from the pickle file
# Takes nick as argument and 
def delete_name(phenny, input):
    if not input.admin: return
    
    try:
        nick = input.groups()[1].split(' ')[0]
        names = load_names()
        name = retrieve_name(nick, names)
        del names[name]
        store(names)
        p_confirm = 'Deleted %s' % nick
        phenny.msg(input.nick, p_confirm)

    except Exception as e:
        p_error = 'Could not delete %s' % nick
        phenny.msg(input.nick, p_error)
        print e, p_error
        pass
delete_name.commands = ['delete_name']
    
    
    

# def update_name(phenny, input):


if __name__ == '__main__': 
   print __doc__.strip()
