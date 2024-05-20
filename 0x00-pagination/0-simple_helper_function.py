#!/usr/bin/env python3
"""
0-simple_helper_function.py
Defines a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those pagination parameters.
    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.
    Returns:
        A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
