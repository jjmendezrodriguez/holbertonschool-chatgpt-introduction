#!/usr/bin/python3

import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursive approach.
    The factorial of a number is the product of all positive integers less than or equal to that number.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the integer 'n'.
    """
    if n == 0:  # Base case: factorial of zero is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Main execution: Read an integer from command line argument, calculate its factorial, and print it.
f = factorial(int(sys.argv[1]))
print(f)
