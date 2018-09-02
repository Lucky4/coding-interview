# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        题目思路：

        如果 nums[m] 和 target 相等，那么返回 True。
        如果 nums[m] 比 nums[l] 大或者 nums[mid] 比 nums[h] 大，那么说明左边的递增序列比右边的递增序列长。
        如果 nums[m] 比 nums[l] 小或者 nums[mid] 比 nums[h] 小，那么说明右边的递增序列比左边的递增序列长。
        """
        l = 0
        h = len(nums) - 1
        m = -1
        
        while l <= h:
            m = (l + h) / 2
            
            if nums[m] == target:
                return True
            
            if nums[m] > nums[l] or nums[m] > nums[h]:
                if target >= nums[l] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
                continue
                    
            if nums[m] < nums[l] or nums[m] < nums[h]:
                if target <= nums[h] and target > nums[m]:
                    l = m + 1
                else:
                    h = m - 1
                continue
                    
            h -= 1
            
        return False