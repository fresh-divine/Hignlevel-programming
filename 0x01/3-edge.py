#!/usr/bin/python
"""a module that handles if and logical operations"""

age =int(input("Enter your age:"))
if age <= 10 and age <= 17:
    print("you are a teenager")
elif age >= 18 and age <= 40:
    print("you are an adult")
else:
    print("you are old")