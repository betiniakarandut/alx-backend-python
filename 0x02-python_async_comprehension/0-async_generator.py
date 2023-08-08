#!/usr/bin/env python3
"""0-async_generator.py module"""
import asyncio
import random


async def async_generator():
    """Coroutine function that loops 10 times.

    Args:
        Takes no arguments
    
    Returns:
        and yield list of random values
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
