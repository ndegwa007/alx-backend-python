#!/usr/bin/env python3
"""module creates a basic coroutine"""
import random


async def wait_random(max_delay=10):
    """waits a random delay before returning"""
    res = random.uniform(0, max_delay)
    return res
