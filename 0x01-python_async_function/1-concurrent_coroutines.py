#!/usr/bin/env python3
"""module returns a list of values from another coroutine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of values"""
    res = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        values = await task
        res.append(values)
    return sorted(res)
