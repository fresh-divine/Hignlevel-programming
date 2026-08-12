#!/usr/bin/python
"""a module that act as a menu-driven calculator"""

def add(a,b):
    """a function that adds two numbers"""
    return a+b

def sub(a,b):
    """a function that subtracts two numbers"""
    return a-b

def multiply(a,b):
    """a function that multiplies two numbers"""
    return a*b

def divide(a,b):
    """a function that divides two numbers"""
    return a/b

def mode(a,b):
    """a function that returns the modulus of two numbers"""
    return a%b

def floor_division(a,b):
    """a function that returns the floor division of two numbers"""
    return a//b

def exponential(a,b):
    """a function that returns the exponential of two numbers"""
    return a**b
if __name__=="__main__": 
 opt=int(input("enter :1-add, 2-sub, 3-multiply, 4-divide, 5-mode, 6-floor division, 7-exponential, 8-Quit. :"))
 num1=int(input("Enter the first number:"))
 num2=int(input("Enter the second number:"))
while True:
    if opt==1:
        print(add(num1,num2))
    elif opt==2:
     print(sub(num1,num2))
    elif opt==3:
        print(multiply(num1,num2))
    elif opt==4:
        print(divide(num1,num2))
    elif opt==5:
        print(mode(num1,num2))
    elif opt==6:
        print(floor_division(num1,num2))
    elif opt==7:
        print(exponential(num1,num2))
    elif opt==8:
        print("Exiting.....")
        break
    else:
        print("Invalid option")

