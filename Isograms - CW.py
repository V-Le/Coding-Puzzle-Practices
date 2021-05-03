"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

def is_isogram(string):
    #your code here
    count = 0
    word = []
    for i in range(len(string)):
        if string[i].lower() in word:
            return False
            break
        else:
            word.append(string[i].lower())
    print(word)
    return True
print(is_isogram("isIsogram"))
