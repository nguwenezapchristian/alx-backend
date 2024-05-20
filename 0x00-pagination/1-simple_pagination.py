#!/usr/bin/env python3
"""
1-simple_pagination.py
Defines a helper function for pagination and a Server class.
"""


import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            """Skip the header"""
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.
        Args:
            page: The current page number (default 1).
            page_size: The number of items per page (default 10).
        Returns:
            A list of lists containing the rows for the requested page.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size" \
            "must be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
