# -*- coding:utf-8 -*-
class Solution:
    # 一开始我的想法，时间复杂度和空间复杂度都很高
    def LeftRotateString1(self, s, n):
        if len(s) == 0:
            return ''
         
        s = list(s)
        tmp_list = s[:]
        count = 0
        while count < n:
            tmp = tmp_list[count]
            for i in range(0, len(s)-1):
                s[i] = s[i+1]
            s[i+1] = tmp
            count += 1
        return ''.join(s)

    # 最优算法
    def LeftRotateString2(self, s, n):
        s_length = len(s)
        if s_length == 0:
            return ''
         
        s = list(s)
        self.ReverseString(s, 0, n-1)
        self.ReverseString(s, n, s_length-1)
        self.ReverseString(s, 0, s_length-1)
         
        return ''.join(s)
         
    def ReverseString(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1


# 1. 应该学会编写，在数组任意两个位置逆序的写法。
