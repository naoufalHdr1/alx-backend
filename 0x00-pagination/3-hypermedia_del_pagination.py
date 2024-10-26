#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates and returns an indexed dataset, truncating to 1000 items."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing paginated data and relevant
        pagination info.

        Handles cases where data has been removed by ensuring next index
        refers to the next actual data item.

        Parameters:
        - index (int): the starting index of the page
        - page_size (int): the number of items per page

        Returns:
        - A dictionary with 'index', 'next_index', 'page_size', and 'data'.
        """
        # Ensure index is within the range of available data
        assert 0 <= index < len(self.indexed_dataset()), (
            "Index is out of range"
        )

        data = []
        current_index = index
        indexed_data = self.indexed_dataset()

        # Collect data, skipping missing indices if necessary
        while len(data) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # Define next_index after the page is filled or end is reached
        next_index = (
                current_index if current_index < len(indexed_data) else None
        )

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
