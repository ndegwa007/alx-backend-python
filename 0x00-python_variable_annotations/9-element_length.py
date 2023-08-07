#!/usr/bin/env python3
"""
module annotates function to
return values with appropriate types
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list"""
    return [(i, len(i)) for i in lst]
