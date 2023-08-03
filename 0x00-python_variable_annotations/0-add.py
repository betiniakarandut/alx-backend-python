#!/usr/bin/env python3
"""
Module for add function
"""

def add(a: float, b: float) -> float:
    """Returns sum of a and b"""
    return a + b


if __name__ == "main":
    add()

# Test
# print(add(1.11, 2.22) == 1.11 + 2.22)
# print(add.__annotations__)