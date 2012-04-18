#!/usr/bin/env python2.5

"""
Problem 21 from Project Euler

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

n = 10000

def factor(n):
    """
    Return a list of factors for number n
    """
    
    f = []

    for i in xrange(1, int(round(sqrt(n)))+1):
        if n%i == 0:
            f.append(i)
            f.append(n/i)

    return f


def d(n):
    f = set(sorted(factor(n))[:-1])
    t = 0
    for i in f:
        t += i
    return t


def isam(n):
    i = d(n)
    j = d(i)
    if i != j and n == j:
        return True

    return False


am = []

for i in range(1, n+1):
    if isam(i):
        am.append(i)

t = 0
for j in am:
    t += j

print t


