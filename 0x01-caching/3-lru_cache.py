#!/usr/bin/python3
'''
1. LRU caching
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache implements Least Recently Used caching strategy.
    """

    def __init__(self):
        """
        Initialization of the LRU cache.
        """
        super().__init__()
        self.order = []  # List to maintain access order for LRU eviction

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, handling LRU eviction.

        Args:
            key (object): The key to associate with the data.
            item (object): The data to cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while True:
                    discarded_key = self.order.pop(0)
                    # Check existence before deletion
                    if discarded_key in self.cache_data:
                        del self.cache_data[discarded_key]
                        print("DISCARD: {}".format(discarded_key))
                        break  # Exit loop after successful eviction
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieves a value from the cache if it exists.

        Args:
            key (object): The key to lookup in the cache.

        Returns:
            object: The cached value if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the order list (LRU)
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
