import random
import nltk

def doge(phenny, input):
    
    s = input.groups()[1]
    
    # doesn't execute if a link
    # if 'http' not in s and ':' not in s:
    if 'http' not in s:
        s = s.lower()
        good_tags = ['NN', 'NNS', 'VBG', 'VBP']
        doges = ['many', 'much', 'such', 'so', 'no']
        words = []
        tokes = nltk.pos_tag(nltk.word_tokenize(s))
        
        # populates the word bank
        for word in tokes:
            if word[1] in good_tags and len(word[0]) > 2 and '\'' not in word[0]:
                words.append(str(word[0]))
        
        # proceeds only if there are sufficient words
        if len(words) > 1:
            # picks the 2 doge terms
            d1 = random.choice(doges)
            doges.remove(d1)
            d2 = random.choice(doges)

            # picks 2 string words from input and stuffs them into a list
            s = []
            s.append(random.choice(words))
            words.remove(s[0])
            s.append(random.choice(words))
            
            for i, word in enumerate(s):
                if len(s) > 3:
                    if s[i][-2:] == 'er':
                        s[i] = word.strip('er')
                        s[i] = ''.join((s[i], 'ing'))

            # builds out the doge strings into a list
            doge = ['wow', '                 %s %s' % (d1, s[0]), '    %s %s' % (d2, s[1])]
            
            # randomizes the order of the doge strings
            random.shuffle(doge)

            # prints the doge to irc
            for d in doge:
                phenny.say(d)

doge.rule = r'^(.*?)(.+\b.+)$'
# doge.commands = ['doge']
    
if __name__ == '__main__': 
   print __doc__.strip()