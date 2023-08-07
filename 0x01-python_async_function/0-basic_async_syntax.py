#!/usr/bin/env python3
"""0-basic_async_syntax.py module"""
import asyncio
from random import uniform
import time


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous task

    Arg:
        max_delay(int/float): int/float value to check

    Returns:
        waits for max_delay time and some random floats
    """
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
