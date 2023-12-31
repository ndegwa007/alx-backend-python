#!/usr/bin/env python3
"""module has a function(async) that uses async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return random numbers in a list"""
    nums = [num async for num in async_generator()]
    return nums
