#!/usr/bin/env python3
"""Annotate the element_length function's parameters and return values"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
