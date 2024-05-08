#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) > 1:
    try:
        input_num = int(sys.argv[1])
        f = factorial(input_num)
        print(f)
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: script_name <number>")
