# -*- coding: utf-8 -*-
class MoreThanHalfNumSolution(object):
    def method1(self, numbers):
        times = {}
        for i in numbers:
            if i not in times:
                times[i] = 1
            else:
                times[i] += 1
        half_length = len(numbers) / 2
        for j in times:
            if times[j] > half_length:
                return j
        return 0

    def method2(self, numbers):
        more_half_number = numbers[0]
        times = 1

        for i in numbers[1:]:
            if i == more_half_number:
                times += 1
            elif times == 0:
                more_half_number = i
                times = 1
            else:
                times -= 1
        
        times = 0

        for j in numbers:
            if j == more_half_number:
                times += 1
                
        if times > len(numbers) / 2:
            return more_half_number

        return 0

    def method3(object):
        '''
	先排序，找中位数。
	'''
