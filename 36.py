# -*- coding:utf-8 -*-
class Solution:
    def func(self, ss, m, target):
        res = []
        subset = [0] * 20
        self.combination(ss, len(ss), m, target, subset, res)
        return res

    def combination(self, ss, n, m, target, subset, res):
        for i in range(n, m-1, -1):
            subset[m] = i
            if m > 1:
                self.combination(ss, i-1, m-1, target, subset, res)
            else:
                if ss[subset[1]-1] + ss[subset[2]-1] + ss[subset[3]-1] == target:
                    res.append(subset[1:4])


print sorted(Solution().func([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 3, 150))

