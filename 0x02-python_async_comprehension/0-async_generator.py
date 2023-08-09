#!/usr/bin/env python3
"""module holds a generator function(async)"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield values randomly"""
    for _ in range(10):
        num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield num
