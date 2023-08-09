#!/usr/bin/env python3
"""module runs four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return time taken for the 4 comprehension"""
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time = time.perf_counter() - start
    return total_time
