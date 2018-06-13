# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict1 = {}

    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dict1[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        self.s = self.s+char
        if char in self.dict1:
            self.dict1[char] = self.dict1[char]+1
        else:
            self.dict1[char] = 1


# 另一种写法，主要熟悉一下队列的用法。
#from collections import deque
#
#
#class Solution:
#    # 返回对应char
#    def __init__(self):
#        self.q = deque()
#        self.s = {}
#        
#    def FirstAppearingOnce(self):
#        while len(self.q) and self.s[self.q[0]] == 2:
#            self.q.popleft()
#            
#        if len(self.q) == 0:
#            return '#'
#        
#        return self.q[0]
#        
#    def Insert(self, char):
#        if not self.s.has_key(char):
#            self.s[char] = 1
#            self.q.append(char) else:
#            self.s[char] += 1
