#!/usr/bin/env python3
"""1-async_comprehension.py module"""
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Coroutine function

    Arg:
        Takes no arguments

    Returns:
        async generator

    """
    result = [i async for i in async_generator()]
    return result
