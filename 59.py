class Solution(object):
    def search(self, nums, target):
        """
        题目思路：

        如果 nums[mid] 和 target 相等，那么返回 True。
        如果 nums[mid] 比 nums[l] 大或者 nums[mid] 比 nums[h] 大，那么说明左边的递增序列比右边的递增序列长。
        如果 nums[mid] 比 nums[l] 小或者 nums[mid] 比 nums[h] 小，那么说明右边的递增序列比左边的递增序列长。
        """
        l = 0
        h = len(nums) - 1
        mid = -1
        
        while l <= h:
            mid = (l + h) / 2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[l] or nums[mid] > nums[h]:
                if target >= nums[l] and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
                continue
                    
            if nums[mid] < nums[l] or nums[mid] < nums[h]:
                if target <= nums[h] and target > nums[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
                continue
                    
            h -= 1
            
        return False