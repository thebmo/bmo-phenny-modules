import os

# grab the CWD of the bot and adjust to the module level
CWD = os.getcwd()
CWD += '\modules'
R_LIST = os.path.join(CWD, 'request_list.txt')

# actually writes to the R_LIST file
def write_request(requester, request):
    with open(R_LIST, 'a') as f:
        f.write('\n' + requester + ': ' + request)
    return True

# calls the helper function
def make_request(phenny, input):
    """ make a bot feature request"""
    request = input.groups()[1]
    requester = input.nick
    if(write_request(requester, request)):
        phenny.say('Request Logged')
make_request.commands = ['request']
make_request.priority = 'medium'
make_request.example = '.request <your request>'


# calls the helper function to list the requests
def list_requests(phenny, input):
    with open(R_LIST, 'r') as f:
        for line in f:
            phenny.msg(input.nick,line)
    
list_requests.commands = ['request_list']
list_requests.priority = 'medium'



if __name__ == "__main__":
    print __doc__.strip()