#!/usr/bin/env python

"""
Problem 7 from Project Euler

What is the 10001st prime number?
"""

n = 10001
#n = 6

def primelist(n):
    """
    Return a list of primes n primes long
    """

    primes = [2]

    i = 3
    while len(primes) < n:
        for p in primes:
            if i % p == 0: break
            elif p == primes[-1]: primes.append(i)
        i += 2

    return primes



print(primelist(n)[-1])

