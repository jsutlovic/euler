#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 31 from Project Euler

How many different ways can £2 be made using any number of coins?
"""

from math import floor

v = [200, 100, 50, 20, 10, 5, 2, 1]
total = 200

def splitlower(x):
    if x == 1: return False
    else:
        i = v.index(x)
        j = v[i+1]
        l = []
        if x % j == 0: l = [j]*(x/j)
        else:
            l = [j]*2+[v[i+2]]
        return l

def reduceval(x):
    if x == 1: return 0
    steps = 1

    for i in splitlower(x):
        steps += reduceval(i)

    return steps


print reduceval(total)+1