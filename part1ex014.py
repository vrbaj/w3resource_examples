"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

import datetime

date1 = datetime.date(2014, 7, 22)
date2 = datetime.date(2014, 7, 11)
date_diff = date1 - date2
print("%i days" % abs(date_diff.days))
