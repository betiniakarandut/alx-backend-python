#!/usr/bin/env python3
"""0-async_generator.py module"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """Coroutine that loops 10 times
    and yield list of random values
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))


# async def print_t():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)
# asyncio.run(print_t())