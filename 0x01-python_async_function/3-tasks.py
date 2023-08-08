#!/usr/bin/env python3
"""module has a function that serves as asyncio.Task subclass"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a foat"""
    value = asyncio.create_task(wait_random(max_delay))
    return value
