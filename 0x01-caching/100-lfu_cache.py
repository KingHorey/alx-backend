#!/usr/bin/env python3

""" import base caching class """
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ implement the least frequently used technique """
    def __init__(self):
        """ local constructor """
        self._count_dict = defaultdict(int)
        super().__init__()

    def put(self, key, data):
        """ add to the cache """
        if (key is not None and data is not None and len(self.cache_data) <
                BaseCaching.MAX_ITEMS):
            self.cache_data.update({
                key: data
            })
            self._count_dict[key] += 1
        elif (key is not None and data is not None and len(self.cache_data) ==
                BaseCaching.MAX_ITEMS):
            # remove the lowest used in the cache
            if key in self.cache_data:
                self.cache_data.update({key: data})
                self._count_dict[key] += 1
            else:
                minimum = 1000
                old_key = ""
                for k, v in self._count_dict.items():
                    if v < minimum:
                        minimum = v
                        old_key = k
                print(f"DISCARD: {old_key}")
                del self._count_dict[old_key]
                del self.cache_data[old_key]
                self.cache_data.update({
                    key: data
                })
                self._count_dict[key] += 1

    def get(self, key: str):
        """ return an item from the cache if it exists """
        if key is not None:
            if key in self._count_dict:
                self._count_dict[key] += 1
            return self.cache_data.get(key, None)
        return None
