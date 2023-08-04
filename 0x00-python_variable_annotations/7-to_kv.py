#!/usr/bin/env python3
"""7-to_kv.py module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return k, v**2
