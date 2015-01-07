import random
import nltk

# says a doge into channel if input is not a link and
# a random number is met. A % of the time
def doge(phenny, input):

    s = input.groups()[1]

    # if 'http' not in s and ':' not in s:
    go = True if random.randrange(250) == 249 else False
    # go = True # for testing, makes doge go every text entry

    # doesn't execute if a link or go statement unsatisfied.
    if 'http' not in s and '\x01' not in s and go:
        s = s.lower()

        # good NLTK tags to use
        good_tags = ['NN', 'VBG', 'VBN', 'NNS', 'VB'] # 'VBP', 'VBD'

        # exception words to leave out
        bad_words = ['be', 'been', 'being', 'their', 'theirs', 'everything']
        
        # doge phrases to be selected by random below
        doges = ['many', 'much', 'such', 'so', 'no']

        # populates the word bank
        words = []
        tokes = nltk.pos_tag(nltk.word_tokenize(s))

        for word in tokes:
            # prints each token for testing purpose. helps to track doge output too
            print word
            if word[1] in good_tags and len(word[0]) > 2 and word[0] not in bad_words:
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

            # changes a word that ends in 'er' to 'ing'
            for i, word in enumerate(s):
                if len(s) > 3:
                    if s[i][-2:] == 'er':
                        s[i] = word.strip('er')
                        s[i] = ''.join((s[i], 'ing'))

            # builds out the doge strings into a list
            doge = [
                        'wow',
                        '                 %s %s' % (d1, s[0]),
                        '    %s %s' % (d2, s[1]),
                        '                                    wow'
                        ]

            # prints the doge to irc
            for d in doge:
                phenny.say(d)

doge.rule = r'^(.*?)(.+\b.+)$'
doge.priority = 'high'
# doge.commands = ['doge']

if __name__ == '__main__': 
   print __doc__.strip()