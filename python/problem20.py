#!/usr/bin/env python2.5

"""
Problem 20 from Project Euler

Find the sum of the digits in the number 100!
"""


n = 100

def factorial(n):
    total = n
    for i in range(n-1, 0, -1):
        total *= i
    return total
    
digits = str(factorial(n))

total = 0
for digit in digits:
    total += int(digit)
    
print total
