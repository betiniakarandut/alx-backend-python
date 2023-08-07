#!/usr/bin/env python3
"""0-basic_async_syntax.py module"""
import random


async def wait_random(max_delay: float | int = 10) -> float:
    """Asynchronous task

    Arg:
        max_delay(int/float): int/float value to check

    Returns:
        waits for max_delay time and some random floats
    """
    return random.uniform(0, max_delay + 1)
