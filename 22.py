# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString2(self, s, n):
        if len(s) == 0:
            return ''
         
        s = list(s)
        self.ReverseString(s, 0, n-1)
        self.ReverseString(s, n, len(s)-1)
        self.ReverseString(s, 0, len(s)-1)
         
        return ''.join(s)
         
    def ReverseString(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1


# 1. 应该学会编写，在数组任意两个位置逆序的写法。
