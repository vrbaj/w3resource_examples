"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def test_number(number):
    return abs(1000 - number) <= 100 or abs(2000 - number) <= 100


print(test_number(800))
