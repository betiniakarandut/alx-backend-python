#!/usr/bin/env python3
"""0-basic_async_syntax.py module"""
from random import uniform


async def wait_random(max_delay: float | int = 10) -> float:
    """Asynchronous task

    Arg:
        max_delay(int/float): int/float value to check

    Returns:
        waits for max_delay time and some random floats
    """
    wait_time = uniform(0, max_delay + 1)
    return wait_time
