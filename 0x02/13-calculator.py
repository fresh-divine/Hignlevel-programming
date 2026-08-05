#!/usr/bin/python
import sys

def get_number(prompt: str) -> float:
    """Prompts the user for a number and validates that the input is a valid float."""
    while True:
        try:
            user_input = input(prompt).strip()
            # Check for empty input
            if not user_input:
                print("⚠️ Input cannot be empty. Please enter a valid number.")
                continue
            return float(user_input)
        except ValueError:
            print("❌ Invalid entry. Letters, symbols, and multiple decimals are not allowed.")

def get_operator() -> str:
    """Validates and returns a chosen mathematical operator or action."""
    valid_operators = ['+', '-', '*', '/', '%', '^', 'exit']
    while True:
        print("\nAvailable Operations:")
        print("  [ + ] Addition       [ - ] Subtraction")
        print("  [ * ] Multiplication [ / ] Division")
        print("  [ % ] Modulo         [ ^ ] Exponentiation")
        print("  Type 'exit' to turn off the calculator")
        
        op = input("Select an operator: ").strip().lower()
        
        if op in valid_operators:
            return op
        else:
            print(f"❌ '{op}' is not a valid selection. Please choose from the list.")

def calculate(num1: float, op: str, num2: float) -> float | str:
    """Executes the mathematical operations safely using conditional branching."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        # Conditional zero division protection
        if num2 == 0:
            return "Error: Mathematical undefined state (Division by Zero)."
        return num1 / num2
    elif op == '%':
        if num2 == 0:
            return "Error: Mathematical undefined state (Modulo by Zero)."
        return num1 % num2
    elif op == '^':
        # Handling complex/imaginary number limits for basic real-number output
        if num1 < 0 and 0 < num2 < 1:
            return "Error: Operation would result in a complex number (fractional power of a negative number)."
        try:
            return num1 ** num2
        except OverflowError:
            return "Error: Result is too large to calculate (Overflow)."
    else:
        return "Error: Unknown operation logic."

def start_calculator():
    """Main control loop running the calculator sequence."""
    print("=============================================")
    print("       Welcome to the Smart Calculator       ")
    print("=============================================")
    
    while True:
        # Step 1: Secure operational intent
        operator = get_operator()
        if operator == 'exit':
            print("\nShutting down. Thank you for using Smart Calculator!")
            sys.exit()
            
        # Step 2: Validate numerical input variables
        print("\n--- Enter Values ---")
        first_num = get_number("Enter the first number: ")
        second_num = get_number("Enter the second number: ")
        
        # Step 3: Compute and isolate calculation anomalies
        print("\n--- Processing ---")
        result = calculate(first_num, operator, second_num)
        
        # Step 4: Display contextual results
        if isinstance(result, str):
            print(f"❌ Calculation Failed: {result}")
        else:
            # Strip trailing zeros for cleaner display if it's a whole number
            formatted_result = f"{result:.6f}".rstrip('0').rstrip('.') if '.' in f"{result}" else f"{result}"
            print(f"✅ Success: {first_num} {operator} {second_num} = {formatted_result}")
            
        print("\n" + "="*45)

if __name__ == "__main__":
    start_calculator