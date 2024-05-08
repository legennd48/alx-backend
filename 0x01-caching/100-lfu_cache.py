#!/usr/bin/env python3
"""Least Frequently Used caching module.

This module implements a Least Frequently Used (LFU) cache. It inherits
from the `BaseCaching` class and provides methods for storing, retrieving,
and evicting items based on their frequency of access.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Represents an object that allows storing and retrieving items from a
    dictionary with an LFU removal mechanism when the limit is reached.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary to
        store key-value pairs.
        keys_freq (list): A list to store frequencies (key, frequency)
        for LFU eviction.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()  # Dictionary for key-value pairs
        self.keys_freq = []  # List to track key frequencies

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on
        the most recently used item.

        This method repositions the provided `mru_key`
        (most recently used key) in the `keys_freq` list
        based on its frequency for LFU ordering.

        Args:
            mru_key (object): The key of the most recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Adds an item in the cache.

        This method adds a key-value pair to the cache, handling eviction
        of the least frequently used item (LFU) if the capacity is reached.
        It also updates the frequency of the accessed key.

        Args:
            key (object): The key to associate with the data.
            item (object): The data to cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.

        This method retrieves an item from the cache based on the provided key.
        It also updates the frequency of the accessed key for LFU ordering.

        Args:
            key (object): The key to lookup in the cache.

        Returns:
            object: The cached value if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
