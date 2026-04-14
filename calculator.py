"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    result = math.sqrt(a)
    return result


def hypotenuse(a, b):
    result = math.hypot(a, b)
    return result


def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = b / a
    return result


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    result = math.log(b, a)
    return result


def exponent(a, b):
    result = a ** b
    return result
