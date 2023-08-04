!/usr/bin/env python3
"""8-make_multiplier.py module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns the child function"""
    def multiplier_a(a: float) -> float:
        """Returns the result of the multiplier"""
        return a * multiplier
    return multiplier_a
