#!/usr/bin/env python3
"""Complex types - string and int/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Use complex string/int/float types

    Args:
        k (str): _description_
        v (List[Union[int, float]]): _description_

    Returns:
        Tuple[str, float]: _description_
    """
    return (k, v*v)
