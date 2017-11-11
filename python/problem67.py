#!/usr/bin/env python2.5

"""
Problem 67 from Project Euler

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.
"""

ts = open("../triangle.txt").read()

t = []
for l in ts.splitlines():
    t.append([int(x) for x in l.split()])

#print t


def tred(t):
    """
    Take a triangle, reduce (find the largest sums) the bottom two rows,
    and return the triangle
    """

    t2 = t

    l = []
    l2 = t2.pop()
    l1 = t2.pop()

    for i in range(len(l1)):
        l.append(l1[i] + max(l2[i:i+2]))

    t2.append(l)
    return t2


while len(t) > 1:
    t = tred(t)

print t[0][0]
