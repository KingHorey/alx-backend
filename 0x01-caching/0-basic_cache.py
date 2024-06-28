#!/usr/bin/env python

""" BaseCaching module
"""
from typing import Union


class BaseCaching:
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache "
                                  "class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache "
                                  "class")


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
