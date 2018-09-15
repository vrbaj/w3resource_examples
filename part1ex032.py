"""
 Write a Python program to get the least common multiple (LCM) of two positive integers.
"""


def get_lcm(integer_1, integer_2):
    min_number = min(integer_1, integer_2)
    max_number = max(integer_1, integer_2)
    max_divisor = max_number
    while True:
        if max_divisor % min_number == 0:
            break

        else:
            max_divisor += max_number

    return max_divisor


print(get_lcm(15, 17))
