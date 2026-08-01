#!/usr/bin/python
"""a module that calculate quadratic equation"""

def quadratic(a,b,c):
    d =(b**2)-(4*a*c)
    x1= -(b+(d**0.5))/(2*a)
    x2= -(b-(d**0.5))/(2*a)
    return x1,x2



if __name__== "__main__":
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    c=int(input("Enter the value of c: "))
    result1,result2=quadratic(a,b,c)
    print(result1)
    print(result2)
