#!/usr/bin/env python3
"""A complex type annotations
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Complex annotations

    Args:
        input_list (list[float]): _description_

    Returns:
        float: _description_
    """
    return sum(input_list)
