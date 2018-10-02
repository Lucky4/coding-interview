class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        
        dp = [[0] * len(s) for i in range(len(s))]
        start = 0
        longest = 1

        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                start = i
                longest = 2
                
        for j in range(3, len(s) + 1):
            for k in range(len(s) - j + 1):
                end = j + k - 1
                if s[k] == s[end] and dp[k + 1][end-1] == 1:
                    dp[k][end] = 1
                    start = k
                    longest = j
                    
        return s[start:start+longest]