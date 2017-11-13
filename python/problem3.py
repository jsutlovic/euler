#!/usr/bin/env python2.5

"""
Problem 3 from Project Euler

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt

n = 600851475143

pfact = []

def factors(n):
    f = []
    i = 1

    while True:
        if i > int(round(sqrt(n))): break
        if n % i == 0: f.append(i)
        i += 1

    return f

#print "Possible Prime Factors:", factors(n)

def hasfactors(n):
    if len(factors(n)) == 2:
        return True
    else:
        return False

f = factors(n)
for i in reversed(f):
    if not hasfactors(i):
        print i
        break
##        pfact.append(i)
##
##print pfact[-1]
