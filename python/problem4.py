#!/usr/bin/env python2.5

"""
Problem 4 from Project Euler

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

digits = 3
n = int("9"*digits)
palin = 0

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        s = str(i*j)
        if s == "".join(reversed(s)):
            if i*j > palin:
                palin = i*j
                
print palin
