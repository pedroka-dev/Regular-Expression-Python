import re

# Method

def isValidExpression(regexInput,string):
    match = re.fullmatch(regexInput, string, re.MULTILINE)
    if(match != None):
        #print("Match found: {match}".format(start = match.start(), end = match.end(), match = match.group()))
        return True
    else:
        return False