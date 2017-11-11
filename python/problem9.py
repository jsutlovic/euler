#!/usr/bin/env python2.5

"""
Problem 9 from Project Euler

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

l = []
n = 1000

#Find all the Pythagorean triplets 
for i in range(1, n+1):
    for j in range(1, n+1):
        k = sqrt(i**2 + j**2)
        if k % 1 == 0:
            l.append([i, j, int(k)])
            
#Go through the list of triplets, and find the one that adds to 1000
for i, j, k in l:
    if i + j + k == n:
        s = i*j*k
        
print s