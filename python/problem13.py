#!/usr/bin/env python2.5

"""
Problem 13 from Project Euler

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

numbers = open("../problem13.txt").read()
numlist = numbers.split("\n")

total = 0
for i in numlist:
    total += int(i)

print(str(total)[:10])
