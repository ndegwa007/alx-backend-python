#!/usr/bin/env python3
"""module has a function that generates random values in a list"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of float"""
    res = []
    for _ in range(n):
        t = task_wait_random(max_delay)
        values = await t
        res.append(values)
    return sorted(res)
