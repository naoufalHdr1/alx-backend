#!/usr/bin/env python3
"""
MRUCache Module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize the MRUCache with a parent constructor and an OrderedDict.
        """
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain order

    def put(self, key, item):
        """Add an item to the cache with MRU eviction policy."""
        if key is None or item is None:
            return

        # If the key is already in the cache, move it to the end
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        else:
            # Check if we need to evict the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Pop the last item, which is the most recently used
                most_recent_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {most_recent_key}")

        # Assign the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
