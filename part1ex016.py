"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""
number = float(input("Input number: "))
if number > 17:
    print(2 * (number - 17))
else:
    print(17 - number)
