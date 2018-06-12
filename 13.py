# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A:
            return []
        
        length = len(A)
        B = [None] * length
        B[0] = 1
        
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]
            
        tmp = 1
        for j in range(length-2, -1, -1):
            tmp *= A[j+1]
            B[j] *= tmp
            
        return B


# 这个题要学会如何使用Python的range()函数从后向前迭代。
