#!/usr/bin/env python3
"""module adds type annotation to function"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(
        dict: Mapping,
        key: Any,
        default: Union[T, None]) -> Union[Any, T]:
    if key in dict:
        return dict[key]
    else:
        return default
