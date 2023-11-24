#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Helper module
@File        : output.py
@IDE         : PyCharm
@Date        : 24/11/2023 15:44
"""


def table(data: dict, width: int = 20) -> str:
    """
    Returns activity summary in a formatted table with dynamic headers.

    Args:
    - data (list): A list of dictionaries containing activity-related data.
                   Each dictionary should contain keys corresponding to the table headers.
    - width (int): The width of each column in the table.

    Returns:
    Returns the activity summary in the specified format as a string.
    """

    return_string = ""
    header_format = ""

    headers = list(data[0].keys())

    for header in headers:
        header_format += "{:<" + str(width) + "s} | "  # Adjust the width as needed

    return_string += "=" * (int(width) * len(headers) + 3 * (len(headers) - 1)) + "\n"
    for header in headers:
        if header == headers[-1]:
            return_string += "{:<{}}\n".format(header, width)
        else:
            return_string += "{:<{}} | ".format(header, width)

    return_string += "=" * (int(width) * len(headers) + 3 * (len(headers) - 1)) + "\n"

    for activity in data:
        for key in headers:
            if key == headers[-1]:
                return_string += "{:<{}}".format(str(activity[key]), width)
            else:
                return_string += "{:<{}} | ".format(str(activity[key]), width)
        return_string += "\n"

    return return_string
