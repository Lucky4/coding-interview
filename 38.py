class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
	if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        state = [0] * num_cols
        for i in range(num_rows):
            for j in range(num_cols):
                if j == 0:
                    state[j] = state[j] + grid[i][j]
                elif i == 0:
		    if j == 0:
		        state[j] = grid[i][j]
	            else:
                        state[j] = state[j-1] + grid[i][j]
                else:
                    state[j] = min(state[j-1], state[j]) + grid[i][j]
        return state[num_cols-1]


思路参考：https://blog.csdn.net/YF_Li123/article/details/71418015
