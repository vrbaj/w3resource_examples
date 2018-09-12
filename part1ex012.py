"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
year = int(input("Calendar for a year : "))
month = int(input("Month : "))
print(calendar.month(year, month))
