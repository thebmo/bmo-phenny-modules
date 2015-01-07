import time


def meow(phenny, input):
    if not input.admin:
        phenny.msg(input.nick, 'uh uh uh. you didnt say the magic word')
        return

    try:
        g = input.groups()[1]
        g = g.split(' ')
        TARGET = g[0]
        DELAY = int(g[1])
    
        TIME = 3600*24
        time.sleep(DELAY)
        meow = [
            '   _.---.._             _.---...__',
            '.-\'   /\   \          .\'  /\     /',
            '`.   (  )   \        /   (  )   /',
            '  `.  \/   .\'\      /`.   \/  .\'',
            '    ``---\'\'   )    (   ``---\'\'',
            '            .\';.--.;`.',
            '          .\' /_...._\ `.',
            '        .\'   `.a  a.\'   `.',
            '       (        \/        )',
            '        `.___..-\'`-..___.\'',
            '           \          /',
            '            `-.____.-\'   meooooow!'
            ]
        
        while True:
            for line in meow:
                phenny.msg(TARGET, line)
            time.sleep(TIME)

    except:
        USAGE = '.meow <TARGET> <SECONDS>'
        phenny.say(USAGE)
        pass
        
meow.commands = ['meow']
meow.priority = 'high'
    
if __name__ == '__main__': 
   print __doc__.strip()
