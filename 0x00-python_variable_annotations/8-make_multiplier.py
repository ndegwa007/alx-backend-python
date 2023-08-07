#!/usr/bin/env python3
"""module returns a function that multiplies a float by argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def func(x: float) -> float:
        return x * multiplier
    return func
