#!/usr/bin/env python3
"""Duck types and iterable object
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck types

    Args:
        lst (_type_): _description_
    """
    return [(i, len(i)) for i in lst]
