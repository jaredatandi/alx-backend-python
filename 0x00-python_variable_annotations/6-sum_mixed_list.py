#!/usr/bin/env python3
"""Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Mixed type

    Args:
        mxd_lst (any): _description_

    Returns:
        any: _description_
    """
    return sum(mxd_lst)
