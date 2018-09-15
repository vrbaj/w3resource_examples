"""
Write a Python program to add two objects if both objects are an integer type.
"""


def my_add_int(number_1, number_2):
    if isinstance(number_1, int) and isinstance(number_2, int):
        return number_1 + number_2
    else:
        return None


print(my_add_int(10, 20))
