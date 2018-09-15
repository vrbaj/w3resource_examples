"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""


def int_checker(integer_1, integer_2):
    if integer_1 == integer_2 or integer_1 + integer_2 == 5 or abs(integer_1 - integer_2) == 5:
        return True
    else:
        return False


print(int_checker(7, 2))
print(int_checker(3, 2))
print(int_checker(20, 2))
