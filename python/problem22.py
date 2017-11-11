#!/usr/bin/env python2.5

"""
Problem 22 from Project Euler

What is the total of all the name scores in the file?
"""


#ord("A")-64 = 1
#ord("B")-64 = 2

def getscore(name, index):
    name = name.strip("\"")
    lt = 0
    for letter in name:
        lt += ord(letter) - 64
    
    total = lt*(index+1)
    return total


fn = "../names.txt"
data = open(fn).read()

names = data.split(",")
names.sort()
        
total = 0

i = 0
while True:
    if i >= len(names): break
    total += getscore(names[i], i)
    i += 1
    
print total
