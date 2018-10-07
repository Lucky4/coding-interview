class Solution(object):
    def __init__(self):
        self.count = 1
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)-1):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        
        return self.count
        
    def helper(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            self.count += 1
            start -= 1
            end += 1