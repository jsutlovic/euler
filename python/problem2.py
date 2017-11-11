#!/usr/bin/env python2.5

"""
Problem 2 from Project Euler

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
"""

def fib(n):
    """
    Fibonacci sequence n
    """
    if n >= 3:
        f = [1, 2]
        for i in range(1, n-1):
            fa = f[i] + f[i-1]
            f.append(fa)
            
        return f
        
def fibnum(n):
    """
    Fibonnaci number for sequence n
    """
    return fib(n)[-1]

fmax = 4000000
fibt = 0
fibmax = 0

for i in range(10, 50):
    if fibnum(i) <= fmax:
        fibmax = i
    else:
        break
    
for j in fib(fibmax):
    if j % 2 == 0:
        fibt += j
        
print fibt