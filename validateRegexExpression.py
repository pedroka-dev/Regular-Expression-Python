import re

class validateRegex:
    def isValidExpression(regexInput,string):
        match = re.fullmatch(regexInput, string, re.MULTILINE)
        #print("Match found: {match}".format(start = match.start(), end = match.end(), match = match.group()))
        return match

    def valitateStringList(regexInput, listOfStrings):
        for expression in listOfStrings:
            if(validateRegex.isValidExpression(regexInput,expression)):
             print("---Test passed for expression: '" + expression + "'")
            else:
                print("!!!Test failed. Invalid expression '" + expression + "' is not compatible with regex input.")



### Tests cases
regexTest = r"^(?![a-z])[A-Z]([(a-z)|( )|(,)]*)([.]|[!]|[?])$"
#One sentence, with the first letter uppercase commas and spaces
#The sentence can contain lettes, commas and spaces.
#The sentence should not contain numbers, special characters or accents
#The setence should end with exactly one period or one exclamation point or one interrogation point.

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
print("===================SHOULD ALL PASS===================")
validateRegex.valitateStringList(regexTest, valid_strings_list)

#Invalid
invalid_strings_list = [
    "Invalid because cammelCase.",
    "AEIOU Invalid because multiple uppercases.",
    "INVALID BECAUSE UPPERCASE.",
    "Invalid because nummbers like 1 to 9.",
    "Invalid because multiple dots...",
    "Invalid because multiple exclamations!!!",
    "Invalid because numbers like 1 to 9..",
    "Invalid because #@#&*+- characters.",
    "Invalid because áóéíãõââ characters.",
]
print("===================SHOULD ALL FAIL===================")
validateRegex.valitateStringList(regexTest, invalid_strings_list)
