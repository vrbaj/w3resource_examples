"""
 Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return thrice of their sum.
"""


def my_triplet_sum(a, b, c):
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c


print(my_triplet_sum(1, 2, 3))
print(my_triplet_sum(3, 3, 3))
