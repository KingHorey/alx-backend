#!/usr/bin/env python3

""" import type hints
    parent class BaseCaching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ implement FIFO caching technique to add to cache """
    def __init__(self):
        """ init method """
        self._count_dict = []
        self._added_keys = []
        super().__init__()

    def put(self, key, data):
        """ add to the cache """
        if (key is not None and data is not None and len(self.cache_data) <
                BaseCaching.MAX_ITEMS):
            if key in self._added_keys:
                self._added_keys.remove(key)
                self._added_keys.append(key)
            else:
                self._added_keys.append(key)
            self.cache_data.update({key: data})

        elif (key is not None and data is not None and len(self.cache_data) ==
              BaseCaching.MAX_ITEMS):
            if key in self._added_keys:
                self._added_keys.remove(key)
                self._added_keys.append(key)
                self.cache_data.update({key: data})
            else:
                old_key = self._added_keys[0]
                print(f"DISCARD: {old_key}")
                del self._added_keys[0]
                del self.cache_data[old_key]
                self._added_keys.append(key)
                self.cache_data.update({key: data})

    def get(self, key: str):
        """ return an item from the cache if it exists """
        if key is not None:
            if key in self._added_keys:
                self._added_keys.remove(key)
                self._added_keys.append(key)
            return self.cache_data.get(key, None)
        return None
