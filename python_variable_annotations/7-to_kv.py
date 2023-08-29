#!/usr/bin/env python3
"""Function to_kv that takes a string k and an int OR float v"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple with k and the square of v"""
    return k, v ** 2.0
