#!/usr/bin/env python2.5

"""
Problem 18 from Project Euler

Find the maximum total from top to bottom of the triangle below:
"""

ts = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


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


    
