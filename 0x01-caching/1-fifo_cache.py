#!/usr/bin/python3
'''
1. FIFO caching
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    class uses FIFO Caching
    '''

    def __init__(self):
        ''' initialisation '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        addes item to cache using FIFO
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''
        gets cache item by key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
