#!/usr/bin/env python3
"""Complex types - function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A callable function return type
    """
    def j(f: float) -> float:
        """Fetch the second arg

        Args:
            f (float): _description_

        Returns:
            float: _description_
        """
        return float(f * multiplier)

    return j
