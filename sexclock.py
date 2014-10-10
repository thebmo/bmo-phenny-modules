import os
from datetime import datetime
# 2014-05-11 02:30:49.246000


# ***********
# * GLOBALS *
# ***********
LAST_SEX = ''
# LAST_SEX_OBJ = ''

CWD = os.getcwd()
sex_file = CWD + '\\modules\\last_sex.txt'
sex_log  = CWD + '\\modules\\sex_log.txt'
FRED_FILE = CWD + '\\modules\\fred.txt'
# not sure this is needed
# # Primes the LAST_SEX string variable
# with open(sex_file) as S:
    # for line in S:
        # LAST_SEX = line

def convertLAST_SEX():
    return datetime.strptime(LAST_SEX, '%Y-%m-%d %H:%M:%S')
        
# retrieves stored time as an obj to manipulate
def retrieveLAST_SEX():
    with open(sex_file) as SEX:
        for sex in SEX:
            time = sex
        time = time.split('.')[0]
    return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

# resets the sexclock
def resetClock():
    global LAST_SEX
    # global sex_file
    # global sex_log
    
    LAST_SEX = str(datetime.now())
    with open(sex_file, 'w') as S:
        S.write(LAST_SEX)
    
    with open(sex_log, 'a') as log:
        log.write(LAST_SEX + '\n')

# clock command params
clock_cmds = 'reset, update'
error = 'use commands: ' + clock_cmds + ' (must be fred to reset)'

# the sexClock request
def sexClock(phenny, input):
    FRED = retrieveFRED()
    global LAST_SEX
    params = input.groups()[1]
    try:
        params = params.split(' ')[0].lower()
        # phenny.say(params)
        if params == 'reset' and input.nick == FRED:
            phenny.say('    -    C                                     ,  .-.___')
            phenny.say('  -     /<                                   @/  /xx\\XXX\\')
            phenny.say(' -   __/\ `\                                \/\  |xx|XXX|')
            phenny.say('    `    \, \_ =                            _\<< |xx|XXX|')
            phenny.say('""""""""""""""""NICE""""SCORE""""FAGGOT""""""""""""""""""')
            # phenny.say('clock reset')
            resetClock()
        elif params == 'update':
            if LAST_SEX == '' or LAST_SEX == None:
                LAST_SEX = str(retrieveLAST_SEX())
            LAST_SEX = LAST_SEX.split('.')[0]
            now = datetime.now()
            time = now - convertLAST_SEX()
            last_date = 'Sex Last Had: ' + LAST_SEX
            time_since = 'Time since last sex: ' + str(time)
            phenny.say(last_date)
            phenny.say(time_since)
        else:
            phenny.say(error)
    except:
        phenny.say(error)
        pass
sexClock.commands = ['sexclock']
sexClock.priority = 'medium'

# borrowed from nick_track find a better method of imporint this.
def retrieveFRED():
    with open(FRED_FILE) as F:
        for line in F:
            fred = line.strip()
    return fred

# for debugging
def testClock(phenny, input):
    global LAST_SEX
    print LAST_SEX
    phenny.say(LAST_SEX)
    
testClock.commands = ['testClock']
testClock.priority = 'medium'
    
if __name__ == '__main__': 
   print __doc__.strip()
