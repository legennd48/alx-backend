#!/usr/bin/python3
'''
1. MRU caching
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements Most Recently Used caching strategy.
    """

    def __init__(self):
        """
        Initialization of the MRU cache.
        """
        super().__init__()
        self.order = []  # List to maintain access order for MRU eviction

    def put(self, key, item):
        """
        Adds a key-value pair to the cache, handling MRU eviction.

        Args:
            key (object): The key to associate with the data.
            item (object): The data to cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.insert(0, key)  # Move to the beginning for MRU
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while True:
                    discarded_key = self.order.pop()
                    # Check existence before deletion
                    if discarded_key in self.cache_data:
                        del self.cache_data[discarded_key]
                        print("DISCARD: {}".format(discarded_key))
                        break  # Exit loop after successful eviction
            self.cache_data[key] = item
            # Insert at the beginning for MRU
            self.order.insert(0, key)

    def get(self, key):
        """
        Retrieves a value from the cache if it exists.

        Args:
            key (object): The key to lookup in the cache.

        Returns:
            object: The cached value if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # No need to update order for MRU (already at the beginning)
            return self.cache_data[key]
        return None
