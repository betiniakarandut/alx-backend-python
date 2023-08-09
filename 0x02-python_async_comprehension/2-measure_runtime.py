#!/usr/bin/env python3
"""2-measure_runtime.py module"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure execution time"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
