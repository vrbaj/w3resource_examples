"""
Write a Python program to check whether a specified value is contained in a group of values.
"""


def check_value(group, value):
    return value in group


print(check_value([1, 3, 4, 5, 1], 6))
