import sys

phrases = {
    'first': ('', ''),
    'second': ('', ''),
    'last': ('', ''),
    }
encoding = sys.stdout.encoding

# Repeats the input string if 3 other peaople have said it in a row
def fred_repeat(phenny, input):
    global phrases
    
    text = input.groups()[1]
    text = text.encode(encoding, 'ignore')
    phrases['first'] = phrases['second']
    phrases['second'] = phrases['last']
    phrases['last'] = (input.nick, text)
    
    if phrases['first'][0] != phrases['second'][0] and phrases['first'][1] == phrases['second'][1]:
        if phrases['first'][0] != phrases['last'][0] and phrases['first'][1] == phrases['last'][1]:
            p = phrases['last'][1]
            phenny.say(p)
            
            # Resets the dict
            phrases = {
                'first': ('', ''),
                'second': ('', ''),
                'last': ('', ''),
                }
fred_repeat.rule = r'^(.*?)(.*)'


if __name__ == "__main__":
    print __doc__.strip()
