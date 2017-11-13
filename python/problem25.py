#!/usr/bin/env python2.5

"""
Problem 25 from Project Euler

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fib(n):
    """
    Fibonacci sequence n
    """
    if n >= 2:
        f = [1, 1]
        for i in range(1, n-1):
            fa = f[0] + f[1]
            f.append(fa)
            f.pop(0)

        return f

def fibnum(n):
    """
    Fibonnaci number for sequence n
    """
    return fib(n)[-1]


i = 2
while True:
    f = fibnum(i)
    if len(str(f)) >= 1000: break
    i += 1
    #print f

print i

