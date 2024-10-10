#!/usr/bin/env python3
'''
a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
'''
from typing import List, Any


def sum_mixed_list(mxd_lst: List[Any]) -> float:
    'return sum of floats'
    return sum(mxd_lst)
