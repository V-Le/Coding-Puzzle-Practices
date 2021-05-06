# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# my solution
def pig_it(text):
    split_text = text.split()

    for i in range(len(split_text)):
        if split_text[i].isalpha():
            temp_char = split_text[i][0] + "ay"
            split_text[i] = split_text[i][1:] + temp_char
    return " ".join(split_text)

""""
def pig_it(text): #other's solution
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""

print(pig_it('Pig latin is cool!'))  # igPay atinlay siay oolcay
