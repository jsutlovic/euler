#!/usr/bin/env python2.5

"""
Problem 19 from Project Euler

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

t = 0

for y in range(1901, 2000+1):
    for m in range(1, 12+1):
        if datetime.date(y, m, 1).weekday() == 6:
            t += 1

print t
        
