#!/usr/bin/env python

"""
Problem 26 from Project Euler

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from mpmath import *
import re

mp.dps = 1000 #precision to 3000 decimal points... just to make sure

m = 1000

r = re.compile(r"(\d+?)(?=\1)") #Find the shortest possible repeating sequence

t = (0,0) #length of sequence, d for 1/d that generates the sequence


for i in range(3, m+1, 2):
    ts = str(mpf(10**2000)/mpf(i))
    res = r.search(ts)
    if res:
        if len(res.group(1)) > t[0]:
            t = len(res.group(1)), i

print t[1]

