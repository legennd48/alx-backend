#!/usr/bin/python3
'''
0. Basic dictionary
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    class that implements methods:
        put - adds an item into the cache
        get - get an item from cache by key
    '''

    def __init__(self):
        ''' initialisation '''
        super().__init__()

    def put(self, key, item):
        '''
        adds an item into the cache
        '''
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        '''
        gets an item by key
        '''
        if key is not None:
            return self.cache_data.get(key)
        return None
