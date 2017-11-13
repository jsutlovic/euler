#!/usr/bin/env python2.5

"""
Problem 15 from Project Euler

How many routes are there through a 20x20 grid?
"""

#Binary digits of the length of the path,
#if the digit has the same number of 1s as
#0s (down, right), then it's a correct path

#Don't actually bother running this

sidelen = 20
pathlen = sidelen*2

##Note, this is REALLY innefficient as the side length gets bigger.

def checkeven(n):
    t = 0
    while n > 0:
        t += (n % 2)
        n = n >> 1

    if t == sidelen: return True


t = 0
i = 2**sidelen-1
while i <= 2**pathlen:
    try:
        if checkeven(i):
            #print int2bin(i)
            t += 1
        i += 1
    except KeyboardInterrupt:
        print i
        break

print t
