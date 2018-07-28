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