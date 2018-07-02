from random import randrange

def roll(phenny, input):
    total = 0

    try:
        rstring = input.groups()[1].strip().split(' ')[0]
        rlist = rstring.split('d')

        if len(rlist) < 2:
            rlist = rstring.split('D')
            
        for i in range(int(rlist[0])):
            total += randrange(1, int(rlist[1])+1)

        msg = "{} rolled a {}!".format(input.nick, total)
        phenny.say(msg)

    except Exception as e:
        print(e)
roll.commands = ['roll']
roll.priority = 'medium'

if __name__ == "__main__":
    print __doc__.strip()

