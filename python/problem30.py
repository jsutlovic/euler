#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 30 from Project Euler

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

powlen = 5
fpl = []

def splitb10(x):
    """Split into a tuple of the ones, tens, hundreds, etc"""
    sl = ()
    while x != 0:
        sl += (x%10,)
        x/=10
    return tuple(reversed(sl))

def applypow(l):
    sl = ()
    for i in l:
        sl += (pow(i, powlen),)
    return sl

for i in xrange(2, int("9"*(powlen+1))):
    if i == sum(applypow(splitb10(i))):
        fpl.append(i)

print fpl
print sum(fpl)