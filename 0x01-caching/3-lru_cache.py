#!/usr/bin/env python3
""" LRU Caching Module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class LRUCache that inherits from BaseCaching and is a caching system
    using the Least Recently Used (LRU) caching policy.
    """

    def __init__(self):
        """
        Initializes the LRUCache class.
        Calls the parent class (BaseCaching) initializer and initializes an
        ordered list to keep track of the order of usage of the cache keys.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Assigns the item value to the key in the self.cache_data dictionary.
        If the key or item is None, the method does nothing.
        If the cache exceeds the MAX_ITEMS limit, it discards the least
        recently used item and prints the discard message.

        Args:
            key: The key to be added or updated in the cache.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Returns the value linked to the key in self.cache_data.
        If the key is None or not found in self.cache_data, returns None.

        Args:
            key: The key whose value needs to be fetched from the cache.

        Returns:
            The value associated with the key, or None if key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        """ Update usage order since the key was accessed """
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
