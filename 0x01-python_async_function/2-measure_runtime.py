#!/usr/bin/env python3
"""2-measure_runtime.py module"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Time measurement

    Args:
        n(int) - number of runs
        max_delay(int) - amount of delay

    Returns:
        float
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total = stop - start
    return total / n
