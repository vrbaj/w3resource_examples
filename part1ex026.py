"""
Write a Python program to create a histogram from a given list of integers.
"""


def my_histogram(histogram, char_to_print):
    for bin in histogram:
        print(bin * char_to_print)


my_histogram([2, 3, 6, 5], "*")
