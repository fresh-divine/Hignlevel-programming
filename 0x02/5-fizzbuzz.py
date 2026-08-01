#!/usr/bin/python
"""a module that print fizz, buzz, and fizzbuzz"""

for i in range(1, 101):
    if i %3 ==0 and i %5 ==0:
        print("fizzbuzz", end=", ")
    elif i %3==0:
        print("Fizz", end=", ")
    elif i %5==0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
