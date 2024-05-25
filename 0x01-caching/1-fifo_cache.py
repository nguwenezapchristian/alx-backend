#!/usr/bin/env python3
""" FIFO Caching Module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the class """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item_key = self.cache.pop(0)
            del self.cache_data[first_item_key]
            print(f"DISCARD: {first_item_key}")
        self.cache_data[key] = item
        self.cache.append(key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
