# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if self.isEven(array[j]) and not self.isEven(array[j+1]):
                    tmp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = tmp
        return array

    # 不要求顺序
    def reOrderArray2(self, array):
        start = 0
        end = len(array)-1

        while start < end:
            if not self.isEven(array[start]):
                start += 1
                continue

            if self.isEven(array[end]):
                end -= 1
                continue
            
            tmp = array[start]
            array[start] = array[end]
            array[end] = tmp

        return array

    def isEven(self, number):
        return number & 1 == 0


# 1. 学习判断偶数的高效写法.