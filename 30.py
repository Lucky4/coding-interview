# -*- coding: utf-8 -*-
class Solution(object):
    def Palindromic(selfs, s):
        if len(s) == 0:
            return 0
        
        res = 0
        dp = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j - i) < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j]:
                    res += 1
        
        return res
