# -*- coding: utf-8 -*-
class Solution:
    def StrToInt(self, s):
        str_length = len(s)
        if str_length == 0:
            return 0
        
        is_minus = False
        index = 0
        num = 0
        
        if s[0] == '+':
            is_minus = False
            index = 1
        elif s[0] == '-':
            is_minus = True
            index = 1
        else:
            is_minus = False
            index = 0
        
        for i in range(index, str_length):
            if '0' < s[i] < '9':
                try:
                    num = num * 10 + int(s[i])
                except Exception as e:
                    num = 0
                    break
            else:
                num = 0
                break
                
        if is_minus:
            num = 0 - num
        return num


# 有几点要注意：
# 1. 目标字符串中是否有非0~9的字符。
# 2. 转换的int型数字是否超出范围。
# 3. 注意转换后数字的正负
# 4. C/C++中可以使用‘如: char *s = '9'; int num = s[0]-'0'的方式获得当前位的数字。ps:利用了ASCII码相减的的方式获得int型数字。
