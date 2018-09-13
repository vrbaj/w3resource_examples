"""
Write a Python program to count the number 4 in a given list.
"""


def count_4(list):
    count = 0
    for item in list:
        if item == 4:
            count += 1
    return count


print(count_4([0, 0, 0, 4, 0, 4, 0, 0, "hello", 4, 0]))
