#!/usr/bin/env python2.5

"""
Problem 23 from Project Euler

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt

alim = 28123

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


def isabundant(n):
    f = set(sorted(factor(n))[:-1])
    #f = set(factor(n))
    #f.remove(n)

    t = 0
    for i in f:
        t += i

    if t > n: return True

    return False

def ablist():
    l = []
    i = 1
    while i <= 28123:
        if isabundant(i):
            l.append(i)
            if l[0]+i > 28123:
                l.pop()
                break
        i += 1

    return l


ab = ablist()
ns = range(1, alim+1)

for i in ab:
    for j in ab[ab.index(i):]:
        index = i+j-1
        #print index
        if index < len(ns):
            ns[index] = 0
        else:
            break

t = 0
for k in ns:
    t += k

print t

