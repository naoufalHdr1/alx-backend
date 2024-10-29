#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache following FIFO policy """
        if key is None or item is None:
            return

        # Add/Update the key in the cache and track order
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        # If cache exceeds max limit, discard the first item added (FIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.order.pop(0)
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
