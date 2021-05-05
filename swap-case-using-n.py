# https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python

def swap(s,n):
    binary_of_num = bin(n).replace("0b", "")*500
    new_str = [x for x in s]
    z = 0

    for i in range(0, len(new_str)):
        if new_str[i].isalpha():
            if binary_of_num[z] == "1":
                new_str[i] = new_str[i].swapcase()
            z += 1
    return "".join(new_str)
