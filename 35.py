# -*- coding:utf-8 -*-
class Solution:
    def PowerSet(self, ss):
        str_length = len(ss)
        num_of_set = pow(2, str_length) # 集合的子集个数为2的集合长度次幂
        
        res = []
        for i in range(num_of_set):
            tmp = []
            for j in range(str_length):
                if i & (1 << j):
                    tmp.append(ss[j])
            res.append(''.join(tmp))

        return res


print Solution().PowerSet('abc')