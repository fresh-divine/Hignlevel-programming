#!/usr/bin/python
'a modified and clean version of a calculator'
def add(choice_a,choice_b):
    return choice_a+choice_b

def sub(choice_a,choice_b):
    return choice_a-choice_b

def multiply(choice_a,choice_b):
    return choice_a*choice_b

def divide(choice_a,choice_b):
    return choice_a/choice_b

def mode(choice_a,choice_b):
    return choice_a%choice_b

def floor_division(choice_a,choice_b):
    return choice_a//choice_b

def exponential(choice_a,choice_b):
    return choice_a**choice_b

if __name__=="__main__":
    opt=int(input("enter :1-add, 2-sub, 3-multiply, 4-divide, 5-mode, 6-floor division, 7-exponential, :"))
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
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