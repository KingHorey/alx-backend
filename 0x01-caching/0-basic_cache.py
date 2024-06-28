#!/usr/bin/env python3

"""
    import type hint, BaseCaching
"""
from typing import Union
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ implementation of a prototype cache """
    def put(self, key: str, item: Union[str, int]) -> None:
        """ add item to the cache """
        if key is not None or item is not None:
            self.cache_data.update({key: item})

    def get(self, key: str) -> Union[str, None]:
        """ return an item from the cache if it exists """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
