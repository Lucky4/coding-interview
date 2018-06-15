# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        
        start = 0
        end = len(rotateArray) - 1
        mid = 0
        
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                mid = end
                break
                
            mid = (start + end) / 2
            if rotateArray[mid] >= rotateArray[start]:
                start = mid
            elif rotateArray[mid] <= rotateArray[end]:
                end = mid
        
        return rotateArray[mid]


# 注意几种情况：
# 1. 把数组前面的0个元素从最前面搬到最后面，也就是原数组不做改动，根据题目的规则这也是一个旋转，此时数组的第一个元素是大于小于或者等于最后一个元素的。
# 2. 排好序的数组中有可能有相等的元素，我们特别需要注意两种情况。一是旋转之后的数组中，第一个元素和最后一个元素是相等的；另外一种情况是最小的元素在数组中重复出现
# 3. 数组有序，还是查找元素，一定要想到折半查找。
