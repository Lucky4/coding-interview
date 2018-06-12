# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        data_length = len(data)
        
        if data_length == 0:
            return 0
        
        tmp_data = data[:]
        return self.InversePairsCore(data, tmp_data, 0, data_length - 1)
    
    def InversePairsCore(self, data, tmp_data, left, right):
        if left == right:
            return 0
        
        center = (left + right) / 2
        left_count = self.InversePairsCore(data, tmp_data, left, center) % 1000000007
        right_count = self.InversePairsCore(data, tmp_data, center + 1, right) % 1000000007
        curr_count = self.Merge(data, tmp_data, left, center + 1, right)
        
        return (left_count + right_count + curr_count)
        
    def Merge(self, data, tmp_data, lpos, rpos, right_end):
        num_elements = right_end - lpos + 1
        left_end = rpos - 1
        tmp_pos = lpos
        count = 0
        
        while lpos <= left_end and rpos <= right_end:
            if data[lpos] < data[rpos]:
                tmp_data[tmp_pos] = data[lpos]
                tmp_pos += 1
                lpos += 1 
            else:
                tmp_data[tmp_pos] = data[rpos]
                tmp_pos += 1
                rpos += 1
                count += left_end - lpos + 1
                if count >= 1000000007:
                    count%=1000000007
        
        while lpos <= left_end:
            tmp_data[tmp_pos] = data[lpos]
            tmp_pos += 1
            lpos += 1
        while rpos <= right_end:
            tmp_data[tmp_pos] = data[rpos]
            tmp_pos += 1
            rpos += 1
            
        for i in range(0, num_elements):
            data[right_end] = tmp_data[right_end]
            right_end -= 1
            
        return count


# 该思路清晰，但使用Python编写该方法时运行时间超时，如果使用使用其他语言的话可能会过，该题主要的作用是学习归并排序。
