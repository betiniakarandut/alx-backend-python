#!/usr/bin/env python3
"""1-concurrent_coroutines.py module"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine Function

    Args:
        n(int) - number of times wait_random() will spawn
        max_delay - amount of delay

    Returns:
        Sorted list of all the delays
    """
    wait_time = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*wait_time))
