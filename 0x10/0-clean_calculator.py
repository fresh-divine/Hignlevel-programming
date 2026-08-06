#!/usr/bin/python
'a modified and clean version of a calculator'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is undefined."
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error: Floor division by zero is undefined."
    return a // b

def average(a, b):
    return (a + b) / 2

def get_number(prompt):
    """Validates and returns a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def main():
    while True:
        # Display Menu
        print("\n" + "="*30)
        print("    MENU-DRIVEN CALCULATOR")
        print("="*30)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (a^b)")
        print("6. Modulo (%)")
        print("7. Floor Division (//)")
        print("8. Average of 2 Numbers")
        print("9. Quit")
        print("="*30)
        
        choice = input("Select an option (1-9): ").strip()
        
        # Clean Exit Condition
        if choice == '9':
            print("\nThank you for using the calculator. Goodbye!")
            break
            
        # Validate Menu Selection
        if choice not in [str(i) for i in range(1, 9)]:
            print("Invalid selection. Please choose a number between 1 and 9.")
            continue
            
        # Get Validated Numerical Inputs
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        # Perform Selected Operation
        if choice == '1':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
        elif choice == '5':
            result = power(num1, num2)
            print(f"\nResult: {num1} ^ {num2} = {result}")
        elif choice == '6':
            result = modulo(num1, num2)
            print(f"\nResult: {num1} % {num2} = {result}")
        elif choice == '7':
            result = floor_divide(num1, num2)
            print(f"\nResult: {num1} // {num2} = {result}")
        elif choice == '8':
            result = average(num1, num2)
            print(f"\nResult: Average of {num1} and {num2} = {result}")

if __name__ == "__main__":
    main()