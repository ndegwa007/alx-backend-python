#!/usr/bin/env python3
"""module annotates elements of unknown type in a list"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element"""
    if lst:
        return lst[0]
    else:
        return None
