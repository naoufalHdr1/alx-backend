#!/usr/bin/env python3
"""
LFU Caching Module
"""
from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.cache_data = {}  # Main cache storage
        self.frequency = defaultdict(int)  # Frequency counter for each key
        self.least_freq = defaultdict(OrderedDict)
        self.min_freq = 0  # Minimum frequency in the cache

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item
            self.cache_data[key] = item
            self.get(key)  # This will update the frequency
            return

        # Check if we need to evict an item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the least frequently used item
            key_to_remove, _ = (
                    self.least_freq[self.min_freq].popitem(last=False)
            )
            if not self.least_freq[self.min_freq]:
                del self.least_freq[self.min_freq]
            del self.cache_data[key_to_remove]
            del self.frequency[key_to_remove]
            print(f"DISCARD: {key_to_remove}")

        # Add new item
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.least_freq[1][key] = item  # Add to frequency 1
        self.min_freq = 1  # Reset min frequency

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency
        freq = self.frequency[key]
        self.frequency[key] += 1
        new_freq = self.frequency[key]

        # Remove the item from the old frequency
        del self.least_freq[freq][key]
        if not self.least_freq[freq]:
            del self.least_freq[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # Add the item to the new frequency
        self.least_freq[new_freq][key] = self.cache_data[key]

        return self.cache_data[key]
