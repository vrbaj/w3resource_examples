"""
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
"""


def change_string(string):
    if len(string) >= 2 and string[:2] == "Is":
        return string
    else:
        return "Is" + string


print(change_string("String"))
print(change_string("IsString"))
