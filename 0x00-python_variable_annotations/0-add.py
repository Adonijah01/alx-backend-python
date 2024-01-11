#!/usr/bin/env python3
"""
Module with type-annotated function add.
"""

def add(a: float, b: float) -> float:
    """
    Function that takes two float arguments and returns their sum.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of the two input numbers.
    """
    return a + b

if __name__ == "__main__":
    add(1.11, 2.22)

