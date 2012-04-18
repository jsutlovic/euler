#!/usr/bin/env python2.5

"""
Problem 15 from Project Euler

How many routes are there through a 20x20 grid?
"""

#This one actually works
#Pascal's triangle with 2n+1 rows, middle value has the # of routes

sidelen = 20

def ptri(n):
    """
    Make a Pascal's triangle 2n+1 lines high
    """
    if n == 0: return [[1]]

    t = []

    #The first 2 rows
    t.append([1])
    t.append([1, 1])

    for i in range(n*2-1):
        l = [1]
        for j in range(len(t[-1])-1):
            l.append(t[-1][j]+t[-1][j+1])
        l.append(1)
        t.append(l)

    return t


def getmax(pt):
    """
    Get the max value in a Pascal's Triangle
    (Bottom row, middle)
    """

    #print pt

    return pt[-1][int(len(pt[-1])/2)]

print(getmax(ptri(sidelen)))
