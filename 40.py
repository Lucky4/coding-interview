class Solution(object):
    def integerBreak(self, n):
        state = [0] * (n+1)
        state[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                state[i] = max(state[i], max(j * (i-j), j * state[i-j]))
        return state[n]


# 找规律：
#
# 2 = 1 + 1 -> 1 * 1 = 1
# 3 = 1 + 2 -> 1 * 2 = 2
# 4 = 2 + 2 -> 2 * 2 = 4
# 5 = 2 + 3 -> 2 * 3 = 6
# 6 = 3 + 3 -> 3 * 3 = 9
# 7 = 3 + 4 -> 3 * 4 = 12
# 8 = 2 + 3 + 3 -> 2 * 3 * 3 = 18
# 9 = 3 + 3 + 3 -> 3 * 3 * 3 = 27
# 10 = 3 + 3 + 4 -> 3 * 3 * 4 = 36
# 11 = 3 + 3 + 3 + 2 -> 3 * 3 * 3 * 2 = 54
# 12 = 3 + 3 + 3 + 3 -> 3 * 3 * 3 * 3 = 81
#
# 可以看出：
# 当n小于4的时候，最大值等于（n分解的数）的成积。如数字3。
# 当n大于等于4的时候，最大值等于（n分解的数的状态）和（n分解的数）的成积的最大值。如数字7。
参考：https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E5%88%86%E5%89%B2%E6%95%B4%E6%95%B0
