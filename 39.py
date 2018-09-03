# -*- coding: utf-8 -*-
class NumArray(object):
    sums = []

    def __init__(self, nums):
        NumArray.sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            NumArray.sums[i+1] = NumArray.sums[i] + nums[i]
        

    def sumRange(self, i, j):
        return NumArray.sums[j+1] - NumArray.sums[i]


# 参考：https://leetcode.com/problems/range-sum-query-immutable/solution/