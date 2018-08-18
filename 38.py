class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    if j == 0:
                        dp[j] = grid[i][j]
                    else:
                        dp[j] = grid[i][j] + dp[j-1]
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                else:
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        
        return dp[cols-1]


思路参考：https://blog.csdn.net/YF_Li123/article/details/71418015
参考：https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E7%9F%A9%E9%98%B5%E8%B7%AF%E5%BE%84
