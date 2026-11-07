"""math_utils — a small module written by us, for the Modules and Packages notebook.

A module is just a normal .py file. Put useful functions in it, and every
other file in the same folder can import them.
"""

PI_APPROXIMATION = 3.14159


def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return PI_APPROXIMATION * radius ** 2


def average(numbers):
    """Return the average of a list of numbers (0.0 for an empty list)."""
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)


def is_even(number):
    """Return True if number is divisible by 2."""
    return number % 2 == 0


def clamp(value, low, high):
    """Return value limited to the range [low, high]."""
    if value < low:
        return low
    if value > high:
        return high
    return value
