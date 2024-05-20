#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(
            self,
            index: Optional[int] = None,
            page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination information for a
        deletion-resilient dataset.

        Args:
            index: The starting index of the page.
            page_size: The number of items per page.

        Returns:
            A dictionary containing the start index, next index, page size,
            and the page data.
        """
        indexed_data = self.indexed_dataset()
        assert isinstance(index, int) and 0 <= index < len(
            indexed_data), "Index out of range"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be an integer" \
            "greater than 0"

        data = []
        next_index = index
        remaining_items = page_size

        while remaining_items > 0 and next_index < len(indexed_data):
            item = indexed_data.get(next_index, None)
            if item:
                data.append(item)
                remaining_items -= 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
