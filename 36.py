# -*- coding:utf-8 -*-
class Solution:
    def func(self, ss, m):
        res = []
        subset = [0] * m
        self.combination(ss, len(ss), m, subset, res)
        return res

    def combination(self, ss, n, m, subset, res):
        for i in range(n, m-1, -1):
            subset[m-1] = i-1
            if m > 1:
                self.combination(ss, i-1, m-1, subset, res)
            else:
                res.append(subset[0:3])


print sorted(Solution().func([10, 20, 30, 40, 50], 3))

