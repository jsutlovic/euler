#!/usr/bin/env python2.5

"""
Problem 5 from Project Euler

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
"""


#List of numbers
#If another number is a factor of it that number, remove it from the list
#Multiply the numbers that are left

from math import sqrt

n = 20
ldl = range(1, n+1)


def factor(n):
    f = []
    i = 1

    while True:
        if i > sqrt(n): break
        if n % i == 0: f.append(i)
        i += 1

    return f

def test(n, total):
    divall = False
    divs = range(1, n+1)
    for i in divs:
        if not total % i == 0:
            divall = False
            break
        else:
            divall = True

    return divall


#for lf in ldl:
    #for slf in factor(lf)[:-1]:
        #for lf2 in ldl[:ldl.index(lf)]:
            #for slf2 in factor(lf2)[1:]:
                #if slf == slf2:
                    #print "Yep", lf, slf, lf2, slf2
                    #ldl.pop(ldl.index(lf2))

#print ldl

#total = 1
#for i in ldl:
    #total *= i

#print total


total = 1
for t in ldl:
    total *= t
print(total)

for i in range(n, 0, -1):
    if test(n, (total/i)):
        total = total/i

print(total)
