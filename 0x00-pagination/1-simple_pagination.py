#!/usr/bin/env python3
"""
This module provides a helper function for pagination, calculating
start and end indexes based on page number and page size.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return paginated data for given page and page size."""
        assert isinstance(page, int) and page > 0, (
                "Page must be a positive integer."
        )
        assert isinstance(page_size, int) and page_size > 0, (
                "Page size must be a positive integer."
        )

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        # Return the page of data, or an empty list if out of range
        return dataset[start:end] if start < len(dataset) else []
