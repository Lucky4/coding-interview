from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_value_list = {}
        self.cache_link_list = deque()

    def get(self, key):
        if key not in self.cache_value_list:
            return -1

        self.cache_link_list.remove(key)
        self.cache_link_list.appendleft(key)

        return self.cache_value_list[key]

    def put(self, key, value):
        if key in self.cache_value_list:
            self.cache_value_list[key] = value
            self.cache_link_list.remove(key)
            self.cache_link_list.appendleft(key)
        elif len(self.cache_link_list) == self.capacity:
            del_key = self.cache_link_list.pop()
            del self.cache_value_list[del_key]
            self.cache_link_list.appendleft(key)
            self.cache_value_list[key] = value
        else:
            self.cache_link_list.appendleft(key)
            self.cache_value_list[key] = value