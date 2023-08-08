#!/usr/bin/env python3
"""1-async_comprehension.py module"""
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator:
    result = [i async for i in async_generator()]
    return result

# async def main():
#     print(await async_comprehension())

# asyncio.run(main())