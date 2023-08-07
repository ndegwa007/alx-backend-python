#!/usr/bin/env python3
"""
module takes annotated
list of ints and floats
returns their sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of a list elements"""
    return sum(mxd_lst)
