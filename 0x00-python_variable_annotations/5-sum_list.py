#!/usr/bin/env python3
"""A complex type annotations
"""


def sum_list(input_list: list[float]) -> float:
    """Complex annotations

    Args:
        input_list (list[float]): _description_

    Returns:
        float: _description_
    """
    ans: float = 0
    for i in range(len(input_list)):
        ans += input_list[i]

    return ans
