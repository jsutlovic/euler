#!/usr/bin/env python2.5

"""
Problem 6 from Project Euler

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n = 100

def sumsquares(n):
    total = 0
    
    for i in range(1, n+1):
        total += i**2
    
    return total

def squaresum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    
    ss = total**2
    return ss


print squaresum(n) - sumsquares(n)