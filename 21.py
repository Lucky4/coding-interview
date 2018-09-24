# -*- coding: utf-8 -*-
from __future__ import division


class Solution:
    def Power(self, base, exponent):
        if base == 0:
	    return False
        if exponent == 0:
	    return 1

        is_minus = False
        if exponent < 0:
	    is_minus = True
	    exponent = abs(exponent)

	curr = base
	res = 1
	while exponent != 0:
	    if exponent & 1 == 1:
		res *= curr
	    curr *= curr
	    exponent >>= 1

	if is_minus:
	    res = 1 / res
	return res

    def Power2(self, base, exponent):
        is_minus = False
        if base == 0:
            return False
        if exponent < 0:
            is_minus = True
            exponent = abs(exponent)
        if exponent == 0:
            return 1
        if exponent == 1: # 这部是处理奇数偶数的关键，运行到这里就返回了，没有继续执行下面的操作。
	    return base

        res = self.Power3(base, exponent >> 1)
	res *= res # 从这部往下的操作只有在第一次调用时执行了一次
	if exponent & 1 == 1:
	    print 'I excute 1 times'
	    res *= base

        if is_minus:
            return 1 / res
        return res
