"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""


def my_triplet_sum(integer_1, integer_2, integer_3):
    if integer_1 == integer_2 or integer_1 == integer_3 or integer_2 == integer_3:
        return 0
    else:
        return integer_1 + integer_2 + integer_3


print(my_triplet_sum(2, 1, 2))
print(my_triplet_sum(3, 2, 2))
print(my_triplet_sum(2, 2, 2))
print(my_triplet_sum(1, 2, 3))
