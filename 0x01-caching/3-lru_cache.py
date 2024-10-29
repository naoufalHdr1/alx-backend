#!/usr/bin/env python3
"""
LRUCache Module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent init method and an OrderedDict
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using the LRU policy."""
        if key is None or item is None:
            return

        # If key already exists, remove it to update the order
        if key in self.cache_data:
            self.cache_data.pop(key)

        # Add the key-value pair to the cache
        self.cache_data[key] = item

        # Check for overflow and remove the LRU item if necessary
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (the least recently used one)
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item by key and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
