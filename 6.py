# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        res = ''
        if not numbers:
            return res
        cmp = lambda x, y: 1 if str(x)+str(y) > str(y)+str(x) else -1
        numbers.sort(cmp)
        for i in numbers:
            res += str(i)
        return res
