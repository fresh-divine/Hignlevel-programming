#/usr/bin/python
'a clean calculator'
"""a module that has all the functions that performs arithemetic operations"""
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def mode(a,b):
    return a%b

def floor_division(a,b):
    return a//b

def exponential(a,b):
    return a**b

if __name__=="__main__":
    print("===========================================")
    print("           welcome to calculator           ")
    print("===========================================")
    
    opt=int(input("enter :1-add, 2-sub, 3-multiply, 4-divide, 5-mode, 6-floor division, 7-exponential, :"))
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
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
    else:
        print("invalid input")