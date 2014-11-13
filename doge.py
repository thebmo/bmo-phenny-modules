import random
def doge(phenny, input):
    
    doges = ['many', 'much', 'such', 'so', 'no']
    d1 = random.choice(doges)
    doges.remove(d1)
    d2 = random.choice(doges)

    s = input.groups()[1]
    if 'http' not in s and ':' not in s:
        s = s.split(' ')
        r1 = s[random.randrange(0, len(s))]
        r2 = ''
        while(r2 == '' or r2 == r1):
            r2 = s[random.randrange(0, len(s))]
        if r2[-2:] == 'er':
            r2 = r2.strip('er')
            r2 = ''.join((r2, 'ing'))

        phenny.say('wow')
        phenny.say('                 %s %s' % (d1, r1))
        phenny.say('    %s %s' % (d2, r2))
doge.rule = r'^(.*?)(.+\b.+)$'
    
if __name__ == '__main__': 
   print __doc__.strip()