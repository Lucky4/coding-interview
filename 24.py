# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        i = 0
        j = len(array)-1
        res = []
        while i < j:
            if array[i] + array[j] == tsum:
                res.append(array[i])
                res.append(array[j])
                break
            if array[i] + array[j] < tsum:
                i += 1
            if array[i] + array[j] > tsum:
                j -= 1
        return res
