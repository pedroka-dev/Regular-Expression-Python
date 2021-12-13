# Introduction
A Python script that verifies if string is part of the determined regular expression or not. The script can accept other custom regular expression as param too, but for now only the expected expression is verified.  

# Regular expression Parameters
  - The tested regular expression is ^(?!\[a-z])\[A-Z](\[(a-z)|( )|(,)]*)(\[.]|\[!]|\[?])$
  - One sentence, with the first letter uppercase commas and spaces
  - The sentence can contain lettes, commas and spaces.
  - The sentence should not contain numbers, special characters or accents
  - The setence should end with exactly one period or one exclamation point or one interrogation point.

# Examples of valid expressions:

"Be kind, for everyone you meet is fighting a harder battle."

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

"Aaaaaaaaaaaaa."

"Aaaaaaaaaaaaa!"

"Aaaaaaaaaaaaa?"

"Aaaaaaa aaaaa aaaaaaa."

"Asafsafsafassaffsaafssfaasf."

"Aaaaaa,aaaaaaa."


# Examples of invalid expressions:
"Invalid because cammelCase."

"AEIOU Invalid because multiple uppercases."

"INVALID BECAUSE UPPERCASE."

"Invalid because nummbers like 1 to 9."

"Invalid because multiple dots..."

"Invalid because multiple exclamations!!!"

"Invalid because #@#&*+- characters."

"Invalid because áóéíãõââ characters."


