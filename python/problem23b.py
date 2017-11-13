#!/usr/bin/env python

from math import sqrt

def findFactors(n):
    """
    Return a list of factors for number n
    """

    f = []

    for i in xrange(1, int(round(sqrt(n)))+1):
        if n%i == 0:
            f.append(i)
            f.append(n/i)

    return f

def fillAbList(m):
    ablist = []
    for i in range(1, m + 1):
        if isAbundant(i): ablist.append(i)
    return ablist

def isAbundant(x):
    t = 0
    l = set(findFactors(x))
    l.remove(x)
    if listSum(l) > x: return True
    return False


def listSum(l):
    t = 0
    for e in l:
        t += e
    return t

def main():
    m = 28123
    abList = fillAbList(m)
    t = 0
    nums = range(1, m + 1)
    for i in nums:
        t += i
    for i in xrange(0, len(abList)):
        for j in xrange(i, len(abList)):
            index = abList[i] + abList[j] - 1

            if (index < len(nums)):
                t -= nums[index]
                nums[index] = 0
            else:
                break

    print t

main()
