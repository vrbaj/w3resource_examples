"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
"""


def get_future_value(amount, rate_of_interest, years):
    future_value = amount * (1 + rate_of_interest / 100) ** years
    return round(future_value, 2)


print(get_future_value(10000, 3.5, 7))
