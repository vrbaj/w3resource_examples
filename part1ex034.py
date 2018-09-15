"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""


def my_sum(integer_1, integer_2):
    int_sum = integer_1 + integer_2
    if int_sum >= 15 and int_sum <= 20:
        return 20
    else:
        return int_sum


print(my_sum(10, 6))
print(my_sum(10, 2))
print(my_sum(10, 12))
