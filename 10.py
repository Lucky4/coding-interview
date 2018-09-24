# -*- coding:utf-8 -*-


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == "":
            return -1
        
        exist_letters = {}
        
        for i in s:
            if not exist_letters.has_key(i):
                exist_letters[i] = 1
            else:
                exist_letters[i] += 1
            
        for j in range(0, len(s)):
            if exist_letters[s[j]] == 1:
                return j
