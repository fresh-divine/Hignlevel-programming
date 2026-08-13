#!/usr/bin/python
""" a module that applies debugging stratagies"""

def index_error_bug():
    numbers = [10, 20, 30]
    return numbers[2]


def key_error_bug():
    students = {"Ada": 90, "Grace": 95}
    return students["Grace"]


def type_error_bug():
    age = 20
    return age + 5


def attribute_error_bug():
    name = "Python"
    return name.upper()


def name_error_bug():
    message = "Debugging complete"
    return message


def off_by_one_bug(items):
    total = 0
    for i in range(len(items)):
        total += items[i]
    return total


def wrong_operator_bug(a, b):
    return a + b


def reversed_condition_bug(age):
    if age >= 18:
        return "adult"
    return "minor"


def missing_return_bug(a, b):
    result = a * b
    return result


assert index_error_bug() == 30
assert key_error_bug() == 95
assert type_error_bug() == 25
assert attribute_error_bug() == "PYTHON"
assert name_error_bug() == "Debugging complete"
assert off_by_one_bug([2, 4, 6]) == 12
assert wrong_operator_bug(7, 3) == 10
assert reversed_condition_bug(20) == "adult"
assert missing_return_bug(6, 7) == 42


if __name__ == "__main__":
    print("All nine fixed functions passed their assertions.")