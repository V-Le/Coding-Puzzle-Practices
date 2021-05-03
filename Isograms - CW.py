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
