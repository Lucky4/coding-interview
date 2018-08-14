# -*- coding:utf-8 -*-
class Solution:
    # 集合的子集个数为2的集合长度次幂
    def PowerSet(self, ss):
	size = len(ss)
	pow_ss_size = pow(2, size)
	res = []

	for count in range(pow_ss_size):
	    tmp = []
	    for j in range(size):
                if count & (1 << j):
                    tmp.append(ss[j])
            res.append(''.join(tmp))

	return res


s = Solution()
print s.PowerSet('abc')
