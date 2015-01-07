import time


def meow(phenny, input):
    if not input.admin: return
    DELAY = int(input.groups()[1])
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
            phenny.msg('lauren', line)
        time.sleep(TIME)
        
meow.commands = ['meow']
meow.priority = 'high'
    
if __name__ == '__main__': 
   print __doc__.strip()
