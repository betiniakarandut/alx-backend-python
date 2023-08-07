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
    wait_time = uniform(0, max_delay)
    return wait_time


# print("start time was {}".format(time.strftime('%X')))
# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))  
# print("End time was {}".format(time.strftime('%X')))