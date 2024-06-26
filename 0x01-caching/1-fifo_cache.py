#!/usr/bin/env python3

""" import type hints
    parent class BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ implement FIFO caching technique to add to cache """
    def put(self, key, data):
        """ add to the cache """
        if (key is not None and data is not None and len(self.cache_data) <
                BaseCaching.MAX_ITEMS):
            self.cache_data.update({key: data})
        elif (key is not None and data is not None and len(self.cache_data) ==
                BaseCaching.MAX_ITEMS):
            # remove the first item in the cache
            dict_key: str = ""
            for i in self.cache_data.keys():
                dict_key = i
                break
            print(f"DISCARD: {dict_key}")
            del self.cache_data[dict_key]
            self.cache_data.update({key: data})

    def get(self, key: str):
        """ return an item from the cache if it exists """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
