"""
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""


def odd_or_even(number):
    if float(number) % 2 == 1:
        return "odd"
    elif float(number) % 2 == 0:
        return "even"
    else:
        return "not an integer"


print(odd_or_even(input("Input a number: ")))
