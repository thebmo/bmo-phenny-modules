import urllib2
import re


# strips a string of html entities
def reformat(temp):
    new_temp = temp.decode("utf-8")
    temp = new_temp.encode("ascii", "ignore")
    temp = temp.replace('&#39;', '\'')
    temp = temp.replace('&quot;', '\"')
    temp = temp.replace('<br/>', ' ')
    temp = temp.replace('\r', ' ')
    temp = temp.replace('\\', '')
    temp = ' '.join(temp.split())

    # strips out link tags if any
    link_match = re.search(r'(<.*?>)', temp)
    while(link_match):
        temp = temp.replace(link_match.group(), '')
        link_match = re.search(r'(</*a.*?>)', temp)

    temp = temp.strip()
    temp = temp.replace('</div><div class=\"example\">', '[!]')
    temp = temp.replace('</div><div class="example">', '[!]')
    temp = temp.replace('<div class="example">', '[!]')
    return temp.split('[!]')


# temp test variable
def urban_search(original_search):
    definition = ''
    example = ''

    # foramts the orginal search string into proper URL format
    search = original_search.replace(' ', '+')

    # the actual search string
    URL = 'http://www.urbandictionary.com/define.php?term=' + search
    html = ''
    # variable to store metadata in memory
    response = urllib2.urlopen(URL)
    html = response.read()

    # string to check if search item is defined
    not_defined = r"<i>" + re.escape(original_search)

    # match = re.search(r'<div class="definition">(.+)</div>', html)
    match = re.search(r'<div class=\'meaning\'>\n(.+)\n</div>', html)

    if re.search(not_defined, html):
        def_error = original_search + " not defined"
        return def_error
    else:
        if match:
            temp = ''
            temp = str(reformat(match.group(1)))
            full_def = original_search + ": " + temp
            return full_def

        else:
            return 'this failed somehow'


def urban(phenny, input):
    search = input.groups()[1]
    s = urban_search(search)
    phenny.msg(input.nick, s)
urban.commands = ['urb']
urban.priority = 'medium'

if __name__ == "__main__":
    print __doc__.strip()
