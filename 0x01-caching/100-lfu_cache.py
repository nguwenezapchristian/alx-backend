#!/usr/bin/env python3
""" LFU Caching Module """
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    A class LFUCache that inherits from BaseCaching and is a caching system
    using the Least Frequently Used (LFU) caching policy.
    """

    def __init__(self):
        """
        Initializes the LFUCache class.
        Calls the parent class (BaseCaching) initializer and initializes
        dictionaries
        to keep track of the frequency of usage of the cache keys and
        the order of usage.
        """
        super().__init__()
        self.usage_freq = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """
        Assigns the item value to the key in the self.cache_data dictionary.
        If the key or item is None, the method does nothing.
        If the cache exceeds the MAX_ITEMS limit, it discards the least
        frequently used item. If multiple items have the same frequency,
        it discards the least recently used item among them and prints the
        discard message.

        Args:
            key: The key to be added.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lfu_keys = [k for k, v in self.usage_freq.items(
            ) if v == min(self.usage_freq.values())]
            if len(lfu_keys) > 1:
                lfu_key = min(
                    lfu_keys, key=lambda k: self.usage_order.index(k))
            else:
                lfu_key = lfu_keys[0]
            self.usage_order.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.usage_freq[lfu_key]
            print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item
        self.usage_freq[key] = 1
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

        self.usage_freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
