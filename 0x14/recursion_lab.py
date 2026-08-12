#!/usr/bin/python

"""a comparison of iterative and recursive approaches to calculating factorial, fibonacci, and recursive sum of a list"""

def factorial_recursive(n):
    """a function that calculates the factorial of a number recursively"""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def fibonacci_recursive(n):
    """a function that calculates the nth fibonacci number recursively"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def sum_recursive(numbers):
    """a function that calculates the sum of a list of numbers recursively"""
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_recursive(numbers[1:])
    
def factorial_iterative(n):
    """a function that calculates the factorial of a number iteratively"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci_iterative(n):
    """a function that calculates the nth fibonacci number iteratively"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_iterative(numbers):
    """a function that calculates the sum of a list of numbers iteratively"""
    total = 0
    for n in numbers:
        total += n
    return total
def run_comparisons():
    """Run both versions of each problem and compare their results."""

    print("FACTORIAL COMPARISON")
    print("-" * 50)
    print(f"{'Input':<10}{'Recursive':<15}{'Iterative':<15}{'Match'}")

    factorial_inputs = [0, 1, 5]

    for n in factorial_inputs:
        recursive_result = factorial_recursive(n)
        iterative_result = factorial_iterative(n)

        assert recursive_result == iterative_result

        print(
            f"{n:<10}"
            f"{recursive_result:<15}"
            f"{iterative_result:<15}"
            f"{recursive_result == iterative_result}"
        )

    print("\nFIBONACCI COMPARISON")
    print("-" * 50)
    print(f"{'Input':<10}{'Recursive':<15}{'Iterative':<15}{'Match'}")

    fibonacci_inputs = [0, 1, 7]

    for n in fibonacci_inputs:
        recursive_result = fibonacci_recursive(n)
        iterative_result = fibonacci_iterative(n)

        assert recursive_result == iterative_result

        print(
            f"{n:<10}"
            f"{recursive_result:<15}"
            f"{iterative_result:<15}"
            f"{recursive_result == iterative_result}"
        )

    print("\nLIST SUM COMPARISON")
    print("-" * 50)
    print(f"{'Input':<20}{'Recursive':<15}{'Iterative':<15}{'Match'}")

    sum_inputs = [
        [],
        [5],
        [1, 2, 3, 4, 5]
    ]

    for numbers in sum_inputs:
        recursive_result = sum_recursive(numbers)
        iterative_result = sum_iterative(numbers)

        assert recursive_result == iterative_result

        print(
            f"{str(numbers):<20}"
            f"{recursive_result:<15}"
            f"{iterative_result:<15}"
            f"{recursive_result == iterative_result}"
        )


if __name__ == "__main__":
    run_comparisons()