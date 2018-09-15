"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""


def get_gcd(number_1, number_2):

    if number_1 % number_2 == 0:
        return number_2
    elif number_2 % number_1 == 0:
        return number_1

    if number_1 > number_2:
        max_divisor = number_1
    else:
        max_divisor = number_2

    for divisor in range(max_divisor // 2, 1, -1):
        if number_1 % divisor == 0 and number_2 % divisor == 0:
            return divisor


print(get_gcd(336, 360))
