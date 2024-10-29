#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache following LIFO policy """

        if key is None or item is None:
            return

        self.cache_data[key] = item

        # If cache exceeds max limit, discard the last item added (LIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARDED : {self.last_key}")
            
        self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
