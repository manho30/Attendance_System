#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Percentage helper
@File        : percentage.py
@IDE         : PyCharm
@Date        : 24/11/2023 15:37
"""

def calculate(presnt: int, total: int,toFixed: int = 2) -> float:
    """
    Calculate percentage.

    Args:
    present (float): The number of present items.
    total (float): The total number of items.
    to_fixed (int, optional): Number of decimal places in the result. Default is 2.

    Returns:
    float: The calculated percentage.
    """
    try:
        return round((presnt / total) * 100, toFixed)
    except ZeroDivisionError:
        return 0.00