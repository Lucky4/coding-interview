# -*- coding:utf-8 -*-
class Solution:
    def func(self, ss):
        res = []
        subset = []
        for i in  range(len(ss)):
            self.Combination(ss, i, subset, res)
        return res

    def Combination(self, ss, number, subset, res):
        if number == 0:
            res.append(''.join(subset))
            return None

        if len(ss) == 0:
            return None
        
        subset.append(ss[0])
        self.Combination(ss[1:], number-1, subset, res)
        subset.pop()

        self.Combination(ss[1:], number, subset, res)


print Solution().func('abcdefg')
