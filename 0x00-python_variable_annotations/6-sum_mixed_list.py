# #!/usr/bin/env python3
"""6-sum_mixed_list.py module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of elements in the list as a float"""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
