#!/usr/bin/python
"""a module that impement the function that can caluculate the are of a triangle, rectangle and circle"""

def triangle(b, h):
    return 0.5*b*h


if __name__=="__main__":
     b=int(input("Enter the base of the triangle:"))
     h=int(input("Enter the height of the triangle:"))
     result=triangle(b, h)
     print(result)
 