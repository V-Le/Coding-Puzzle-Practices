"""
You are given a list of character sequences as a comma separated string. Write a function which returns another string containing all the character sequences except the first and the last ones, separated by spaces. If the input string is empty, or the removal of the first and last items would cause the string to be empty, return a null value.
"""

def array(string):
    string = string.replace(" ", "").split(",")
    if len(string) <= 2:
        return None
    else:
        string.pop(0)
        string.pop(-1)
        if len(string) == 0:
            return None
        else:
            string = " ".join(map(str, string))
            return string
