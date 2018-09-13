"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""


def list2string(input_list):
    return "".join(map(str, input_list))  # map applies function on the each element of the given list


print(list2string([1, 5, 2, 12]))
