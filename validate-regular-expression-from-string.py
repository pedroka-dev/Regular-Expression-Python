import re

# Method
def isValidExpression(regexInput,string):
    match = re.fullmatch(regexInput, string, re.MULTILINE)
    if(match != None):
        #print("Match found: {match}".format(start = match.start(), end = match.end(), match = match.group()))
        return True
    else:
        return False


# Tests
regex = r"^(?![a-z])[A-Z]([(a-z)|( )|(,)]*)([.]|[!]|[?])$"

def valitateStringList(listOfStrings):
    for expression in listOfStrings:
        if(isValidExpression(regex,expression)):
            print("---Test passed for expression: '" + expression + "'")
        else:
            print("!!!Test failed. Invalid expression '" + expression + "' is not compatible with regex input.")

valid_strings_list = [
    "Be kind, for everyone you meet is fighting a harder battle.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Aaaaaaaaaaaaa.",
    "Aaaaaaaaaaaaa!",
    "Aaaaaaaaaaaaa?",
    "Aaaaaaa aaaaa aaaaaaa.",
    "Asafsafsafassaffsaafssfaasf.",
    "Aaaaaa,aaaaaaa.",
]

invalid_strings_list = [
    "Invalid because cammelCase.",
    "INVALID BECAUSE UPPERCASE.",
    "Invalid because mbers like 1 to 9.",
    "Invalid because multiple dots...",
    "Invalid because multiple exclamations!!!",
    "Invalid because numbers like 1 to 9..",
    "Invalid because #@#&*+- characters.",
    "Invalid because áóéíãõââ characters.",
    "Invalid because áóéíãõââ characters.",
]

valitateStringList(valid_strings_list)
valitateStringList(invalid_strings_list)
