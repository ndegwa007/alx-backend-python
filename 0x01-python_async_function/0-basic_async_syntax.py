#!/usr/bin/env python3
"""module creates a basic coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits a random delay before returning"""
    res = random.uniform(0, max_delay)
    await asyncio.sleep(res)
    return res
