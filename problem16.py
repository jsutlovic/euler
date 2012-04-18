#!/usr/bin/env python3

"""
Problem 16 from Project Euler

What is the sum of the digits of the number 21000?
"""

#a = 2**1000
#s = str(a)

#total = 0

#for digit in s:
    #digit = int(digit)
    #total += digit
    
#print(total)

#Condensed version
print( sum( [int(x) for x in str(2**1000)] ))
