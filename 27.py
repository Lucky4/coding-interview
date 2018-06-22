# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)>>1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output


# 这个解法和我刚开始想的思路很像,都是small最大不能超过middle.