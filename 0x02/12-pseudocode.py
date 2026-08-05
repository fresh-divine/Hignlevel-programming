#!/usr/bin/python

print("Welcome to the calculator")

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

choice = input("Choose operation (add/subtract): ")

if choice == "add":
    result = number_1 + number_2
elif choice == "subtract":
    result = number_1 - number_2
else:
    print("Invalid choice")
    result = None

if result is not None:
    print(result)