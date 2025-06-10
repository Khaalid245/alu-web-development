#!/usr/bin/python3
"""
BasicCache class that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Define BasicCache """

    def put(self, key, item):
        """ Add key/value pair to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve value from the cache based on given key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
