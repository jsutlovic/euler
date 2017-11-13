#!/usr/bin/env python2.5

"""
Problem 12 from Project Euler

What is the value of the first triangle number to have over five hundred divisors?
"""

from math import sqrt

ndiv = 500


#def factor(n):
    #"""
    #Return a list of factors for number n
    #"""

    #f = []

    #for i in range(1, int(round(sqrt(n)))+1):
        #if n%i == 0:
            #f.append(i)
            #f.append(n/i)

    #return f

def factor(n):
    """
    Return the number of factors for n
    """

    f = 0
    lim = int(sqrt(n))

    for i in range(1, lim):
        if n%i == 0:
            f += 2

    return f


##for i in range(1, 8):
##    print "% 3d: %s" % ( triangle(i), len(factor(triangle(i))) )

t = 1
i = 2
while True:
    #print "% 3d: %d, %s" % (t, i-1, factor(t))

    if factor(t) > ndiv: break

    t += i
    i += 1


print(t)
