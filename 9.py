# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        times = 0
        
        for i in range(1, n+1):
            while i != 0:
                if i % 10 == 1:
                    times += 1
                i = i / 10
                
        return times


# 1. 这个题要学会如何获得一个数字的最后一位。
#
# 2. 如1~12: 1 —— 1个1
#         10 —— 1一个1
#	  11 —— 两个1
#	  12 —— 1个1      共5个1。
#
# 3. 这个题还有其他解法，心情不好看不下去，以后再看。
