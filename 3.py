# -*- coding: utf-8 -*-
class SumSolution(object):
    def method1(self, n):
	f = lambda x, y : x + y
	return reduce(f, range(1, n + 1))

    def method2(self, n):
        return n and (n + self.method2(n - 1))
