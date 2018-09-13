"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2.
"""


def substring_copier(string, n):
    if len(string) < 2:
        return n * string
    else:
        return n * string[:2]


print(substring_copier("h", 4))
print(substring_copier("abcd", 3))
