# THIS IS BUILT FOR FRED ONLY AT TIME OF CREATION
# SPECIFICALLY FOR SEX CLOCK
import os

# grab the CWD of the bot and adjust to the module level
CWD = os.getcwd()
CWD += '\modules'
FRED_FILE = os.path.join(CWD, 'fred.txt')
FRED = ''

# ******************************** #
# storeFRED                        #
# takes old nick, new nick to edit #
# ******************************** #

def storeFRED(oldnick, newnick):
    with open(FRED_FILE) as F:
        text = F.readlines()
    with open(FRED_FILE, 'w') as F:
        for entry in text:
            print 'entry: ' + entry.strip()
            if entry.strip() == oldnick:
                F.write(newnick)
            else:
                F.write(entry)
    print 'Fred change'

def retrieveFRED():
    with open(FRED_FILE) as F:
        for line in F:
            fred = line.strip()
    return fred


# updates the phonebook on nick change
def nick_update(phenny, input):
    oldnick = ''
    global FRED
    if not FRED:
        FRED = retrieveFRED()
    
    temp = input.group().split(' ')
    oldnick = input.nick
    newnick = temp[-1]
    print oldnick + " | " + newnick
    if oldnick == FRED:
        FRED = newnick
        storeFRED(oldnick,newnick)
    
nick_update.event = 'NICK'
nick_update.rule = r'.*'
nick_update.priority = 'high'

if __name__ == '__main__': 
   print __doc__.strip()
