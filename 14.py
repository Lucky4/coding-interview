# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        tmp = [False] * len(numbers)
        for i in xrange(0, len(numbers)):
            if tmp[numbers[i]] == True:
                duplication[0] = numbers[i]
                return True
            tmp[numbers[i]] = True
        return False
