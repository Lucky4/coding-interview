# -*- coding: utf-8 -*-
from heapq import *


class GetLeastNumbersSolution(object):
    def method1(self, tinput, k):
        '''
	冒牌排序k次，复杂度O(n*k)。
	'''
	if k > len(tinput) or k == 0: return []

        for i in range(0, k):
            for j in range(0, len(tinput)-i-1):
                if tinput[j] < tinput[j+1]:
                    tinput[j] = tinput[j] ^ tinput[j+1]
		    tinput[j+1] = tinput[j] ^ tinput[j+1]
		    tinput[j] = tinput[j] ^ tinput[j+1]

	return tinput[len(tinput):-(k+1):-1]

    def method2(self, tinput, k):
        '''
	构建堆， 调整k次，复杂度O(k*log(n))
	'''
	if k > len(tinput) or k == 0:
            return []

        res = []
	heapify(tinput)

	for i in range(0, k):
            res.append(heappop(tinput))

	return res
