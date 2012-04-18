#!/usr/bin/env python3

"""
Problem 14 from Project Euler

n => n/2 (n is even)
n => 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
"""

m = 1000000

def getchainlen(n):
    i = n
    c = 1
    while i != 1:
        #print n
        #Even
        if i%2==0:
            i = i/2
        #Odd
        else:
            i = 3*i + 1

        c += 1

    return c

chainlist = []

for i in range(1, m):
    chainlist.append(getchainlen(i))

num = sorted(chainlist)[-1]
print(chainlist.index(num)+1)
#print(num)

