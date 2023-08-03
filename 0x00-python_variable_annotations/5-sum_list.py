#!/usr/bin/env python3
"""5-sum_list.py module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns their sum as float"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
