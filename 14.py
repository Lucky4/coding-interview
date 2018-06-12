# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        tmp = [False] * len(numbers)
        
        for i in xrange(0, len(numbers)):
            if tmp[numbers[i]] == True:
                duplication[0] = numbers[i]
                return True
            
            tmp[numbers[i]] = True
            
        return False


# ps: 经我自己证明，使用布尔类型比使用数字更省空间。
