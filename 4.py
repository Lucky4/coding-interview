# -*- coding: utf-8 -*-
class FindGreatestSumOfSubArray(object):
    def method1(self, array):
        max_sum = array[0]
        array_length = len(array)
        for i in range(0, array_length):
            curr_sum = 0
            for j in range(i, array_length):
                curr_sum += array[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
        return max_sum

    def method2(self, array):
        '''
        联机算法，对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对
        整体和是有贡献的。如果前几项累计值负数，则认为有害于总和，total记录当前值。
        '''
        curr_sum = 0
        max_sum = array[0]
        for i in array:
            if curr_sum <= 0:
                curr_sum = i
            else:
                curr_sum += i
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
    
    def method3(self, array):
        '''
        动态规划，以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
        F（i）= max（F（i-1）+array[i] ， array[i]）
        '''
        max_sum = curr_max = array[0]
        for i in array[1:]:
            curr_max = max(curr_max+i, i)
            max_sum = max(curr_max, max_sum)
        return max_sum
