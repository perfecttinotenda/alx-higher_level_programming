#!/usr/bin/python3
def print_last_digit(number):
    """Print the last dig of a num & return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
