class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0

        num_length = len(nums)
        dp = [0] * num_length

        for i in range(num_length):
            tmp = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp = max(tmp, dp[j]+1)
            dp[i] = tmp

        return max(dp)

# tmp存放的就是以某一个数为最后一个数的一次遍历中，临时最大的子序列数量。
参考：https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E6%9C%80%E9%95%BF%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97