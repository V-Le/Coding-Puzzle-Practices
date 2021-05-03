"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    alpha_dict = {}
    string_num = [x for x in text.lower() if x in alphabet]

    for x in range(len(alphabet)):
        alpha_dict[alphabet[x]] = i
        i += 1

    return ' '.join([str(alpha_dict[string_num[z]]) for z in range(len(string_num)) if string_num[z] in alpha_dict])
