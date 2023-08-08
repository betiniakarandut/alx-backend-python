# !/usr/bin/env python3
"""4-tasks.py module"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Coroutine Function

    Args:
        n(int) - number of times wait_random() will spawn
        max_delay - amount of delay

    Returns:
        Sorted list of all the delays
    """
    wait_time = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*wait_time))


# if __name__ == "__main__":
#     task_wait_n = __import__('4-tasks').task_wait_n

#     n = 5
#     max_delay = 6
#     print(asyncio.run(task_wait_n(n, max_delay)))
