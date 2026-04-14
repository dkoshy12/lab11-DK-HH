#https://github.com/dkoshy12/lab11-DK-HH
#Partner 1: Daniel Koshy
#Partner 2: Haseeb Haq
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


def mul(a, b):
    result = a * b
    return result


def div(a, b):
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


def exp(a, b):
    result = a ** b
    return result
