#!/usr/bin/python
"a calculator that does simple calculations"
print("welcome to my calculator")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
if __name__=="__main__": 
 opt=int(input("enter :1-add, 2-sub, 3-multiply :"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if opt==1:
        """add the two numbers together"""
        print(add(num1,num2))
elif opt==2:
     """subtract the two numbers"""
     print(subtract(num1,num2))
elif opt==3:
        """multiplys the two numbers"""
        print(multiply(num1,num2))
else:
     print("thank you for using my calculator")

print("thanks for using my calculator")
