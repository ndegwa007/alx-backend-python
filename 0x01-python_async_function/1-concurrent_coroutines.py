#!/usr/bin/env python3
"""module returns a list of values from another coroutine"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> list[float]:
    """returns a list of values"""
    res = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        values = await task
        res.append(values)
    return res
