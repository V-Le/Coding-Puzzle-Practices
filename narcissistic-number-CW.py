# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# my original solution
"""
def narcissistic(value):
    num_lst = [int(i) for i in str(value)]
    for i in range(len(num_lst)):
        num_lst[i] = num_lst[i] ** len(str(value))

    total_sum = sum(num_lst)

    if value != total_sum:
        return False
    else:
        return True
"""

# refactored
def narcissistic(value):
    return value == sum([int(i) ** len(str(value)) for i in str(value)])
