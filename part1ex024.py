"""
Write a Python program to test whether a passed letter is a vowel or not.
"""


def check_vowel(letter):
    vowels = 'aeioui'
    return letter in vowels


print(check_vowel("a"))
